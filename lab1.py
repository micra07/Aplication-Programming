import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request


def Create_Directory(directory_polarbear, directory_brownbear):
    if not os.path.exists('dataset'):
        os.mkdir('dataset')
    if not os.path.exists(directory_polarbear):
        os.mkdir('dataset/polarbear')
    if not os.path.exists(directory_brownbear):
        os.mkdir('dataset/brownbear')

def Scroll_Driver(driver, height):
    scroll_range = 0
    while scroll_range < height:
        driver.execute_script(f"window.scrollTo(0, {scroll_range});") 
        scroll_range += 10
    

list_polarbear=[]
list_brownbear=[]

def Create_Driver(link, path_name, name):
    global list_polarbear,  list_brownbear
    driver = webdriver.Edge()
    driver.get(link)
    time.sleep(4)
    Scroll_Driver(driver, 20000)
    list_pictures = driver.find_elements(By.XPATH, path_name)
    if name=="polarbear":
        list_polarbear += list_pictures
    if name=="brownbear":
        list_brownbear += list_pictures
    print(len(list_polarbear),len(list_brownbear))

def Create_Name(value):
    return '0'*(4-len(str(value))) + str(value)

def Save_Image():
    global list_polarbear,  list_brownbear
    directory_polarbear = "dataset/polarbear"
    directory_brownbear = "dataset/brownbear"
    Create_Directory(directory_polarbear, directory_brownbear)
    print(f'lens: {len(list_polarbear)}, {len(list_brownbear)}')

    for elem in range(len(list_polarbear)):
        img = urllib.request.urlopen(list_polarbear[elem].get_attribute('src')).read()
        out = open(f"{directory_polarbear}/{Create_Name(elem)}.jpg", "wb")
        out.write(img)
        out.close
    for elem in range(len(list_brownbear)):
        img = urllib.request.urlopen(list_brownbear[elem].get_attribute('src')).read()
        out = open(f"{directory_brownbear}/{Create_Name(elem)}.jpg", "wb")
        out.write(img)
        out.close
        
def main():
    for i in range(7):
        if len(list_polarbear) < 1000:
            Createe_Driver(f"https://yandex.ru/images/search?p={i}&from=tabbar&text=polar_bear&lr=51&rpt=image", "//img[@class='serp-item__thumb justifier__thumb']","polar_bear")
            time.sleep(10)
    for i in range(7):        
        if len(list_brownbear) < 1000:
            Createe_Driver(f"https://yandex.ru/images/search?p={i}&from=tabbar&text=brown_bear&lr=51&rpt=image", "//img[@class='serp-item__thumb justifier__thumb']", "brown_bear")
            time.sleep(10)
    Save_Image()



if __name__ == "__main__":
   
    main()
