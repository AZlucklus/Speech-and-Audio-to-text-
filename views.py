from django.shortcuts import render

from django.http import HttpResponse
from gtts import gTTS
from playsound import playsound
import os
import requests
# Create your views here.

############# ATALLTECH
from django.shortcuts import render , redirect 
import speech_recognition as sr
from .models import *
import speech_recognition as spr 
#from pyarabic.araby import join_arabic_letters
from googletrans import Translator 
import base64 
translator = Translator()



def hi(request):
    return render(request,"hi.html")
def vspage(request):
    return render(request,"vspage.html")
def txtpage(request):
    return render(request,"txtpage.html")


    
def vs_reg(request):
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
        print("Speak: ")
        audio = r.record(source , duration=20 )

    # recognize speech using Google Speech Recognition
    try:
        text_arabic = r.recognize_google(audio, language='ar-SA')
        print("You said: " + text_arabic)

        # translate text to English
        # text_english = r.recognize_google(audio)
        text_english = translator.translate(text_arabic, src='ar', dest='en').text
        print("Translation: " + text_english)
        return render(request, 'vspage.html', {'text': text_english,"text2":text_arabic })
    except sr.UnknownValueError:
                # Handle unrecognized speech
                error_msg = "Sorry, could not recognize speech in the audio file."
                return render(request, 'vspage.html', {'error_msg': error_msg})
    with open("transcribed_tex5.txt", "w" , encoding='utf-8') as text_file:
        text_file.write(text_arabic)            
     
         

def transcribe_audio(request):
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'audio_file' in request.FILES:
            # Get the uploaded file from the request
            audio_file = request.FILES['audio_file']

            # Create a speech recognition object
            r = sr.Recognizer()
            translator = Translator()

            # Convert the audio file to audio data
            audio_data = sr.AudioFile(audio_file)
            with audio_data as source:
                audio = r.record(source , duration=20)
            
            # Transcribe the audio data to text using Google Speech Recognition
            try:
                text_from = r.recognize_google(audio , language='ar-SA')
                print(text_from)
                
                text= r.recognize_google(audio)
                print(text)
                
                # Render the transcribed text in the response
                return render(request, 'txtpage.html', {'text': text_from , 'text2':text })
            except sr.UnknownValueError:
                # Handle unrecognized speech
                error_msg = "Sorry, could not recognize speech in the audio file."
                return render(request, 'txtpage.html', {'error_msg': error_msg})
            with open("transcribed_tex5.txt", "w" , encoding='utf-8') as text_file:
                text_file.write(text_from)    
        else:
            # Handle case where no file was uploaded
            error_msg = "No audio file was uploaded."
            return render(request, 'txtpage.html', {'error_msg': error_msg})
    else:
        # Render the file upload form
        return render(request, 'txtpage.html')
    
        
        

            
        
               
            
def goo(request):
    data = requests.get("https://www.google.com/")
    print(data.text)
    data=data.text
    return render(request,"hi.html",{"data":data})    