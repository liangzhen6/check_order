#!/usr/bin/python3
import xlrd, xlwt, os
from xlutils.copy import copy
from selenium import webdriver
from selenium.webdriver import ChromeOptions
import time
import platform

originUrl = 'https://sellercentral.amazon.com/orders-v3/order/'
system = platform.system()
xlsPath = ''
#根据系统识别路径
if system == 'Darwin':#mac
	originPath = os.path.abspath('.')
	xlsPath = os.path.join(originPath,'order_data.xls')
elif system == 'Windows':
	originPath = 'C:/Users/Administrator/Desktop/checkOrders'
	xlsPath = os.path.join(originPath,'order_data.xls')


 # 初始化浏览器
options = ChromeOptions()
options.debugger_address = "127.0.0.1:" + '9222'
browser = webdriver.Chrome(executable_path="C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe", chrome_options=options)


#保存xls表格
def savexls(workbookCopy):
	os.remove(xlsPath)
	workbookCopy.save(xlsPath)
#获取当前表格的信息
def get_sheet_mes():
	workbook = xlrd.open_workbook(xlsPath)
	workbookCopy = copy(workbook)

	sheet_name = workbook.sheet_names()[0]
	sheet_one = workbook.sheet_by_name(sheet_name)
	orders = sheet_one.col_values(0)
	return workbookCopy, orders

# 获取时间精确到秒s
def get_date():
	return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))


def get_data_order_number(order_num):
	url = originUrl + order_num
	browser.get(url)

	time.sleep(1)

	status_tabs = browser.find_elements_by_xpath(".//*[@class='a-keyvalue']")

	if len(status_tabs):
		status_tab = status_tabs[0]
		td_s = status_tab.find_elements_by_tag_name("td")

		status_spans = td_s[0].find_elements_by_tag_name("span")
		status_span = status_spans[-1]
		status_value = status_span.get_attribute('textContent')

		asin_b =  td_s[2].find_elements_by_tag_name('b')[0]
		asin = asin_b.get_attribute('textContent')

		num = td_s[4].get_attribute('textContent')

		prix_span = td_s[5].find_elements_by_tag_name('span')[0]
		prix = prix_span.get_attribute('textContent')

		print(status_value,asin,num,prix)
		return status_value, asin, num, prix
	else:
		return "数据异常", "数据异常", "数据异常", "数据异常"



def start_get_all_data():
	workbookCopy, orders = get_sheet_mes()
	sheet = workbookCopy.get_sheet(0)
	for x in range(1,len(orders)):
		status, asin, num, prix = get_data_order_number(orders[x])
		time = get_date()
		sheet.write(x, 1, status)
		sheet.write(x, 2, asin)
		sheet.write(x, 3, num)
		sheet.write(x, 4, prix)
		sheet.write(x, 5, time)

		savexls(workbookCopy)




start_get_all_data()

