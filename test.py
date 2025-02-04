from DrissionPage import Chromium, ChromiumOptions
co = ChromiumOptions().set_browser_path(r'./chrome/ungoogled-chromium_131.0.6778.264-1_linux/chrome').set_local_port(9111).set_user_data_path(r'./test1')
co.set_argument('--fingerprint','2')
co.set_argument('--fingerprinting-canvas-image-data-noise')
co.set_argument('--fingerprinting-canvas-measuretext-noise')
co.set_argument('--fingerprinting-client-rects-noise')
co.set_argument('--lang','de')
co.set_argument('--accept-lang','de')
co.set_argument('--no-sandbox')
browser = Chromium(co)
tab = browser.latest_tab
tab.get('https://httpbin.co/anything')
browser.wait(5)
print(tab.html)
browser.quit(del_data=True)

