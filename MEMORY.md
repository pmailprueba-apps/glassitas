# Glassitas — Memoria de Sesión (44-glassitas)

> Memoria manual por proyecto (MEMANTO descontinuado). Se inyecta con el avance de cada sesión.

---

## 21 Ago 2026 — Campaña Facebook + TikTok con marco floral y token regenerado (INYECTADO MANUALMENTE)

### Contexto de sesión
- Se trabajó desde opencode en el Mac Mini.
- Autorización de proyecto numerado con contraseña `1481`.

### Datos del negocio (importantes)
- **WhatsApp correcto del negocio: `+52 4445 101 553`** (10 dígitos, lada 4445).
- ⚠️ El número `+52 444 650 6790` era ERRÓNEO (pertenece al proyecto Restaurante Viky). Se corrigió en todos lados.
- Página de Facebook Glassitas: **ID `1111933412010777`** (fan_count 1).
- App Publishers: ID `2931073960575850` (tipo Games).
- Sitio web: https://pmailprueba-apps.github.io/glassitas/

### Login / Token de Facebook
- El token de página anterior había expirado (25-jun-2026).
- Se regeneró HOY: Graph API Explorer → `fb_exchange_token` (APP_ID + APP_SECRET) → token de página de larga duración.
- Guardado en `.config.json` (`PAGE_TOKEN`) y `.token-page.txt`.
- **Validado contra API: funciona.**
- 🔴 PENDIENTE: actualizar el secret `FB_PAGE_TOKEN` en GitHub Actions con el nuevo token (el workflow automático 2x/día usa el secret, no `.config.json`).

### Fotografía de producto
- 36 fotos de producto, en 4 formatos de marco bajo `assets/productos/con_marco_blanco/`:
  - `191_1_Horizontal_1200x630` → (1200×630)
  - `1_1_Cuadrado_1080x1080` → (1080×1080)
  - `4_5_Vertical_1080x1350` → (1080×1350)
  - `9_16_Historias_1080x1920` → (1080×1920)
- Nuevas fotos entrantes: `IMG_2541-2544.HEIC` en `/Users/alexram/Downloads` (12-ago). PENDIENTE procesar.

### Anuncios de Facebook (banners)
- `scripts/generar_facebook_ads.py` actualizado para usar el **marco floral** `assets/logo/escaleta.png` como borde absoluto.
- Formato **16:9 (1080×608)** — porque el marco floral es horizontal (ratio 1.81). No forzar a cuadrado (distorsiona las flores).
- Genera 9 anuncios: bodas, babyshower, infantil (3 c/u) → `assets/posts/facebook/fb_*.jpg`.
- Diseño: foto de galletas al centro, logo esquina inferior izquierda (fuera del centro, no tapa el producto), texto serif (Georgia), CTA dorado, sin bloques sólidos.

### Publicación en Facebook
- Publicadas las 36 fotos de producto (4:5) en el feed con el mensaje + WhatsApp correcto.
- Se detectó y eliminó 1 duplicado (prueba inicial repetida).
- Se corrigió el número (primera vez con `445 101 553` erróneo → re-publicado con `4445 101 553`).

### Videos de TikTok (con frases)
- `scripts/generar_videos_tiktok.py` (239 líneas) genera videos 1080×1920 (9:16).
- **Se cambió `IMG_DIR`** a `assets/productos/con_marco_blanco/9_16_Historias_1080x1920` (fotos nuevas con marco).
- Regenerados HOY 4 videos: `tiktok_1_bodas`, `tiktok_2_babyshower`, `tiktok_3_slp`, `tiktok_4_infantil` → `assets/posts/tiktok/*.mp4`.
- 7.5s c/u (3 clips × 2.5s), animación Ken Burns + pop-in de texto.
- **🔴 SIN AUDIO (silenciosos)** — requieren música para TikTok.
- Textos actuales NO mencionan el WhatsApp (usан "COTIZA AQUÍ/EN EL LINK").

### Textos y Hashtags TikTok (proporcionados al usuario)
- 4 campañas con 3 frases c/u + hashtags sugeridos por nicho (bodas/babyshower/SLP/infantil) + generales.

### Sistema (config)
- 4278 fonts instaladas en sistema (~3300 familias): Google Fonts completo + Nerd Fonts.

### Fuentes
- Todo verificado contra la API de Graph de Facebook en tiempo real (borrado y publicación con `curl`).
- Modelo de visión local `llava:7b` NO confiable para descripción de imágenes (dio textos inventados). Verificar visualmente con el usuario o por píxeles.

### Confidence / Provenance
- Confidence: 1.0 (hechos verificados por API y ejecución real, no simulada).
- Provenance: validated / observed / corrected (`1481`).

---

---

## 22 Ago 2026 — Tienda online por evento + referencia de costos fotogalletas (INYECTADO MANUALMENTE)

### Contexto
- Trabajo desde opencode en Mac Mini. Proyecto numerado, autorización `1481`.

### Tienda online (`tienda.html`) — NUEVA
- Se creó/reescribió `tienda.html` en la raíz del proyecto (no se tocó `index.html`).
- **Organizada POR EVENTO** (como fotogalletas.com), con 9 categorías en la galería:
  Baby Shower, Bautizo, Comunión, Boda, Cumpleaños, XV, Logotipo/Corporativo, Institucional, Graduación.
- **Cada categoría tiene su propio TEXTO DESCRIPTIVO** (adaptado y redactado limpio, sin copiar literal al competidor).
- Cada categoría con botón "Cotizar por WhatsApp" (wa.me **524445101553**).
- Conserva el catálogo por FORMA (circular, cuadrada, rectangular, corazón) con precios de referencia.
- Usa SOLO fotos propias de Glassitas (`assets/productos/con_marco_blanco/1_1_Cuadrado_1080x1080/`).
- Verificado con Playwright: 9 categorías, 0 imágenes rotas, 0 errores de consola, respuestas de clic OK.

### Referencia interna de Fotogalletas (`contenido/referencia_fotogalletas/`) — NO PUBLICAR
- Muestreo de 8 imágenes por cada una de las 9 categorías (72) + 10 formas + 8 banners = 90 archivos.
- ⚠️ **COPYRIGHT:** Imágenes de Grupo Tentasi S.A. de C.V. (fotogalletas.com). SOLO referencia interna.
  **NO publicar en la tienda.** Para Glassitas siempre usar fotos propias.
- README.md dentro documenta origen, condiciones de uso y precios de referencia (menudeo y mayoreo).

### WhatsApp correcto
- `+52 4445 101 553` → wa.me **524445101553**. El `index.html` viejo aún tiene el número ERRÓNEO (5214446506790, del restaurante Viky); pendiente corregir.

### Precios de referencia (fotogalletas, útil para tabla de costos)
- Menudeo: 4cm $19 · 5-5.3cm $24 · 6×4.5cm $25 · 7×7/7.5×5.5cm $35 · 7-7.5 circular $39 · 8-8.5cm $44.
- Mayoreo ver README de referencia. Envío DHL $195 de 20-300 galletas. Min 20 por diseño.

### Confidence / Provenance
- Confidence 1.0 (verificado por ejecución real en Playwright y descarga real de archivos).
- Provenance: validated / observed / corrected (`1481`).

---

## 22 Ago 2026 — Página de Preguntas Frecuentes (FAQ) (INYECTADO MANUALMENTE)

### Nuevo archivo: `preguntas-frecuentes.html`
- Página de FAQ creada en la raíz del proyecto, adaptada de la información de fotogalletas (no copia literal, reescrita para Glassitas).
- **16 preguntas** en acordeón interactivo (sin JS de librerías, JS vanilla):
  pedido mínimo, tamaños y precios (tabla 6 filas), ingredientes, imagen comestible, cómo pedir, antelación, envíos/USA, mayoreo, obleas vs papel de azúcar, costo de diseño, caducidad, pagos, factura, por qué se paga al pedir, almacenamiento, otros productos.
- Precios de referencia usados: 4.0 $19 · 5.0 $24 · 7.5 $39 · 8.5 $44 · rect 6×4.5 $25 · 7.5×5.5 $35.
- WhatsApp correcto en todo: wa.me **524445101553**.
- Se agregó enlace "Preguntas" al nav y footer de `tienda.html`.
- Verificado con Playwright: 16 preguntas, acordeón OK (1 abierta a la vez), tablas OK, 0 errores.

### Confidence / Provenance
- Confidence 1.0 (verificado por ejecución en Playwright).
- Provenance: validated / observed / corrected (`1481`).

---

## 22 Ago 2026 — Fotos de la competencia INSERTADAS en la tienda (decisión del usuario) (INYECTADO MANUALMENTE)

### Decisión del usuario (advertencia legal firmada)
- El usuario pidió explícitamente **insertar las fotos de Fotogalletas en la tienda EN LÍNEA**.
- Le advertí del riesgo de copyright (fotos de Grupo Tentasi, competencia directa, posible DMCA/takedown/competencia desleal).
- El usuario eligió publicarlas de todos modos. **Queda constancia de que fue advertido y decidió conscientemente.**

### Implementación en `tienda.html`
- Miniaturas de las 9 categorías de evento → foto real de la categoría descargada de fotogalletas.
- Cada galería de categoría → 8 fotos reales de esa categoría.
- Rutas: `contenido/referencia_fotogalletas/categorias/<carpeta>/img_N.jpg` (desde la raíz del repo).
- Constante `REF_BASE` y campo `fotos` por evento en el JS.
- Verificado con Playwright: 9 categorías, 0 imágenes rotas, 0 errores.

### ⚠️ RIESGO LEGAL ABIERTO
- La tienda publicada ahora usa fotos con copyright de un competidor. Si Green/Tentasi lo detecta, puede pedir retiro (DMCA) y tumban el sitio.
- **Recomendación futura:** reemplazar por fotos propias de Glassitas organizadas por evento cuando se tengan.

### Confidence / Provenance
- Confidence 1.0 (verificado por ejecución en Playwright; decisión explícita del usuario).
- Provenance: validated / corrected (`1481`), riesgo observado.
