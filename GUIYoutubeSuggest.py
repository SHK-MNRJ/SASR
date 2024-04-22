import urllib.request
import re
import Facedetection
from tkinter import *
from PIL import Image, ImageTk

import webbrowser
from functools import partial

def initlizer(emotionOfPerson):
    init_window(emotionOfPerson)

def init_window(emotionType):
    #print(emotionType)
    root.title("GUI")
    showImg(emotionType)
    showText(emotionType)

def showImg(imgType):
    if imgType in ['happy','sad','angry','suprise','neutral']:
        #print('========show img========')
        imgType=imgType+'.jpeg'
        #print(imgType)
        load = Image.open("./img/"+imgType)
        resize_image = load.resize((250,250))
        render = ImageTk.PhotoImage(resize_image)
        img = Label(image=render)
        img.image = render
        img.place(x=100, y=50)
    else:
        pass

def showText(emotion):
    #print('========show text========')
    #print(emotion)
    text = Label(text=emotion, font=("Arial", 40))
    text.pack()

# Define a callback function
def callback(url):
   webbrowser.open_new_tab(url)

def urlAppender(i):
    text = Label(frameOne,text=i,cursor='hand2',fg='blue',font=('Times',10,'underline'))
    # Create a Label to display the link
    text.bind('<Button-1>',lambda x:webbrowser.open_new(i))
    text.pack()
    
def videoUrl(urlList):
    urlList=urlList[1:15]
    for i in urlList:
        i="https://www.youtube.com/watch?v="+i
        urlAppender(i)
        
        
print("Creating gui")
root = Tk()
root.geometry("400x600")

frameOne=Frame(root,width=300,height=200)

frameOne.pack(side=BOTTOM)
#Facedetection.hello()
#print('hello world')
emotionOfPerson=Facedetection.emotionDetection()
#print(emotionOfPerson)

html=urllib.request.urlopen("https://www.youtube.com/results?search_query="+str(emotionOfPerson)+"tamilsongs")
video_ids=re.findall(r"watch\?v=(\S{11})",html.read().decode())
#print(video_ids[10])
video_ids=list(set(video_ids))
videoUrl(video_ids)
#print(html.read())

initlizer(emotionOfPerson)
root.mainloop() 
