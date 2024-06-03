from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.example.com")

element = driver.find_element(By.ID, "my_element")
