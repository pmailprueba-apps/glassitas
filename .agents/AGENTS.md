# Project Context: Glassitas

**Nombre:** Glassitas — Galletas decoradas para eventos sociales.
**Ubicación:** San Luis Potosí.
**Estado:** Negocio existente, arranque de presencia digital.

## Stack
- **Web:** HTML/CSS vanilla (GitHub Pages).
- **Redes sociales:** Facebook Page + Instagram Business.
- **Publicación:** Node.js scripts con Facebook Graph API.
- **Imágenes:** Fotos reales de producto + generación IA (ComfyUI/Gemini).
- **Logo:** SVG vectorizado.
- **Automatización:** Cron local (Mac Mini) o Docker.

## Estructura del proyecto
```
44-glassitas/
├── .agents/                    # Configuración de agentes
├── assets/                     # Activos visuales
│   ├── logo/                   # Logos en varios formatos
│   ├── productos/              # Fotos reales de galletas
│   ├── plantillas/             # Plantillas de flyers
│   ├── posts/                  # Posts terminados organizados
│   └── videos/                 # TikTok/reels
├── contenido/                  # Calendario y textos
│   ├── calendario.json         # Schedule de publicaciones
│   └── copias.conf             # Textos por día
├── marketing/                  # Estrategia y campañas
│   ├── COPYS/                  # Textos por categoría de evento
│   ├── ESTRATEGIA_360.md       # Estrategia completa
│   └── prompts-imagenes.md     # Prompts para generación de imágenes
├── web/                        # Landing page
│   ├── index.html
│   └── style.css
├── scripts/                    # Automatización
│   └── overlay_logo.py
├── AVANCES.md                  # Checklist de progreso
└── README.md
```

## Reglas para agentes
1. Todo contenido debe ser en español mexicano, tono cálido y cercano.
2. Las imágenes deben tener marca de agua de Glassitas.
3. Los posts deben alternar entre flyer diseñado y foto real de producto.
4. Las categorías de evento principales: XV años, Baby Shower, Bodas, Cumpleaños, Bautizo.
