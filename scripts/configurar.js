const puppeteer = require('puppeteer');
const path = require('path');

const PROFILE_DIR = path.join(__dirname, '..', '.fb-profile');
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const browser = await puppeteer.launch({
    headless: false,
    userDataDir: PROFILE_DIR,
    args: ['--no-sandbox', '--disable-dev-shm-usage', '--window-size=1280,900']
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 900 });
  await page.goto('https://www.facebook.com/', { waitUntil: 'networkidle2', timeout: 60000 });
  await sleep(3000);

  const isLogin = page.url().includes('login');
  if (isLogin) {
    console.log('============================================');
    console.log('  INICIA SESION EN LA VENTANA DE CHROME');
    console.log('  Cuando termines, cierra la ventana.');
    console.log('============================================');
    while (page.url().includes('login')) {
      await sleep(3000);
    }
    await sleep(3000);
    await page.goto('https://www.facebook.com/people/Glassitas/61591136832245/', {
      waitUntil: 'networkidle2', timeout: 60000
    });
    await sleep(3000);
  }

  console.log('============================================');
  console.log('  SESION GUARDADA');
  console.log('  Puedes publicar desde esta ventana');
  console.log('  o cerrarla cuando termines.');
  console.log('  Proximo paso: node scripts/publicar.js');
  console.log('============================================');
})().catch(console.error);
