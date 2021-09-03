from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver') # version 92.0.4515.107

# chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title

user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('Inserting some text in this input field using Python and Selenium')

assert 'Show Message' in chrome_browser.page_source

show_message_button = chrome_browser.find_element_by_class_name('btn-default')
show_message_button.click()

output_message = chrome_browser.find_element_by_id('display')
assert 'Inserting some text in this input field using Python and Selenium' in output_message.text # or .get_attribute('innerHTML')

# chrome_browser.close() # close current chrome driver
# chrome_browser.quit() # close the entire chrome driver in case more than one window was openned
