from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Change range to the number of times that you want the script to run. Defaulted at 1.

# Must have login information and addresses saved on website before using script.
for p in range(1):

	driver = webdriver.Chrome(executable_path=r'C:\Users\camre\Downloads\chromedriver_win32\chromedriver.exe')

	driver.get("https://www.bestbuy.com/site/sony-playstation-5-dualsense-wireless-controller-midnight-black/6464307.p?skuId=6464307")

	addToCart = driver.find_element(By.XPATH, '/html/body/div[4]/main/div[4]/div[3]/div[2]/div/div/div[14]/div[2]/div/div/div/button')

	addToCart.click()

	driver.get("https://www.bestbuy.com/cart")

	checkoutPS5 = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[4]/div/div[1]/button')

	checkoutPS5.click()


 