from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random, time 

#Arbitrary Wait Time to Prevent Bot-Checking
wait = random.randrange(5.0,10.0)

#Open Chrome
wd = wd.Chrome()
wd.implicitly_wait(10) #time to wait to account for loading times

url = input("Url of Best Buy Item!")
try:
    wd.get(url)#url of item you want
except:
    print("Not a BestBuy URL >:(")

#Use Selenium to find & click buttons and input info!
#Using Absolute XPath b/c too lazy to learn Relative XPath rn :P
try: 
    add_to_cart_button = wd.find_element_by_css_selector(".add-to-cart-button")
    add_to_cart_button.click()
except:
    print ("Out of Stock :(")

wd.get('https://www.bestbuy.com/cart')
#Add to Cart Keeps Your Spot Since It Has Sent A Request
#Fill in other personal info