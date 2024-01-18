#importing modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import time

#opening firefox and going to Google homepage
browser = webdriver.Firefox()
browser.get('https://www.google.co.nz')


#going to seek.co.nz's website
search_elem = browser.find_element(By.CSS_SELECTOR, '#APjFqb')
search_elem.click()
time.sleep(3)
search_elem.send_keys('seek.co.nz')
search_elem.submit()
time.sleep(5)
seek_elem = browser.find_element(By.CSS_SELECTOR, '.eKjLze > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > a:nth-child(1) > h3:nth-child(2)')
seek_elem.click()
#congratulations, you have gained access to seeks homepage website


#now signing into you're account
sign_in_elem = browser.find_element(By.CSS_SELECTOR, ' div.a1msqiga:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)')
sign_in_elem.click()
time.sleep(5)
email_elem = browser.find_element(By.CSS_SELECTOR, '#emailAddress')
email_elem.click()
email_elem.send_keys('insert email address')
pass_elem = browser.find_element(By.CSS_SELECTOR, '#password')
pass_elem.click()  
pass_elem.send_keys('insert password')
pass_elem.submit()
time.sleep(10)

#now finding you're saved jobs list
savedjobs = browser.find_element(By.CSS_SELECTOR, '.a1msqi5c > div:nth-child(2) > div:nth-child(1) > nav:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)')
savedjobs.click()
time.sleep(5)

while True:
    try:
        # Find an expired job element on the page
        expy_element = browser.find_element(By.CSS_SELECTOR, 'span[title="Expired"] .d3eu8q0._1hfu55i1._1igc8rl4y._1igc8rl0._1igc8rlr')
    except NoSuchElementException:
        print('Expired job elements not found')
        break # Exit the loop
    try:
        # Click the "Remove Job" button for the expired job
        remove_job_button = browser.find_element(By.CSS_SELECTOR, 'button.d3eu8q0.d3eu8q7._1igc8rl7q._1igc8rl6m._1igc8rl9y._1igc8rl8u._1igc8rl7._1igc8rl5u._1igc8rl5e._1igc8rl4y._1igc8rly._1igc8rlx._1igc8rl5._1igc8rlh6._1igc8rl4._1igc8rlh._1o3f13b0._1o3f13b6._1fosusw0.dx1ixi0')
        remove_job_button.click()
        time.sleep(5)

        # Click the "Remove Job Dropdown" button for the expired job
        delete_job_buttons = browser.find_elements(By.CSS_SELECTOR, 'button[id^="menu-actions-delete-job-"]')
        for button in delete_job_buttons:
            try:
                browser.execute_script("arguments[0].scrollIntoView();", button)
                button.click()
                time.sleep(5)
            except ElementNotInteractableException:
                pass # Element was not interactable, so the button was skipped.


        # Click the confirmation button in the popup        
        xbutton = browser.find_elements(By.CSS_SELECTOR, 'button[id^="dialog-delete-button-"]')
        for button in xbutton:
            button.click()
            time.sleep(5)
    except NoSuchElementException:
        print('"Ignore this text"')
        break

print('All done')

