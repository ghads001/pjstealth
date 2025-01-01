# undetected-playwright here!
from undetected_playwright.sync_api import sync_playwright


with sync_playwright() as p:
    args = []
    
    # disable navigator.webdriver:true flag
    args.append("--disable-blink-features=AutomationControlled")
    browser = p.chromium.launch(args=args, headless=False)
    page = browser.new_page()
    page.goto("https://nowsecure.nl/#relax")
    input("Press ENTER to continue to Creep-JS:")
    page.goto("https://nowsecure.nl/#relax")
    page.goto("https://abrahamjuliot.github.io/creepjs/")
    input("Press ENTER to exit:")
    browser.close()
