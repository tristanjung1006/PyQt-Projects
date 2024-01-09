from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyperclip
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 크롬 창 최대화
driver.maximize_window()
wait = WebDriverWait(driver, 10)

id = "tristan1006@naver.com"
pw = "seungwon3079!"
city = "서울"
hall = "강동"

driver.get('https://www.lottecinema.co.kr/NLCHS/Member/login')

id_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#userId')))
id_input.click()
pyperclip.copy(id)
id_input.send_keys(Keys.CONTROL, 'v')
pw_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#userPassword')))
pw_input.click()
pyperclip.copy(pw)
pw_input.send_keys(Keys.CONTROL, 'v')
submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, f"//button[@class='btn_login']")))
submit_button.click()
time.sleep(5)
driver.get('https://www.lottecinema.co.kr/NLCHS/Ticketing')
movie_city = wait.until(EC.element_to_be_clickable((By.XPATH, f"//li[@class='depth1']//a[text()='{city}']")))
movie_city.click()
movie_hall = wait.until(EC.element_to_be_clickable((By.XPATH, f"//li//a[text()='{hall}']")))
movie_hall.click()
