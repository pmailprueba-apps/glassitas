const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

const PROFILE_DIR = path.join(__dirname, '..', '.fb-profile');
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const browser = await puppeteer.launch({
    headless: false,
    userDataDir: PROFILE_DIR,
    args: ['--no-sandbox', '--disable-dev-shm-usage', '--window-size=1280,900']
  });
  const page = await browser.newPage();

  // Go to Graph API Explorer with our app selected
  await page.goto('https://developers.facebook.com/tools/explorer/?app_id=2931073960575850', {
    waitUntil: 'networkidle2', timeout: 60000
  });
  await sleep(5000);

  const url = page.url();
  console.log('URL:', url);

  if (url.includes('login')) {
    console.log('Redirigido a login. Navegando a Facebook primero...');
    await page.goto('https://www.facebook.com/', { waitUntil: 'networkidle2' });
    await sleep(4000);
    console.log('URL FB:', page.url());

    if (!page.url().includes('login')) {
      console.log('Sesion activa en Facebook!');
      await page.goto('https://developers.facebook.com/tools/explorer/?app_id=2931073960575850', {
        waitUntil: 'networkidle2', timeout: 60000
      });
      await sleep(5000);
    }
  }

  console.log('URL final:', page.url());
  
  // Take screenshot
  await page.screenshot({ path: '/tmp/explorer.png' });
  console.log('Screenshot guardado');

  // Get page content / buttons
  const info = await page.evaluate(() => {
    const buttons = Array.from(document.querySelectorAll('[role=\"button\"], button, [data-testid]'))
      .filter(b => b.offsetParent !== null)
      .map(b => ({
        text: (b.innerText || '').substring(0, 60),
        aria: b.getAttribute('aria-label') || '',
        testid: b.getAttribute('data-testid') || ''
      }));
    return buttons.slice(0, 30);
  });
  console.log('Elementos:', JSON.stringify(info, null, 2));

  await sleep(100000);
  await browser.close();
})();
