import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
import os
import pywhatkit as kt

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak("Good Morning ")
    elif 12 <= hour < 18:
        speak("Good Afternoon ")
    else:
        speak("Good Evening")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said : {query} \n")
    except:
        print("Please say that again.")
        return "None"
    return query


def send_email(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("viknit2003@gmail.com", "Vikas@2003")
    server.sendmail("viknit2003@gmail.com", to, content)
    server.close()


if __name__ == "__main__":
    wish()
    speak("can i know what's Your Name")
    name = take_command()
    speak(f"welcome {name}")
    speak(f"Hey i am professor {name} HOW MAY I HELP YOU")

    # while True:

    #     if "professor" in query:
    while True:
        # speak(f"yes {name} how can i help you")
        query = take_command().lower()
        if ("hey" in query) or ("hi" in query) or ("hello" in query):
            print(f"Hey!{name} how can i help you.")
            speak(f"Hey!{name} how can i help you.")

        elif "how are you" in query or "what's up buddy" in query:
           print("i'm fine.You're very kind to ask")
           speak(f"i'm fine.You're very kind to ask")

        elif "are you doing" in query:
            print("\nWell,Nothing.")
            speak("well nothing")
            print("\nWorking on my skills.")
            speak("working on my skills")
            speak("how can i help you")

        elif "you can do" in query or "why are you here" in query:
            speak("i can do several things like")
            tasks = ["I can open several applications and sites like : chrome,camera..etc",
                    "I can tell you what's ",
                    "current time.",
                    "I can send Email,but make sure you are connected to internet"]
            for task in tasks:
                print(task)
                speak("I can open several applications and sites like chrome,camera..etc")
                speak("How May i help you.")
                query = take_command()
                break

        elif ("who made you" in query) or ("who are you" in query) or ("your birthday" in query):
            print("I am vik.I was made by Vikas and My birthday comes on 20 january.")
            speak("I am vik.I was made by Vikas and My birthday comes on 20 january.")

        elif 'wikipedia' in query:
            try:
                speak("Searching Wikipedia")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                print(result)
                speak(result)
            except:
                print("sorry i didn't find any thing")
                speak("sorry i didn't find any thing")

        elif "open" in query:
                if ("note" in query) or ("notes" in query) or ("notepad" in query) or ("editor" in query):
                   speak("Opening NOTEPAD")
                   os.system("Notepad")

                elif ("camera" in query) or ("take photo" in query) or ("take a photo" in query):
                    speak("opening camera")
                    os.startfile("C:\\Users\\rahul\\OneDrive\\Desktop\\Camera")

                elif ("google earth" in query) or ("earth" in query):
                    speak("opening google earth pro")
                    os.startfile("C:\\Program Files\\Google\\Google Earth Pro\\client\\googleearth.exe")

                    # elif ("photos" in query) or ("images" in query) or ("pictures" in query):
                    #     speak("opening photos")
                    #     os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\Google Photos")

                elif "chrome" in query:
                    speak("opening google chrome browser")
                    os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

                else:
                    l_query = query.split(" ")
                    i = 0
                    for item in l_query:
                        if i == 1:
                            to_open = item
                            speak(f"opening {to_open} in browser")
                            webbrowser.open(f"{to_open}.com")
                            break
                        if item == "open":
                            i += 1

        elif "the time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(strtime)

        elif "send email" in query or "send a mail" in query or "send mail" in query:
            dic = {"vikas": "vksihra8@gamil.com", "rahul": "rahulnit1998@gmail.com","bhola":"bholak993@gmail.com"}
            while True:
                speak("whom do you want to send email")
                to_whom = take_command().lower()
                print(to_whom)
                if to_whom != 'none':
                    break
                try:
                    if to_whom in dic or "gmail.com" in to_whom:
                        speak("what should i say in email")
                        content = take_command()
                        to = dic.get(to_whom)
                        send_email(to, content)
                        speak("email has been sent")
                except:
                    speak(f"sorry {name} mail can't be sent")

        elif "keep quiet" in query or "shut up" in query or "quiet" in query or "that's it" in query:
            speak("ok sir")
            break

        elif "good" in query:
                speak("thank you")
                # speak("any other query.")

        else:
            # if "none" not in query:
            speak("i found these result from web")
            kt.search(query)
            # break

            query = take_command().lower()