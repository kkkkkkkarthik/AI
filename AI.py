import speech_recognition as sr 
import datetime
import wikipedia
import pyttsx3 
import smtplib 
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
 engine.say(audio)
 engine.runAndWait()
def wishMe():
 hour = int(datetime.datetime.now().hour)
 if hour>=0 and hour<12:
 speak("Good Morning!")
 elif hour>=12 and hour<18:
 speak("Good Afternoon!") 
 else:
 speak("Good Evening!") 
 speak("hello sir this is haris assistant specially made for you") 
 def takeCommand():
 r = sr.Recognizer()
 with sr.Microphone() as source:
 print("Listening...")
 r.pause_threshold = 1
 audio = r.listen(source)
 try:
 print("Recognizing...") 
 query = r.recognize_google(audio, language='en-in')
 print(f"User said: {query}\n")
 except Exception as e:
 print("Say that again please...") 
 return "None"
 return query
def sendEmail(to, content):
 server = smtplib.SMTP('smtp.gmail.com', 587)
 server.ehlo()
 server.starttls()
 server.login('youremail@gmail.com', 'your-password')
 server.sendmail('youremail@gmail.com', to, content)
 server.close()
if _name_ == "_main_":
 wishMe()
 while True:
 # if 1:
 query = takeCommand().lower()
 # Logic for executing tasks based on query
 if 'wikipedia' in query:
 speak('Searching Wikipedia...')
 query = query.replace("wikipedia", "")
 results = wikipedia.summary(query, sentences=2)
 speak("According to Wikipedia")
 print(results)
 speak(results)
 elif 'open youtube' in query:
 webbrowser.open("youtube.com")
 elif 'what is your name ' in query:
 speak(" iam a combination of siri and google so my name is sigo")
elif 'open google' in query:
 webbrowser.open("google.com")
 elif 'open stackoverflow' in query:
 webbrowser.open("stackoverflow.com") 
 elif 'open v top' in query:
 webbrowser.open("vtop.ac.in")
elif 'open gog' in query:
webbrowser.open("geeks of geek.com")
 elif 'netflix' in query: 
webbrowser.open("www.netflix.com")
 elif 'play music' in query:
 music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
 songs = os.listdir(music_dir)
 print(songs) 
 os.startfile(os.path.join(music_dir, songs[0]))
 elif 'the time' in query:
 strTime = datetime.datetime.now().strftime("%H:%M:%S") 
 speak(f"Sir, the time is {strTime}")
 elif 'email to hari' in query:
 try:
 speak("What should I say?")
 content = takeCommand()
 to = "yerramkarthik29@gmail.com" 
 sendEmail(to, content)
 speak("Email has been sent!")
 except Exception as e:
 print(e)
 speak("Sorry my friend . I am not able to send this email")
