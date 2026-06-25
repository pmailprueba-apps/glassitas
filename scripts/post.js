const https = require('https')
const fs = require('fs')
const path = require('path')

const config = require('../.config.json')
const PAGE_ID = config.PAGE_ID
const PAGE_TOKEN = process.env.PAGE_TOKEN || config.PAGE_TOKEN
const IG_ID = config.IG_USER_ID
const FB_PROFILE = config.FB_PROFILE_DIR || './.fb-profile'

function graphPost(endpoint, data, isMultipart = false) {
  return new Promise((resolve, reject) => {
    const url = new URL(`https://graph.facebook.com/v22.0${endpoint}`)
    const options = { method: 'POST', headers: {} }

    if (isMultipart) {
      options.headers = data.headers
      const req = https.request(url, options, res => {
        let body = ''
        res.on('data', c => body += c)
        res.on('end', () => {
          try { resolve(JSON.parse(body)) }
          catch { resolve(body) }
        })
      })
      req.write(data.body)
      req.end()
    } else {
      const body = new URLSearchParams(data).toString()
      options.headers['Content-Type'] = 'application/x-www-form-urlencoded'
      options.headers['Content-Length'] = Buffer.byteLength(body)
      const req = https.request(url, options, res => {
        let body = ''
        res.on('data', c => body += c)
        res.on('end', () => {
          try { resolve(JSON.parse(body)) }
          catch { resolve(body) }
        })
      })
      req.write(body)
      req.end()
    }
  })
}

function graphGet(endpoint) {
  return new Promise((resolve, reject) => {
    https.get(`https://graph.facebook.com/v22.0${endpoint}`, res => {
      let body = ''
      res.on('data', c => body += c)
      res.on('end', () => {
        try { resolve(JSON.parse(body)) }
        catch { resolve(body) }
      })
    })
  })
}

function makeMultipart(fields, filePath) {
  const boundary = '----Boundary' + Math.random().toString(36).slice(2)
  const fileData = fs.readFileSync(filePath)
  const fileName = path.basename(filePath)

  let body = ''
  for (const [k, v] of Object.entries(fields)) {
    body += `--${boundary}\r\nContent-Disposition: form-data; name="${k}"\r\n\r\n${v}\r\n`
  }
  body += `--${boundary}\r\nContent-Disposition: form-data; name="source"; filename="${fileName}"\r\nContent-Type: image/jpeg\r\n\r\n`

  const buffer = Buffer.concat([
    Buffer.from(body),
    fileData,
    Buffer.from(`\r\n--${boundary}--\r\n`)
  ])

  return {
    headers: {
      'Content-Type': `multipart/form-data; boundary=${boundary}`,
      'Content-Length': buffer.length
    },
    body: buffer
  }
}

async function postToFacebook(imagePath, message) {
  const fullPath = path.resolve(imagePath)
  if (!fs.existsSync(fullPath)) {
    console.error(`Archivo no encontrado: ${fullPath}`)
    process.exit(1)
  }
  console.log(`Facebook — Subiendo foto...`)

  const multipart = makeMultipart({ message, access_token: PAGE_TOKEN }, fullPath)
  const result = await graphPost(`/${PAGE_ID}/photos`, multipart, true)
  if (result.error) {
    console.error('Error Facebook:', result.error.message)
    process.exit(1)
  }
  console.log(`Facebook — Publicada! ID: ${result.id}`)
  return result
}

async function postText(message) {
  console.log('Publicando texto en Facebook...')
  const result = await graphPost(`/${PAGE_ID}/feed`, { message, access_token: PAGE_TOKEN })
  if (result.error) {
    console.error('Error Facebook:', result.error.message)
    process.exit(1)
  }
  console.log(`Facebook — Publicado! ID: ${result.id}`)
  return result
}

async function postToInstagram(imagePath, caption) {
  if (!IG_ID) {
    console.log('Instagram: IG_USER_ID no configurado')
    return null
  }
  const fullPath = path.resolve(imagePath)
  if (!fs.existsSync(fullPath)) {
    console.error(`Archivo no encontrado: ${fullPath}`)
    return null
  }
  console.log(`Instagram — Subiendo foto a Facebook CDN...`)

  const multipart = makeMultipart({ access_token: PAGE_TOKEN, published: 'false' }, fullPath)
  const fbPhoto = await graphPost(`/${PAGE_ID}/photos`, multipart, true)
  if (fbPhoto.error) {
    console.error('Error al subir a Facebook (CDN):', fbPhoto.error.message)
    return null
  }

  console.log(`   Obteniendo URL...`)
  const photoData = await graphGet(`/${fbPhoto.id}?fields=images&access_token=${PAGE_TOKEN}`)
  const imageUrl = photoData?.images?.[0]?.source

  if (!imageUrl) {
    console.error('No se pudo obtener URL de CDN')
    return null
  }

  console.log(`   Creando contenedor en Instagram...`)
  const container = await graphPost(`/${IG_ID}/media`, {
    image_url: imageUrl,
    caption: caption,
    access_token: PAGE_TOKEN
  })
  if (container.error) {
    console.error('Error Instagram (contenedor):', container.error.message)
    return null
  }
  console.log(`   Contenedor: ${container.id}`)

  await new Promise(r => setTimeout(r, 5000))

  console.log(`   Publicando en Instagram...`)
  const result = await graphPost(`/${IG_ID}/media_publish`, {
    creation_id: container.id,
    access_token: PAGE_TOKEN
  })
  if (result.error) {
    console.error('Error Instagram (publicar):', result.error.message)
    return null
  }
  console.log(`Instagram — Publicada! ID: ${result.id}`)
  return result
}

async function main() {
  const args = process.argv.slice(2)
  const onlyInstagram = args.includes('--ig-only')
  const onlyFacebook = args.includes('--fb-only')
  const showHelp = args.length === 0

  if (showHelp) {
    console.log(`
Uso: node scripts/post.js <mensaje> [imagen] [flags]

Flags:
  --ig-only     Solo Instagram
  --fb-only     Solo Facebook

Ejemplos:
  node scripts/post.js "Hola Glassitas!"
  node scripts/post.js "Nuevas galletas!" "assets/productos/foto.jpg"
  node scripts/post.js "Texto!" "ruta/imagen.jpg" --ig-only
    `)
    process.exit(0)
  }

  const message = args[0]
  const imagePath = args[1] && !args[1].startsWith('--') ? args[1] : null

  const doFacebook = !onlyInstagram
  const doInstagram = !onlyFacebook && !!imagePath

  if (doFacebook) {
    if (imagePath) await postToFacebook(imagePath, message)
    else await postText(message)
  }

  if (doInstagram && imagePath) {
    await postToInstagram(imagePath, message)
  }
}

main().catch(console.error)
