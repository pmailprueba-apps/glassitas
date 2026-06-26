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

  if (url.includes('login')) {
    // Fill in credentials
    console.log('Llenando formulario de login...');
    const emailInput = await page.$('input[name="email"], input[name="pass"]');
    if (emailInput) {
      await page.type('input[name="email"]', 'alexram80@me.com', { delay: 20 });
      await page.type('input[name="pass"]', 'Ironfloor88LE@N', { delay: 20 });
      await Promise.all([
        page.waitForNavigation({ timeout: 30000 }).catch(() => {}),
        page.click('button[name="login"]')
      ]);
      await sleep(5000);
      console.log('Post-login URL:', page.url().substring(0, 150));
    }
  }

  // Now check if we got the token
  const finalUrl = page.url();
  console.log('Final URL:', finalUrl.substring(0, 200));
  
  if (finalUrl.includes('access_token=')) {
    const match = finalUrl.match(/access_token=([^&]+)/);
    if (match) {
      const token = decodeURIComponent(match[1]);
      console.log('\n✅ TOKEN OBTENIDO!');
      console.log(token.substring(0, 50) + '...');
      fs.writeFileSync('./.token-final.txt', token);
    }
  } else {
    const text = await page.evaluate(() => document.body.innerText.substring(0, 300));
    console.log('Text:', text);
    await page.screenshot({ path: '/tmp/oauth2.png' });
  }

  await sleep(30000);
  await browser.close();
})();
