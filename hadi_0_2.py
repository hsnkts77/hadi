from extract_white import extract_white
from write_hadi_json import write_json
from PIL import ImageGrab
import numpy as np
import pytesseract
import pyperclip
import pyautogui
import g_search
import random
import time
import sys
import cv2
import os

pytesseract.pytesseract.tesseract_cmd = (r'C:\Program Files (x86)\Tesseract-OCR\tesseract')

def duplicate_tab():
    pyautogui.hotkey('alt','d')
    pyautogui.hotkey('alt','enter')

def check_answers_bool(lst):
    if bool(lst) == True:
        return True
    else:
        return False

def fix_junk_character(lst):
    fixed_list = []
    for i in lst:
        if '_' not in i:
            fixed_list.append(i)
    return fixed_list
def decrease_list(lst,number):
    while True:
        if len(lst) > number:
            lst.remove(min(lst))
        if len(lst) == number:
            break

def capture(area):
    img = ImageGrab.grab(bbox=area)
    new_img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    return new_img
def crop_question(img,area):
    crop_img = img[area[1]:area[3], area[0]:area[2]]
    return crop_img

def convert_to_text(img):
    text = pytesseract.image_to_string(img, lang = 'tur')
    return text
def seperate_q_a(text):
    question,answers = text.split('?',1)
    return question, answers
def character_edit(question):
    question = question.replace("\n'",' ').replace('“','"').replace('”','"').replace('  ',' ').replace('  ',' ').replace('  ',' ').replace('  ',' ').replace('  ',' ').replace('  ',' ').replace('  ',' ')
    return question
def edit_text(question,answers):
    question = question.lower()

    question = question.replace('.','').replace(',','').strip().replace('!','').replace("İ",'i')
    question = question.replace('aşağıdakilerden',' ').replace('degildir',' ').replace('değildir',' ').replace('yoktur','vardır')
    question = question.replace('bulunmamaktadır','').replace(' hangileridir','').replace(' hangisidir','').replace(' hangisinden','').replace(' hangisinin','')
    question = question.replace(' biri ',' ').replace(' hangisiydi',' ne').replace(' hangisini',' ne ').replace(' hangileri',' ').replace('hangisi ',' ne ').replace(' hangi','')

    answers = answers.lower()
    answers = answers.replace(',','').replace('/','\n').replace('—','\n').replace('%%','\n').replace('%','\n').replace(']','I').replace('[','I').split('\n')
    answers = list(map(str.strip, answers))
    answers = list(filter(bool, answers))

    for i in answers: #If there is only one character then delete it
        if len(i) == 1 and i.isdigit() == False:
            answers.remove(i)

    return question, answers

def auto_click_search_stuff(question,answers,answers_bool=True):
    first_p = pyautogui.position()
    pyautogui.click(471,429)

    pyperclip.copy(question)

    pyautogui.hotkey('ctrl','v')
    pyautogui.typewrite(['enter'])
    pyautogui.moveTo(first_p)

    time.sleep(0.5)

    pyautogui.hotkey('ctrl','f')

    if answers_bool == True:
        pyperclip.copy(answers[0])
        pyautogui.hotkey('ctrl','v')
        #pyautogui.typewrite(' ')

        time.sleep(0.6)
        pyperclip.copy(answers[1])
        duplicate_tab()

        time.sleep(0.5)
        pyautogui.hotkey('ctrl','f')
        pyautogui.hotkey('ctrl','v')
        #pyautogui.typewrite(' ')

        time.sleep(0.6)
        pyperclip.copy(answers[2])
        duplicate_tab()

        time.sleep(0.5)
        pyautogui.hotkey('ctrl','f')
        pyautogui.hotkey('ctrl','v')
        #pyautogui.typewrite(' ')

        #Return to first tab from 3 tabs
        # time.sleep(0.7)
        # pyautogui.hotkey('ctrl','shift','tab')
        # pyautogui.hotkey('ctrl','shift','tab')
