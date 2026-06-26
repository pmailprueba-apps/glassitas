const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const browser = await puppeteer.launch({
    headless: false,
    userDataDir: path.join(__dirname, '..', '.fb-profile'),
    args: ['--no-sandbox', '--window-size=1000,800']
  });
  const page = await browser.newPage();

  console.log('========================================');
  console.log(' VENTANA DE CHROME ABIERTA');
  console.log(' INGRESA TUS CREDENCIALES Y APRUEBA 2FA');
  console.log(' YO ESPERO Y CAPTURO EL TOKEN');
  console.log('========================================');

  await page.goto(
    'https://www.facebook.com/v19.0/dialog/oauth?client_id=2931073960575850&redirect_uri=https://www.facebook.com/connect/login_success.html&scope=pages_manage_posts,pages_read_engagement,business_management&response_type=token',
    { waitUntil: 'networkidle2', timeout: 60000 }
  );

  // Wait for redirect to login_success (means token was granted)
  await page.waitForFunction(
    () => window.location.href.includes('login_success') || window.location.href.includes('access_token='),
    { timeout: 300000 }
  ).catch(() => {});

  const finalUrl = page.url();
  console.log('\nURL final:', finalUrl.substring(0, 200));

  if (finalUrl.includes('access_token=')) {
    const match = finalUrl.match(/access_token=([^&]+)/);
    if (match) {
      const token = decodeURIComponent(match[1]);
      console.log('\n✅ TOKEN OBTENIDO!');
      fs.writeFileSync('./.token-final.txt', token);
      console.log(token.substring(0, 60) + '...');

      // Try to use it
      const https = require('https');
      https.get(`https://graph.facebook.com/v19.0/1111933412010777?fields=access_token&access_token=${token}`, res => {
        let data = '';
        res.on('data', c => data += c);
        res.on('end', () => {
          const pt = JSON.parse(data).access_token;
          if (pt) {
            console.log('\nPage token obtenido! Probando publicacion...');
            const postData = `message=🍪 Glassitas — Publicacion automatica funcionando!&access_token=${pt}`;
            const req = https.request({ hostname: 'graph.facebook.com', path: '/v19.0/1111933412010777/feed', method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' } }, r => {
              let b = '';
              r.on('data', c => b += c);
              r.on('end', () => console.log('Resultado:', b.substring(0, 150)));
            });
            req.write(postData);
            req.end();
          }
        });
      });
    }
  } else {
    console.log('No se obtuvo token. Posible error de permisos.');
    const text = await page.evaluate(() => document.body.innerText.substring(0, 400));
    console.log('Pagina:', text.substring(0, 200));
  }

  await sleep(20000);
  await browser.close();
})();
