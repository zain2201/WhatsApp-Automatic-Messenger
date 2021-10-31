import openpyxl
import pandas as pd

import time
import ait
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_argument(r'--user-data-dir=C:/Users/zain9/AppData/Local/Google/Chrome/User Data/Default')
options.add_argument('--profile-directory=Default')
browser=webdriver.Chrome(options=options)
loc="C:/Users/zain9/OneDrive/Desktop/whatsapp.xlsx"
df=pd.read_excel(loc,engine='openpyxl')
for i in range(len(df)):
	name=df.iloc[i,0]
	number=df.iloc[i,1]
	browser.execute_script("window.open('about:blank','tab2');")
	browser.switch_to.window("tab2")
	url='https://web.whatsapp.com/send?phone=91'+str(number)
	try:
		browser.get(url)
	except:
		continue
	time.sleep(15)
	try:
		msg_box=browser.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]/div/div[2]')
	except:
		continue
	msg="Congratulations!! "+name+", you were selected as a test subject for my automation project on whatsapp by the great Ali Zain"
	msg_box.send_keys(msg)
	send_button=browser.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]/button/span')
	send_button.click()
	time.sleep(2)
browser.close()
print("messages sent")
			
