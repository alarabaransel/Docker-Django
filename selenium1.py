from selenium import webdriver
from selenium.webdriver.common.by import By
import time


total_time = time.process_time()
def user_add_test(addName, browser, time_collector):
    time_p = time.process_time()
    browser.get("http://127.0.0.1:8000/")
    browser.get("http://127.0.0.1:8000/admin")
    username = browser.find_element_by_id("id_username")
    password = browser.find_element_by_id("id_password")
    username.send_keys("omer")
    password.send_keys("baal1018")
    login = browser.find_element_by_class_name("submit-row")
    login.click()
    browser.get("http://127.0.0.1:8000/admin/auth/user/")
    addUser = browser.find_element_by_class_name("addlink")
    addUser.click()
    addNewUser = browser.find_element_by_id("id_username")
    addNewUser.send_keys(addName)
    addNewPassword = browser.find_element_by_id("id_password1")
    addNewPassword.send_keys("Baal.06111967")
    passwordConfig = browser.find_element_by_id("id_password2")
    passwordConfig.send_keys("Baal.06111967")
    saveButton = browser.find_element(By.NAME, "_save")
    saveButton.click()
    browser.find_element_by_id("user-tools")
    browser.quit()
    elapsed_time = time.process_time() - time_p
    time_collector.append(elapsed_time)

def chrome_test(addName,time_collector):
    browser = webdriver.Chrome(executable_path="./chromedriver")
    user_add_test(addName, browser, time_collector)

#def opera_test(addName,time_collector):
    #browser = webdriver.Opera(executable_path="./operadriver")
    #user_add_test(addName, browser, time_collector)

def firefox_test(addName,time_collector):
    browser = webdriver.Firefox(executable_path="./geckodriver")
    user_add_test(addName, browser, time_collector)

#def test_adder():
   # time_opera_collector = []
   # time_firefox_collector = []
   # time_chrome_collector = []

   # for x in range(100):
    #    addName = "Chrome" + str(400 + x)
    #    chrome_test(addName,time_chrome_collector)
    #    addName = "Firefox" + str(500 + x)
    #    firefox_test(addName,time_firefox_collector)

    #print("Average Opera : ", sum(time_opera_collector)/100)
    #print("Average Chrome : ", sum(time_chrome_collector) / 100)
    #print("Average Firefox : ", sum(time_firefox_collector) / 100)


time_chrome = time.process_time()
time_chrome_collector = []
for x in range(1000):
    addName = "Chrome" + str(100000 + x)
    chrome_test(addName, time_chrome_collector)
print("Total Chrome Time: ", sum(time_chrome_collector))
print("Average Chrome : ", sum(time_chrome_collector) / 1000)
elapsed_chrome_time = time.process_time() - time_chrome

time_firefox = time.process_time()
time_firefox_collector = []
for x in range(1000):
    addName = "Firefox" + str(200000 + x)
    firefox_test(addName, time_firefox_collector)
elapsed_firefox_time = time.process_time() - time_firefox

total_execution_time = time.process_time() - total_time
print("Total Firefox Time: ", sum(time_firefox_collector))
print("Average Firefox : ", sum(time_firefox_collector) / 1000)

print("Total Execution Time to add 2000 users: ",sum(time_firefox_collector) + sum(time_chrome_collector))
print("Total Google Chrome Time: ",time_chrome)
print("Google Chrome Time per User Addition: ",time_chrome/1000)
print("Total Mozilla Time: ",time_firefox)
print("Mozilla per User Addition: ",time_firefox/1000)
print("Total Execution Time of the Python Code: ",total_execution_time)