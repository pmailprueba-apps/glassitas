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
    console.log('  La sesion se guardara automaticamente.');
    console.log('  Cierra esta ventana cuando termines.');
    console.log('============================================');
    await page.waitForFunction(
      () => !window.location.href.includes('login'),
      { timeout: 300000 }
    ).catch(() => console.log('Timeout esperando login'));
    await sleep(3000);
  }

  console.log('✅ Sesion guardada en .fb-profile/');
  console.log('Ahora puedes publicar con: node scripts/publicar.js');
})().catch(console.error);
