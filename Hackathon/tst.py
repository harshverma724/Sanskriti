from tkinter import *
from sanskriti import *
from threading import Thread
from playsound import playsound


root=Tk()
root.title("Sanskriti")
root.iconbitmap("logoico.ico")

root.state("zoomed")

bg=PhotoImage(file="hihi.png")


def updateHead(arg):
    my_canvas.itemconfig(line1,text=arg)


def updatetext(arg):
    #arg="User Said: {}".format(arg)
    my_canvas.itemconfig(line2,text=arg)

def updateline3():
    my_canvas.itemconfig(line3,text="")


def updateline4():
    #arg="User Said: {}".format(arg)
    my_canvas.itemconfig(line4,text="")


#Create a canvas

my_canvas=Canvas(root,width=1920,height=1080)
my_canvas.pack(fill="both",expand=True)

#set image in canvas

my_canvas.create_image(0,0, image=bg, anchor='nw')

#add a label

line1=my_canvas.create_text(1150,250 ,text="Welcome to Sanskriti",font=("Optima",50),fill='#000000')
line2=my_canvas.create_text(1150,450 ,text="Kindly speak your language",font=("Optima",40),fill='#000000')

line3=my_canvas.create_text(900,650 ,text="1. Hindi",font=("Optima",40),fill='#000000')
line4=my_canvas.create_text(1350,650 ,text="2. English",font=("Optima",40),fill='#000000')


def hindi():
    l=["1.कृषि, ग्रामीण और पर्यावरण",
    "2.बैंकिंग, वित्तीय सेवाएं और बीमा",
    "3.व्यापार और उद्यमिता",
    "4.शिक्षण और अधिगम",
    "5.स्वास्थ्य और कल्याण",
    "6.आवास और आश्रय",
    "7.सार्वजनिक सुरक्षा, कानून और न्याय",
    "8.विज्ञान, आई.टी एवं संचार",
    "9.कौशल और रोजगार",
    "10.सामाजिक कल्याण और सशक्तिकरण",
    "11.खेल और संस्कृति",
    "12.आवागमन और बनावट",
    "13.यात्रा और पर्यटन",

    
    "14.उपयोगिता और स्वच्छता"]

    menu1=my_canvas.create_text(460,750 ,text=l[0],font=("Helvetica",20),fill='#000000') 
    menu2=my_canvas.create_text(485,800 ,text=l[1],font=("Helvetica",20),fill='#000000')
    menu3=my_canvas.create_text(410,850 ,text=l[2],font=("Helvetica",20),fill='#000000')
    menu4=my_canvas.create_text(405,900 ,text=l[3],font=("Helvetica",20),fill='#000000')
    menu5=my_canvas.create_text(405,950 ,text=l[4],font=("Helvetica",20),fill='#000000')
    menu6=my_canvas.create_text(397,1000 ,text=l[5],font=("Helvetica",20),fill='#000000')
    menu7=my_canvas.create_text(523,1050 ,text=l[6],font=("Helvetica",20),fill='#000000')
    
    menu8=my_canvas.create_text(1560,750,text=l[7],font=("Helvetica",20),fill='#000000')
    menu9=my_canvas.create_text(1525,800 ,text=l[8],font=("Helvetica",20),fill='#000000')
    menu10=my_canvas.create_text(1660,850 ,text=l[9],font=("Helvetica",20),fill='#000000')
    menu11=my_canvas.create_text(1510,900 ,text=l[10],font=("Helvetica",20),fill='#000000')
    menu12=my_canvas.create_text(1550,950 ,text=l[11],font=("Helvetica",20),fill='#000000')
    menu13=my_canvas.create_text(1510,1000 ,text=l[12],font=("Helvetica",20),fill='#000000')
    menu14=my_canvas.create_text(1570,1050 ,text=l[13],font=("Helvetica",20),fill='#000000')

    fotter=my_canvas.create_text(1150,1200 ,text="* अधिक प्रश्नों के लिए, आप संबंधित विभागों को मेल भेजने के लिए आदेश दे सकते हैं *",font=("Helvetica",20),fill='#000000')
    
def english():
    l=["1) Agriculture,Rural & Environment",
        "2) Banking,Financial Services and Insurance",
        "3) Business & Entrepreneurship",
        "4) Education & Learning",
        "5) Health & Wellness",
        "6) Housing & Shelter",
        "7) Public Safety,Law & Justice",
        "8) Science, IT & Communications",
        "9) Skills & Employment",
        "10) Social welfare & Empowerment",
        "11) Sports & Culture",
        "12) Transport & Infrastructure",
        "13) Travel & Tourism",
        "14) Utility & Sanitation"]

    menu1=my_canvas.create_text(485,750 ,text=l[0],font=("Helvetica",20),fill='#000000')
    menu2=my_canvas.create_text(570,800 ,text=l[1],font=("Helvetica",20),fill='#000000')
    menu3=my_canvas.create_text(460,850 ,text=l[2],font=("Helvetica",20),fill='#000000')
    menu4=my_canvas.create_text(390,900 ,text=l[3],font=("Helvetica",20),fill='#000000')
    menu5=my_canvas.create_text(360,950 ,text=l[4],font=("Helvetica",20),fill='#000000')
    menu6=my_canvas.create_text(360,1000 ,text=l[5],font=("Helvetica",20),fill='#000000')
    menu7=my_canvas.create_text(440,1050 ,text=l[6],font=("Helvetica",20),fill='#000000')

    menu8=my_canvas.create_text(1560,750 ,text=l[7],font=("Helvetica",20),fill='#000000')
    menu9=my_canvas.create_text(1470,800 ,text=l[8],font=("Helvetica",20),fill='#000000')
    menu10=my_canvas.create_text(1580,850 ,text=l[9],font=("Helvetica",20),fill='#000000')
    menu11=my_canvas.create_text(1440,900 ,text=l[10],font=("Helvetica",20),fill='#000000')
    menu12=my_canvas.create_text(1520,950 ,text=l[11],font=("Helvetica",20),fill='#000000')
    menu13=my_canvas.create_text(1450,1000 ,text=l[12],font=("Helvetica",20),fill='#000000')
    menu14=my_canvas.create_text(1460,1050,text=l[13],font=("Helvetica",20),fill='#000000')

    fotter=my_canvas.create_text(1200,1200 ,text="* For more queries, you can give a command to send mail to the respective departments. *",font=("Helvetica",20),fill='#000000')


def chalteraho():
    lanquery=takecommand()
    if "english" in lanquery[0]:
       english()
       updateline3()
       updateline4()
       updatetext("")
       speak("Hello. My name is  Sanskriti.  i am an assistant , who can assist you with the various governmental schemes established by the Indian government for the welfare of the citizens of India. I can help to ease your reach to various categories under which the Government of India has enforced these schemes through various departments and ministeries. Below given are the categories you can explore the schemes for.")
       speak("For more queries, you can give a command to send mail to the respective departments.")
    elif "hindi" in lanquery[0]:
        
        hindi()
        updateline3()
        updateline4()
        updatetext("")
        playsound('introhindi.mp3')
        playsound("footer.mp3")
    #if "hindi" in topquery:
       # hindi()

    #if "english" in topquery:
        #english()
    

    while True:
        
        updateHead("")
        updateHead("Listening")
        query = takecommand()
        updatetext(query[0])
        print(query)

        if (query[1] == False):
            updateHead("Recognizing...")
        if (query[1] == True):
            updateHead("Say that again")

        elif 'introduce yourself' in query[0]:
            speak('Hello. My name is  Sanskriti.  i am an assistant , who can assist you with the various governmental schemes established by the Indian government for the welfare of the citizens of India. I can help to ease your reach to various categories under which the Government of India has enforced these schemes through various departments and ministeries. Below given are the categories you can explore the schemes for.')
        
        elif 'apne bare mein batao' in query[0]:
            playsound('SwaraNeural.mp3')
        
        elif 'environment' in query[0]: 
            speak("Opening Agriculture, Rural and Environment")
            link="https://www.myscheme.gov.in/search/category/Agriculture,Rural%20&%20Environment"
            webbrowser.open("{}".format(link))

        elif 'paryavaran' in query[0]: 
            playsound('agriculture1.mp3') 
            link="https://www.myscheme.gov.in/hi/search/category/Agriculture,Rural%20&%20Environment"
            webbrowser.open("{}".format(link))

        elif 'banking' in query[0]:
            speak("Opening banking, financial services and insurance.")
            link="https://www.myscheme.gov.in/search/category/Banking,Financial%20Services%20and%20Insurance"
            webbrowser.open("{}".format(link))

        elif 'bhima' in query[0]:
            playsound('no2.mp3')
            link="https://www.myscheme.gov.in/hi/search/category/Business%20&%20Entrepreneurship"
            webbrowser.open("{}".format(link))

        elif 'business' in query[0]:
            speak("Opening business & entrepreneurship")
            link=" https://www.myscheme.gov.in/search/category/Business%20&%20Entrepreneurship"
            webbrowser.open("{}".format(link))

        elif 'Vyapar' in query[0]:
            playsound('business3.mp3')
            link="https://www.myscheme.gov.in/hi/search/category/Business%20&%20Entrepreneurship"
            webbrowser.open("{}".format(link))

        elif 'education' in query[0]:
            speak("Opening education & learning")  
            link="https://www.myscheme.gov.in/search/category/Education%20&%20Learning"
            webbrowser.open("{}".format(link))

        elif 'shikshan' in query[0]:
            playsound('no4.mp3')
            link="https://www.myscheme.gov.in/hi/search/category/Education%20&%20Learning"
            webbrowser.open("{}".format(link))

        elif 'health' in query[0]:
            speak("Opening health & wellness")
            link="https://www.myscheme.gov.in/search/category/Health%20&%20Wellness"
            webbrowser.open("{}".format(link))

        elif 'swasthya' in query[0]:
            playsound('health5.mp3')  
            link="https://www.myscheme.gov.in/hi/search/category/Health%20&%20Wellness"
            webbrowser.open("{}".format(link))

        elif 'housing' in query[0]:
            speak("Opening housing & shelter")
            link="https://www.myscheme.gov.in/search/category/Housing%20&%20Shelter"
            webbrowser.open("{}".format(link))

        elif 'Aawas' in query[0]:
            playsound('housing6.mp3')  
            link="https://www.myscheme.gov.in/hi/search/category/Housing%20&%20Shelter"
            webbrowser.open("{}".format(link))

        elif 'safety' in query[0]:
            speak("Opening public safety,law & justice")
            link="https://www.myscheme.gov.in/search/category/Public%20Safety,Law%20&%20Justice"
            webbrowser.open("{}".format(link))

        elif 'suraksha' in query[0]:
            playsound('publicsafety7.mp3')
            link="https://www.myscheme.gov.in/hi/search/category/Public%20Safety,Law%20&%20Justice"
            webbrowser.open("{}".format(link))

        elif 'science' in query[0]:
            speak("Opening science, IT & communications")
            link="https://www.myscheme.gov.in/search/category/Science,%20IT%20&%20Communications"
            webbrowser.open("{}".format(link))

        elif 'vigyan' in query[0]:
            playsound('no8.mp3')
            link="https://www.myscheme.gov.in/hi/search/category/Science,%20IT%20&%20Communications"
            webbrowser.open("{}".format(link))


        elif 'skills' in query[0]:
            speak("Opening skills & employment")
            link="https://www.myscheme.gov.in/search/category/Skills%20&%20Employment"
            webbrowser.open("{}".format(link))

        elif 'Kaushal' in query[0]:
            playsound('skills9.mp3')
            link="https://www.myscheme.gov.in/hi/search/category/Skills%20&%20Employment"
            webbrowser.open("{}".format(link))

        elif 'social welfare' in query[0]:
            speak("Opening social welfare & empowerment")
            link="https://www.myscheme.gov.in/search/category/Social%20welfare%20&%20Empowerment"
            webbrowser.open("{}".format(link))

        elif 'samajik kalyan' in query[0]:
            playsound('no10.mp3')
            link="https://www.myscheme.gov.in/hi/search/category/Social%20welfare%20&%20Empowerment"
            webbrowser.open("{}".format(link))

        elif 'sports' in query[0]:
            speak("Opening sports & culture")
            link=" https://www.myscheme.gov.in/search/category/Sports%20&%20Culture"
            webbrowser.open("{}".format(link))

        elif 'khel' in query[0]:
            playsound('sports11.mp3')
            link="https://www.myscheme.gov.in/hi/search/category/Sports%20&%20Culture"
            webbrowser.open("{}".format(link))

        elif 'transport' in query[0]:
            speak("Opening transport & infrastructure")
            link="  https://www.myscheme.gov.in/search/category/Transport%20&%20Infrastructure"
            webbrowser.open("{}".format(link))

        elif 'bnavat' in query[0]:
            playsound('transport12.mp3')
            link="https://www.myscheme.gov.in/hi/search/category/Transport%20&%20Infrastructure"
            webbrowser.open("{}".format(link))

        elif 'travel' in query[0]:
            speak("Opening travel & tourism")
            link="https://www.myscheme.gov.in/search/category/Travel%20&%20Tourism"
            webbrowser.open("{}".format(link))

        elif 'yatra' in query[0]:
            playsound('travel13.mp3')
            link="https://www.myscheme.gov.in/search/category/Travel%20&%20Tourism"
            webbrowser.open("{}".format(link))

        elif 'utility' in query[0]:
            speak("Opening utility & sanitation")
            link="https://www.myscheme.gov.in/search/category/Utility%20&%20Sanitation"
            webbrowser.open("{}".format(link))

        elif 'upyogita' in query[0]:
            playsound('utility14.mp3')
            link="https://www.myscheme.gov.in/hi/search/category/Utility%20&%20Sanitation"
            webbrowser.open("{}".format(link))


        elif 'learn more' in query[0]:
            speak("if you want to know more i'll redirect you to the main website, please wait")
            print("redirecting")
            link="https://www.myscheme.gov.in/"
            webbrowser.open("{}".format(link))


        elif 'aur jaane' in query[0]:
            playsound('reply.mp3')
            print("redirecting")
            link="https://www.myscheme.gov.in/"
            webbrowser.open("{}".format(link))

        elif 'close voice assistant' in query[0]:
            speak("see you soon buddy.")
            os.system("taskkill /f /im python.exe")
            break
        
        elif 'band ho jao' in query[0]:
            playsound('seeyousoon.mp3')
            os.system("taskkill /f /im python.exe")
            break

        elif 'sandesh paryavarn' in query[0]:
            emailtoparyavaran()

        elif 'sandesh bhima' in query[0]:
            emailtobhima()

        elif 'sandesh vyapar' in query[0]:
            emailtovyapar()

        elif 'sandesh shikshan' in query[0]:
            emailtoshikshan()

        elif 'sandesh swasthya' in query[0]:
            emailtoswasthya()

        elif 'sandesh aawas' in query[0]:
            emailtoaawas()

        elif 'sandesh suraksha' in query[0]:
            emailtosuraksha()

        elif 'sandesh vigyan' in query[0]:
            emailtovigyan()

        elif 'sandesh kaushal' in query[0]:
            emailtokaushal()

        elif 'sandesh samajik kalyan' in query[0]:
            emailtosamajikkalyan()

        elif 'sandesh khel' in query[0]:
            emailtokhel()

        elif 'sandesh bnavat' in query[0]:
            emailtobnavat()

        elif 'sandesh yatra' in query[0]:
            emailtoyatra()

        elif 'sandesh upyogita' in query[0]:
            emailtoupyogita()

        elif 'email environment' in query[0]:
            emailtoenvironment()

        elif 'email banking' in query[0]:
            emailtoenvironment()

        elif 'email business' in query[0]:
            emailtoenvironment()

        elif 'email education' in query[0]:
            emailtoenvironment()

        elif 'email health' in query[0]:
            emailtoenvironment()

        elif 'email housing' in query[0]:
            emailtoenvironment()

        elif 'email safety' in query[0]:
            emailtoenvironment()

        elif 'email science' in query[0]:
            emailtoenvironment()

        elif 'email skills' in query[0]:
            emailtoenvironment()

        elif 'email social welfare' in query[0]:
            emailtoenvironment()

        elif 'email sports' in query[0]:
            emailtoenvironment()

        elif 'email transport' in query[0]:
            emailtoenvironment()

        elif 'email travel' in query[0]:
            emailtoenvironment()

        elif 'email utility' in query[0]:
            emailtoenvironment()
            
        
        else:
            speak("please enter a valid command")
            print("please enter a valid command")

th = Thread(target=chalteraho)
th.start()
root.mainloop()
