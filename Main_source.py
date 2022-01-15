from random import randint as rand
import numpy as np
import pandas as pd
import time
#version - 1.2


'''recent update :
 completed save\load
 need to work on dictionary(identify grammer and define auto) and web search API
 update process_text() to analyze the question to facilitate search API
 '''

log_ = ""
def log(text):
    global log_
    log_ += "\n_____\n"
    log_ += text
    log_ += "\n_____\n"


#GUI GUI GUI __________________________________________________________


#MAIN________________________________________________________________________
# defining greeting words

greetings = ["hello", "good morning","Hi","what a wonderful day","Lovely day","love to be back","how are you?"]

top_common = '''the,at,there,some,my,',",.,/,<,>,?,\,{,},[,],(,),*,&,^,%,$,#,@,!, ,of,be,use,her,than,and,this,an,know,damn,fuck,shit,ha,hah,lmao,would,first,a,have,each,make,water,to,from,which,like,idk,lol,heck,fuck,shit,been,in,or,she,him,call,is,one,do,into,who,you,had,how,time,oil,that,by,their,has,its,it,word,if,look,now,he,but,will,two,find,was,not,up,more,long,for,what,other,write,down,on,all,about,go,day,are,were,out,see,did,as,we,many,number,get,with,when,then,no,come,his,your,them,way,made,they,can,these,could,may,I,said,so,people,part,hlo,hah,idk,nope,yes,no'''
common_words = top_common.split(",")
keyword = ["i","you"]

#main brain of the program
memory = np.array(
        [["obj","what","why","when","how"],
        ["me",0,0,0,0],["you",0,0,0,0]]
)

#defining editing memory tools

def create_mem(obj):
    new = np.array([[str(obj),0,0,0,0]])
    k = np.concatenate((memory,new),axis=0)
    return k

#defining the vocabulary

vocabulary = []
for i in range(1,len(memory)):
    vocabulary.append(memory[i][0])


#defining the chat history

recent = ""

def greet(text = None):
    if text == None:
        print(greetings[rand(0,6)])
    else:
        print(text)


def reply(word=None):
    if word == "quest":
        log("question detected")
        reply = "Nice question, do you want me to google it?"
    else:
       reply = "Great :)"
    return reply   
    
def memory_processor():
    global memory
    for i in keyword:
        if i in vocabulary:
            None
        else:    
            memory = create_mem(i)
            vocabulary.append(i)

def learn(text,mode=0):
    if mode == 0:
        text = text.lower()
        words = text.split(" ")
        for word in words:
            if word in common_words:
                None
            elif word in keyword:
                None
            else:    
                keyword.append(word)
    elif mode == 1:
        keyword.append(text)

# mood of the word tracking - beta      
      
def mood(words):
    positive = ["wow","amazing","great","good","excellent","perfect","loved it","love","exceptional","superb"]
    negative = ['shit','no','hate','damn','wtf','wth','bad','worse','worst','fool','mad','nope']
    
    x = 0
    text = words.split(" ")
    for word in text:
        if word in positive:
            x += 2
            log(word + "___postive")
        elif word in negative:
            x -= 1
            log(word + "___negative")
        else:
            None
            log(word + "neutral")
    mood = ["great","neutral","bad"]
    
    #mood score x//len(words)
    mood_score = x/len(text)
    log("mood score:" + str(mood_score))
    if mood_score >= 2:
        log(str(mood[0]))
        return mood[0]
    elif mood_score < 0:
        log(str(mood[2]))
        return mood[2]
    else:
        log(str(mood[1]))
        return mood[1]

mood_ = 0    

def process(text):
    global mood_
    mood_ = mood(text)
    text = text.lower()
    words = text.split(" ")
    for word in words:
            if word in common_words:
                None
            elif word in keyword:
                None
            else:    
                learn(word,1)    
    rep = reply()    
    return rep
    
def speak():
    global recent
    global log_
    inp = input(":")
    recent = inp
    log("input:" + inp)
    chat()

def error(word):
#dont forget to log
    global recent
    if word == "maintainance":
        note = ''' sorry, we've shut down this feature for maintainance
        sorry for the inconvinience, we'll bring it online
        ASAP :) '''
        log("error -- maintainance")
        save()
        log("autosave complete")
        recent = ""
    
    print(note)
    time.sleep(2)
    print("redirecting ")
    print("\n")
    chat()
        

def chat():
    global recent
    memory_processor()
    if recent == "":
        greet()
        speak()
    elif recent == "\save":
        save()
        speak()
    elif recent == "\data":
        print(memory)
        print(questions)
        speak()
    elif recent == "\load":
        #error("maintainance")
        load()
        speak()
    elif recent == "\log":
        global log_
        print(log_)
        speak()
    else:
        num =rand(0,7)
        if num >= 5:
            question()
        else:
            #print("1")
            print(process(recent))
            speak()

#questioning fucntion
questions=[]
def question():
    global memory
    for i in range(len(memory)):
        for j in range(len(memory[i])):
            if memory[i][j] == str(0):
                question = str(memory[0][j]) + " is " + memory[i][0] + " ?"
                questions.append(question)
                answer = input(question+":")
                memory[i][j] = answer   
                #processing the answer
                word = answer.lower()
                gram_text = ['grammer','gra','noun','verb','adjective','nvm']
                if word in gram_text:
                    for k in range(len(memory[i]) - 1):
                        memory[i][k+1] = "Null"
                    chat()
                else:    
                    learn(word,0)
                    chat()
        
 # saving the memory       

def save():
    global memory
    memory_ = open("mem.dat3",'w')
    #writing memory as list
    k = ""
    for i in range(len(memory)):
        for j in range(len(memory[i])):
            k += memory[i][j] +","
    
    memory_.write(k)

    '''note (Saving Bug)
    the save structure has a bug in which it saves
    unncessarily another ", " finally causing an extra block
    avoid the extra block in save
    
    to observe this bug uncomment below line and type \save in interface V1.2
    #print(k)
    '''
    memory_.close()
 
 
def load():
    #adapted to saving bug
    global memory
    memory_ = open("mem.dat3",'r')
    
    print("loading 0%",end = " ")
    time.sleep(0.1)
    
    #reading the memory
    memory_read = memory_.read()
    
    #processing text
    print("loading 36%",end = " ")
    time.sleep(0.2)
    
    _memory = memory_read.split(",")
    #adapting the saving bug [refer save() for explanation]
    _memory = _memory[:len(_memory)-1]
    
    rows = len(_memory)/5
    status = "number of rows: " + str(rows) +"\n" + "memory_read :" + str(len(memory_read))
    log(status)

    #1)create an array called memory
    memory = np.array(["0",2,3,4,5],dtype =str,ndmin = 2)
    #print(memory)
    
    #checking the loading data
    #print(_memory)

    #2) loading the data
    print("loading the data 83%")
    k = 0
    for i in range(int(rows)):
        for j in range(5):
            #print(_memory[k])
            if j==0:
                new = np.array([[_memory[k],0,0,0,0]])
                memory = np.concatenate((memory,new),axis=0)
                k +=1
                #REFINING THE PREDEFINED MEMORY DUMMY
                if k == 1:
                    memory = memory[1:]
                    log("refining complete")
            else:
                memory[i][j] = _memory[k]
                k +=1
                   
    #print(memory)
    print("loading complete 100% :)")
    memory_.close()
    
    '''LOAD_V2 COMPLETE 20/09/2021 :)'''

chat()

#MAIN________________________________________________________________________

#watchlist
