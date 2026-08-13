#!/bin/bash
# PUBLICADOR AUTOMÁTICO GLASSITAS
# Emula el sistema de publicación automática de Cráneo Noble.
# Funciona con curl + python3 (no requiere Node.js).
# Se ejecuta desde GitHub Actions (2x/día), QNAP (cron) o cualquier servidor.
#
# Uso:
#   ./scripts/publicar-glassitas.sh [slot]
#     slot: 0 (12:00) | 1 (18:00) — recomendado desde GitHub Actions
#     si se omite, se detecta automáticamente por hora local CDMX (±10 min)

cd "$(dirname "$0")/.." || exit 1
LOG="cron-glassitas.log"
echo "[$(date)] Iniciando..." >> "$LOG"

export TZ=America/Mexico_City

# Token: prioridad a variable de entorno (secret de GitHub), fallback .config.json
TOKEN="${FB_PAGE_TOKEN:-$(python3 -c "import json; print(json.load(open('.config.json'))['PAGE_TOKEN'])" 2>/dev/null)}"
PAGE_ID="1111933412010777"

[ -z "$TOKEN" ] && { echo "[$(date)] ERROR: No hay token" >> "$LOG"; exit 1; }

SLOT_ARG="${1:-auto}"

# Generar plan: hoy|slot|imagen — el copy se guarda en /tmp/_glassitas_copy.txt
PLAN=$(python3 - "$SLOT_ARG" <<'PYEOF' 2>/dev/null
import json, sys, os, datetime, unicodedata

def norm(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn').lower()

slot_arg = sys.argv[1]
cal = json.load(open('contenido/calendario.json'))
now = datetime.datetime.now()
dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
hoy = dias[now.weekday()]

# El calendario.json usa acentos ("Miércoles") pero las carpetas no ("Miercoles").
# Buscar la clave del día normalizando sin acentos.
cal_dias = {norm(k): k for k in cal['dias']}
hoy_cal = cal_dias.get(norm(hoy), hoy)

if slot_arg == 'auto':
    hh, mm = map(int, now.strftime('%H:%M').split(':'))
    actual = hh * 60 + mm
    candidatos = []
    for i, h in enumerate(cal['horarios']):
        sh, sm = map(int, h.split(':'))
        if abs(actual - (sh * 60 + sm)) <= 10:
            candidatos.append(i)
    if not candidatos:
        print('NONE')
        sys.exit(0)
    slot = candidatos[0]
else:
    slot = int(slot_arg)

post = cal['dias'].get(hoy_cal)
if not post or slot >= len(post):
    print('NONE')
    sys.exit(0)

copy = post[slot].get('copy', '').strip()
if not copy:
    print('NONE')
    sys.exit(0)

carpeta = f'contenido/{hoy}'
if not os.path.isdir(carpeta):
    print('NONE')
    sys.exit(0)

imagenes = sorted(f for f in os.listdir(carpeta)
                  if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')))
if not imagenes:
    print('NONE')
    sys.exit(0)

idx = min(slot, len(imagenes) - 1)
img = os.path.join(carpeta, imagenes[idx])

with open('/tmp/_glassitas_copy.txt', 'w') as f:
    f.write(copy)

print(f"{hoy}|{slot}|{img}")
PYEOF
)

if [ -z "$PLAN" ] || [ "$PLAN" = "NONE" ]; then
    echo "[$(date)] Sin publicación programada" >> "$LOG"
    exit 0
fi

IFS='|' read -r HOY SLOT IMAGEN <<< "$PLAN"
COPY=$(cat /tmp/_glassitas_copy.txt 2>/dev/null)

# Anti-duplicado: una sola publicación por (fecha, slot)
ESTADO=".glassitas-published.json"
FECHA=$(date +%Y-%m-%d)
CLAVE="${FECHA}:${SLOT}"

CHECK=$(python3 - "$ESTADO" "$CLAVE" <<'PYEOF'
import json, sys, os
estado, clave = sys.argv[1], sys.argv[2]
if os.path.exists(estado):
    data = json.load(open(estado))
    if clave in data:
        print("DONE")
        sys.exit(0)
print("NEW")
PYEOF
)

if [ "$CHECK" = "DONE" ]; then
    echo "[$(date)] ${HOY} slot ${SLOT} ya publicado (${CLAVE})" >> "$LOG"
    exit 0
fi

echo "[$(date)] Publicando ${HOY} slot ${SLOT}..." >> "$LOG"

if [ -n "$IMAGEN" ] && [ -f "$IMAGEN" ]; then
    RESULT=$(curl -s -X POST "https://graph.facebook.com/v19.0/$PAGE_ID/photos" \
        -F "message=$COPY" \
        -F "access_token=$TOKEN" \
        -F "source=@$IMAGEN")
else
    RESULT=$(curl -s -X POST "https://graph.facebook.com/v19.0/$PAGE_ID/feed" \
        -d "message=$COPY" \
        -d "access_token=$TOKEN")
fi

FB_ID=$(echo "$RESULT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('id','ERROR'))" 2>/dev/null)

if [ "$FB_ID" != "ERROR" ]; then
    echo "[$(date)] ✅ ${HOY} slot ${SLOT} publicado: ${FB_ID}" >> "$LOG"
    python3 - "$ESTADO" "$CLAVE" "$FB_ID" <<'PYEOF'
import json, sys, os
estado, clave, fb_id = sys.argv[1], sys.argv[2], sys.argv[3]
data = {}
if os.path.exists(estado):
    data = json.load(open(estado))
data[clave] = fb_id
with open(estado, 'w') as f:
    json.dump(data, f, indent=2)
PYEOF
else
    echo "[$(date)] ❌ Error: $RESULT" >> "$LOG"
fi
