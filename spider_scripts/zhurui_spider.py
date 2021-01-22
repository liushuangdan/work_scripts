from time import sleep
import requests
# import socket
# import pyautogui

from PIL import Image
# import pyperclip
# import json
# from lxml import etree
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import os
# 引入excel模块
import xlrd
# 制作excel 向excel里面插入图片
import xlsxwriter
# 复制
import pyperclip


def down_main(path):
    print(path)
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_argument("disable-infobars")
    # option.add_argument('--headless')
    # 设置下载地址
    download_path = path.replace('./static', '')
    download_path = r"D:\work_scripts\spider_scripts\BI_log" + download_path.replace('/', '\\')
    print(download_path)
    prefer = {'profile.default_content_settings.popups': 0, 'download.default_directory': download_path}
    option.add_experimental_option('prefs', prefer)
    # option.add_argument("--user-data-dir="+r"C:/Users/bfec/AppData/Local/Google/Chrome/User Data")
    driver = webdriver.Chrome(executable_path=r'C:\Program Files\Google\Chrome\Application\chromedriver.exe',
                              options=option)
    driver.maximize_window()

    driver.get(r"https://fuwu.taobao.com/activity/index.htm?"
               r"spm=687.8433302/new.33000085.1.6d38226a3fAoxj&scm=1028.1.1.33000085")
    sleep(1)
    driver.find_element_by_link_text("请登录").click()
    sleep(1)
    # driver.find_element_by_css_selector('i[class ~= "iconfont"]').click()
    driver.switch_to.frame("J_loginIframe")
    driver.find_element_by_css_selector('i[class ~= "icon-qrcode"]').click()
    driver.switch_to.default_content()
    sleep(3)
    driver.save_screenshot(path + r'/gmv_log.png')
    imgelement = driver.find_element_by_id('login-banner-wrap')
    # location = imgelement.location
    # size = imgelement.size
    location = {'x': 0, 'y': 88}
    size = {'height': 600, 'width': 1920}
    screenshots_code_image = (int(location['x']) + 1250, int(location['y']) + 180, int(location['x'] + size['width']) - 530,
                              int(location['y'] + size['height'])-260)
    i = Image.open(path + "/gmv_log.png")
    frame4 = i.crop(screenshots_code_image)
    frame4 = frame4.convert('RGB')
    frame4.save(path + '/gmv_log_main.png')
    files = {'file': open(path + r"/gmv_log_main.png", 'rb')}

    # 获取当前页面url保存
    current_page_url = driver.current_url

    def is_login():
        if driver.current_url == current_page_url:
            sleep(2)
            is_login()
        else:
            print('拉登录了！')
            full_path = path + '/ok.txt'  # 也可以创建一个.doc的word文档
            file = open(full_path, 'w')
            file.write('msg')
            # msg也就是下面的Hello world!
            driver.get(r"https://zuanshi.taobao.com/index_poquan.jsp#!/report1/download")
            sleep(3)
            print(len(driver.find_elements_by_tag_name("label")))
            for i in driver.find_elements_by_tag_name("label"):  # 实现遍历点击所有的radio
                print(i.text)
                if "历史分日数据" in i.text:
                    i.click()
                sleep(1)
                if "创意" in i.text:
                    i.click()
            sleep(1)
            for i in driver.find_elements_by_class_name("w220"):  # 实现遍历点击所有的radio
                print(i.text)
                if "过去" in i.text:
                    i.click()
                    sleep(0.5)
                    for j in i.find_elements_by_class_name("dWrqhsrPbp"):   # 实现遍历点击所有的radio
                        print(j.text)
                        if "上月" in j.text:
                            j.click()
            sleep(1)
            print(len(driver.find_elements_by_tag_name("label")))
            for i in driver.find_elements_by_tag_name("label"):  # 实现遍历点击所有的radio
                print(i.text)
                if "点击效果" in i.text:
                    i.click()
                sleep(0.1)
                if "3天" in i.text:
                    i.click()
                sleep(0.1)
                if "7天" in i.text:
                    i.click()
                sleep(0.1)
                if "30天" in i.text:
                    i.click()
            sleep(1)
            driver.find_element_by_link_text("批量下载报表").click()
                
    is_login()
    
    sleep(2)
    open_file = os.listdir(download_path)
    
    # 去重方法
    def remove_repeat_data(data):
        return list(set(data))

    # 下载网络图片的方法
    def download_img(img_url, api_token, name):
        print(img_url)
        header = {"Authorization": "Bearer " + api_token}  # 设置http header，视情况加需要的条目，这里的token是用来鉴权的一种方式
        r = requests.get(img_url, headers=header, stream=True)
        print(r.status_code)  # 返回状态码
        if r.status_code == 200:
            open(download_path+'\\'+name+'.jpg', 'wb').write(r.content)  # 将内容写入图片
            print("done")
        del r

    # 挨个下载图片保存到本地并重命名
    def save_local(file_name):
        driver.refresh()  # 刷新方法 refresh
        sleep(3)
        # 复制名字
        pyperclip.copy(file_name)
        sleep(3)
        # 键盘的粘贴操作
        driver.find_element_by_css_selector('#J_creative_sipt').send_keys(Keys.CONTROL, 'v')
        el = driver.find_element(By.ID, 'J_creative_sipt')
        el.send_keys(Keys.ENTER)
        # 所搜结果列表的第一个的iframe
        tbody = driver.find_elements_by_tag_name("tbody")[0]
        sleep(2)
        print(tbody)
        iframe = tbody.find_elements_by_class_name("previewHtmlShop")[0]
        iframe = iframe.find_elements_by_tag_name("iframe")[0]
        print(iframe)
        sleep(2)
        # 要跳进iframe，不然找不到iframe里面的元素
        driver.switch_to.frame(iframe)
        sleep(2)
        img_url = driver.find_elements_by_tag_name("a")[0]
        print(img_url)
        str_img_style = str(img_url.get_attribute("style"))
        sleep(2)
        print(str_img_style)
        start = str_img_style.find('https://')
        end = str_img_style.find('.jpg')+4
        print(end, start)
        img_url = str_img_style[start:end]
        print(img_url)
        # 调出iframe，不然会报错
        driver.switch_to.default_content()
        # 下载要的图片
        img_url = img_url
        api_token = ""
        download_img(img_url, api_token, file_name)  # 路径，token，名字

    # 创建一个新Excel文件并添加一个工作表。
    work_path = download_path+'\\images.xlsx'
    workbook = xlsxwriter.Workbook(work_path)
    worksheet = workbook.add_worksheet()
    # 加宽第一列使文本更清晰。设置行高为130
    worksheet.set_column('A:M', 20)
    worksheet.set_row(1, 130)
    # 插入一段文字。
    # {'bold': True, 'font_size': 14, 'align': 'center','valign': 'vcenter','border':1, 'color':'red',
    # 'bg_color':'blue'}
    # 文字参数
    format_data = workbook.add_format({'align': 'center', 'valign': 'vcenter'})
    headers = ['创意名称', '花费', '展现量', '点击量', '总成交金额', '总成交笔数', '收藏量', '加购量', '平均点击花费',
               '投产比', '点击量', '转化率', ]
    table_header = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', ]
    # 制作表头
    for index, i in enumerate(headers):
        print(index)
        worksheet.write(table_header[index] + '1', i, format_data)
    
    for i in open_file:
        print(i)
        if i[0:5] == '创意日报表':
            # 打开文件
            data = xlrd.open_workbook(download_path+'\\'+i)
            # 表1
            st = data.sheet_by_index(0)
            # 读取一整列的数据
            lie = [str(st.cell_value(i, 0)) for i in range(0, st.nrows)]
            # 获取到“创意名称”列，去重
            lie = remove_repeat_data(lie)
            for index, j in enumerate(lie):
                # indexD = str(index+2)
                # keyS = 'B' + indexD
                # print(keyS)
                # valueS = j
                worksheet.write('B' + str(index+2), j, format_data)
                sleep(2)
                # 打开图片页面
                driver.get(r"https://zuanshi.taobao.com/index_creative.jsp"
                           r"?spm=a2322.8199842.888888.81.6b0a787eANktH3#!/materiel/proxy/banner")
                # 可能搜索不到图片
                try:
                    save_local(j)
                except Exception as e:
                    print(e.args)
                finally:
                     print('finally...')
                     
                sleep(2)
                try:
                    # 插入一张图片。
                    # 图片参数
                    img_data = {
                        'x_offset': 10,
                        'y_offset': 10,
                        'x_scale': 0.2,
                        'y_scale': 0.2,
                        'url': None,
                        'tip': None,
                        'image_data': None,
                        'positioning': None,
                    }
                    img_index_num = 'A' + str(index+2)
                    worksheet.set_row(index+2, 130)
                    worksheet.insert_image(img_index_num, download_path+'\\'+j+'.jpg', img_data)
                except Exception as e:
                    print(e.args)
                finally:
                     print('finally...')
            print()
        else:
            print('朱瑞')
            
    workbook.close()


if __name__ == '__main__':
    down_main(path=r'./static/20210121151355')