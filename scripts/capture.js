const { chromium } = require('playwright');

(async () => {

  const browser = await chromium.launch({
    headless: true
  });

  const page = await browser.newPage({
    viewport: {
      width: 1600,
      height: 5000
    }
  });

  await page.goto(
    'https://evostack.vercel.app',
    {
      waitUntil: 'networkidle'
    }
  );

  console.log('EvoStack loaded');

  await page.locator('input').first().fill(
    'https://github.com/Fayeek5/evostack'
  );

  console.log('Repository URL entered');

  await page.locator('button').filter({
    hasText: 'Analyze'
  }).click();

  console.log('Analysis started');

  await page.waitForTimeout(12000);

  await page.screenshot({
    path: 'assets/screenshots/dashboard.png',
    fullPage: true
  });

  console.log('Dashboard screenshot captured');

  await page.evaluate(() => {
    window.scrollTo(0, 1800);
  });

  await page.waitForTimeout(2000);

  await page.screenshot({
    path: 'assets/screenshots/hotspots.png',
    fullPage: false
  });

  console.log('Hotspot screenshot captured');

  await page.evaluate(() => {
    window.scrollTo(0, 3500);
  });

  await page.waitForTimeout(2000);

  await page.screenshot({
    path: 'assets/screenshots/trends.png',
    fullPage: false
  });

  console.log('Trend screenshot captured');

  await browser.close();

})();
