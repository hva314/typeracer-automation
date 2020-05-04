#!/usr/bin/env python3

from selenium import webdriver
from time import sleep

SPEED = 0.11 # second between requests

class Typer():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open(self):
        self.driver.get("https://play.typeracer.com/")

    def join(self):
        while True:
            try:
                link = self.driver.find_element_by_xpath('//*[@id="dUI"]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/a')
                link.click()
                break
            except Exception as e:
                print("[!] Waiting for site to load:", e)
                sleep(1)

        while True:
            try:

                text = self.driver.find_element_by_xpath('//*[@id="gwt-uid-15"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table').text
                print(text)
                break
            except Exception as e:
                print("[!] Waiting for game to load:", e)
                sleep(1)

        while True:
            try:
                textbox = self.driver.find_element_by_xpath('//*[@id="gwt-uid-15"]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input')
                print("[+] Located textbox")
                break
            except Exception as e:
                print("[!]", e)
                pass
            sleep(0.1)

        while True:
            try:
                status = self.driver.find_element_by_xpath('//*[@id="gwt-uid-15"]/table/tbody/tr[1]/td/table/tbody/tr[1]/td/table/tbody/tr/td[1]/div').text
                print("[!]", status)
                if "The race is on!" in status:
                    break
            except:
                pass
            sleep(0.2)

        for char in text:
            if (char == "\n") or (char == "\r"):
                break
            textbox.send_keys(char)
            print(char, end="", flush=True)
            sleep(SPEED)


racer = Typer()
racer.open()
racer.join()
