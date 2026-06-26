const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const browser = await puppeteer.launch({
    headless: false,
    userDataDir: path.join(__dirname, '..', '.fb-profile'),
    args: ['--no-sandbox', '--window-size=1100,850']
  });
  const page = await browser.newPage();

  await page.goto('https://www.facebook.com/v19.0/dialog/oauth?client_id=2931073960575850&redirect_uri=https://www.facebook.com/connect/login_success.html&scope=pages_manage_posts,pages_read_engagement,business_management&response_type=token', { waitUntil: 'networkidle2', timeout: 30000 });
  await sleep(3000);
  
  console.log('=== LLENANDO CREDENCIALES ===');
  await page.type('input[name="email"]', 'alexram80@me.com', { delay: 10 });
  await page.type('input[name="pass"]', 'Ironfloor88LE@N', { delay: 10 });
  await sleep(500);
  await page.evaluate(() => document.querySelector('input[type="submit"]').click());
  await sleep(3000);
  
  if (page.url().includes('two_step')) {
    console.log('=== 2FA DETECTADO ===');
    console.log('REVISA TU TELEFONO Y APRUEBA');
    console.log('Esperando...');
    while (page.url().includes('two_step')) {
      await sleep(3000);
    }
    await sleep(5000);
    console.log('2FA PASO! URL:', page.url().substring(0, 150));
  }

  const finalUrl = page.url();
  if (finalUrl.includes('access_token=')) {
    const token = decodeURIComponent(finalUrl.match(/access_token=([^&]+)/)[1]);
    console.log('\n=== ✅ TOKEN OBTENIDO ===');
    fs.writeFileSync('./.token-final.txt', token);
    console.log(token.substring(0, 60) + '...');
  } else {
    const text = await page.evaluate(() => document.body.innerText.substring(0, 500));
    console.log('Respuesta:', text.substring(0, 200));
    
    // Maybe it shows permissions dialog instead
    const clicked = await page.evaluate(() => {
      const items = document.querySelectorAll('[role="button"], button, a[role="button"]');
      for (const el of items) {
        const t = (el.innerText || '').toLowerCase();
        if ((t.includes('continuar') || t.includes('continue')) && el.offsetParent !== null) {
          el.click(); return true;
        }
      }
      return false;
    });
    if (clicked) {
      await sleep(5000);
      const u2 = page.url();
      if (u2.includes('access_token=')) {
        const token = decodeURIComponent(u2.match(/access_token=([^&]+)/)[1]);
        console.log('\n=== ✅ TOKEN OBTENIDO ===');
        fs.writeFileSync('./.token-final.txt', token);
        console.log(token.substring(0, 60) + '...');
      } else {
        console.log('URL final:', u2.substring(0, 200));
      }
    }
  }
  
  await sleep(15000);
  await browser.close();
})();
