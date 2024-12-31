import os
from typing import Optional
from playwright.sync_api import sync_playwright
from steel import Steel


STEEL_API_KEY = 'ste-q69pQR7DVO5j5V5svjh1RA5elAKnE14JDe4ifogl00OwPNuPWGUMIqAX8GA356JB6PYYnxV09NWH0hGhVx8dSp31A77H6rSueCn'

# Initialize Steel client with the API key from environment variables
client = Steel(
    steel_api_key=STEEL_API_KEY,
)

def main():
    session = None
    browser = None

    try:
        print("Creating Steel session...")

        # Create a new Steel session with all available options
        session = client.sessions.create(
            # === Basic Options ===
            use_proxy=True,              # Use Steel's proxy network (residential IPs)
            # proxy_url='http://...',      # Use your own proxy (format: protocol://username:password@host:port)
            # solve_captcha=True,          # Enable automatic CAPTCHA solving
            # session_timeout=1800000,     # Session timeout in ms (default: 15 mins, max: 60 mins)
            # === Browser Configuration ===
            user_agent=r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'     # Set a custom User-Agent
        )

        print(f"""Session created successfully with Session ID: {session.id}.
You can view the session live at {session.session_viewer_url}
        """)

        # Connect Playwright to the Steel session
        playwright = sync_playwright().start()
        browser = playwright.chromium.connect_over_cdp(
            f"wss://connect.steel.dev?apiKey={STEEL_API_KEY}&sessionId={session.id}"
        )

        print("Connected to browser via Playwright")

        # Create page at existing context to ensure session is recorded.
        currentContext = browser.contexts[0]
        page = currentContext.new_page()

        # ============================================================
        # Your Automations Go Here!
        # ============================================================

        # Example script - Navigate to Hacker News and extract the top 5 stories
        print("Navigating to httpbin...")
        page.goto("https://www.ip77.net/")
        page.wait_for_timeout(30000)
        print(page.content())

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Cleanup: Gracefully close browser and release session when done
        if browser:
            browser.close()
            print("Browser closed")

        if session:
            print("Releasing session...")
            client.sessions.release(session.id)
            print("Session released")

        print("Done!")

# Run the script
if __name__ == "__main__":
    main()
