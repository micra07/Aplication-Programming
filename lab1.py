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
