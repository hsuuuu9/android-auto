name = "大可　悠"
name2 = "オオカワ　ユウ"
tel = "09023457654"
mail = "jetfixdue@mbox.re"
prefecture = '東京都'
store_name = 'GEO国立店'

from appium import webdriver
import time
caps = {}
caps["platformName"] = "android"
caps["ensureWebviewsHavePages"] = True


driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

el1 = driver.find_element_by_accessibility_id("ゲオ")
el1.click()
time.sleep(2)

while True:
    if len(driver.find_elements_by_id("jp.co.geoonline.app:id/imgMedia")) == 0:
        driver.swipe(start_x=75, start_y=500, end_x=75, end_y=200, duration=100)
    else:
        break
time.sleep(2)
driver.find_elements_by_id("jp.co.geoonline.app:id/imgMedia")[0].click()

while True:
    if len(driver.find_elements_by_accessibility_id("抽選販売に申し込む")) == 0:
        driver.swipe(start_x=75, start_y=1000, end_x=75, end_y=100, duration=100)
    else:
        break
time.sleep(2)
driver.find_elements_by_accessibility_id("抽選販売に申し込む")[0].click()



while True:
    try:
        el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.widget.Spinner")
        el1.click()
        break
    except:
        driver.swipe(start_x=75, start_y=500, end_x=75, end_y=400, duration=100)

while True:
    pres = driver.find_elements_by_class_name('android.widget.CheckedTextView')
    break_point = 0
    for pre in pres:
        if pre.text == prefecture:
            break_point = 1
    if break_point == 0:
        driver.swipe(start_x=75, start_y=500, end_x=75, end_y=400, duration=100)
    else:
        break
pre.click()

while True:
    try:
        el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.widget.Spinner[2]")
        el1.click()
        break
    except:
        driver.swipe(start_x=75, start_y=500, end_x=75, end_y=400, duration=100)

while True:
    pres = driver.find_elements_by_class_name('android.widget.CheckedTextView')
    break_point = 0
    for pre in pres:
        if pre.text == store_name:
            break_point = 1
    if break_point == 0:
        driver.swipe(start_x=75, start_y=500, end_x=75, end_y=400, duration=100)
    else:
        break
pre.click()

while True:
    try:
        el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.widget.EditText[1]")
        el2.send_keys(name)
        break
    except:
        driver.swipe(start_x=75, start_y=500, end_x=75, end_y=400, duration=100)

while True:
    try:
        el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.widget.EditText[2]")
        el2.send_keys(name2)
        break
    except:
        driver.swipe(start_x=75, start_y=500, end_x=75, end_y=400, duration=100)

while True:
    try:
        el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.widget.EditText[3]")
        el2.send_keys(tel)
        break
    except:
        driver.swipe(start_x=75, start_y=500, end_x=75, end_y=400, duration=100)

while True:
    try:
        el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.widget.EditText[4]")
        el2.send_keys(tel)
        break
    except:
        driver.swipe(start_x=75, start_y=500, end_x=75, end_y=400, duration=100)

while True:
    try:
        el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[8]/android.widget.EditText[1]")
        el2.send_keys(mail)
        break
    except:
        driver.swipe(start_x=75, start_y=500, end_x=75, end_y=400, duration=100)

while True:
    try:
        el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[8]/android.widget.EditText[2]")
        el2.send_keys(mail)
        break
    except:
        driver.swipe(start_x=75, start_y=500, end_x=75, end_y=400, duration=100)


while True:
    try:
        el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]/android.widget.CheckBox")
        el1.click()
        break
    except:
        driver.swipe(start_x=75, start_y=500, end_x=75, end_y=400, duration=100)



while True:
    try:
        el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[5]/android.widget.CheckBox")
        el2.click()
        break
    except:
        driver.swipe(start_x=75, start_y=500, end_x=75, end_y=400, duration=100)



while True:
    try:
        el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.widget.Button")
        el2.click()
        break
    except:
        driver.swipe(start_x=75, start_y=500, end_x=75, end_y=400, duration=100)

while True:
    try:
        el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.widget.CheckBox")
        el1.click()
        break
    except:
        driver.swipe(start_x=75, start_y=500, end_x=75, end_y=200, duration=100)

for i in range(5):
    driver.swipe(start_x=75, start_y=500, end_x=75, end_y=400, duration=100)
while True:
    try:
        el2 = driver.find_element_by_accessibility_id("申し込む")
        el2.click()
        break
    except:
        pass

while True:
    try:
        el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[5]/android.view.View[2]/android.widget.Button")
        el1.click()
        break
    except:
        driver.swipe(start_x=75, start_y=500, end_x=75, end_y=400, duration=100)

el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[1]")

idid = el2.text.split('\n')[1]
print(mail,idid)
