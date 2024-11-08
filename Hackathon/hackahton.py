import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os                                                       
import pyperclip3
import random
import requests
from random import randrange
import pyautogui
from webbrowser import open
import pyautogui as pg
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# to give the voice code pipiprint(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    #It takes microphone input        
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        #speak(query)

    except Exception as e:


        phases=["Say that again please","I didn't hear that","Oops, i missed that","Say loudly","Try again"]
        ranphase=random.choice(phases)
        print(ranphase)
        speak(ranphase)
        # it shows error print(e)
        #print("Say that again please")
        #speak("Say that again please")
        return "None"
    return query 

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning.") 

    elif hour>=12 and hour<18:
        speak("Good Afternoon.")

    else:
        speak("Good Evening.")

    speak("Namastayy! I am Friday ,how may i help you today")



#email Sender

def emailtoharsh():
    email_sender='fridaycare2511@gmail.com'
    email_password= 'xqdbowxjegzqryol'
    email_receiver='harshvermajpr1@gmail.com'
    speak("Tell me the subject")
    subject=takecommand()
    print("Subject of the email:- ",subject)
    speak("Tell me the body of the email.")
    body=takecommand()
    print("Body of the email:- ",body)
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject
    em.set_content(body)

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())

    print("Email Sent.")
    speak("Email Sent.")


def emailtokhushi():
    email_sender='fridaycare2511@gmail.com'
    email_password= 'xqdbowxjegzqryol'
    email_receiver='ratrakr@gmail.com'
    speak("Tell me the subject")
    subject=takecommand()
    print("Subject of the email:- ",subject)
    speak("Tell me the body of the email.")
    body=takecommand()
    print("Body of the email:- ",body)
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject
    em.set_content(body)

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())

    print("Email Sent.")
    speak("Email Sent.")

def emailtopriya():
    email_sender='fridaycare2511@gmail.com'
    email_password= 'xqdbowxjegzqryol'
    email_receiver='khushichoudhary120504@gmail.com'
    speak("Tell me the subject")
    subject=takecommand()
    print("Subject of the email:- ",subject)
    speak("Tell me the body of the email.")
    body=takecommand()
    print("Body of the email:- ",body)
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject
    em.set_content(body)

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())

    print("Email Sent.")
    speak("Email Sent.") 

def emailtolakshika():
    email_sender='fridaycare2511@gmail.com'
    email_password= 'xqdbowxjegzqryol'
    email_receiver='lakshika4sharma@gmail.com'
    speak("Tell me the subject")
    subject=takecommand()
    print("Subject of the email:- ",subject)
    speak("Tell me the body of the email.")
    body=takecommand()
    print("Body of the email:- ",body)
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject
    em.set_content(body)

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())

    print("Email Sent.")
    speak("Email Sent.")


#Play games

#1. play snake game 
def snakegame(): 
    food = vector(0, 0)
    snake = [vector(10, 0)]
    aim = vector(0, -10)


    def change(x, y):
        """Change snake direction."""
        aim.x = x
        aim.y = y


    def inside(head):
        """Return True if head inside boundaries."""
        return -200 < head.x < 190 and -200 < head.y < 190


    def move():
        """Move snake forward one segment."""
        head = snake[-1].copy()
        head.move(aim)

        if not inside(head) or head in snake:
            square(head.x, head.y, 9, 'red')
            update()
            return

        snake.append(head)

        if head == food:
            print('Snake:', len(snake))
            food.x = randrange(-15, 15) * 10
            food.y = randrange(-15, 15) * 10
        else:
            snake.pop(0)

        clear()

        for body in snake:
            square(body.x, body.y, 9, 'black')

        square(food.x, food.y, 9, 'green')
        update()
        ontimer(move, 100)


    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    listen()
    onkey(lambda: change(10, 0), 'Right')
    onkey(lambda: change(-10, 0), 'Left')
    onkey(lambda: change(0, 10), 'Up')
    onkey(lambda: change(0, -10), 'Down')
    move()
    done()


#Web Scrapping
def bigbasket(query):
    query=query.split(" ")[0]
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver=webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.bigbasket.com/?nc=logo")
    sleep(4)
    search=driver.find_element("xpath","/html/body/div[1]/div[1]/div[9]/div/div[3]/div/input")
    search.send_keys(query)

    Submit=driver.find_element("xpath","/html/body/div[1]/div[1]/div[9]/div/div[3]/div/div/button")
    Submit.click()
    speak("Searching{}".format(query))
    speak("Here are the results.")

#Web Scrapping

def bookmyshow(query):
    query=query.replace("bookmyshow","")
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver=webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://in.bookmyshow.com/")
    sleep(4)
    speak("Tell me the city.")
    city=takecommand()
    pg.typewrite("{}\n".format(city),0.2)
    
    sleep(2)

    moviesearchclick=driver.find_element("xpath","/html/body/div[1]/div[1]/div[2]/header/div[1]/div/div/div/div[1]/div[2]/div/span[2]")
    moviesearchclick.click()
    pg.typewrite("{}\n".format(query),0.2)


#open pc apps

def openpcapps(query):
    query=query.replace("open pc app","")
    pg.hotkey("winleft")
    pg.typewrite("{}\n".format(query),0.2)
    print("Mission Accomplished")



#Write a word file.
def wordfile():
    document=Document()
    print("Tell me the Heading.")
    speak("Tell me the Heading.")
                    
    head=takecommand()
    document.add_heading(head, 0)
    print("Tell me the Body.")
    speak("Tell me the Body.")
                    
    body=takecommand()
    document.add_paragraph(body).bold= True
    document.save("C:/Users/Harsh Verma/Desktop/Friday/Notepad file accessing/Document.docx")
    speak("done writing word file")

#Random password generator
def genpass():
    uppercase_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters=uppercase_letters.lower()
    digits="1234567890"
    upper,lower,nums=True,True,True 
    al=""
    if upper:
        al+=uppercase_letters

    if lower:
        al+=lowercase_letters

    if digits:
        al+=digits

    length=8
    amount=1

    for x in range(amount):
        password="".join(random.sample(al,length))
        
        print("Password Generated: {}".format(password))
        speak("Password Generated.")
        print("")

def screeninshot():
    screenshot=pyautogui.screenshot()
    uppercase_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters=uppercase_letters.lower()
    digits="1234567890"
    upper,lower,nums=True,True,True 
    al=""
    if upper:
        al+=uppercase_letters

    if lower:
        al+=lowercase_letters

    if digits:
        al+=digits

    length=8
    amount=1

    for x in range(amount):
        password="".join(random.sample(al,length))
        a=".png"
        new=(password+a)
        print("Image name: {}".format(new))
        screenshot.save("C://Users//Harsh Verma//Desktop//Friday//Notepad file accessing//{}".format(new)) 
        speak("Screenshot Taken.")
        print("Screenshot Taken.")   

#Voice Recorder
def voicerecorder():
    print("Recording start.")
    speak("Recording start.")
    
    audio=pyaudio.PyAudio()
    stream=audio.open(format=pyaudio.paInt16,channels=1,rate=44100,input=True,frames_per_buffer=1024)
    frames=[]
    try:
        while True:
            data=stream.read(1024)
            frames.append(data)

    except KeyboardInterrupt:
        pass

    stream.stop_stream()
    stream.close()
    audio.terminate()
    sound_file=wave.open("C://Users//Harsh Verma//Desktop//Friday//Notepad file accessing//recordedaudio.wav","wb")
    sound_file.setnchannels(1)
    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(44100)
    sound_file.writeframes(b''.join(frames))
    sound_file.close()
    print("Voice Recorded.")
    speak("Voice Recorded.")

def volsetup():
    devices=AudioUtilities.GetSpeakers()    
    interface=devices.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL, None)
    volume=cast(interface,POINTER(IAudioEndpointVolume))
    if ' 0%' in query:
        volume.SetMasterVolumeLevel(-65.0, None)
        speak("Volume Level Changed to Zero.")
    elif ' 100%' in query:
        volume.SetMasterVolumeLevel(0.0, None)
        speak("Volume Level Changed to Full.")
    elif ' 50%' in query:
        volume.SetMasterVolumeLevel(-10.0, None)
        speak("Volume Level Changed to Half.")

    elif ' 30%' in query:
        volume.SetMasterVolumeLevel(-18.0, None)
        speak("Volume Level Changed to 30 Percent.")

    elif ' 70%' in query:
        volume.SetMasterVolumeLevel(-5.0, None)
        speak("Volume Level Changed to 70 Percent.")


#Emergency Calls and help.
def emergency():
    y=''
    while(y==''):
        devices=AudioUtilities.GetSpeakers()    
        interface=devices.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL, None)
        volume=cast(interface,POINTER(IAudioEndpointVolume))
        volume.SetMasterVolumeLevel(0.0, None)
        print("Emergency Mode On.")
        speak("Emergency Mode On.")
        

        #alert sound
        def alertsound():
            music_dir = "C:\\Users\\Harsh Verma\\Desktop\\Friday\\Popular Emergency Alarm Clock  Danger Alarm  Sound Effect.mp3"
            os.startfile(os.path.join(music_dir))
        
        alertsound()

        
        options=webdriver.ChromeOptions()
        options.add_experimental_option("detach",True)
        driver=webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.gps-coordinates.net/my-location")
        sleep(8)

        lat=driver.find_element("xpath","/html/body/div[2]/div[2]/div[2]/div[1]/p/span[1]")
        lon=driver.find_element("xpath","/html/body/div[2]/div[2]/div[2]/div[1]/p/span[2]")
        sleep(5)
    
        newlat=str(lat.text)
        newlon=str(lon.text)

        newlat=newlat.split(" ")[0]
        newlon=newlon.split(" ")[0]

        coordinates=(newlat+","+newlon)
        
        print(coordinates)

        ########
        driver.get("https://www.google.com/maps/@26.8561162,75.7695622,16z")
        sleep(5)
        place=driver.find_element("xpath","/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div/div[2]/form/input[1]")


        place.send_keys(coordinates)
        Submit=driver.find_element("xpath","/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
        Submit.click()
        sleep(4)
        sharebutton=driver.find_element("xpath","/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[5]/button/span/img")
        sharebutton.click()
        sleep(4)
        clickbutton=driver.find_element("xpath","/html/body/div[3]/div[1]/div/div[2]/div/div[3]/div/div/div[1]/div[4]/div[2]/button")
        clickbutton.click()
        a=str(pyperclip3.paste())

        alertsound()
        

        try:
            
            content='Help I Need Help as soon as possible. My Current Location is {}'.format(a)
            hour = int(datetime.datetime.now().hour)
            minute = int(datetime.datetime.now().minute)
            phone='+91 63679 82717'
            kit.sendwhatmsg_instantly(phone, content , hour , minute)
            print("Message Sent sir.")
            speak("message Sent sir.")   

        except Exception as e:
            print(e)  
            speak("Sorry sir . i can't do that right now")
        
        alertsound()
        
        #email              
        email_sender='fridaycare2511@gmail.com'
        email_password= 'xqdbowxjegzqryol'
        email_receiver='harshvermajpr1@gmail.com'
        subject=("Urgent Help Needed. ")
        print("Subject of the email:- ",subject)
        body='Help I Need Help as soon as possible. My Current Location is {}'.format(a)
        print("Body of the email:- ",body)
        em=EmailMessage()
        em['From']=email_sender
        em['To']=email_receiver
        em['Subject']=subject
        em.set_content(body)

        context=ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login(email_sender,email_password)
            smtp.sendmail(email_sender,email_receiver,em.as_string())

        print("Email Sent For your help.")
        speak("Email Sent For your help.")

        y=takecommand()
        if y=='stop':
            speak("Emergency Mode Turned Off.")
            continue
        else:
            y=''


# Spell by characters
def speakByLetter(query):
    query = query.replace("spell","")
    for c in query:
        speak(c)


#it will tell the internet speed
def currentinternetspeed():
    webbrowser.open("https://fast.com")
    sleep(10)
    speak("This is Your Current Internet Speed.")


#it will tell you the current location.
def currentlocation():
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver=webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.gps-coordinates.net/my-location")
    sleep(6)

    lat=driver.find_element("xpath","/html/body/div[2]/div[2]/div[2]/div[1]/p/span[1]")
    lon=driver.find_element("xpath","/html/body/div[2]/div[2]/div[2]/div[1]/p/span[2]")

    newlat=str(lat.text)
    newlon=str(lon.text)

    newlat=newlat.split(" ")[0]
    newlon=newlon.split(" ")[0]

    coordinates=(newlat+" , "+newlon)
        
    print(coordinates)

    ########
    driver.get("https://www.google.com/maps/@26.8561162,75.7695622,16z")
    
    place=driver.find_element("xpath","/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div/div[2]/form/input[1]")
    place.send_keys(coordinates)
    Submit=driver.find_element("xpath","/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
    Submit.click()
    speak("Found you.")


#it will set the brightness level of main screen.
def setbrightnesslevel(query):
    query=query.replace("set brightness level","")
    query=query.replace("%","")
    sbc.set_brightness('{}'.format(query))
    print("Brightness Level Changed to{}%".format(query))
    speak("Brightness Level Changed to{}%".format(query))


#it will tell the arial distance between 2 places.
def arialdiatance():

    locOne = query.split(' ')[-1]
    locTwo = query.split(' ')[-3]

    loc = Nominatim(user_agent="GetLoc")

    getLoc1 = loc.geocode(locOne)
    lat1=getLoc1.latitude
    long1=getLoc1.longitude

    getLoc2 = loc.geocode(locTwo)
    lat2=getLoc2.latitude
    long2=getLoc2.longitude

    
    coordinate1=(lat1,long1)
    coordinate2=(lat2,long2)

    totaldistance=distance.distance(coordinate1,coordinate2)
    
    
    disspeak=f"The Arial Distance Between {locTwo} and {locOne} is approx {totaldistance}"
    print(disspeak)
    speak(disspeak)

# This function adds two numbers


def calc(query):

    op = query.split(' ')[1]
    num1 = int(query.split(' ')[-3])
    num2 = int(query.split(' ')[-1])

    if "add" in query:
        return (num1+num2)
    if "subtract" in query:
        return (num1-num2)
    if "multiply" in query:
        return (num1*num2)
    if "divide" in query:
        return (num1/num2)
    else :
        print(f"{op} is not valid operator")
        return f"{op} is not valid operator"


        
def gmaps(query):
    query=query.replace("search","")
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver=webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.google.com/maps/@26.8561162,75.7695622,16z")

    sleep(2)
    
    place=driver.find_element("xpath","/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/form/div[2]/div[3]/div/input[1]")
    place.send_keys(query)
    Submit=driver.find_element("xpath","/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
    Submit.click()

    speak("Here are the results.")


mainmenu()
#Main Program
if __name__ == "__main__":
    wishme()
    while True:
#if 1:
        query = takecommand().lower()
#logical things
        if 'introduce yourself' in query:
            speak('Hey. i am friday.  i am basically an assistant , who can do some amazing things , like i can play music if you want , i can send emails , i can open folders you want , and many more .  you wanna try something ? ')
        
        elif 'sing' in query:
            str=speak('By the way im not too good at singing but i can try...')
            song=('Tumko paaya hai to jaise khoya hoon kehna chahoon bhi to tumse kya kahoo kisi zabaan mein bhivo lavz hi nahi ki jinme tum ho kya tumhe bata sakoon main agar kahoon tumsa haseen')
            song1=('If you wanna run away with me, I know a galaxy And I can take you for a ride......... I had a premonition that we fell into a rhythm Where the music dont stop for life....... Glitter in the sky.... glitter in my eyes..... Shining just the way I like. If youre feeling like you need a little bit of company You met me at the perfect time')
            speak(song1)
            speak("I can sing very well..right?")


        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
#WEB BASED FUNCTIONS.    
        elif 'open youtube' in query:
            speak("Opening Youtube...")
            webbrowser.open("https://www.youtube.com/")

        elif 'poornima university website' in query:
            speak("Opening Poornima University Website.")
            webbrowser.open("https://www.poornima.edu.in/")

        elif 'open google.com' in query:
            speak("Opening Google...")
            webbrowser.open("https://www.google.com/")

        elif 'open youtube trending page' in query:
            speak("Opening youtube trending page...")
            webbrowser.open(" https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl")

        elif 'open amazon.com' in query:
            speak("Opening Amazon")
            webbrowser.open("https://www.amazon.in/")

        elif 'open gmail.com' in query:
            speak("Opening Gmail")
            webbrowser.open("https://mail.google.com")

        elif 'open maps.com' in query:
            speak("Opening Google Maps")
            webbrowser.open("https://www.google.com/maps/@26.6307398,73.873897,7z")

        elif 'open translate.com' in query:
            speak("Opening Google Translate")
            webbrowser.open("https://translate.google.co.in/")

        elif 'open flipkart.com' in query:
            speak("Opening Flipkart")
            webbrowser.open("https://www.flipkart.com/")

        elif 'open github.com' in query:
            speak("Opening Github")
            webbrowser.open("https://github.com/")

        elif 'open googledrive.com' in query:
            speak("Opening Google drive")
            webbrowser.open("https://drive.google.com/drive/my-drive")

#Play Music
        elif 'start music' in query:
            n= random.randint(0,18)
            print(n)
            speak("Here WE Go")
            music_dir = 'C:\\Users\\Harsh Verma\\Music'
            songs= os.listdir(music_dir)
            speak("Playing Song Number")
            speak(n)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[n]))

        elif 'change music' in query:
            n= random.randint(0,18)
            print(n)
            speak("Okay.")
            music_dir = 'C:\\Users\\Harsh Verma\\Music'
            songs= os.listdir(music_dir)
            speak("Playing Song Number")
            speak(n)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[n]))

#Software closing 

        

        elif 'close vs code' in query:
            os.system("taskkill /f /im Code.exe")
            speak("Visual Studio Code has been Closed.")
            
        

        elif 'close visual studio' in query:
            os.system("taskkill /f /im devenv.exe")
            speak("Visual Studio has been Closed.")

        

        elif 'close android studio' in query:
            os.system("taskkill /f /im studio64.exe")
            speak("Android Studio has been Closed.")

        

        elif 'close brave' in query:
            os.system("taskkill /f /im brave.exe")
            speak("Brave has been Closed.")

        

        elif 'close google chrome' in query:
            os.system("taskkill /f /im chrome.exe")
            speak("Google Chrome has been Closed.")

        

        elif 'close discord' in query:
            os.system("taskkill /f /im Discord.exe")
            speak("Discord has been Closed.")


#email sender

        elif 'send email to harsh' in query:
            emailtoharsh()

        elif 'send email to khushi' in query:
            emailtokhushi()

        elif 'send email to priya' in query:
            emailtopriya()

        elif 'send email to lakshika' in query:
            emailtolakshika()

#play youtube videos          
        elif 'play' in query:
            query = query.replace("play", "")
            results = kit.playonyt(query)
            str=('playing',query)
            speak(str)
            print(results)

#Google Search Anything
        elif 'google' in query:
            query = query.replace("google", "")
            results = kit.search(query)
            str=('searching for',query)
            speak(str)
            print("Searching results for", query )

#send whatsapp messages


        elif 'send a message to' in query:
            query=query.replace("send a message to ","")
            try:
                speak('What should i say?')
                content= takecommand()
                hour = int(datetime.datetime.now().hour)
                minute = int(datetime.datetime.now().minute)
                if content=='None':
                    content=content.replace(content , "")

                if query=="pankaj":
                    phone='+91 70236 22705'

                elif query=="khushi":
                    phone='+91 88825 30012'

                elif query=="chandu":
                    phone='+91 80056 46802'

                elif query=="priya":
                    phone='+91 73398 98849'

                elif query=="itisha":
                    phone='+91 74269 32093'

                elif query=="roshan":
                    phone='+91 97841 17842'

                elif query=="harjeet sir":
                    phone='+91 81074 54956'


             
                else :
                    print("contact not found.")
                    speak("contact not found.")

                kit.sendwhatmsg_instantly(phone, content , hour , minute)
                print("Message Sent sir.")
                speak("message Sent sir.")
            except Exception as e:
                print(e)  
                speak("Sorry sir . i can't do that right now")


        elif 'run snake game' in query:
            snakegame()

        elif 'close voice assistant' in query:
            speak("see you soon buddy.")
            break

        elif 'weather in' in query:
            query=query.replace("temperature in","")
            print(query)
            print("Displaying Weather Report For :- "+query)
            speak("Displaying Weather Report For :- "+query)
            url='https://wttr.in/{}'.format(query)
            res = requests.get(url)
            print(res.text) 

        elif 'shutdown the pc' in query:
                speak("Okay. your PC is going to be shutdown in 2 minutes")
                kit.shutdown(time=120)
                
        elif 'cancel shutdown' in query:
                kit.cancel_shutdown()
                speak("Shutdown has been cancelled.")

            
        elif 'joke' in query:
            a=pyjokes.get_joke()
            print(a) 
            speak(a)

        elif 'spell' in query:
            speakByLetter(query)
        
        elif 'notepad' in query:
            query=query.replace("write a note","")
            speak("tell me what you want to write.")
            query=takecommand()
            f=open("C:/Users/Harsh Verma/Desktop/Friday/Notepad file accessing/new.txt","w")
            f.write(query)
            f.close()
            speak("File created.")

        elif 'word file' in query:
            wordfile()

        elif "generate password" in query:
            genpass()

        elif 'take screenshot' in query:
            screeninshot()

        elif 'record my voice' in query:
            voicerecorder()

        

        elif 'mute' in query:
            devices=AudioUtilities.GetSpeakers()    
            interface=devices.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL, None)
            volume=cast(interface,POINTER(IAudioEndpointVolume))
            volume.SetMute(0,None)

        elif 'unmute' in query:
            devices=AudioUtilities.GetSpeakers()    
            interface=devices.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL, None)
            volume=cast(interface,POINTER(IAudioEndpointVolume))
            volume.SetMute(1,None)


        elif 'emergency' in query:
            emergency()

        elif 'open whatsapp' in query:
            kit.open_web()

        elif 'internet speed' in query:
            currentinternetspeed()

        elif 'set volume level' in query:
            query=query.replace("set volume level","")
            volsetup()
            
        elif 'set brightness level' in query:
            setbrightnesslevel(query)

        elif 'current brightness level' in query:
            print("Current Brightness Level{}%".format(sbc.get_brightness()))

        elif 'my current location'in query:
            currentlocation()

        elif 'distance between' in query:
            arialdiatance()

        elif 'calculate' in query:
            res = calc(query)
            print(res)
            speak(res)

        elif 'search' in query:
            gmaps(query)

        elif 'big basket' in query:
            bigbasket(query)

        elif 'bookmyshow' in query:
            bookmyshow(query)

        elif 'open pc app' in query:
            openpcapps(query)

        elif 'thanks' in query:
            speak('no problem sir.')

        elif 'friday' in query:
            speak("yes....")

        elif 'open cloud portal' in query:
            speak("Opening cloud portal...")
            webbrowser.open("https://portal.azure.com/#home")
 

        else:
            print("Please Enter  a valid Command ")
            print("")  




        

            





        



       