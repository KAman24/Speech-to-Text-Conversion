import speech_recognition as s 
sr=s.Recognizer()
with s.Microphone() as m:
    print("Noice Adjustment ")
    sr.adjust_for_ambient_noise(m)
    print("Hey Dora is Here to Help You. Ask me ")
    audio=sr.listen(m)
    print("I have heard your voice ")
    query=sr.recognize_google(audio,language='eng-in')
    print(query)








