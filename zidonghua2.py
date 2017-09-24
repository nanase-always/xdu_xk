# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

wd = webdriver.Chrome()
wd.get("http://ids.xidian.edu.cn/authserver/login?service=http%3A%2F%2Fjwxt.xidian.edu.cn%2Fcaslogin.jsp")
wd.maximize_window()
def isElementExist(_wd, _string, _type):
    flag=True
    wd=_wd
    try:
        if _type == 'name':
            wd.find_element_by_name(_string)
            wd.find_element_by_xpath(_string)
        elif _type == 'text':
            wd.find_element_by_link_text(_string)
        return flag
    except:
        flag=False
        return flag
def check_is_curruntwindow():
    wd.switch_to_default_content()
    wd.switch_to_frame("bottomFrame")
    wd.switch_to_frame("mainFrame")
try:
    email = WebDriverWait(wd,timeout=10).until(EC.presence_of_element_located((By.ID,'username')),message=u'元素加载超时!')
    email.send_keys("16010410023")
    passwd = WebDriverWait(wd,timeout=10).until(EC.presence_of_element_located((By.ID,'password')),message=u'元素加载超时!')
    passwd.send_keys("057815")
    wd.find_element_by_name("submit").click()
    path=".//*[@id='divCoHome']/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[3]/td[1]/a/div"
    if False == isElementExist(wd, path, "xpath"):
        wd.refresh()
    check_is_curruntwindow()
    wd.implicitly_wait(10)

    wd.find_element_by_xpath(".//*[@id='divCoHome']/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[3]/td[1]/a/div").click()  # 点击登录
    check_is_curruntwindow()
    wd.implicitly_wait(10)
    wd.find_element_by_xpath("html/body/form/table/tbody/tr[2]/td/input").click()
    wd.implicitly_wait(10)
    wd.find_element_by_xpath("html/body/form/table/tbody/tr[3]/td/input[1]").click()


except NoSuchElementException as e:
    print e.message
wd.switch_to_frame("inforUpContent")

wanted_course_num = 1
for wanted_course_num in range(1,51):

    wanted_course_string =".//*[@id='user']/tbody/tr["
    wanted_course = wanted_course_string + str(wanted_course_num) + "]/td[4]/a"
    logic_button = wd.find_element_by_xpath(wanted_course)
    if u'英语' in logic_button.text:
        wanted_course_string2 = ".//*[@id='user']/tbody/tr["
        wanted_course_choose = wanted_course_string2 + str(wanted_course_num) + "]/td[1]/input"
        wd.implicitly_wait(10)
        wd.find_element_by_xpath(wanted_course_choose).click()
        check_is_curruntwindow()
        wd.implicitly_wait(10)
        wd.find_element_by_xpath("html/body/table[6]/tbody/tr/td/img[1]").click()
