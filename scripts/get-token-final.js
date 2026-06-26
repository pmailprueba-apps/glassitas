const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

const PROFILE_DIR = path.join(__dirname, '..', '.fb-profile');
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const browser = await puppeteer.launch({
    headless: false,
    userDataDir: PROFILE_DIR,
    args: ['--no-sandbox', '--window-size=1000,800']
  });
  const page = await browser.newPage();

  // First go to Facebook to establish session
  await page.goto('https://www.facebook.com/', { waitUntil: 'networkidle2', timeout: 30000 });
  await sleep(3000);
  const loggedIn = !page.url().includes('login');
  console.log('Logged in:', loggedIn);

  if (!loggedIn) {
    await page.type('input[name="email"]', 'alexram80@me.com', { delay: 10 });
    await page.type('input[name="pass"]', 'Ironfloor88LE@N', { delay: 10 });
    await page.click('button[name="login"]');
    await sleep(5000);

    if (page.url().includes('two_step')) {
      console.log('2FA requerido - aprueba desde tu telefono');
      await page.waitForNavigation({ timeout: 120000 }).catch(() => {});
      await sleep(3000);
    }
  }

  // Now go to OAuth dialog - this should auto-login
  const oauthUrl = `https://www.facebook.com/v19.0/dialog/oauth?client_id=2931073960575850&redirect_uri=https://www.facebook.com/connect/login_success.html&scope=pages_manage_posts,pages_read_engagement,business_management&response_type=token,granted_scopes&auth_type=rerequest`;

  await page.goto(oauthUrl, { waitUntil: 'networkidle2', timeout: 30000 });
  await sleep(5000);

  let currentUrl = page.url();
  console.log('OAuth URL:', currentUrl.substring(0, 200));

  // Check for various states
  if (currentUrl.includes('access_token=')) {
    const match = currentUrl.match(/access_token=([^&]+)/);
    if (match) {
      const token = decodeURIComponent(match[1]);
      console.log('\n✅ TOKEN OBTENIDO!');
      console.log(token.substring(0, 60) + '...');
      fs.writeFileSync('./.token-final.txt', token);
      await browser.close();
      return;
    }
  }

  if (currentUrl.includes('login_success')) {
    const token = currentUrl.match(/access_token=([^&]+)/);
    if (token) {
      console.log('\n✅ TOKEN!');
      fs.writeFileSync('./.token-final.txt', decodeURIComponent(token[1]));
      await browser.close();
      return;
    }
  }

  // Check content
  const content = await page.evaluate(() => document.body.innerText.substring(0, 500));
  console.log('Content:', content);
  await page.screenshot({ path: '/tmp/oauth5.png' });

  // If it shows "Continue as" or a permissions dialog
  if (content.includes('continuar') || content.includes('Continue') || content.includes('permisos')) {
    console.log('Dialog detected! Attempting to accept...');
    const clicked = await page.evaluate(() => {
      const btns = Array.from(document.querySelectorAll('[role="button"], button'));
      for (const b of btns) {
        const text = (b.innerText || '').toLowerCase();
        if (text.includes('continuar') || text.includes('continue') || text.includes('permitir') || text.includes('allow')) {
          if (b.offsetParent !== null) { b.click(); return true; }
        }
      }
      return false;
    });
    console.log('Clicked:', clicked);
    await sleep(5000);
    console.log('After click URL:', page.url().substring(0, 200));

    const afterUrl = page.url();
    if (afterUrl.includes('access_token=')) {
      const match = afterUrl.match(/access_token=([^&]+)/);
      if (match) {
        const token = decodeURIComponent(match[1]);
        console.log('\n✅ TOKEN OBTENIDO!');
        fs.writeFileSync('./.token-final.txt', token);
        await browser.close();
        return;
      }
    }
  }

  await sleep(10000);
  await browser.close();
})();
