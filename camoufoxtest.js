import os
import asyncio
from patchright.async_api import async_playwright
from hyperbrowser import AsyncHyperbrowser
from hyperbrowser.models.session import CreateSessionParams, ScreenConfig

client = AsyncHyperbrowser(api_key='hb_614c0f40c481f71e6be91423144e')
async def main():
    async with async_playwright() as p:
        session = await client.sessions.create(
            params=CreateSessionParams(
                use_stealth=True,
                operating_systems=["macos"],
                device=["desktop"],
                locales=["en"],
                screen=ScreenConfig(width=1920, height=1080),
            )
        )
        browser = p.chromium.connect(session.ws_endpoint)
        page = await browser.new_page()
        await page.goto('https://httpbin.co/anything')
        await print(page.content())
        await browser.close()

asyncio.run(main())
