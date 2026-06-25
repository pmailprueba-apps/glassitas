# Guía para Configurar Facebook e Instagram de Glassitas

## 1. Crear Página de Facebook

1. Ve a https://www.facebook.com/pages/create
2. Categoría: **Servicios locales** > **Panadería / Repostería**
3. Nombre: **Glassitas**
4. Sube el logo de `assets/logo/logo-glassitas.svg` o `logo-glassitas.png`
5. Agrega:
   - Descripción: Galletas decoradas artesanales para tus eventos especiales. XV años, baby showers, bodas y más. 🍪 San Luis Potosí.
   - Horario: Lunes a Domingo
   - Ubicación: San Luis Potosí, SLP
   - WhatsApp: +52 444 650 6790
   - Sitio web: https://pmailprueba-apps.github.io/glassitas/

## 2. Configurar Instagram Business

1. Desde la página de Facebook > Configuración > Instagram
2. Vincula o crea una cuenta de Instagram: **@glassitas**
3. Biografía:
   ```
   🍪 Galletas decoradas para tus eventos
   🎀 XV | Baby Shower | Bodas | Cumpleaños
   📍 San Luis Potosí
   📲 Cotiza por DM
   ```

## 3. Obtener Tokens para Post.js

### Opción A: Graph API Explorer (fácil, token de 2 meses)
1. Ve a https://developers.facebook.com/tools/explorer/
2. Selecciona tu app o crea una nueva (tipo Negocio)
3. Permisos: `pages_manage_posts`, `pages_read_engagement`, `instagram_basic`, `instagram_content_publish`
4. Genera token → cópialo a `.config.json` como `PAGE_TOKEN`
5. Haz GET a `/{page-id}?fields=instagram_business_account` para obtener el `IG_USER_ID`

### Opción B: Token Permanente (recomendado)
Sigue: Meta Business Suite > Configuración > Usuarios del sistema > Crear token
- Permisos: `pages_manage_posts`, `instagram_basic`, `instagram_content_publish`
- El token dura 60 días o es permanente si usas System User

## 4. Probar Publicación

```bash
node scripts/post.js "Hola Glassitas! Primera publicación 🤖" --fb-only
```

Si funciona:
```bash
node scripts/post.js "Probando con foto!" "assets/productos/con-marca/14396917-52d9-4685-8103-2a31c5021a75.JPG"
```
