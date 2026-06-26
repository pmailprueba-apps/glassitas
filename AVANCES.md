# Glassitas — Avances y Checklist

> Proyecto: `44-glassitas`
> Inicio: 25 junio 2026

---

## Etapa 1 — Fundación

- [x] Crear estructura de directorios
- [x] `.agents/product-marketing.md` — contexto de negocio
- [x] `.agents/AGENTS.md` — instrucciones del proyecto
- [x] `CLAUDE.md` — reglas de codificación
- [x] Logo "Glassitas" colocado en `assets/logo/` (SVG + PNG)
- [x] Fotos de producto en `assets/productos/` (36 imágenes)
- [x] Paleta de colores + tipografías definidas
- [x] `scripts/overlay_logo.py` — marca de agua ejecutado ✓
- [x] Token de Facebook actualizado en `.config.json`
- [x] `scripts/post.js` — publicador por navegador (Puppeteer)

## Etapa 2 — Contenido + Copys

- [x] `marketing/ESTRATEGIA_360.md` — estrategia completa
- [x] `marketing/CALENDARIO_30_DIAS.md` — calendario editorial
- [x] `marketing/COPYS/15-anos.md` — textos para XV años
- [x] `marketing/COPYS/baby-shower.md` — textos para baby shower
- [x] `marketing/COPYS/bodas.md` — textos para bodas
- [x] `marketing/COPYS/generales.md` — textos para otros eventos
- [x] `marketing/prompts-imagenes.md` — prompts para IA
- [x] `marketing/respuestas-comerciales.md` — respuestas para clientes

## Etapa 3 — Landing Page (web/)

- [x] `index.html` — hero + galería + WhatsApp CTA
- [x] Diseño responsive (móvil primero)
- [x] Publicar en GitHub Pages → https://pmailprueba-apps.github.io/glassitas/

## Etapa 4 — Redes Sociales

- [x] Crear página de Facebook "Glassitas" → ID: 1111933412010777
- [x] Instagram convertido a Business (@alexram80)
- [ ] Vincular Instagram a página Glassitas (desde Centro de cuentas)
- [x] App Glassitas Publisher creada (ID: 2931073960575850)
- [x] System User "Glassitas bot" creado (ID: 122094378873384233)
- [x] Business Manager "Glassitas Publisher" (ID: 989666967381176)
- [x] `scripts/generar-token-system-user.js` — script para generar token permanente
- [ ] **PENDIENTE**: Solicitar `pages_manage_posts` via App Review en:
      https://developers.facebook.com/apps/2931073960575850/app-review/
- [ ] Después de App Review, ejecutar: `ADMIN_TOKEN="EAA..." node scripts/generar-token-system-user.js`
- [ ] `scripts/post.js` configurado con token de System User
- [ ] Publicar manual (primera semana)
- [ ] `contenido/calendario.json` con schedule
- [ ] Automatizar publicación con cron/Docker

## Etapa 5 — Flyers y Posts Visuales

- [ ] Plantillas de flyer por categoría de evento
- [ ] Primeros 10 posts generados (flyer + foto real)
- [x] Marca de agua aplicada a todas las imágenes (en `assets/productos/con-marca/`)

## Etapa 6 — TikTok (futuro)

- [ ] Crear cuenta TikTok Business
- [ ] Guión para primeros 3 videos (proceso de decoración)
- [ ] Publicar primer video

## Etapa 7 — Anuncios (futuro)

- [ ] Campaña Meta Ads para XV años
- [ ] Campaña Meta Ads para Baby Shower
- [ ] Segmentación San Luis Potosí

---

## Notas

| Fecha | Avance |
|-------|--------|
| 25/06/26 | Estructura inicial creada, 15 archivos, web publicada en GitHub Pages |
| 25/06/26 | Logo + 36 fotos de producto + marca de agua aplicada |
| 25/06/26 | Repo: pmailprueba-apps/glassitas → push a main |
| 25/06/26 | Nuevo token FB + Puppeteer instalado. IG Business convertido (@alexram80) |
| 25/06/26 | App Glassitas Publisher (ID: 2931073960575850) + System User (122094378873384233) |
| 25/06/26 | Token generation vía System User FUNCIONA (appsecret_proof) — falta pages_manage_posts en la app |
| 25/06/26 | 🔴 BLOQUEANTE: Meta eliminó pages_manage_posts para apps nuevas. Requiere App Review. |
