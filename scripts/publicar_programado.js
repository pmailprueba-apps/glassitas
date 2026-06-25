const { execSync } = require('child_process')
const fs = require('fs')
const path = require('path')

const NODE = process.execPath
const calendario = JSON.parse(fs.readFileSync('./contenido/calendario.json'))
const ahora = new Date()
const horaActual = `${String(ahora.getHours()).padStart(2, '0')}:${String(ahora.getMinutes()).padStart(2, '0')}`

const idxHora = calendario.horarios.findIndex(h => {
  const [hh, mm] = h.split(':').map(Number)
  const [ah, am] = horaActual.split(':').map(Number)
  return ah === hh && am >= mm - 10 && am <= mm + 10
})

if (idxHora === -1) {
  console.log(`Sin publicacion para las ${horaActual}`)
  process.exit(0)
}

const dias = ['Domingo', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
const hoy = dias[ahora.getDay()]
const carpeta = `./contenido/${hoy}`

if (!fs.existsSync(carpeta)) {
  console.log(`Carpeta ${carpeta} no existe`)
  process.exit(0)
}

const archivos = fs.readdirSync(carpeta)
  .filter(f => /\.(png|jpg|jpeg|webp)$/i.test(f))
  .sort()

if (archivos.length === 0) {
  console.log(`${carpeta} — sin imagenes`)
  process.exit(0)
}

const idxImg = Math.min(idxHora, archivos.length - 1)
const imgPath = path.resolve(carpeta, archivos[idxImg])
const post = calendario.dias[hoy]?.[idxHora]
const copy = post?.copy || `Glassitas — ${hoy}`

console.log(`Publicando: ${hoy} ${calendario.horarios[idxHora]}`)
const cmd = `${NODE} scripts/post.js "${copy.replace(/"/g, '\\"')}" "${imgPath}"`
execSync(cmd, { stdio: 'inherit' })
