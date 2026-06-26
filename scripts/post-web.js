const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

const PAGE_URL = 'https://www.facebook.com/people/Glassitas/61591136832245/';
const PROFILE_DIR = path.join(__dirname, '..', '.fb-profile');
const sleep = ms => new Promise(r => setTimeout(r, ms));

async function main() {
  const message = process.argv[2] || "🍪 Glassitas — Galletas decoradas artesanales";
  const imagePath = process.argv[3] ? path.resolve(process.argv[3]) : null;

  console.log('Abriendo navegador...');
  const browser = await puppeteer.launch({
    headless: false,
    userDataDir: PROFILE_DIR,
    args: ['--no-sandbox', '--disable-dev-shm-usage', '--window-size=1200,900']
  });

  try {
    const page = await browser.newPage();
    await page.setViewport({ width: 1200, height: 900 });
    console.log('Navegando a la pagina de Glassitas...');
    await page.goto(PAGE_URL, { waitUntil: 'networkidle2', timeout: 60000 });
    await sleep(5000);

    if (page.url().includes('login')) {
      console.log('Requiere login. Hazlo manualmente en la ventana del navegador.');
      console.log('Esperando 60 segundos...');
      await new Promise(r => setTimeout(r, 60000));
      await page.goto(PAGE_URL, { waitUntil: 'networkidle2' });
      await sleep(5000);
    }

    console.log('Buscando la caja de crear publicacion...');
    const clicked = await page.evaluate(() => {
      const buttons = document.querySelectorAll('[aria-label="Crear publicación"], [aria-label="Escribe algo..."], [aria-label="Create post"]');
      for (const b of buttons) {
        b.click();
        return true;
      }
      return false;
    });

    if (!clicked) {
      console.log('No se encontro boton de crear publicacion, intentando click en el area del timeline...');
    }

    await sleep(3000);

    if (imagePath && fs.existsSync(imagePath)) {
      console.log('Subiendo imagen...');
      const fileInput = await page.$('input[type="file"]');
      if (fileInput) {
        await fileInput.uploadFile(imagePath);
        await sleep(3000);
      }
    }

    console.log('Escribiendo mensaje...');
    const textBox = await page.$('[aria-label="Escribe algo..."], [role="textbox"], div[contenteditable="true"]');
    if (textBox) {
      await textBox.type(message, { delay: 30 });
      await sleep(1000);
    }

    console.log('Publicando...');
    const publishBtn = await page.$('[aria-label="Publicar"], [aria-label="Publish"], [label="Publicar"]');
    if (publishBtn) {
      await publishBtn.click();
      console.log('Publicado!');
    } else {
      console.log('Boton de publicar no encontrado');
    }

    await sleep(5000);
    console.log('Listo!');
  } catch (err) {
    console.error('Error:', err.message);
  }

  console.log('Cerrando en 10 segundos...');
  await sleep(10000);
  await browser.close();
}

main().catch(console.error);
