from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_google_search():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Jenkins pipeline Selenium test")
    search_box.send_keys(Keys.RETURN)
    
    print("Page title is:", driver.title)
    driver.quit()

if __name__ == "__main__":
    test_google_search()
