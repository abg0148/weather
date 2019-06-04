from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

option = webdriver.ChromeOptions()
browser = webdriver.Chrome(executable_path=r'C:\Users\gupta\Downloads\chromedriver.exe', options=option)
browser.get("https://weather.com/en-IN/weather/today/l/4790efe7d1cbfe93d5e0970933a13fe73bd2f0eb60a10eccbf369489080f4003")
print(browser.find_elements_by_class_name("today_nowcard-temp"));
