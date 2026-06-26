const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

const PROFILE_DIR = path.join(__dirname, '..', '.fb-profile');
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const browser = await puppeteer.launch({
    headless: false,
    userDataDir: PROFILE_DIR,
    args: ['--no-sandbox', '--window-size=1100,850']
  });

  try {
    const page = await browser.newPage();

    // Step 1: Go to Facebook main page
    console.log('Paso 1: Abriendo Facebook...');
    await page.goto('https://www.facebook.com/', { waitUntil: 'networkidle2', timeout: 30000 });
    await sleep(3000);
    
    const needsLogin = page.url().includes('login');
    if (needsLogin) {
      console.log('Paso 2: Escribiendo credenciales...');
      await page.type('input[name="email"]', 'alexram80@me.com', { delay: 12 });
      await page.type('input[name="pass"]', 'Ironfloor88LE@N', { delay: 12 });
      await sleep(500);
      console.log('Paso 3: Haciendo clic en Iniciar sesion...');
      await page.evaluate(() => {
        document.querySelector('input[type="submit"]').click();
      });
      await sleep(8000);

      if (page.url().includes('two_step') || page.url().includes('2fa')) {
        console.log('Paso 4: ⚠️ 2FA detectado');
        console.log('REVISA TU TELEFONO y aprueba la notificacion de Facebook');
        console.log('Esperando hasta que apruebes...');
        
        for (let i = 0; i < 40; i++) {
          await sleep(3000);
          if (!page.url().includes('two_step') && !page.url().includes('2fa')) {
            console.log('✅ 2FA aprobado!');
            break;
          }
        }
        await sleep(3000);
      }
    }

    // Step 5: Navigate to OAuth dialog
    console.log('Paso 5: Solicitando token via OAuth...');
    await page.goto(
      `https://www.facebook.com/v19.0/dialog/oauth?client_id=2931073960575850&redirect_uri=https://www.facebook.com/connect/login_success.html&scope=pages_manage_posts,pages_read_engagement,business_management&response_type=token,granted_scopes&auth_type=rerequest`,
      { waitUntil: 'networkidle2', timeout: 30000 }
    );
    await sleep(5000);

    let currentUrl = page.url();
    console.log('URL OAuth:', currentUrl.substring(0, 200));

    // Check for permissions dialog
    const dialogText = await page.evaluate(() => document.body.innerText.substring(0, 600));
    
    if (dialogText.includes('continuar') || dialogText.includes('Continue') || dialogText.includes('permisos')) {
      console.log('✅ Dialogo de permisos detectado! Aceptando...');
      
      // Try clicking "Continue as" or "Allow" buttons
      await page.evaluate(() => {
        const btns = document.querySelectorAll('[role="button"], button, a');
        for (const b of btns) {
          const t = (b.innerText || '').toLowerCase();
          if ((t.includes('continuar') || t.includes('continue') || t.includes('permitir') || t.includes('allow')) && b.offsetParent !== null) {
            b.click();
            return;
          }
        }
      });
      await sleep(5000);
      currentUrl = page.url();
      console.log('URL despues de aceptar:', currentUrl.substring(0, 200));
    }

    // Extract token
    if (currentUrl.includes('access_token=')) {
      const match = currentUrl.match(/access_token=([^&]+)/);
      if (match) {
        const token = decodeURIComponent(match[1]);
        console.log('\n🎉🎉🎉 TOKEN OBTENIDO!');
        fs.writeFileSync('./.token-final.txt', token);
        console.log(token.substring(0, 60) + '...');
        console.log('Guardado en .token-final.txt');
        
        // Try to use it immediately
        const pageToken = await fetchPageToken(token);
        if (pageToken) {
          console.log('\nPage token obtenido! Probando publicacion...');
          await testPost(pageToken);
        }
        await browser.close();
        return;
      }
    }

    console.log('\nTexto del dialogo:', dialogText.substring(0, 300));
    await page.screenshot({ path: '/tmp/oauth-result.png' });

    // If all fails, just save the session
    console.log('\nSesion guardada en .fb-profile/');
    console.log('Puedes publicar manualmente desde la ventana abierta');

  } catch (err) {
    console.error('Error:', err.message);
  }
})();

async function fetchPageToken(userToken) {
  const https = require('https');
  return new Promise((resolve) => {
    https.get(`https://graph.facebook.com/v19.0/1111933412010777?fields=access_token&access_token=${userToken}`, res => {
      let data = '';
      res.on('data', c => data += c);
      res.on('end', () => {
        try {
          const token = JSON.parse(data).access_token;
          console.log('Page token:', token.substring(0, 30) + '...');
          resolve(token);
        } catch { resolve(null); }
      });
    });
  });
}

async function testPost(pageToken) {
  const https = require('https');
  const data = `message=🍪 Glassitas — Publicacion automatica exitosa!&access_token=${pageToken}`;
  const req = https.request({
    hostname: 'graph.facebook.com', path: '/v19.0/1111933412010777/feed',
    method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
  }, res => {
    let body = '';
    res.on('data', c => body += c);
    res.on('end', () => console.log('Resultado:', body.substring(0, 100)));
  });
  req.write(data); req.end();
}
