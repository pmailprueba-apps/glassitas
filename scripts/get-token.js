const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

const PROFILE_DIR = path.join(__dirname, '..', '.fb-profile');
const APP_ID = '2931073960575850';
const REDIRECT_URI = 'https://www.facebook.com/connect/login_success.html';
const SCOPE = 'pages_manage_posts,pages_read_engagement,business_management';
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const browser = await puppeteer.launch({
    headless: false,
    userDataDir: PROFILE_DIR,
    args: ['--no-sandbox', '--disable-dev-shm-usage', '--window-size=1100,800']
  });
  const page = await browser.newPage();

  const oauthUrl = `https://www.facebook.com/v19.0/dialog/oauth?client_id=${APP_ID}&redirect_uri=${REDIRECT_URI}&scope=${SCOPE}&response_type=token&display=popup&auth_type=rerequest`;

  await page.goto(oauthUrl, { waitUntil: 'networkidle2', timeout: 60000 });
  await sleep(5000);

  const url = page.url();
  console.log('URL actual:', url);

  if (url.includes('login')) {
    console.log('Sesion expirada, re-login necesario...');
    await page.goto('https://www.facebook.com/', { waitUntil: 'networkidle2' });
    await sleep(3000);
    await page.goto(oauthUrl, { waitUntil: 'networkidle2' });
    await sleep(5000);
  }

  if (url.includes('login_success') || url.includes('access_token=')) {
    const token = url.match(/access_token=([^&]+)/);
    if (token) {
      console.log('\n✅ TOKEN OBTENIDO!');
      const t = decodeURIComponent(token[1]);
      console.log(t);
      fs.writeFileSync('./.token-nuevo.txt', t);
      console.log('Guardado en .token-nuevo.txt');
    }
  } else {
    const buttons = await page.evaluate(() => {
      return Array.from(document.querySelectorAll('[role="button"], button'))
        .filter(b => b.offsetParent !== null)
        .map(b => b.innerText?.substring(0, 50) || b.getAttribute('aria-label') || '?');
    });
    console.log('Botones disponibles:', buttons);
    console.log('\nRevisa la ventana de Chrome abierta y acepta los permisos');
    console.log('Se esperara hasta 2 minutos...');

    await page.waitForFunction(
      () => window.location.href.includes('login_success') || window.location.href.includes('access_token='),
      { timeout: 120000 }
    ).catch(() => {});

    const finalUrl = page.url();
    console.log('URL final:', finalUrl);
    const token = finalUrl.match(/access_token=([^&]+)/);
    if (token) {
      console.log('\n✅ TOKEN OBTENIDO!');
      const t = decodeURIComponent(token[1]);
      console.log(t);
      fs.writeFileSync('./.token-nuevo.txt', t);
    } else {
      console.log('No se obtuvo token');
    }
  }

  await sleep(10000);
  await browser.close();
})();
