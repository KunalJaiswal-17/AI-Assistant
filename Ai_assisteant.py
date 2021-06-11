import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains 

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)
newVoiceRate = 190 
engine.setProperty('rate', newVoiceRate)
browser = webdriver.Chrome()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("right now the time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("and The current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Hello sir!")

    hour = datetime.datetime.now().hour
    if hour >= 4 and hour <= 12:
        speak("Good morning")
    elif hour >= 12 and hour <=17:
        speak("Good afternoon")
    elif hour >=17 and hour <=20:
        speak("Good evening")
    else:
        def night():
            speak("Good night")

    speak("AI Assistant Serina on your Service. So, How can I help you?")
    
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en=US")
        print(query)
    except Exception as e:
        print(e)
        speak("Cannot able to recognize, please say that again...")
        return "None"

    return query

def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("kunalmannat2001@gmail.com", "kunal4101")
    server.sendmail("kunalmannat2001@gmail.com", to, content)
    server.close()

def timeTable():
    browser.get('https://s.amizone.net/')

def findElement(type, selector):
	while True:
		try:
			if type=='css':
				element = browser.find_element_by_css_selector(selector)
				break
			elif type=='class':
				element = browser.find_elements_by_class_name(selector)
				break
			elif type=='xpath':
				element = browser.find_element_by_xpath(selector)
				break
			elif type=='id':
				element = browser.find_element_by_id(selector)
				break
	
		except:
			pass

	return element


username = findElement('css', '#loginform > div:nth-child(2) > input.input100')
username.send_keys('7988549')

password = findElement('css', '#loginform > div:nth-child(3) > input')
password.send_keys('manoj@02')

login = findElement('css', '#loginform > div.container-login100-form-btn > button')
login.click()

clickaway = findElement('css', '#navbar-container > div:nth-child(3) > h4')
ac = ActionChains(browser)
ac.move_to_element(clickaway).move_by_offset(0, 0).click().perform()
ac.move_to_element(clickaway).move_by_offset(0, 0).click().perform()

menu = findElement('css', '#menu-toggler')
menu.click()

timeTable = findElement('xpath', '//*[@id="10"]')
timeTable.click()


if __name__ == "__main__":

    wishme()

    while True:
        query = take_command().lower()

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "power off" in query:
            quit() 
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            speak(result)
        elif "send email" in query:
            try:
                speak("what should I write in mail?")
                content = take_command()
                speak("Whom to send this email?")
                who = take_command()
                if "dad" in who:
                    to = "manojjaiswal1976@gmail.com"
                elif "me myself" in who:
                    to = "kunalmannat2001@gmail.com"
                elif "mom" in who:
                    to = "kiranpihujaiswal1978@gmail.com"
                
                send_email(to, content)
                speak("Email sent successfully")
            except Exception as e:
                speak(e)
                speak("Unable to send the mail")
        elif "search in chrome" in query:
            speak("what should I search?")
            chromepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
            search = take_command().lower()            
            wb.get(chromepath).open_new_tab(search + ".com")
        elif "Time Table" in query:
            timeTable()
    