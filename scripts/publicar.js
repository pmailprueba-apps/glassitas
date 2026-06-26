const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

const PAGE_URL = 'https://www.facebook.com/people/Glassitas/61591136832245/';
const PROFILE_DIR = path.join(__dirname, '..', '.fb-profile');
const sleep = ms => new Promise(r => setTimeout(r, ms));

async function main() {
  const args = process.argv.slice(2);
  const message = args[0] || "🍪 Glassitas — Galletas decoradas artesanales para tus eventos. Cotiza por WhatsApp!";
  const imagePath = args[1] ? path.resolve(args[1]) : null;

  console.log('Abriendo navegador...');
  const browser = await puppeteer.launch({
    headless: false,
    userDataDir: PROFILE_DIR,
    args: ['--no-sandbox', '--disable-dev-shm-usage', '--window-size=1280,900']
  });

  try {
    const page = await browser.newPage();
    await page.setViewport({ width: 1280, height: 900 });

    await page.goto(PAGE_URL, { waitUntil: 'networkidle2', timeout: 60000 });
    await sleep(5000);

    console.log('Abriendo el editor de publicaciones...');
    await page.goto('https://www.facebook.com/1111933412010777/publisher', {
      waitUntil: 'networkidle2', timeout: 60000
    }).catch(() => {});
    await sleep(4000);

    if (imagePath && fs.existsSync(imagePath)) {
      try {
        const [fileChooser] = await Promise.all([
          page.waitForFileChooser({ timeout: 5000 }).catch(() => null),
          page.evaluate(() => {
            const btns = document.querySelectorAll('[data-testid="media-attachment"], [aria-label="Foto/video"], [data-pagelet="MediaSection"]');
            for (const b of btns) b.click();
          }).catch(() => {})
        ]);
        if (fileChooser) {
          await fileChooser.accept([imagePath]);
          console.log('Imagen seleccionada');
          await sleep(4000);
        }
      } catch (e) {
        console.log('Upload manual necesario');
      }
    }

    const written = await page.evaluate((msg) => {
      const editors = document.querySelectorAll('[contenteditable="true"], [role="textbox"]');
      for (const e of editors) {
        if (e.offsetParent !== null) {
          e.focus();
          e.textContent = '';
          document.execCommand('insertText', false, msg);
          return true;
        }
      }
      return false;
    }, message);
    console.log(written ? 'Texto insertado' : 'Insertar texto manualmente');
    await sleep(2000);

    const clicked = await page.evaluate(() => {
      const btns = document.querySelectorAll('[aria-label="Publicar"], [aria-label="Publish"], [data-testid="react-composer-submit"]');
      for (const b of btns) {
        if (b.offsetParent !== null) { b.click(); return true; }
      }
      const spans = document.querySelectorAll('span');
      for (const s of spans) {
        if (s.textContent === 'Publicar' && s.offsetParent !== null) {
          s.click(); return true;
        }
      }
      return false;
    });

    if (clicked) {
      console.log('✅ Publicado!');
      await sleep(10000);
    } else {
      console.log('⚠️ No se encontro el boton Publicar');
      console.log('Completa la publicacion manualmente en la ventana abierta');
      await page.waitForFunction(
        () => !window.location.href.includes('publisher'),
        { timeout: 120000 }
      ).catch(() => {});
    }
  } catch (err) {
    console.error('Error:', err.message);
  }

  console.log('Cerrando en 15 segundos...');
  await sleep(15000);
  await browser.close();
}

main().catch(console.error);
