from selenium import webdriver# Do not pass executable_path or Service paths manually unless strictly required
from selenium.webdriver.common.by import By



driver=webdriver.Firefox()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.CSS_SELECTOR("input[name='username']")).send_keys("Admin")
driver.find_element(By.NAME,'password').send_keys("admin123")

