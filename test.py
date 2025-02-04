from patchright.sync_api import sync_playwright

executable_path = r'./ungoogled-chromium_131.0.6778.264-1_linux'

with sync_playwright() as p:
    browser = p.chromium.launch_persistent_context(
        user_data_dir="./test1",
        executable_path=executable_path,
        channel="chrome",
        headless=False,
        no_viewport=True,
        args=['--fingerprint=1000',
            '--fingerprint-platform=macos',
            '--fingerprinting-canvas-image-data-noise',
            '--fingerprinting-canvas-measuretext-noise',
            '--fingerprinting-client-rects-noise',
            '--no-sandbox',
            '--lang=zh',
            '--accept-lang=zh']
    )
    page = browser.new_page()
    page.goto('https://httpbin.co/anything')
    page.wait_for_timeout(5000)
    print(page.content())
    browser.close()



