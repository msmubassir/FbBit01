from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

# Configure your Facebook credentials
FACEBOOK_EMAIL = os.getenv('FACEBOOK_EMAIL')
FACEBOOK_PASSWORD = os.getenv('FACEBOOK_PASSWORD')
REPLY_MESSAGE = 'Hello! This is an automated reply. Thank you for your message.'

# Initialize the Chrome driver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # To run Chrome in headless mode on Render
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=options)

def login_to_facebook():
    driver.get("https://www.facebook.com")
    email_element = driver.find_element_by_id("email")
    email_element.send_keys(FACEBOOK_EMAIL)
    password_element = driver.find_element_by_id("pass")
    password_element.send_keys(FACEBOOK_PASSWORD)
    password_element.send_keys(Keys.RETURN)
    time.sleep(5)  # Adjust as needed

def check_messages_and_reply():
    driver.get("https://www.facebook.com/messages/t/")
    time.sleep(5)
    
    message_threads = driver.find_elements_by_xpath('//div[@aria-label="Message thread"]')
    
    if len(message_threads) > 0:
        message_threads[0].click()
        time.sleep(5)
        
        message_input = driver.find_element_by_xpath('//div[@aria-label="Type a message..."]')
        message_input.send_keys(REPLY_MESSAGE)
        message_input.send_keys(Keys.RETURN)
        print(f"Replied to message with: '{REPLY_MESSAGE}'")
        
    else:
        print("No new messages found.")

if __name__ == "__main__":
    login_to_facebook()
    
    while True:
        check_messages_and_reply()
        time.sleep(10)

    driver.quit()
