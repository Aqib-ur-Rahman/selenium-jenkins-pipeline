from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup headless Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# Initialize the Chrome driver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Test case 1: Open homepage and check the title
    driver.get("http://127.0.0.1:5000/")
    WebDriverWait(driver, 10).until(EC.title_contains("Microblog"))
    assert "Microblog" in driver.title, "Test case 1 failed: Title does not match"
    print("Test case 1 passed: Title matches.")

    # Test case 2: Check if the login page loads properly
    driver.get("http://127.0.0.1:5000/auth/login")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
    assert "Login" in driver.title or "login" in driver.current_url, "Test case 2 failed: Login page not loaded correctly"
    print("Test case 2 passed: Login page loaded correctly.")

    # Test case 3: Attempt login with invalid credentials
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, '//input[@value="Sign In"]')

    username_input.send_keys("wrong_user")
    password_input.send_keys("wrong_password")
    login_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "alert-info")))
    assert "Invalid username or password" in driver.page_source, "Test case 3 failed: Error message not displayed"
    print("Test case 3 passed: Error message displayed correctly.")

    # Test case 4: Check if the registration page loads
    driver.get("http://127.0.0.1:5000/auth/register")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
    assert "Register" in driver.title, "Test case 4 failed: Registration page not loaded correctly"
    print("Test case 4 passed: Registration page loaded correctly.")

finally:
    # Ensure the browser is closed
    driver.quit()
