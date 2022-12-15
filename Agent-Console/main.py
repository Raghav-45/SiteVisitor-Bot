from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os, time, requests

# Wake Repls
print('Waking IPZone')
requests.get('https://ipzone.raghavbhai4545.repl.co/')
print('Waking GuiltlessCodeProvider')
requests.get('https://guiltlesscodeprovider.raghavbhai4545.repl.co/')

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.headless = True

driver = webdriver.Chrome(options=chrome_options)
# driver.get("file://" + str(os.getcwd()) + "/ReplitStart (NEW).html")

Viewports = 5
AgentsPerViewport = 5
for a in range(1, Viewports + 1):
    print('\nSleeping 10 Seconds...')
    time.sleep(10)
    print('\n[Viewport -> ' + str(a) + ']')
    driver.get("file://" + str(os.getcwd()) + "/Viewports/Viewport-" + str(a) + ".html")
    for i in range(1, AgentsPerViewport + 1):
        print('Running Agent Number -> ' + str(i))
        # driver.execute_script("window.scrollTo(0, {Y})".format(Y=str(500*i)))
        # iframe = driver.find_element_by_xpath("//iframe[@name='agent-{num}']".format(num=str(i)))
        iframe = driver.find_element("xpath", "//iframe[@name='agent-{num}']".format(num=str(i)))
        # iframe = driver.find_element("xpath", '//*[@id="modal"]/div/div[1]/iframe[@name="raghavbhai01_agent-{num}"]'.format(num=str(i)))
        driver.switch_to.frame(iframe)
        RunButton = driver.find_element(By.CLASS_NAME, "css-m7x2pn")
        RunButton.click()
        driver.switch_to.default_content()
        # time.sleep(5)

# Agents = 30
# for i in range(1, Agents + 1):
#     print('Running Agent Number -> ' + str(i))
#     # driver.execute_script("window.scrollTo(0, {Y})".format(Y=str(500*i)))
#     iframe = driver.find_element_by_xpath("//iframe[@name='agent-{num}']".format(num=str(i)))
#     # iframe = driver.find_element("xpath", '//*[@id="modal"]/div/div[1]/iframe[@name="raghavbhai01_agent-{num}"]'.format(num=str(i)))
#     driver.switch_to.frame(iframe)
#     RunButton = driver.find_element(By.CLASS_NAME, "css-m7x2pn")
#     RunButton.click()
#     driver.switch_to.default_content()
#     time.sleep(5)