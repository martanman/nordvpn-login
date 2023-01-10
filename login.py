import asyncio
import subprocess
from playwright.async_api import async_playwright
from playwright_stealth.stealth import stealth_async
import sys
import os

async def main(email, passwd):
    async with async_playwright() as p:
        output = os.popen("nordvpn login").read()
        if "You are already logged in." in output:
            print("Already logged in.")
            return
        
        login_url = output.split()[-1]

        browser = await p.firefox.launch()
        context = await browser.new_context()
        page = await context.new_page()
        await stealth_async(page)
        page.set_default_timeout(18000)

        print(f"going to {login_url}")
        await page.goto(login_url)
        print("inputting email")
        await page.get_by_placeholder("Username or email address").fill(email)
        await page.get_by_role("button", name="Continue").click()
        print("inputting password")
        await page.get_by_placeholder("Password").fill(passwd)
        await page.get_by_role("button", name="Log in").click()
        print("awaiting authorization")
        callback = await page.get_by_role("link", name="Continue").get_attribute("href")
        print(f"callback url is: {callback}")

        await context.close()
        await browser.close()
        subprocess.Popen(f'nordvpn login --callback "{callback}"', shell=True).wait()

if __name__ == "__main__":
    asyncio.run(main(*sys.argv[-2:]))
