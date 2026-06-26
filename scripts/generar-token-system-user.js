/**
 * Genera un token de System User para Glassitas
 * 
 * Requisitos:
 * 1. La app debe tener pages_manage_posts en sus permisos (App Review)
 * 2. Ejecutar: node scripts/generar-token-system-user.js
 * 
 * El token generado es permanente y funciona desde cualquier servidor (QNAP, Render, etc.)
 * SIN necesidad de 2FA ni sesión de navegador.
 */
const https = require('https');

const APP_ID = '2931073960575850';
const APP_SECRET = 'a019202fbbc605511c1e059fc2ca6ba2';
const SYS_USER = '122094378873384233';
const BUSINESS_ID = '989666967381176';
const PAGE_ID = '1111933412010777';

const scopes = ['pages_manage_posts', 'pages_read_engagement', 'business_management'];

function getAppSecretProof(token, secret) {
  const crypto = require('crypto');
  return crypto.createHmac('sha256', secret).update(token).digest('hex');
}

function apiPost(path, data) {
  return new Promise((resolve, reject) => {
    const body = new URLSearchParams(data).toString();
    const req = https.request({
      hostname: 'graph.facebook.com',
      path: `/v19.0${path}`,
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
    }, res => {
      let d = '';
      res.on('data', c => d += c);
      res.on('end', () => resolve(JSON.parse(d)));
    });
    req.write(body);
    req.end();
  });
}

async function main() {
  if (!process.env.ADMIN_TOKEN) {
    console.log('⚠️  Este script requiere un token de administrador');
    console.log('Ejecuta:');
    console.log('  ADMIN_TOKEN="EAA..." node scripts/generar-token-system-user.js');
    console.log('\nEl token de admin debe ser de la app Glassitas Publisher');
    console.log('(generado desde https://developers.facebook.com/tools/explorer/)\n');
    process.exit(1);
  }

  const adminToken = process.env.ADMIN_TOKEN;
  const proof = getAppSecretProof(adminToken, APP_SECRET);

  console.log('Generando token de System User...');
  const result = await apiPost(`/${SYS_USER}/access_tokens`, {
    app_id: APP_ID,
    business_app: APP_ID,
    scope: scopes.join(','),
    access_token: adminToken,
    appsecret_proof: proof
  });

  if (result.access_token) {
    const sysToken = result.access_token;
    console.log('\n✅ TOKEN DE SYSTEM USER GENERADO');
    console.log(sysToken);
    console.log('\nProbando publicación...');
    
    const postResult = await apiPost(`/${PAGE_ID}/feed`, {
      message: '🍪 Glassitas — Sistema de publicación automática activado!',
      access_token: sysToken
    });
    
    if (postResult.id) {
      console.log('✅ Publicación exitosa! ID:', postResult.id);
    } else {
      console.log('❌ Error:', postResult.error?.message);
    }
  } else {
    console.log('❌ Error:', result.error?.message);
  }
}

main().catch(console.error);
