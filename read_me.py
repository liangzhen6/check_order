#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver import ChromeOptions

options = ChromeOptions()
options.debugger_address = "127.0.0.1:" + '9222'
browser = webdriver.Chrome(executable_path="C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe", chrome_options=options)
browser.get('http://www.baidu.com')

# 1.启用googlel浏览器 调试
# C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe  --remote-debugging-port=9222

# 2.使用python脚本
