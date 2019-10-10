from gui import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import xlrd
import os
import datetime
import random
import sys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



file_queue = 0
stop_upload = False

class Start(QtCore.QThread):
	def __init__(self,parent=None):
		super(Start,self).__init__(parent)

	def run(self):
                try:
                        global stop_upload
                        global file_queue

                        self.current_dir = os.getcwd()

                        self.options = Options()
                        self.options.add_experimental_option("excludeSwitches",
                                                        ["ignore-certificate-errors",
                                                         "safebrowsing-disable-download-protection",
                                                         "safebrowsing-disable-auto-update",
                                                         "disable-client-side-phishing-detection"])
                        self.prefs = {"profile.default_content_setting_values.notifications" : 2}
                        self.options.add_experimental_option("prefs", self.prefs)


                        #self.options.add_argument("--headless")
                        self.options.add_argument("--disable-infobars")
                        self.options.add_argument("--disable-extensions")
                        self.options.add_argument("--incognito")
                        self.options.add_argument("--disable-plugins-discovery")

                        self.chromedriver_path ="chromedriver"
                        self.browser = webdriver.Chrome(self.chromedriver_path, chrome_options=self.options)

                        file_queue = 0
                        self.check = True
                        while stop_upload == False:

                                self.wb = xlrd.open_workbook("info.xlsx")
                                self.sheet = self.wb.sheet_by_index(0)

                                self.file_count = self.sheet.nrows
                                self.title = ""
                                while True:
                                                self.image_name = random.choice(os.listdir(self.current_dir + "\\image"))
                                                self.image_path =  self.current_dir + "\\image\\" + self.image_name

                                                for i in range(self.file_count):
                                                        if self.sheet.cell_value(i,0) == self.image_name.split(".")[0]:
                                                                self.title = self.sheet.cell_value(i,1)
                                                                self.url = self.sheet.cell_value(i,2)
                                                                self.description = self.sheet.cell_value(i,3)
                                                                if window.excel_board.isChecked():
                                                                        window.board_link.setText(self.sheet.cell_value(i,4))
                                                                break
                                                
                                                break
                                if self.title != "":
                                        if file_queue == 0:
                                                self.browser.get("https://www.pinterest.com/")
                                                time.sleep(5)

                                                if not window.google_account.isChecked():
                                                        try:
                                                                self.browser.find_element_by_xpath(
                                                                        "/html/body/div[1]/div/div/div/div/div/div[3]/div/div[1]/div/div/div[1]/div/div/div[1]/div[4]/div/div[3]/div/div/a").click()  # click on 'already have an account'
                                                        except:
                                                                self.browser.find_element_by_xpath(
                                                                        "/html/body/div[1]/div/div/div/div/div[3]/div/div[1]/div/div/div[1]/div/div/div[1]/div[4]/div/div[3]/div/div/a").click()
                                                                pass

                                                        time.sleep(10)

                                                        self.mail_box = self.browser.find_element_by_xpath(
                                                                "//*[@id='email']")
                                                        self.mail_box.send_keys(window.mail_address.text())

                                                        time.sleep(10)

                                                        self.password_box = self.browser.find_element_by_xpath(
                                                                "//*[@id='password']")
                                                        self.password_box.send_keys(window.password.text())

                                                        time.sleep(5)

                                                        try:
                                                                self.browser.find_element_by_xpath(
                                                                        "/html/body/div[1]/div/div/div/div/div/div[3]/div/div[1]/div/div/div[1]/div/div/div/div[3]/div[1]/form/div[4]/button/div").click()  # click on 'log in'
                                                        except:
                                                                try:
                                                                        self.browser.find_element_by_xpath(
                                                                                "/html/body/div[1]/div/div/div/div/div/div[3]/div/div[1]/div/div/div[1]/div/div/div/div[3]/div[1]/form/div[5]/button").click()
                                                                except:
                                                                        self.browser.find_element_by_xpath(
                                                                                "/html/body/div[1]/div/div/div/div/div[3]/div/div[1]/div/div/div[1]/div/div/div/div[3]/div[1]/form/div[5]/button").click()
                                                                        pass
                                                                pass

                                                else:
                                                        self.first_browser = self.browser.window_handles[0]
                                                        self.browser.find_element_by_xpath(
                                                                "//*[@id='googleConnectButton']/span").click()

                                                        time.sleep(5)

                                                        self.second_window = self.browser.window_handles[1]
                                                        self.browser.switch_to_window(self.second_window)

                                                        time.sleep(10)

                                                        self.mail_box = self.browser.find_element_by_xpath(
                                                                "//*[@id='identifierId']")
                                                        self.mail_box.send_keys(window.mail_address.text())

                                                        time.sleep(5)

                                                        self.browser.find_element_by_xpath(
                                                                "//*[@id='identifierNext']/span/span").click()

                                                        time.sleep(10)

                                                        self.password_box = self.browser.find_element_by_xpath(
                                                                "//*[@id='password']/div[1]/div/div[1]/input")
                                                        self.password_box.send_keys(window.password.text())

                                                        time.sleep(5)

                                                        self.browser.find_element_by_xpath(
                                                                "//*[@id='passwordNext']/span/span").click()

                                                        time.sleep(15)
                                                        self.browser.switch_to_window(self.first_browser)

                                        time.sleep(15)




                                        if window.board_option.isChecked() and self.check == True:
                                                newboard_name = window.new_board.text()
                                                if newboard_name != "":
                                                        try:
                                                                emp_link = self.browser.find_element_by_xpath('//*[@id="__PWS_ROOT__"]/div[1]/div[3]/div/div/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[1]/div/div[2]/a')
                                                        except:
                                                                emp_link = self.browser.find_element_by_xpath('//*[@id="__PWS_ROOT__"]/div[1]/div[3]/div/div/div/div[2]/div[1]/div/div/div[1]/div[1]/div/div/div/div[1]/div[1]/div/div[1]/div/div[2]/a')
                                                                pass
                                                        account_link = emp_link.get_attribute("href")
                                                        boardlink = account_link[:-5] + "boards"
                                                        self.browser.get(boardlink)
                                                        time.sleep(15)
                                                        self.check = False
                                                        try:
                                                                myElem = WebDriverWait(self.browser, 15).until(
                                                                        EC.presence_of_element_located((By.ID, 'HeaderContent')))
                                                                self.browser.find_element_by_xpath("/html/body/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]").click()
                                                                time.sleep(3)
                                                                self.browser.find_element_by_id("boardEditName").send_keys(newboard_name)
                                                                self.browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/div[2]/div/form/div[2]/div/div[2]/div/div[2]/button").click()
                                                                time.sleep(3)
                                                                self.board_link = self.browser.current_url
                                                        except:
                                                                pass
                                        elif self.check == True:
                                                self.board_link = window.board_link.text()

                                        self.browser.get(self.board_link)

                                        time.sleep(15)
                                        try:
                                                self.browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/div[3]/div/div/div/button").click()
                                        except:
                                                pass
                                        time.sleep(1)
                                        try:
                                                self.browser.find_element_by_xpath(
                                                        "//*[@id='__PWS_ROOT__']/div/div[1]/div/div[1]/div[2]/div[3]/div/div/div/div[1]/div/div/div/div[1]/div/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div/button/div/div").click()  # click on '+' button
                                        except:
                                                try:
                                                        self.browser.find_element_by_xpath(
                                                                "/html/body/div/div/div[1]/div/div[1]/div[2]/div[3]/div/div/div/div[1]/div/div/div/div[1]/div/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div/button/div/div/svg").click()
                                                except:
                                                        try:

                                                                self.browser.find_element_by_xpath(
                                                                        "/html/body/div/div[1]/div[3]/div/div/div/div[1]/div/div/div/div[1]/div/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div[1]/button/div/div").click()

                                                        except:
                                                                # self.browser.find_element_by_xpath("/html/body/div/div[2]/div[3]/div/div/div/div[1]/div/div/div/div[1]/div/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div/button/div/div").click()
                                                                self.browser.find_element_by_xpath(
                                                                        "/html/body/div/div/div[1]/div/div[1]/div[2]/div[3]/div/div/div/div[1]/div/div/div/div[1]/div/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div/button").click()
                                                                pass
                                                        pass
                                                pass

                                        time.sleep(5)

                                        try:
                                                self.browser.find_element_by_xpath(
                                                        "//*[@id='__PWS_ROOT__']/div/div[1]/div/div[1]/div[2]/div[3]/div/div/div/div[1]/div/div/div/div[1]/div/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div/div/div/div/div[1]").click()
                                        except:
                                                try:
                                                        self.browser.find_element_by_xpath(
                                                                "/html/body/div/div[1]/div[3]/div/div/div/div[1]/div/div/div/div[1]/div/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div/div/div/div/div[1]").click()

                                                except:
                                                        # self.browser.find_element_by_xpath("/html/body/div/div[2]/div[3]/div/div/div/div[1]/div/div/div/div[1]/div/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div/div/div/div/div[1]").click()
                                                        self.browser.find_element_by_xpath(
                                                                "/html/body/div/div/div[1]/div/div[1]/div[2]/div[3]/div/div/div/div[1]/div/div/div/div[1]/div/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div/div/div").click()
                                                        pass
                                                pass

                                        time.sleep(5)

                                        self.soup = BeautifulSoup(self.browser.page_source, "html.parser")
                                        self.browser.find_element_by_id("media-upload-input").send_keys(self.image_path)

                                        time.sleep(10)

                                        try:
                                                title_id = \
                                                (self.soup.find_all("textarea", {"placeholder": "Add your title"}))[
                                                        0].get("id")
                                                title = self.browser.find_element_by_id(title_id)
                                                title.send_keys(self.title)
                                        except:
                                                title_id = (self.soup.find_all("textarea",
                                                                               {"placeholder": "Başlığınızı ekleyin"}))[
                                                        0].get("id")
                                                self.browser.find_element_by_id(title_id).send_keys(self.title)
                                                pass

                                        time.sleep(5)

                                        try:
                                                pin_id = (self.soup.find_all("textarea", {
                                                        "placeholder": "Tell everyone what your Pin is about"}))[0].get(
                                                        "id")
                                                self.browser.find_element_by_id(pin_id).send_keys(self.description)
                                        except:
                                                pin_id = (self.soup.find_all("textarea", {
                                                        "placeholder": "Pininizin ne hakkında olduğunu herkese söyleyin"}))[
                                                        0].get("id")
                                                self.browser.find_element_by_id(pin_id).send_keys(self.description)
                                                pass

                                        time.sleep(5)

                                        try:
                                                dest_id = (self.soup.find_all("textarea", {
                                                        "placeholder": "Add a destination link"}))[0].get("id")
                                                self.browser.find_element_by_id(dest_id).send_keys(self.url)
                                        except:
                                                dest_id = (self.soup.find_all("textarea", {
                                                        "placeholder": "Bir hedef bağlantı ekleyin"}))[0].get("id")
                                                self.browser.find_element_by_id(dest_id).send_keys(self.url)
                                                pass

                                        time.sleep(5)

                                        try:
                                                # self.browser.find_element_by_xpath("//*[@id='__PWS_ROOT__']/div/div[1]/div/div[1]/div[2]/div[3]/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/button[2]/div").click()
                                                self.browser.find_element_by_xpath(
                                                        "/html/body/div/div[1]/div[3]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/button[2]").click()
                                        except:
                                                try:
                                                        self.browser.find_element_by_xpath(
                                                                "/html/body/div/div/div[1]/div/div[1]/div[2]/div[3]/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/button[2]").click()
                                                except:
                                                        self.browser.find_element_by_xpath(
                                                                "/html/body/div/div[2]/div[3]/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/button[2]").click()
                                                        pass
                                                pass

                                        print("k")
                                        time.sleep(10)
                                        print("skipped time")

                                        file_queue += 1

                                        os.remove(self.image_path)

                                        self.wb = xlrd.open_workbook("info.xlsx")
                                        self.sheet = self.wb.sheet_by_index(0)

                                        self.file_count = self.sheet.nrows

                                        print(self.file_count)
                                        print(file_queue)

                                        if self.file_count > file_queue:
                                                self.wait = random.randint(int(window.min_int.value()) * 60,
                                                                           int(window.max_int.value()) * 60)
                                                while stop_upload == False and self.wait >= 0:
                                                        window.time_remaining.setText(
                                                                str(datetime.timedelta(seconds=self.wait)))
                                                        time.sleep(1)
                                                        self.wait -= 1
                                                if stop_upload == True:
                                                        window.time_remaining.setText("Program stopped")
                                                        self.browser.quit()

                                        else:
                                                window.start_but.setEnabled(True)
                                                window.mail_address.setEnabled(True)
                                                window.password.setEnabled(True)
                                                window.show_browser.setEnabled(True)
                                                window.min_int.setEnabled(True)
                                                window.max_int.setEnabled(True)
                                                window.google_account.setEnabled(True)
                                                window.board_link.setEnabled(True)
                                                window.excel_board.setEnabled(True)
                                                window.new_board.setEnabled(True)
                                                window.board_option.setEnabled(True)
                                                window.time_remaining.setText(
                                                        "All images have been uploaded succesfully")
                                                return

                except:
                        self.browser.close()
                        pass
                        return

                finally:
                        self.browser.close()

class PinterestBot():
        def start_pressed(self):
                global file_queue
                global stop_upload
                
                stop_upload = False

                if window.min_int.value() > window.max_int.value():
                        QtWidgets.QMessageBox.about(window, "Error", "Min. interval cannot be bigger than max. interval!")
                        return

                if window.mail_address.text() == "" or window.password.text() == "" or (window.excel_board.isChecked() == False and window.board_link.text() == ""):
                        QtWidgets.QMessageBox.about(window, "Error", "Please insert your mail, password and board link")
                        return

                window.start_but.setEnabled(False)
                window.mail_address.setEnabled(False)
                window.password.setEnabled(False)
                window.show_browser.setEnabled(False)
                window.min_int.setEnabled(False)
                window.max_int.setEnabled(False)
                window.google_account.setEnabled(False)
                window.board_link.setEnabled(False)
                window.excel_board.setEnabled(False)
                window.new_board.setEnabled(False)
                window.board_option.setEnabled(False)
                self.start = Start()
                self.start.start()
                #self.start.run()

        def stop_pressed(self):
                global stop_upload
                stop_upload = True

                window.start_but.setEnabled(True)
                window.mail_address.setEnabled(True)
                window.password.setEnabled(True)
                window.show_browser.setEnabled(True)
                window.min_int.setEnabled(True)
                window.max_int.setEnabled(True)
                window.google_account.setEnabled(True)
                window.board_link.setEnabled(True)
                window.excel_board.setEnabled(True)
                window.new_board.setEnabled(True)
                window.board_option.setEnabled(True)
                window.time_remaining.setText("Time Remaining")

app = QtWidgets.QApplication(sys.argv)
window = Ui_Form()
window.show()

pinterestbot = PinterestBot()

window.start_but.clicked.connect(pinterestbot.start_pressed)
window.stop_but.clicked.connect(pinterestbot.stop_pressed)

sys.exit(app.exec_())
