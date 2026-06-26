const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

const PROFILE_DIR = path.join(__dirname, '..', '.fb-profile');
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const browser = await puppeteer.launch({
    headless: true,
    userDataDir: PROFILE_DIR,
    args: ['--no-sandbox']
  });
  const page = await browser.newPage();

  // Go to Graph API Token Debugger (doesn't need business login)
  await page.goto('https://developers.facebook.com/tools/debug/accesstoken/', {
    waitUntil: 'networkidle2', timeout: 30000
  });
  await sleep(3000);
  console.log('1. Debug URL:', page.url().substring(0, 100));

  // Go to the OAuth dialog for our app
  const oauthUrl = `https://www.facebook.com/v19.0/dialog/oauth?client_id=2931073960575850&redirect_uri=https://developers.facebook.com/tools/explorer/callback/&scope=pages_manage_posts,pages_read_engagement,business_management&response_type=token,granted_scopes&auth_type=rerequest&display=popup`;
  
  await page.goto(oauthUrl, { waitUntil: 'networkidle2', timeout: 30000 });
  await sleep(5000);
  console.log('2. OAuth URL:', page.url().substring(0, 150));

  const url = page.url();
  if (url.includes('login_success') || url.includes('access_token=')) {
    const match = url.match(/access_token=([^&]+)/);
    if (match) {
      const token = decodeURIComponent(match[1]);
      console.log('\n✅ TOKEN OBTENIDO!');
      console.log(token.substring(0, 50) + '...');
      fs.writeFileSync('./.token-final.txt', token);
      console.log('Guardado en .token-final.txt');
    }
  } else {
    const text = await page.evaluate(() => document.body.innerText.substring(0, 500));
    console.log('3. Page text:', text.substring(0, 200));
    
    // Try clicking "Continue as" or permission buttons
    const buttons = await page.evaluate(() => {
      return Array.from(document.querySelectorAll('[role="button"], button, [data-testid]'))
        .filter(b => b.offsetParent !== null)
        .map(b => ({
          text: (b.innerText || '').substring(0, 40),
          aria: (b.getAttribute('aria-label') || '').substring(0, 40),
          testid: (b.getAttribute('data-testid') || '').substring(0, 40)
        }));
    });
    console.log('4. Buttons:', JSON.stringify(buttons, null, 2));

    // Take screenshot
    await page.screenshot({ path: '/tmp/oauth-dialog.png' });
    console.log('5. Screenshot saved');
  }

  await browser.close();
})();
