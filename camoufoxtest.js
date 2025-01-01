const { chromium } = require('patchright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('https://httpbin.co/anything');
  console.log(page.content());
  await browser.close();
})();
