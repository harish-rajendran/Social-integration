from selenium import webdriver


# Read data from excel file (saved with extension ".csv")



driver=webdriver.Chrome("C:/Users/Admin/Desktop/chromedriver.exe")   # Selenium chromedriver path
driver.get("https://web.whatsapp.com/")

#input("Enter any keyword after scanning QR code.\n ")
name = '"Avantika"'

user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
user.click()

text_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
text_box.send_keys("You're Fucked up!!")

button = driver.find_element_by_class_name("_29RFr")
button.click()