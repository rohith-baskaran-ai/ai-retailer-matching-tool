from core.driver import create_driver

driver = create_driver()

print(driver.title)

input("\nPress ENTER to close...")

driver.quit()