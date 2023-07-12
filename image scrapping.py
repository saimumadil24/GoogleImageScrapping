from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from urllib import request
import os
import time

#Setup Chrome driver
path=r'C:\Users\Saimum Adil Khan\OneDrive\Desktop\Python Course\Untitled Folder\Image_scrapping\chromedriver.exe'
service=Service(path)
driver=webdriver.Chrome(service=service)

#Input Search Querry
search_querry=input('Enter the word to get photos >> ')

#Open google images
driver.get('https://www.google.com/imghp')

#Find search input element and input the search querry
search_element=driver.find_element(By.NAME,'q')
search_element.send_keys(search_querry)
search_element.submit()

#Scroll down to load more images
scroll_pause_time=2
scroll_height=driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(scroll_pause_time)
    new_scroll_height=driver.execute_script('return document.body.scrollHeight')
    if new_scroll_height==scroll_height:
        break
    scroll_height=new_scroll_height

#Finding the image element in the page
image_elements=driver.find_elements(By.CSS_SELECTOR,'img.rg_i')

#Download the images
download_directory='downloaded_images'
downloaded_count=0
for i, image_element in enumerate(image_elements):
    if downloaded_count>=25:
        break
    image_url=image_element.get_attribute('src')
    if image_url:
        image_path=os.path.join(download_directory,f'{search_querry}_{i+1}.jpg')
        request.urlretrieve(image_url,image_path)
        print(f'Saved image_{i+1}')
        downloaded_count +=1

#Close the browser
driver.quit()