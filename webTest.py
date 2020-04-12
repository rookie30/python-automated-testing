from time import sleep
import xlwt
from selenium import webdriver

# 打开浏览器驱动
driver = webdriver.Chrome(r"D:\tool\chromeDriver\chromedriver.exe")

# 打开网址
driver.get("http://www.51job.com")

# 设置一个等待时间，等待页面元素加载
driver.implicitly_wait(5)

# 定位输入框元素
input_element = driver.find_element_by_id("kwdselectid")

# 在找到输入框元素后，在其中输入文本
input_element.send_keys("python")

# 定位城市选择按钮元素
cityChoose_ele = driver.find_element_by_id("work_position_input")

# 点击城市选择按钮
cityChoose_ele.click()

# 将已选择的城市全部取消选择
# ------------------------------method1-------------------------------------------
# eles = driver.find_elements_by_css_selector("#work_position_click_center_right_list_000000 em[class=on]")
#
# for ele in eles:
#     sleep(1)
#     ele.click()
#
# sleep(1)
# driver.find_element_by_id("work_position_click_center_right_list_category_000000_080200").click()
# ------------------------------method2-------------------------------------------
eles = driver.find_elements_by_css_selector("#work_position_click_multiple_selected .ttag")

for ele in eles:
    sleep(1)
    ele.click()

sleep(1)
driver.find_element_by_id("work_position_click_center_right_list_category_000000_080200").click()

# 保存城市选择
driver.find_element_by_id("work_position_click_bottom_save").click()

# 点击搜索
# sleep(1)
driver.find_element_by_css_selector(".fltr button").click()

# 搜索结果
jobs = driver.find_elements_by_css_selector("#resultList div[class=el]")

for job in jobs:
    fields = job.find_elements_by_tag_name("span")
    stringFields = [field.text for field in fields]
    print("  |  ".join(stringFields))


# 创建一个Excel workbook对象
book = xlwt.Workbook()

# 新建一个sheet
sheet = book.add_sheet("职位结果")

# 写入内容
row = 0
for job in jobs:
    fields = job.find_elements_by_tag_name("span")
    col = 0
    for field in fields:
        text = field.text
        sheet.write(row, col, text)
        col += 1
    row += 1

# 保存文件
book.save(r"C:\Users\hp\Desktop\job.xls")

driver.quit()
