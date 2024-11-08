import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import pyperclip3
import random
from email.message import  EmailMessage
import googletrans
import ssl
import smtplib
import pywhatkit as kit 
import webbrowser
import sys 
import requests
from random import randrange
import random 
import pyautogui
from ctypes import cast,POINTER
from comtypes import CLSCTX_ALL
from webbrowser import open
import pyautogui as pg
from tkinter import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import os
from playsound import playsound

gt=googletrans.Translator()
 


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# to give the voice code pipiprint(voices[1].id)
engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    #It takes microphone input  
    global iserror, query   
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        iserror = False
        

    except Exception as e:

        phases=["Say that again please","I didn't hear that","Oops, i missed that","Say loudly","Try again"]
        ranphase=random.choice(phases)
        print(ranphase)
        speak(ranphase)
        # it shows error print(e)
        #print("Say that again please")
        #speak("Say that again please")
        iserror = True
    
    return query.lower(), iserror



def emailtoenvironment():
    email_sender='fridaycare2511@gmail.com'
    email_password= 'xqdbowxjegzqryol'
    email_receiver='daera.helpline@daera-ni.gov.uk'
    speak("Tell me the subject")
    subject=takecommand()
    print("Subject of the email:- ",subject[0])
    speak("Tell me the body of the email.")
    body=takecommand()
    print("Body of the email:- ",body[0])
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject[0]
    em.set_content(body[0])

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())

    print("Email Sent.")
    speak("Email Sent.")

def emailtobanking():
    email_sender='fridaycare2511@gmail.com'
    email_password= 'xqdbowxjegzqryol'
    email_receiver='missionfi@nic.in'
    speak("Tell me the subject")
    subject=takecommand()
    print("Subject of the email:- ",subject[0])
    speak("Tell me the body of the email.")
    body=takecommand()
    print("Body of the email:- ",body[0])
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject[0]
    em.set_content(body[0])

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())

    print("Email Sent.")
    speak("Email Sent.")

def emailtobusiness():
    email_sender='fridaycare2511@gmail.com'
    email_password= 'xqdbowxjegzqryol'
    email_receiver='contactmsde@gov.in'
    speak("Tell me the subject")
    subject=takecommand()
    print("Subject of the email:- ",subject[0])
    speak("Tell me the body of the email.")
    body=takecommand()
    print("Body of the email:- ",body[0])
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject[0]
    em.set_content(body[0])

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())

    print("Email Sent.")
    speak("Email Sent.")

def emailtoeducation():
    email_sender='fridaycare2511@gmail.com'
    email_password= 'xqdbowxjegzqryol'
    email_receiver='minister.sm@gov.in'
    speak("Tell me the subject")
    subject=takecommand()
    print("Subject of the email:- ",subject[0])
    speak("Tell me the body of the email.")
    body=takecommand()
    print("Body of the email:- ",body[0])
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject[0]
    em.set_content(body[0])

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())

    print("Email Sent.")
    speak("Email Sent.")

def emailtohealth():
    email_sender='fridaycare2511@gmail.com'
    email_password= 'xqdbowxjegzqryol'
    email_receiver='hfm@gov.in'
    speak("Tell me the subject")
    subject=takecommand()
    print("Subject of the email:- ",subject[0])
    speak("Tell me the body of the email.")
    body=takecommand()
    print("Body of the email:- ",body[0])
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject[0]
    em.set_content(body[0])

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())

    print("Email Sent.")
    speak("Email Sent.")

def emailtohousing():
    email_sender='fridaycare2511@gmail.com'
    email_password= 'xqdbowxjegzqryol'
    email_receiver='@hudco.org'
    speak("Tell me the subject")
    subject=takecommand()
    print("Subject of the email:- ",subject[0])
    speak("Tell me the body of the email.")
    body=takecommand()
    print("Body of the email:- ",body[0])
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject[0]
    em.set_content(body[0])

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())

    print("Email Sent.")
    speak("Email Sent.")

def emailtosafety():
    email_sender='fridaycare2511@gmail.com'
    email_password= 'xqdbowxjegzqryol'
    email_receiver='slaw@nic.in'
    speak("Tell me the subject")
    subject=takecommand()
    print("Subject of the email:- ",subject[0])
    speak("Tell me the body of the email.")
    body=takecommand()
    print("Body of the email:- ",body[0])
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject[0]
    em.set_content(body[0])

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())

    print("Email Sent.")
    speak("Email Sent.")

def emailtoscience():
    email_sender='fridaycare2511@gmail.com'
    email_password= 'xqdbowxjegzqryol'
    email_receiver='contactmsde@gov.in'
    speak("Tell me the subject")
    subject=takecommand()
    print("Subject of the email:- ",subject[0])
    speak("Tell me the body of the email.")
    body=takecommand()
    print("Body of the email:- ",body[0])
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject[0]
    em.set_content(body[0])

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())

    print("Email Sent.")
    speak("Email Sent.")

def emailtoskills():
    email_sender='fridaycare2511@gmail.com'
    email_password= 'xqdbowxjegzqryol'
    email_receiver='Contactmsde@gov.in'
    speak("Tell me the subject")
    subject=takecommand()
    print("Subject of the email:- ",subject[0])
    speak("Tell me the body of the email.")
    body=takecommand()
    print("Body of the email:- ",body[0])
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject[0]
    em.set_content(body[0])

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())

    print("Email Sent.")
    speak("Email Sent.")

def emailtosocialwelfare():
    email_sender='fridaycare2511@gmail.com'
    email_password= 'xqdbowxjegzqryol'
    email_receiver='sje@hry.nic.in'
    speak("Tell me the subject")
    subject=takecommand()
    print("Subject of the email:- ",subject[0])
    speak("Tell me the body of the email.")
    body=takecommand()
    print("Body of the email:- ",body[0])
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject[0]
    em.set_content(body[0])

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())

    print("Email Sent.")
    speak("Email Sent.")

def emailtosports():
    email_sender='fridaycare2511@gmail.com'
    email_password= 'xqdbowxjegzqryol'
    email_receiver='complaint.sewakendra@gmail.com'
    speak("Tell me the subject")
    subject=takecommand()
    print("Subject of the email:- ",subject[0])
    speak("Tell me the body of the email.")
    body=takecommand()
    print("Body of the email:- ",body[0])
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject[0]
    em.set_content(body[0])

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())

    print("Email Sent.")
    speak("Email Sent.")

def emailtotransport():
    email_sender='fridaycare2511@gmail.com'
    email_password= 'xqdbowxjegzqryol'
    email_receiver='transportMinistry@dot.gov.za'
    speak("Tell me the subject")
    subject=takecommand()
    print("Subject of the email:- ",subject[0])
    speak("Tell me the body of the email.")
    body=takecommand()
    print("Body of the email:- ",body[0])
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject[0]
    em.set_content(body[0])

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())

    print("Email Sent.")
    speak("Email Sent.")

def emailtotravel():
    email_sender='fridaycare2511@gmail.com'
    email_password= 'xqdbowxjegzqryol'
    email_receiver='as.tourism@gov.in'
    speak("Tell me the subject")
    subject=takecommand()
    print("Subject of the email:- ",subject[0])
    speak("Tell me the body of the email.")
    body=takecommand()
    print("Body of the email:- ",body[0])
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject[0]
    em.set_content(body[0])

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())

    print("Email Sent.")
    speak("Email Sent.")

def emailtoutility():
    email_sender='fridaycare2511@gmail.com'
    email_password= 'xqdbowxjegzqryol'
    email_receiver='minister-mowr@nic.in'
    speak("Tell me the subject")
    subject=takecommand()
    print("Subject of the email:- ",subject[0])
    speak("Tell me the body of the email.")
    body=takecommand()
    print("Body of the email:- ",body[0])
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject[0]
    em.set_content(body[0])

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())

    print("Email Sent.")
    speak("Email Sent.")


def emailtoparyavaran():
    email_sender='fridaycare2511@gmail.com'
    email_password= 'xqdbowxjegzqryol'
    email_receiver='daera.helpline@daera-ni.gov.uk'
    playsound('subject.mp3')
    subject=takecommand()
    print("Subject of the email:- ",subject[0])
    playsound('body.mp3')
    body=takecommand()
    print("Body of the email:- ",body[0])
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject[0]
    em.set_content(body[0])

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())

    print("Email Sent.")
    playsound('email sent.mp3')

def emailtobhima():
    email_sender='fridaycare2511@gmail.com'
    email_password= 'xqdbowxjegzqryol'
    email_receiver='missionfi@nic.in'
    playsound('subject.mp3')
    subject=takecommand()
    print("Subject of the email:- ",subject[0])
    playsound('body.mp3')
    body=takecommand()
    print("Body of the email:- ",body[0])
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject[0]
    em.set_content(body[0])

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())

    print("Email Sent.")
    playsound('email sent.mp3')

def emailtovyapar():
    email_sender='fridaycare2511@gmail.com'
    email_password= 'xqdbowxjegzqryol'
    email_receiver='contactmsde@gov.in'
    playsound('subject.mp3')
    subject=takecommand()
    print("Subject of the email:- ",subject[0])
    playsound('body.mp3')
    body=takecommand()
    print("Body of the email:- ",body[0])
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject[0]
    em.set_content(body[0])

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())

    print("Email Sent.")
    playsound('email sent.mp3')

def emailtoshikshan():
    email_sender='fridaycare2511@gmail.com'
    email_password= 'xqdbowxjegzqryol'
    email_receiver='minister.sm@gov.in'
    playsound('subject.mp3')
    subject=takecommand()
    print("Subject of the email:- ",subject[0])
    playsound('body.mp3')
    body=takecommand()
    print("Body of the email:- ",body[0])
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject[0]
    em.set_content(body[0])

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())

    print("Email Sent.")
    playsound('email sent.mp3')

def emailtoswasthya():
    email_sender='fridaycare2511@gmail.com'
    email_password= 'xqdbowxjegzqryol'
    email_receiver='hfm@gov.in'
    playsound('subject.mp3')
    subject=takecommand()
    print("Subject of the email:- ",subject[0])
    playsound('body.mp3')
    body=takecommand()
    print("Body of the email:- ",body[0])
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject[0]
    em.set_content(body[0])

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())

    print("Email Sent.")
    playsound('email sent.mp3')

def emailtoaawas():
    email_sender='fridaycare2511@gmail.com'
    email_password= 'xqdbowxjegzqryol'
    email_receiver='@hudco.org'
    playsound('subject.mp3')
    subject=takecommand()
    print("Subject of the email:- ",subject[0])
    playsound('body.mp3')
    body=takecommand()
    print("Body of the email:- ",body[0])
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject[0]
    em.set_content(body[0])

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())

    print("Email Sent.")
    playsound('email sent.mp3')

def emailtosuraksha():
    email_sender='fridaycare2511@gmail.com'
    email_password= 'xqdbowxjegzqryol'
    email_receiver='slaw@nic.in'
    playsound('subject.mp3')
    subject=takecommand()
    print("Subject of the email:- ",subject[0])
    playsound('body.mp3')
    body=takecommand()
    print("Body of the email:- ",body[0])
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject[0]
    em.set_content(body[0])

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())

    print("Email Sent.")
    playsound('email sent.mp3')

def emailtovigyan():
    email_sender='fridaycare2511@gmail.com'
    email_password= 'xqdbowxjegzqryol'
    email_receiver='contactmsde@gov.in'
    playsound('subject.mp3')
    subject=takecommand()
    print("Subject of the email:- ",subject[0])
    playsound('body.mp3')
    body=takecommand()
    print("Body of the email:- ",body[0])
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject[0]
    em.set_content(body[0])

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())

    print("Email Sent.")
    playsound('email sent.mp3')

def emailtokaushal():
    email_sender='fridaycare2511@gmail.com'
    email_password= 'xqdbowxjegzqryol'
    email_receiver='Contactmsde@gov.in'
    playsound('subject.mp3')
    subject=takecommand()
    print("Subject of the email:- ",subject[0])
    playsound('body.mp3')
    body=takecommand()
    print("Body of the email:- ",body[0])
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject[0]
    em.set_content(body[0])

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())

    print("Email Sent.")
    playsound('email sent.mp3')

def emailtosamajikkalyan():
    email_sender='fridaycare2511@gmail.com'
    email_password= 'xqdbowxjegzqryol'
    email_receiver='sje@hry.nic.in'
    playsound('subject.mp3')
    subject=takecommand()
    print("Subject of the email:- ",subject[0])
    playsound('body.mp3')
    body=takecommand()
    print("Body of the email:- ",body[0])
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject[0]
    em.set_content(body[0])

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())

    print("Email Sent.")
    playsound('email sent.mp3')

def emailtokhel():
    email_sender='fridaycare2511@gmail.com'
    email_password= 'xqdbowxjegzqryol'
    email_receiver='complaint.sewakendra@gmail.com'
    playsound('subject.mp3')
    subject=takecommand()
    print("Subject of the email:- ",subject[0])
    playsound('body.mp3')
    body=takecommand()
    print("Body of the email:- ",body[0])
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject[0]
    em.set_content(body[0])

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())

    print("Email Sent.")
    playsound('email sent.mp3')

def emailtobnavat():
    email_sender='fridaycare2511@gmail.com'
    email_password= 'xqdbowxjegzqryol'
    email_receiver='transportMinistry@dot.gov.za'
    playsound('subject.mp3')
    subject=takecommand()
    print("Subject of the email:- ",subject[0])
    playsound('body.mp3')
    body=takecommand()
    print("Body of the email:- ",body[0])
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject[0]
    em.set_content(body[0])

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())

    print("Email Sent.")
    playsound('email sent.mp3')

def emailtoyatra():
    email_sender='fridaycare2511@gmail.com'
    email_password= 'xqdbowxjegzqryol'
    email_receiver='as.tourism@gov.in'
    playsound('subject.mp3')
    subject=takecommand()
    print("Subject of the email:- ",subject[0])
    playsound('body.mp3')
    body=takecommand()
    print("Body of the email:- ",body[0])
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject[0]
    em.set_content(body[0])

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())

    print("Email Sent.")
    playsound('email sent.mp3')

def emailtoupyogita():
    email_sender='fridaycare2511@gmail.com'
    email_password= 'xqdbowxjegzqryol'
    email_receiver='minister-mowr@nic.in'
    playsound('subject.mp3')
    subject=takecommand()
    print("Subject of the email:- ",subject[0])
    playsound('body.mp3')
    body=takecommand()
    print("Body of the email:- ",body[0])
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject[0]
    em.set_content(body[0])

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())

    print("Email Sent.")
    playsound('email sent.mp3')
    
