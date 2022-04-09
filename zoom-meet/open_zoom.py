from selenium import webdriver
import pyautogui as py
import time

passcode = "abcdef"
meet_code = "756 922 0410"

def join(meet, password):
    driver = webdriver.Chrome("/opt/homebrew/bin/chromedriver")
    driver.get('https://zoom.us/join')

    time.sleep(5)

    driver.find_element_by_xpath(
        "//input[@id='join-confno']").send_keys(meet_code)

    # time.sleep(2)
    # driver.find_element_by_xpath("//a[@id='btnSubmit']").click()

    # time.sleep(5)

join(meet_code, passcode)
