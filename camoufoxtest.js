const { chromium } = require('patchright');
const { newInjectedContext } require('fingerprint-injector');

(async () => {
  const browser = await chromium.launch({ headless: false });
  const context = await newInjectedContext(
      browser,
      {
            // Constraints for the generated fingerprint (optional)
          fingerprintOptions: {
              devices: ['mobile'],
              operatingSystems: ['ios'],
          },
          
        },
    );
  const page = await browser.newPage();
  await page.goto('https://httpbin.co/anything');
  console.log(await page.content());
  await browser.close();
})();
