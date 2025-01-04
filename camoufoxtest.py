from patchright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://httpbin.co/anything')    
    page.wait_for_timeout(1000)
    print(page.content())
    browser.close()




