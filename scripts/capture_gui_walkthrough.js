const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async()=>{
  const root = '/Users/zachscott/Claude/Projects/Onnixus Technologies/_ops/careers/smartcat-5838436004/onnixus-os-mock-demo';
  const shots = path.join(root, 'assets', 'gui_walkthrough');
  fs.mkdirSync(shots, { recursive: true });

  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  await page.goto('file://' + path.join(root, 'gui-artifact.html'));
  await page.waitForTimeout(500);

  let i = 1;
  const snap = async(name)=>{
    const p = path.join(shots, `frame_${String(i).padStart(2,'0')}_${name}.png`);
    await page.screenshot({ path: p });
    i++;
  };

  await snap('overview');
  await page.click('button[data-tab="queue"]');
  await page.waitForTimeout(250);
  await snap('queue_open');

  await page.click('#approve');
  await page.waitForTimeout(250);
  await snap('queue_approve');

  await page.click('#snooze');
  await page.waitForTimeout(250);
  await snap('queue_snooze');

  await page.click('button[data-tab="packs"]');
  await page.waitForTimeout(250);
  await snap('packs');

  await page.click('button[data-tab="skeleton"]');
  await page.waitForTimeout(250);
  await snap('skeleton');

  await page.click('button[data-tab="architecture"]');
  await page.waitForTimeout(250);
  await snap('architecture');

  await page.click('button[data-tab="overview"]');
  await page.waitForTimeout(250);
  await snap('overview_return');

  await browser.close();
  console.log('frames captured to', shots);
})();
