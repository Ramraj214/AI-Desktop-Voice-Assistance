import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import speech_recognition as sr
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good Morning")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon")
    elif hour >=16 and hour <19:
        speak("Good Evening")
    else:
        speak("Good Night")

    speak("I am Jarvis sir. please tell me how may i help you")

def takeCommand():
    """
    It takes microphone input from the user and returns string output
    """
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        #print(e)
        print("Say that again Please....")
        return "None"

    return query

def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("ramrajnagapure54321@gmail.com","tgla cadx yqeh bkbp")
    server.sendmail("ramrajnagapure54321@gmail.com",to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    #Logic for executing task
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open chrome' in query:
            webbrowser.open("chrome.com")
        
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir='C:\\Users\\ramra\\Music'
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is{strTime}")

        elif 'open code' in  query:
            codePath="C:\\Users\\ramra\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'email to ramraj' in query:
            try:
                speak("What should i say?")
                content=takeCommand()
                to="ramrajnagapure54321@gmail.com"
                sendEmail(to,content)
                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry my friend ram ,i am not able to send this email")