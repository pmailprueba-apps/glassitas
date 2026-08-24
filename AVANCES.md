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
- [x] `pages_manage_posts` obtenido exitosamente
- [x] `scripts/post.js` configurado con Page Token via API (Graph API v19.0)
- [x] Publicación de texto e imagen funcionando
- [x] `contenido/calendario.json` con schedule
- [x] Automatización con GitHub Actions (emula sistema Cráneo Noble)
- [x] `scripts/publicar-glassitas.sh` — publicador bash+curl (sin Node), 2 slots/día
- [x] `.github/workflows/glassitas.yml` — corre 12:00 y 18:00 CDMX
- [x] `.glassitas-published.json` — estado anti-duplicados
- [x] ✅ Page Token regenerado el 21/08/26 (larga duración). PENDIENTE: actualizar secret `FB_PAGE_TOKEN` en GitHub Actions
- [ ] Configurar System User para token permanente (la app es tipo Games, necesita ser Business)
- [ ] Publicar manual (primera semana)

## Etapa 5 — Flyers y Posts Visuales

- [x] Plantillas de flyer por categoría de evento (9 banners 16:9 con marco floral generados)
- [x] Primeros posts generados (foto real + branding)
- [x] Marca de agua aplicada a todas las imágenes (en `assets/productos/con-marca/`)

## Etapa 6 — TikTok (futuro)

- [ ] Crear cuenta TikTok Business
- [x] Guión + textos para primeros videos (4 campañas en `generar_videos_tiktok.py`)
- [x] Videos generados (21/08/26): `tiktok_1_bodas`, `tiktok_2_babyshower`, `tiktok_3_slp`, `tiktok_4_infantil` (1080×1920, 7.5s, con marco)
- [ ] Publicar primer video
- [ ] 🔴 PENDIENTE: agregar música/audio a los videos TikTok (actualmente silenciosos)

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
| 25/06/26 | ✅✅✅ API DE FACEBOOK REPARADA! pages_manage_posts concedido. Post via API funcionando. |
| 21/08/26 | Instaladas 4278 fonts (~3300 familias): Google Fonts completo (3875 en `~/Library/Fonts/GoogleFonts/`) + packs Nerd Fonts vía brew (Fira Code, JetBrains, Cascadia, Hack, Geist). |
| 21/08/26 | Regenerado script `generar_facebook_ads.py`: banners 16:9 (1080×608) con **marco floral** (`escaleta.png`) como borde absoluto, logo fuera del centro, texto serif. Genera 9 anuncios (bodas/babyshower/infantil ×3). |
| 21/08/26 | ✅ TOKEN DE PÁGINA REGENERADO (Graph API Explorer → fb_exchange_token → token de página larga duración). Guardado en `.config.json` + `.token-page.txt`. Validado contra API. |
| 21/08/26 | ✅ WhatsApp CORREGIDO a **+52 4445 101 553** (era 444 650 6790). Actualizado en `generar_facebook_ads.py`, `generar_escaleta.py`, `GUIA_FACEBOOK.md`. |
| 21/08/26 | Publicadas en el feed las 36 fotos de producto (`con_marco_blanco/4_5_Vertical_1080x1350`) con el número correcto. Detección y borrado de duplicados (prueba inicial). |
| 21/08/26 | Regenerados 4 videos TikTok con las **nuevas fotos con marco** (`9_16_Historias_1080x1920`): `tiktok_1_bodas`, `tiktok_2_babyshower`, `tiktok_3_slp`, `tiktok_4_infantil`. 1080×1920, 7.5s c/u, silenciosos. |
| 21/08/26 | Pendiente: agregar música/audio a los videos TikTok; decidir si incluir WhatsApp en los textos de TikTok; procesar nuevas fotos IMG_2541-2544.HEIC (en `~/Downloads`). |
