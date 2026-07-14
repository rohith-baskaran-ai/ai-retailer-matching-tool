from core.browser import Browser

browser = Browser()

try:

    browser.start()

    browser.open("https://example.com")

    print(browser.title())

    print(browser.url())

    print(browser.text("h1"))

finally:

    input("\nPress ENTER to close...")

    browser.quit()