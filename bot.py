from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import pyautogui
from tkinter import *

class Instagram:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome()
        self.wait = WebDriverWait(self.bot, 20)

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(1)
        email = bot.find_element_by_name("username")
        password = bot.find_element_by_name("password")
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(2)

    def like(self, entry3, entry4):
        bot = self.bot
        n = int(str(entry4))
        bot.get('https://www.instagram.com/explore/tags/' + str(entry3))
        time.sleep(0.5)
        bot.find_element_by_xpath("//*[@id='react-root']").click()
        time.sleep(0.5)
        for i in range(n):
            likes = bot.find_element_by_xpath("//*[@aria-label='Like']")
            time.sleep(0.2)
            likes.click()
            time.sleep(0.2)
            bot.find_element_by_link_text('Next').click()
            time.sleep(0.2)

    def follow(self):
        bot = self.bot
        time.sleep(3)
        for j in range(21):
            follow_button = bot.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button')
            time.sleep(0.5)
            follow_button.click()
            bot.find_element_by_link_text('Next').click()
            time.sleep(0.5)

# Main execution function
def execute():
    log = Instagram(str(entry1.get()), str(entry2.get()))
    log.login()
    log.like(entry3.get(), entry4.get())
    log.follow()

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

likes = Label(window, text="How many likes do you want to automate?", font='times 24 bold')
likes.grid(row=5, column=0)
entry4 = Entry(window)
entry4.grid(row=5, column=6)


b1 = Button(window, text=" GO ", command=execute, width=12, bg='gray')
b1.grid(row=10, column=5)

exitbutton = Button(window, text="Exit", command=window.destroy, width=12, bg='gray')
exitbutton.grid(row=30, column=5)

window.mainloop()
