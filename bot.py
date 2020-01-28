from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from tkinter import *

class Instagram:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome()

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(1)
        email = bot.find_element_by_name("username")
        password = bot.find_element_by_name("password")
        email.clear()
        password.clear()
        email.send_keys('3234717654')
        password.send_keys('Sujely97')
        password.send_keys(Keys.RETURN)
        time.sleep(2)

    def follow(self, entry3):
        bot = self.bot
        bot.get('https://www.instagram.com/explore/tags/' + str(entry3))
        pyautogui.moveTo(2000, None, 1)
        time.sleep(0.5)
        for i in range(1, 6):
            for j in range(1, 15):
                pyautogui.click(pyautogui.locateCenterOnScreen('experiment.png'), duration=1)
                time.sleep(0.5)
                pyautogui.moveTo(2000, None, 1)
                time.sleep(0.5)
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(0.2)

def execute():
    log = Instagram(str(entry1.get()), str(entry2.get()))
    log.login()
    log.follow(entry3.get())

# dtinker gui
window = Tk()

window.attributes("-fullscreen", True)
emails = Label(window, text="enter your email here", font='times 24 bold')
emails.grid(row=0, column=0)
entry1 = Entry(window)
entry1.grid(row=0, column=6)

password = Label(window, text="enter your password here", font='times 24 bold')
password.grid(row=2, column=0)
entry2 = Entry(window)
entry2.grid(row=2, column=6)

hashtag = Label(window, text="enter your hashtag here", font='times 24 bold')
hashtag.grid(row=3, column=0)
entry3 = Entry(window)
entry3.grid(row=3, column=6)

b1 = Button(window, text=" GO ", command=execute, width=12, bg='gray')
b1.grid(row=10, column=5)

exitbutton = Button(window, text="Exit", command=window.destroy, width=12, bg='gray')
exitbutton.grid(row=30, column=5)

window.mainloop()
