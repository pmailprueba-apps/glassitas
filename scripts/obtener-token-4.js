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

  const oauthUrl = `https://www.facebook.com/v19.0/dialog/oauth?client_id=2931073960575850&redirect_uri=https://developers.facebook.com/tools/explorer/callback/&scope=pages_manage_posts,pages_read_engagement,business_management&response_type=token,granted_scopes&auth_type=rerequest&display=popup`;

  await page.goto(oauthUrl, { waitUntil: 'networkidle2', timeout: 30000 });
  await sleep(3000);

  const url = page.url();
  console.log('URL:', url.substring(0, 150));

  if (url.includes('skip_api_login')) {
    // Fill credentials 
    await page.evaluate(() => {
      document.querySelector('input[name="email"]').value = 'alexram80@me.com';
      document.querySelector('input[name="pass"]').value = 'Ironfloor88LE@N';
    });
    await sleep(1000);
    
    // Click the login button
    await page.evaluate(() => {
      const btn = document.querySelector('button[id="loginbutton"], button[type="submit"]');
      if (btn) btn.click();
    });
    
    await sleep(5000);
    console.log('Post-login URL:', page.url().substring(0, 200));
  }

  const finalUrl = page.url();
  if (finalUrl.includes('access_token=')) {
    const match = finalUrl.match(/access_token=([^&]+)/);
    if (match) {
      const token = decodeURIComponent(match[1]);
      console.log('\n✅ TOKEN!');
      fs.writeFileSync('./.token-final.txt', token);
      console.log(token.substring(0, 60) + '...');
    }
  } else {
    await page.screenshot({ path: '/tmp/oauth3.png' });
    const errorText = await page.evaluate(() => document.body.innerText.substring(0, 400));
    console.log('Text:', errorText);
    
    // Check if we need 2FA
    if (finalUrl.includes('two_step')) {
      console.log('\n⚠️ 2FA requerido - Revisa tu telefono y aprueba');
      await page.waitForNavigation({ timeout: 120000 }).catch(() => {});
      console.log('After 2FA URL:', page.url().substring(0, 200));
      
      const afterUrl = page.url();
      if (afterUrl.includes('access_token=')) {
        const match = afterUrl.match(/access_token=([^&]+)/);
        if (match) {
          const token = decodeURIComponent(match[1]);
          console.log('\n✅ TOKEN!');
          fs.writeFileSync('./.token-final.txt', token);
          console.log(token.substring(0, 60) + '...');
        }
      }
    }
  }

  await sleep(30000);
  await browser.close();
})();
