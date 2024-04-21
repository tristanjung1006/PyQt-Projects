import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QUrl, QFile)
from PySide2.QtGui import (QColor)
from PySide2.QtWidgets import *

# SPLASH SCREEN
from ui_splash_screen import Ui_Splash_Screen

# MAIN WINDOW
from ui_main import Ui_MainWindow
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import pyperclip
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException

"""
cgv_ats 0.1.4 update:
1. okbutton_3를 thread화시켜서 프로그램 응답없음문제 해결
2. 로그인 이후 50분 지나면 로그인 세션 무효처리문제 해결
cgv_ats 0.1.5 update:
1. 상영시간대 매진 외에도 준비중 상태까지 예외처리 완료
cgv_ats 0.1.6 update:
1. 상영시간표 스크롤 필요한 경우를 대비해서 대기시간 걸어놓음
cgv_ats 0.1.7 update:
1. 좌석표에서 인원(청소년) 체크할 경우 대기시간 걸어놓음
cgv_ats 0.1.8 update:
1. 아직 오픈되지 않은 날짜에 해당하는 영화도 매크로가 가능함
cgv_ats 0.1.9 update:
1. 좌석표 갱신과정에서 속도개선을 위해 문구 삭제
cgv_ats 0.2.0 update:
1. 상영시간표 루프에서는 로그인 세션 만료가 되지 않으므로 재로그인 삭제
cgv_ats 0.2.1 update:
1. 4DX 일회용 팝업창 제거X
2. 유효한 상영날짜 확인 후 과부하 방지를 위한 대기시간 부여
3. 로그인 세션 만료 방지 부분에서 로그아웃버튼 클릭 추가
4. 시간초과로 인한 상영시간표 세션으로 이동할 때 iframe 대기시간 부여
5. 해당 시간대가 매진이나 준비중일 경우 갱신을 2번이나 하는 문제해결
cgv_ats 0.2.2 update:
1. 로그아웃 버튼 클릭불가문제로 인한 로그아웃 세션으로 접근
cgv_ats 0.2.3 update:
1. 상영시간표 프레임 코드 위치 변경
cgv_ats 0.2.4 update:
1. 매진 부분 개선
cgv_ats 0.2.5 update
1. 로그인 세션 유지를 위한 시간 재기 부분 개선
cgv_ats 0.2.6 update
1. 전 구문에 ElementClickIntercepted 예외처리
cgv_ats 0.2.7 update
1. 모든 find_element 메서드 wait시킴
cgv_ats 0.2.8 update
1. 프로그램 pause resume 버튼 삽입 및 pause delay시간 설정 버튼 추가
cgv_ats 0.2.9 update
1. 전체관람가 영화 팝업창 문제 해결
"""

mode_list = {
    '전체': 'sbmt_all',
    '2D': 'sbmt_digital',
    'IMAX': 'sbmt_imax',
    '4DX': 'sbmt_4dx',
    'SOUNDX': 'sbmt_soundx',
    'SCREENX': 'sbmt_screenx',
    '프리미어 상영': 'thidItem_PS',
    'PRIVATE BOX': 'thidItem_YG',
    '무대인사': 'thidItem_NO',
    'PRIVATE BOX,무대인사': 'thidItem_38'
}

# GLOBALS
counter = 0
global id, pw, name, mode, city, hall, date, clock, person, group, delay, paused
row = []
seat_1 = []
seat_2 = []


class ThreadClass(QtCore.QThread):
    def __init__(self, parent=None):
        super(ThreadClass, self).__init__(parent)
        self.parent = parent

    def pausebuttonfunc(self):
        global paused
        paused = True
        print("일시중지를 실행합니다.")

    def resumebuttonfunc(self):
        global paused
        paused = False
        print("일시중지를 해제합니다.")

    def run(self):
        global paused
        paused = False
        # 크롬 115버전부터 셀레니움 오류
        options = webdriver.ChromeOptions()
        # options.add_experimental_option('excludeSwitches', ['enable-logging'])
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        # 크롬 창 최대화
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        break_login = False
        while True:
            if break_login:
                break

            # 로그인 세션 만료 방지를 위한 시간 재기
            start_time_all = time.time()

            # CGV 로그인
            driver.get('https://www.cgv.co.kr/user/login/')
            time.sleep(10)
            id_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#txtUserId')))
            id_input.click()
            pyperclip.copy(id)
            id_input.send_keys(Keys.CONTROL, 'v')
            time.sleep(1)
            pw_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#txtPassword')))
            pw_input.click()
            pyperclip.copy(pw)
            pw_input.send_keys(Keys.CONTROL, 'v')
            time.sleep(1)
            submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#submit')))
            submit_button.click()
            time.sleep(4)

            break_timetable = False
            while True:
                if break_timetable:
                    break

                try:
                    # CGV 사이트 빠른 예매 접속
                    driver.get('http://www.cgv.co.kr/ticket/')

                    # 해당 XPath를 가진 프레임 요소가 로드될 때까지 기다립니다.
                    iframe = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/iframe")))

                    # 프레임으로 전환합니다.
                    driver.switch_to.frame(iframe)
                    while True:
                        while True:
                            # 영화 제목
                            movie_name = wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[@title='{name}']")))
                            time.sleep(1)
                            movie_name.click()

                            # 영화 모드
                            mode_find = mode_list.get(mode)
                            movie_mode = wait.until(
                                EC.element_to_be_clickable((By.CSS_SELECTOR, f'li[id="{mode_find}"]')))
                            time.sleep(1)
                            movie_mode.click()

                            # 영화관 도시 위치
                            movie_city = wait.until(EC.element_to_be_clickable(
                                (By.XPATH, f"//div[@class='theater-area-list']//span[text()='{city}']")))
                            time.sleep(1)
                            movie_city.click()

                            # 영화관 도시의 지역 위치
                            movie_hall = wait.until(
                                EC.element_to_be_clickable((By.XPATH, f"//div//li//a[text()='{hall}']")))
                            time.sleep(1)
                            movie_hall.click()

                            # 영화 상영 날짜
                            movie_date = wait.until(EC.element_to_be_clickable((By.XPATH, f"//li[@date='{date}']")))
                            movie_date_class = movie_date.get_attribute('class')
                            time.sleep(3)
                            if 'dimmed' in movie_date_class:
                                print("미오픈 상영날짜이므로 상영시간표를 갱신합니다.")
                                refresh = wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[@class='button "
                                                                                           f"button-reservation"
                                                                                           f"-restart']")))
                                refresh.click()
                            else:
                                movie_date.click()
                                time.sleep(2)
                                print("유효한 상영날짜입니다.")
                                break

                        # 영화 상영 시간
                        movie_time = wait.until(
                            EC.element_to_be_clickable((By.XPATH, f"//li[@play_start_tm='{clock}']")))
                        movie_time_tag = movie_time.find_element(By.XPATH, f".//a/span[@class='count']")
                        time.sleep(3)
                        if "매진" in movie_time_tag.text:
                            print("해당 시간대는 현재 매진입니다.")
                            while True:
                                movie_date.click()
                                time.sleep(2)
                                print(paused)
                                if paused:
                                    time.sleep(int(delay))
                                movie_time = wait.until(
                                    EC.element_to_be_clickable((By.XPATH, f"//li[@play_start_tm='{clock}']")))
                                movie_time_tag = movie_time.find_element(By.XPATH, f".//a/span[@class='count']")
                                time.sleep(3)
                                if "매진" not in movie_time_tag.text:
                                    movie_time.click()
                                    time.sleep(2)
                                    break
                            continue
                        elif "준비중" in movie_time_tag.text:
                            print("해당 시간대는 현재 준비중입니다.")
                            while True:
                                movie_date.click()
                                time.sleep(2)
                                movie_time = wait.until(
                                    EC.element_to_be_clickable((By.XPATH, f"//li[@play_start_tm='{clock}']")))
                                movie_time_tag = movie_time.find_element(By.XPATH, f".//a/span[@class='count']")
                                time.sleep(2)
                                if "준비중" not in movie_time_tag.text:
                                    movie_time.click()
                                    time.sleep(2)
                                    break
                            continue
                        else:
                            movie_time.click()
                            time.sleep(2)
                            break

                        # 오펜하이머 천호 주말 전용 코드
                        # movie_times = driver.find_elements(By.XPATH, "//li[starts-with(@play_start_tm, '19') or "
                        #                                              "starts-with(@play_start_tm, '20')]")
                        # time.sleep(2)
                        # if movie_times:  # 선택된 요소가 있을 경우
                        #     movie_times[0].click()
                        #     break

                    # 좌석선택 버튼 클릭
                    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#tnb_step_btn_right')))
                    button.click()
                    time.sleep(2)

                    try:
                        time.sleep(3)
                        # 팝업창 클릭
                        popup = driver.find_element(By.CSS_SELECTOR,
                                                    'body > div[class*="ft_layer_popup popup_alert"] > div.ft > a')
                        popup.click()
                        print("팝업창을 닫았습니다.")
                    except (NoSuchElementException, TimeoutException):
                        pass

                    # 일반/청소년 구분 후 해당 인원 수 클릭
                    if group == "일반":
                        people = wait.until(
                            EC.element_to_be_clickable((By.XPATH, f"//li[@data-count='{person}'][@type='adult']")))
                        people.click()
                        time.sleep(1)
                    else:
                        people = wait.until(
                            EC.element_to_be_clickable((By.XPATH, f"//li[@data-count='{person}'][@type='youth']")))
                        people.click()
                        time.sleep(1)

                    # 좌석표
                    ## 좌석표 체류 시간 제한으로 인해 체류 시간 카운팅
                    start_time = time.time()
                    break_seat_reserved = False
                    while True:
                        if break_seat_reserved:
                            break
                        for i in range(len(row)):
                            if break_seat_reserved:
                                break
                            for j in range(int(seat_2[i]) - int(seat_1[i]) + 1):
                                r_elem = driver.find_element(By.XPATH, f"//div[@class='row']//div[text()='{row[i]}']")
                                r2_elem = r_elem.find_element(By.XPATH, './..')
                                s_elem = r2_elem.find_element(By.XPATH,
                                                              f".//span[@class='no' and text()='{str(int(seat_1[i]) + j)}']")
                                parent_elem = s_elem.find_element(By.XPATH, './../..')
                                class_attr = parent_elem.get_attribute('class')
                                if "seat reserved" in class_attr:
                                    print(row[i] + str(int(seat_1[i]) + j) + ": 예약불가이므로 좌석표를 갱신합니다.")
                                    time.sleep(random.uniform(0.5, 1))
                                    refresh = wait.until(
                                        EC.element_to_be_clickable((By.CSS_SELECTOR, '#ticket > div.steps > '
                                                                                     'div.step.step2 > a')))
                                    refresh.click()
                                    if group == "일반":
                                        people = wait.until(EC.element_to_be_clickable(
                                            (By.XPATH, f"//li[@data-count='{person}'][@type='adult']")))
                                        time.sleep(1)
                                        people.click()
                                    else:
                                        people = wait.until(EC.element_to_be_clickable(
                                            (By.XPATH, f"//li[@data-count='{person}'][@type='youth']")))
                                        time.sleep(1)
                                        people.click()
                                    continue
                                else:
                                    s_elem.click()
                                    button2 = wait.until(
                                        EC.element_to_be_clickable((By.CSS_SELECTOR, '#tnb_step_btn_right')))
                                    button2.click()
                                    break_seat_reserved = True
                                    break_timetable = True
                                    break_login = True
                                    break

                        # 루프 시작부터 현재까지의 시간이 1분 40초 (100초)가 넘었는지 확인
                        elapsed_time = time.time() - start_time
                        if elapsed_time > 100:
                            print("좌석 선택 시간이 초과되어 상영시간표로 이동합니다.")
                            break

                    if break_login:
                        break

                    # 루프 시작부터 현재까지의 시간이 50분 (3000초)가 넘었는지 확인
                    elapsed_time_all = time.time() - start_time_all
                    if elapsed_time_all > 3000:
                        print("로그인 세션 유효 기간이 초과되어 로그아웃 후, 로그인 화면으로 이동합니다.")
                        driver.get('https://www.cgv.co.kr/user/login/logout.aspx')
                        time.sleep(10)
                        break

                except ElementClickInterceptedException:
                    time.sleep(10)
                    break

        # 텔레그램 봇으로 알림
        # import requests
        #
        # def send_telegram_message(token, chat_id, message):
        #     base_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        #     response = requests.get(base_url)
        #     return response.json()

        # replace with your bot token and chat ID(cgv_alarm)
        # token = "6375642379:AAGLNSvdE17QCrFnATnvmCq5Qx6tA5Jc3VM"
        # chat_id = "6324662357"

        # response_check = send_telegram_message(token, chat_id, message)
        # print("원하는 좌석이 선택되었습니다.")
        # print(response_check)

        # WAV 파일을 읽어와서 재생
        import wave
        import pyaudio

        # 오디오 파일 열기
        with wave.open("alert.wav", 'rb') as wf:
            p = pyaudio.PyAudio()

            # 스트림 설정
            stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True)

            # 3초 동안의 데이터만 읽기
            frames_to_read = int(wf.getframerate() * 3)  # 초당 프레임 수 * 3초
            data = wf.readframes(frames_to_read)

            # 데이터 재생
            stream.write(data)

            # 스트림 닫기
            stream.stop_stream()
            stream.close()

            # PyAudio 종료
            p.terminate()

        time.sleep(720)  # 720초 대기

        driver.quit()  # 드라이버 종료


# YOUR APPLICATION
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## CONNECT OKBUTTON
        self.ui.okButton.clicked.connect(self.okButtonFunc)
        self.ui.okButton_2.clicked.connect(self.message)
        self.ui.okButton_3.clicked.connect(self.okButton_3Func)
        self.ui.okButton_4.clicked.connect(self.okButton_4Func)

        ## CONNECT QUITBUTTON
        self.ui.quitButton.clicked.connect(self.quitButtonFunc)

        ## CONNECT PAUSE, RESUME BUTTON
        self.ui.pauseButton.clicked.connect(ThreadClass.pausebuttonfunc)
        self.ui.resumeButton.clicked.connect(ThreadClass.resumebuttonfunc)

    def quitButtonFunc(self):
        QCoreApplication.instance().quit()

    def okButtonFunc(self):
        global id, pw, name, mode, city, hall, date, clock
        id = self.ui.lineEdit_id.text()
        pw = self.ui.lineEdit_pw.text()
        name = self.ui.lineEdit_name.text()
        mode = self.ui.lineEdit_mode.text()
        city = self.ui.lineEdit_city.text()
        hall = self.ui.lineEdit_hall.text()
        date = self.ui.lineEdit_date.text()
        clock = self.ui.lineEdit_clock.text()
        self.ui.textBrowser.append("아이디: " + id)
        self.ui.textBrowser.append("비밀번호: " + pw)
        self.ui.textBrowser.append("영화제목: " + name)
        self.ui.textBrowser.append("모드: " + mode)
        self.ui.textBrowser.append("도시: " + city)
        self.ui.textBrowser.append("상영관: " + hall)
        self.ui.textBrowser.append("날짜: " + date)
        self.ui.textBrowser.append("상영시간: " + clock)

    def message(self):
        msgbox = QMessageBox()
        msgbox.setIcon(QMessageBox.Information)
        msgbox.setWindowTitle("확인")
        msgbox.setText("검토를 완료하셨습니까? 오타는 오류를 생성합니다!")
        msgbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        ending = msgbox.exec_()

        if ending == QMessageBox.Ok:
            self.okButton_2Func()

    def okButton_2Func(self):
        global person, group
        group = self.ui.lineEdit_group.text()
        person = self.ui.lineEdit_person.text()
        rownum = self.ui.lineEdit_row.text()
        row.append(rownum)
        seat_1num = self.ui.lineEdit_seat_1.text()
        seat_1.append(seat_1num)
        seat_2num = self.ui.lineEdit_seat_2.text()
        seat_2.append(seat_2num)
        self.ui.textBrowser.append(group + ": " + person + "명")
        self.ui.textBrowser.append(rownum + seat_1num + " ~ " + rownum + seat_2num)

    def okButton_3Func(self):
        thread_class = ThreadClass(self)
        thread_class.start()

    def okButton_4Func(self):
        global delay
        delay = self.ui.lineEdit_delay.text()
        self.ui.textBrowser.append("일시정지 대기시간: " + delay + "초")

    def mousePressEvent(self, event):
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        x = event.globalX()
        y = event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x - x_w, y - y_w)


# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Splash_Screen()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>WELCOME</strong> TO MY APPLICATION")

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000,
                                 lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):
        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1

    def mousePressEvent(self, event):
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        x = event.globalX()
        y = event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x - x_w, y - y_w)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
