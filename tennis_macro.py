import sys
from PySide2 import QtCore
from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.alert import Alert

# MAIN WINDOW
from ui_test_tennis import Ui_MainWindow


court_list = {
    '복사골테니스장': '111',
    '원미테니스장': '112',
    '소사배수지테니스장': '114',
    '종합운동장테니스장': '115',
    '성주산체육공원테니스장': '116',
    '오정레포츠센터 테니스장': '188',
    '부천체육관테니스장(하드)': '192',
    '남부수자원테니스장': '193',
    '해그늘체육공원 테니스장': '194',
    '부천실내테니스장': '195',
}

period_list = {
    '06:00~08:00': 0,
    '08:00~10:00': 1,
    '10:00~12:00': 2,
    '12:00~14:00': 3,
    '14:00~16:00': 4,
    '16:00~18:00': 5,
    '18:00~20:00': 6,
    '20:00~22:00': 7
}

global browser_c, browser_f, browser_e, id_c, id_f, id_e, pw_c, pw_f, pw_e, court_c, court_f, court_e
global count_c, count_f, count_e

date_c = []
period_c = []
status_c = []
date_f = []
period_f = []
status_f = []
date_e = []
period_e = []
status_e = []


class ThreadClass_c(QtCore.QThread):
    def __init__(self, parent=None):
        super(ThreadClass_c, self).__init__(parent)
        self.parent = parent

    def run(self):
        browser_c = "Chrome"
        global count_c
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        service = Service(ChromeDriverManager(version="114.0.5735.90").install())
        chrome_driver = webdriver.Chrome(service=service, options=options)
        chrome_wait = WebDriverWait(chrome_driver, 20)

        ## SITE LOGIN
        chrome_driver.get('https://reserv.bucheon.go.kr/site/main/login')
        member_login = chrome_wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[@class='login_btn']")))
        member_login.click()
        id_input = chrome_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login_id")))
        pw_input = chrome_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login_pwd")))
        time.sleep(3)
        id_input.click()
        id_input.send_keys(id_c)
        time.sleep(3)
        pw_input.click()
        pw_input.send_keys(pw_c)
        login_button = chrome_wait.until(EC.element_to_be_clickable((By.XPATH, f"//p[@class='ui1300-logBtn']")))
        login_button.click()
        time.sleep(5)

        count_c = 0

        while any(a == "예약미완료" for a in status_c):
            print("----------------" + browser_c + "----------------")
            for i in range(len(date_c)):
                print(date_c[i] + " " + period_c[i] + " (" + status_c[i] + ")" + "\n")
            for i in range(len(status_c)):
                if status_c[i] == "예약완료":
                    continue
                else:
                    ## TENNIS COURT RESERVE MACRO START(REQUESTS)
                    session = requests.session()
                    url_lending = f"https://reserv.bucheon.go.kr/site/main/lending/lendingDetail?lending_info_seq={court_c}&inst_cate=0103&sch_year={date_c[i][0:4]}&sch_month={date_c[i][4:6]}"
                    res = session.get(url_lending)
                    soup = BeautifulSoup(res.text, "html.parser")
                    try:
                        calendar_date_tag = soup.find('ul', id=f"{date_c[i][4:8]}")
                        calendar_clock_tags = calendar_date_tag.select(".tm")
                        clock_tag = period_list.get(period_c[i])
                    except AttributeError:
                        print("사이트 오픈시간이 아직 아닙니다.")
                        continue

                    if "grn" in calendar_clock_tags[clock_tag].find_next_sibling()["class"]:
                        print(browser_c + ": " + str(i + 1) + "번째 날짜는 예약이 가능하므로 자동예매작업을 시작합니다.")
                        chrome_driver.get(
                            f'https://reserv.bucheon.go.kr/site/main/lending/lendingDetail?lending_info_seq={court_c}&inst_cate=0103&sch_year={date_c[i][0:4]}&sch_month={date_c[i][4:6]}')

                        ## AFTER CHECKING SEAT RESERVATION STATUS EMPTY --> REALTIME RESERVE START
                        court_clock = chrome_wait.until(EC.element_to_be_clickable((By.XPATH, f"//ul[@id='{date_c[i][4:8]}']//li//a[text()='{period_c[i]}']")))
                        court_clock.click()

                        address = chrome_wait.until(EC.element_to_be_clickable((By.XPATH, f"//input[@id='search_address']")))
                        address.click()
                        address.send_keys("(14547)경기도 부천시 길주로 210")
                        address_search = chrome_wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[@class='btn-style post-btn btn_pop']")))
                        address_search.click()
                        address_select = chrome_wait.until(EC.element_to_be_clickable((By.XPATH, f"//input[@class='btn_m btn_co01']")))
                        address_select.click()

                        ## AFTER CHOOSING DATE --> CHOOSE COURT NUMBER, CLICK TWO AGREE BUTTONS, FINAL CONTRIBUTE
                        agree1_button = chrome_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#a1')))
                        agree1_button.click()
                        agree2_button = chrome_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#a2')))
                        agree2_button.click()
                        td_element = chrome_driver.find_element(By.CSS_SELECTOR, 'td.labeldioest')
                        court_button = td_element.find_element(By.XPATH, './*')
                        court_button.click()
                        submit_button = chrome_wait.until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, '#CtznLendingBooking > '
                                                                         'div.right-btn >'
                                                                         'a.btn-style.search')))
                        submit_button.click()
                        time.sleep(2)
                        da = Alert(chrome_driver)
                        da.accept()
                        time.sleep(1)
                        status_c[i] = "예약완료"
                        da.accept()
                        time.sleep(5)
                    else:
                        print(browser_c + ": " + str(i + 1) + "번째 날짜는 예약이 불가능합니다.")
                        count_c += 1
                        if count_c / 10 == 1:
                            chrome_driver.get('https://reserv.bucheon.go.kr/site/main/main')


class ThreadClass_f(QtCore.QThread):
    def __init__(self, parent=None):
        super(ThreadClass_f, self).__init__(parent)
        self.parent = parent

    def run(self):
        browser_f = "Firefox"
        global count_f
        firefox_service = Service(GeckoDriverManager().install())
        firefox_driver = webdriver.Firefox(service=firefox_service)
        firefox_wait = WebDriverWait(firefox_driver, 20)

        ## SITE LOGIN
        firefox_driver.get('https://reserv.bucheon.go.kr/site/main/login')
        member_login = firefox_wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[@class='login_btn']")))
        member_login.click()
        id_input = firefox_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login_id")))
        pw_input = firefox_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login_pwd")))
        time.sleep(3)
        id_input.click()
        id_input.send_keys(id_f)
        time.sleep(3)
        pw_input.click()
        pw_input.send_keys(pw_f)
        login_button = firefox_wait.until(EC.element_to_be_clickable((By.XPATH, f"//p[@class='ui1300-logBtn']")))
        login_button.click()
        time.sleep(5)

        count_f = 0

        while any(a == "예약미완료" for a in status_f):
            print("----------------" + browser_f + "----------------")
            for i in range(len(date_f)):
                print(date_f[i] + " " + period_f[i] + " (" + status_f[i] + ")" + "\n")
            for i in range(len(status_f)):
                if status_f[i] == "예약완료":
                    continue
                else:
                    ## TENNIS COURT RESERVE MACRO START(REQUESTS)
                    session = requests.session()
                    url_lending = f"https://reserv.bucheon.go.kr/site/main/lending/lendingDetail?lending_info_seq={court_f}&inst_cate=0103&sch_year={date_f[i][0:4]}&sch_month={date_f[i][4:6]}"
                    res = session.get(url_lending)
                    soup = BeautifulSoup(res.text, "html.parser")
                    try:
                        calendar_date_tag = soup.find('ul', id=f"{date_f[i][4:8]}")
                        calendar_clock_tags = calendar_date_tag.select(".tm")
                        clock_tag = period_list.get(period_f[i])
                    except AttributeError:
                        print("사이트 오픈시간이 아직 아닙니다.")
                        continue

                    if "grn" in calendar_clock_tags[clock_tag].find_next_sibling()["class"]:
                        print(browser_f + ": " + str(i + 1) + "번째 날짜는 예약이 가능하므로 자동예매작업을 시작합니다.")
                        firefox_driver.get(
                            f'https://reserv.bucheon.go.kr/site/main/lending/lendingDetail?lending_info_seq={court_f}&inst_cate=0103&sch_year={date_f[i][0:4]}&sch_month={date_f[i][4:6]}')

                        ## AFTER CHECKING SEAT RESERVATION STATUS EMPTY --> REALTIME RESERVE START
                        court_clock = firefox_wait.until(EC.element_to_be_clickable(
                            (By.XPATH, f"//ul[@id='{date_f[i][4:8]}']//li//a[text()='{period_f[i]}']")))
                        court_clock.click()

                        address = firefox_wait.until(EC.element_to_be_clickable((By.XPATH, f"//input[@id='search_address']")))
                        address.click()
                        address.send_keys("(14547)경기도 부천시 길주로 210")
                        address_search = firefox_wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[@class='btn-style post-btn btn_pop']")))
                        address_search.click()
                        address_select = firefox_wait.until(EC.element_to_be_clickable((By.XPATH, f"//input[@class='btn_m btn_co01']")))
                        address_select.click()

                        ## AFTER CHOOSING DATE --> CHOOSE COURT NUMBER, CLICK TWO AGREE BUTTONS, FINAL CONTRIBUTE
                        agree1_button = firefox_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#a1')))
                        agree1_button.click()
                        agree2_button = firefox_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#a2')))
                        agree2_button.click()
                        td_element = firefox_driver.find_element(By.CSS_SELECTOR, 'td.labeldioest')
                        court_button = td_element.find_element(By.XPATH, './*')
                        court_button.click()
                        submit_button = firefox_wait.until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, '#CtznLendingBooking > '
                                                                         'div.right-btn >'
                                                                         'a.btn-style.search')))
                        submit_button.click()
                        time.sleep(2)
                        da = Alert(firefox_driver)
                        da.accept()
                        time.sleep(1)
                        status_f[i] = "예약완료"
                        da.accept()
                        time.sleep(5)
                    else:
                        print(browser_f + ": " + str(i + 1) + "번째 날짜는 예약이 불가능합니다.")
                        count_f += 1
                        if count_f / 10 == 1:
                            firefox_driver.get('https://reserv.bucheon.go.kr/site/main/main')


class ThreadClass_e(QtCore.QThread):
    def __init__(self, parent=None):
        super(ThreadClass_e, self).__init__(parent)
        self.parent = parent

    def run(self):
        browser_e = "Microsoft Edge"
        global count_e
        edge_service = Service(EdgeChromiumDriverManager().install())
        edge_driver = webdriver.Edge(service=edge_service)
        edge_wait = WebDriverWait(edge_driver, 20)

        ## SITE LOGIN
        edge_driver.get('https://reserv.bucheon.go.kr/site/main/login')
        member_login = edge_wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[@class='login_btn']")))
        member_login.click()
        id_input = edge_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login_id")))
        pw_input = edge_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login_pwd")))
        time.sleep(3)
        id_input.click()
        id_input.send_keys(id_e)
        time.sleep(3)
        pw_input.click()
        pw_input.send_keys(pw_e)
        login_button = edge_wait.until(EC.element_to_be_clickable((By.XPATH, f"//p[@class='ui1300-logBtn']")))
        login_button.click()
        time.sleep(5)

        count_e = 0

        while any(a == "예약미완료" for a in status_e):
            print("----------------" + browser_e + "----------------")
            for i in range(len(date_e)):
                print(date_e[i] + " " + period_e[i] + " (" + status_e[i] + ")" + "\n")
            for i in range(len(status_e)):
                if status_e[i] == "예약완료":
                    continue
                else:
                    ## TENNIS COURT RESERVE MACRO START(REQUESTS)
                    session = requests.session()
                    url_lending = f"https://reserv.bucheon.go.kr/site/main/lending/lendingDetail?lending_info_seq={court_e}&inst_cate=0103&sch_year={date_e[i][0:4]}&sch_month={date_e[i][4:6]}"
                    res = session.get(url_lending)
                    soup = BeautifulSoup(res.text, "html.parser")
                    try:
                        calendar_date_tag = soup.find('ul', id=f"{date_e[i][4:8]}")
                        calendar_clock_tags = calendar_date_tag.select(".tm")
                        clock_tag = period_list.get(period_e[i])
                    except AttributeError:
                        print("사이트 오픈시간이 아직 아닙니다.")
                        continue
                    if "grn" in calendar_clock_tags[clock_tag].find_next_sibling()["class"]:
                        print(browser_e + ": " + str(i + 1) + "번째 날짜는 예약이 가능하므로 자동예매작업을 시작합니다.")
                        edge_driver.get(
                            f'https://reserv.bucheon.go.kr/site/main/lending/lendingDetail?lending_info_seq={court_e}&inst_cate=0103&sch_year={date_e[i][0:4]}&sch_month={date_e[i][4:6]}')

                        ## AFTER CHECKING SEAT RESERVATION STATUS EMPTY --> REALTIME RESERVE START
                        court_clock = edge_wait.until(EC.element_to_be_clickable(
                            (By.XPATH, f"//ul[@id='{date_e[i][4:8]}']//li//a[text()='{period_e[i]}']")))
                        court_clock.click()

                        address = edge_wait.until(EC.element_to_be_clickable((By.XPATH, f"//input[@id='search_address']")))
                        address.click()
                        address.send_keys("(14547)경기도 부천시 길주로 210")
                        address_search = edge_wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[@class='btn-style post-btn btn_pop']")))
                        address_search.click()
                        address_select = edge_wait.until(EC.element_to_be_clickable((By.XPATH, f"//input[@class='btn_m btn_co01']")))
                        address_select.click()

                        ## AFTER CHOOSING DATE --> CHOOSE COURT NUMBER, CLICK TWO AGREE BUTTONS, FINAL CONTRIBUTE
                        agree1_button = edge_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#a1')))
                        agree1_button.click()
                        agree2_button = edge_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#a2')))
                        agree2_button.click()
                        td_element = edge_driver.find_element(By.CSS_SELECTOR, 'td.labeldioest')
                        court_button = td_element.find_element(By.XPATH, './*')
                        court_button.click()
                        submit_button = edge_wait.until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, '#CtznLendingBooking > '
                                                                         'div.right-btn >'
                                                                         'a.btn-style.search')))
                        submit_button.click()
                        time.sleep(2)
                        da = Alert(edge_driver)
                        da.accept()
                        time.sleep(1)
                        status_e[i] = "예약완료"
                        da.accept()
                        time.sleep(5)
                    else:
                        print(browser_e + ": " + str(i + 1) + "번째 날짜는 예약이 불가능합니다.")
                        count_e += 1
                        if count_e / 10 == 1:
                            edge_driver.get('https://reserv.bucheon.go.kr/site/main/main')


# YOUR APPLICATION
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## CONNECT OKBUTTON
        self.ui.chromeButton.clicked.connect(self.chromebuttonfunc)
        self.ui.firefoxButton.clicked.connect(self.firefoxbuttonfunc)
        self.ui.edgeButton.clicked.connect(self.edgebuttonfunc)

        ## INSERT INFORMATIONS, CHECK MESSAGEBOX
        self.ui.infoButton.clicked.connect(self.message)

        ## DRIVER --> PROGRESSBROWSER
        self.ui.chromeButton.clicked.connect(self.chrome_progress)
        self.ui.firefoxButton.clicked.connect(self.firefox_progress)
        self.ui.edgeButton.clicked.connect(self.edge_progress)

    def chrome_progress(self):
        self.ui.progressBrowser.append("Chrome에서 매크로작업을 시작합니다.")

    def firefox_progress(self):
        self.ui.progressBrowser.append("Firefox에서 매크로작업을 시작합니다.")

    def edge_progress(self):
        self.ui.progressBrowser.append("Edge에서 매크로작업을 시작합니다.")

    def info_progress(self):
        self.ui.progressBrowser.append("제출되었습니다.")

    def message(self):
        msgbox = QMessageBox()
        msgbox.setIcon(QMessageBox.Information)
        msgbox.setWindowTitle("확인")
        msgbox.setWindowIcon(QIcon('tennis_icon.ico'))
        msgbox.setText("검토를 완료하셨습니까? 오타는 오류를 생성합니다!")
        msgbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        ending = msgbox.exec_()

        if ending == QMessageBox.Ok:
            self.infobuttonfunc()
            self.info_progress()

    def infobuttonfunc(self):
        global browser_c, browser_f, browser_e, id_c, id_f, id_e, pw_c, pw_f, pw_e, court_c, court_f, court_e

        browser = self.ui.browserBox.currentText()
        id = self.ui.idEdit.text()
        pw = self.ui.pwEdit.text()
        court_name = self.ui.courtBox.currentText()
        court = court_list.get(court_name)
        date = self.ui.dateEdit.text()
        period = self.ui.timeBox.currentText()
        self.ui.infoBrowser.append("브라우저: " + browser)
        self.ui.infoBrowser.append("아이디: " + id)
        self.ui.infoBrowser.append("패스워드: " + pw)
        self.ui.infoBrowser.append("테니스장: " + court_name)
        self.ui.infoBrowser.append("날짜: " + date)
        self.ui.infoBrowser.append("시간대: " + period + "\n")

        if browser == "Chrome":
            browser_c = "Chrome"
            id_c = id
            pw_c = pw
            court_c = court
            date_c.append(date)
            period_c.append(period)
            status_c.append("예약미완료")
        elif browser == "Firefox":
            browser_f = "Firefox"
            id_f = id
            pw_f = pw
            court_f = court
            date_f.append(date)
            period_f.append(period)
            status_f.append("예약미완료")
        else:
            browser_e = "Microsoft Edge"
            id_e = id
            pw_e = pw
            court_e = court
            date_e.append(date)
            period_e.append(period)
            status_e.append("예약미완료")

    def chromebuttonfunc(self):
        thread_class_c = ThreadClass_c(self)
        thread_class_c.start()

    def firefoxbuttonfunc(self):
        thread_class_f = ThreadClass_f(self)
        thread_class_f.start()

    def edgebuttonfunc(self):
        thread_class_e = ThreadClass_e(self)
        thread_class_e.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
