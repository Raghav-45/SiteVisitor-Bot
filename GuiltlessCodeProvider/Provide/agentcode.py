import random
import time
import requests
import json

from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem, Popularity
from selenium_stealth import stealth
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Gets new useragents # https://pypi.org/project/random-user-agent/
software_names = [SoftwareName.CHROME.value, SoftwareName.EDGE.value, SoftwareName.FIREFOX.value, SoftwareName.OPERA.value]
operating_systems = [OperatingSystem.WINDOWS.value]
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100) #popularity=popularity
user_agent = user_agent_rotator.get_random_user_agent()

print("Starting Bot after 10 Seconds...", flush=True)
time.sleep(10)
print(user_agent)

def getadverturl():
    response_API = requests.get('https://innocenturlprovider.raghavbhai4545.repl.co/')
    data = json.loads(response_API.text)['url']
    return str(data)

Ad_url = 'http://httpbin.org/ip'
print('Url to Open ' + Ad_url)

def Run_Selenium():
    List_Of_Displays = {1: (1366, 768),
                        2: (1920, 1080),
                        3: (1536, 864),
                        4: (1440, 900),
                        5: (1280, 720),
                        6: (1600, 900),
                        7: (1280, 800),
                        8: (1280, 1024),
                        9: (1024, 768),
                        10: (768, 1024)}
    
    opts = Options()
    opts.add_argument('--disable-extensions')
    opts.add_argument('--profile-directory=Default')
    # opts.add_argument("--incognito")
    opts.add_argument("--disable-plugins-discovery")
    opts.add_argument('--no-sandbox')
    # opts.add_argument('--headless')
    opts.add_argument('--enable-javascript')
    opts.add_argument('--disable-gpu')
    opts.add_argument('--ignore-certificate-errors')  # says its unsupported
    opts.add_experimental_option("detach", True)
    
    # driver = webdriver.Chrome(options=opts, version_main=91) # version_main=91
    driver = webdriver.Chrome(options=opts) # version_main=91
    
    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
           )
    
    # driver.delete_all_cookies() # Delete Cookies
    driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": user_agent})
    driver.set_window_size(random.randrange(360, 1440), random.randrange(640, 1080))  # changes window size
    driver.set_window_position(0, 0)
    
    driver.get(Ad_url)  # go to url
    # driver.implicitly_wait(100)  # wait few seconds
    time.sleep(10)
    driver.close()
    # driver.quit()


if __name__ == "__main__":
    print("Waiting For Approval From IP Zone...")
    agent_ip = requests.get('http://httpbin.org/ip').json()['origin']
    # Approved = True
    Approved_resp = requests.post('https://ipzone.raghavbhai4545.repl.co/check', json=json.loads('{"ip": "' + str(agent_ip) + '"}')).json()
    print(Approved_resp)
    Approved = str(json.loads(Approved_resp)["allowed"])

    if Approved == 'true':
        print('IP is Approved...')
        # print("Setting New Proxy", flush=True)
        time.sleep(2)
    
        print("Going to try to run selenium", flush=True)
        time.sleep(random.randrange(1, 5)) # amount of time to wait before loading the page again
    
        Connected = True
        print("Connected is "+ str(Connected), flush=True)
        time.sleep(2)
    
        if Connected == False:
            print("Failed network check")
            # os.system("echo " + ip + " >> /blacklist.txt")
        if Connected == True:
            Run_Selenium()
            print("Just ran a successful run of selenium", flush=True)

    else:
      print('You Already Visited with this IP...')