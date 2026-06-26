const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

const PAGE_URL = 'https://www.facebook.com/people/Glassitas/61591136832245/';
const PROFILE_DIR = path.join(__dirname, '..', '.fb-profile');
const sleep = ms => new Promise(r => setTimeout(r, ms));

async function main() {
  const args = process.argv.slice(2);
  if (args.length === 0 || args[0] === '--help') {
    console.log(`Uso: node scripts/post.js "mensaje" [imagen]`);
    process.exit(0);
  }

  const message = args[0];
  const imagePath = args[1] && !args[1].startsWith('--') ? path.resolve(args[1]) : null;

  if (imagePath && !fs.existsSync(imagePath)) {
    console.error(`Archivo no encontrado: ${imagePath}`);
    process.exit(1);
  }

  console.log('Abriendo Facebook en el navegador...');
  const browser = await puppeteer.launch({
    headless: false,
    userDataDir: PROFILE_DIR,
    args: ['--no-sandbox', '--disable-dev-shm-usage', '--window-size=1280,900']
  });

  try {
    const page = await browser.newPage();
    await page.setViewport({ width: 1280, height: 900 });

    console.log('Navegando a la pagina de Glassitas...');
    await page.goto(PAGE_URL, { waitUntil: 'networkidle2', timeout: 90000 });
    await sleep(5000);

    if (page.url().includes('login') || (await page.$('input[name="email"]'))) {
      console.log('Necesitas iniciar sesion en la ventana del navegador.');
      console.log('Esperando hasta 120 segundos a que inicies sesion...');
      for (let i = 0; i < 24; i++) {
        await sleep(5000);
        const url = page.url();
        if (!url.includes('login') && !(await page.$('input[name="email"]'))) {
          console.log('Sesion detectada!');
          break;
        }
      }
      await page.goto(PAGE_URL, { waitUntil: 'networkidle2' });
      await sleep(5000);
    }

    await page.evaluate(() => {
      const btns = document.querySelectorAll('[aria-label="Crear publicación"], [aria-label="Escribe algo..."], [aria-label="Create post"]');
      for (const b of btns) { b.click(); return; }
    });
    await sleep(3000);

    if (imagePath) {
      const fileInput = await page.$('input[type="file"]');
      if (fileInput) {
        await fileInput.uploadFile(imagePath);
        await sleep(3000);
        console.log('Imagen subida');
      }
    }

    const textBox = await page.$('div[contenteditable="true"][aria-label], [role="textbox"]');
    if (textBox) {
      await textBox.type(message, { delay: 20 });
      await sleep(1000);
      console.log('Texto escrito');
    }

    await page.evaluate(() => {
      const btns = document.querySelectorAll('[aria-label="Publicar"], [aria-label="Publish"]');
      for (const b of btns) {
        if (b.offsetParent !== null) { b.click(); return; }
      }
    });
    await sleep(3000);
    console.log('Publicacion enviada!');
    console.log(`\nMensaje: ${message.substring(0, 60)}...`);
    if (imagePath) console.log(`Imagen: ${path.basename(imagePath)}`);

    await sleep(5000);
  } catch (err) {
    console.error('Error:', err.message);
  }

  console.log('\nCerrando navegador en 15 segundos...');
  await sleep(15000);
  await browser.close();
}

main().catch(console.error);
