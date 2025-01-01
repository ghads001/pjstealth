import { chromium } from 'patchright';
import { newInjectedContext } from 'fingerprint-injector';

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
  const page = await context.newPage();
  await page.goto('https://httpbin.co/anything');
  console.log(await page.content());
  await browser.close();
})();
