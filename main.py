import speech_recognition as sr
import os
import smtplib
import webbrowser
import pyaudio
# Initialize the recognizer
r = sr.Recognizer()
def send_email(subject, body, to):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('your_email_address', 'your_email_password')
    message = f'Subject: {subject}\n\n{body}'
    server.sendmail('your_email_address', to, message)
    server.quit()
def open_app(app_name):
    os.system(f'open /Applications/{app_name}.app')
def open_website(url):
    webbrowser.open(url)
def play_music():
    os.system('open -a Music')
# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print('Speak Anything :')
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f'You said: {text}')
            return text
        except:
            print('Sorry, could not recognize your speech.')
            return ''
# Main program loop
while True:
    # Recognize speech
    text = recognize_speech()
    # Check if user said 'send email'
    if 'send email' in text:
        send_email('Hello', 'This is a test email.', 'recipient@example.com')
    # Check if user said 'open app'
    if 'open app' in text:
        open_app('Calculator')
    # Check if user said 'open website'
    if 'open website' in text:
        open_website('https://www.google.com')
    # Check if user said 'play music'
    if 'play music' in text:
        play_music()
