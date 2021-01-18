from tkinter import *
from tkinter import ttk
import speech_recognition as sr

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

def mod(a,b):
    return a % b

def lcm(a,b):
    L = a if a>b else b
    while L <= a*b:
        if L%a == 0 and L%b == 0:
            return L
        L+=1

def hcf(a,b):
    H = a if a<b else b
    while H >= 1:
        if a%H == 0 and b%H == 0:
            return H
        H-=1


def split_words(text):
    wrd=[]
    for i in text.split():
        try:
            wrd.append(float(i))
        except Exception:
            pass
    return wrd


def calculate(*agrs):
    comm=command.get()
    for word in comm.split():
        if word.upper() in operations.keys():
            try:
                dig=split_words(comm)
                res=operations[word.upper()](dig[0],dig[1])
                box.delete(0,END)
                box.insert(END,res)
            except Exception:
                box.delete(0,END)
                box.insert(END,'something went wrong please enter again')
            finally:
                break
        elif word.upper() not in operations.keys():
            box.delete(0,END)
            box.insert(END,'something went wrong please enter again')

def speak():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print('speak something')
        audio=r.listen(source)

        try:
            comm=r.recognize_google(audio)
            print('You said',comm)
        except:
            print('sorry')

    for word in comm.split():
        if word.upper() in operations.keys():
            try:
                dig=split_words(comm)
                res=operations[word.upper()](dig[0],dig[1])
                box.delete(0,END)
                box.insert(END,res)
            except Exception:
                box.delete(0,END)
                box.insert(END,'something went wrong please enter again')
            finally:
                break
        elif word.upper() not in operations.keys():
            box.delete(0,END)
            box.insert(END,'something went wrong please enter again')


operations = {'ADD':add , 'ADDITION':add , 'SUM':add , 'PLUS':add ,
                'SUB':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub,
                 'LCM':lcm , 'HCF':hcf , 'PRODUCT':mul , 'MULTIPLICATION':mul,
                 'MULTIPLY':mul , 'DIVISION':div , 'DIV':div ,'DIVIDE':div, 'MOD':mod ,
                  'REMANDER':mod , 'MODULUS':mod}

root=Tk()
root.geometry("450x450")
root.title('Smart Calculator')
ttk.Label(root,text='Welcome to Smart Calculator',font=("arial 20 bold")).pack(pady=5)
ttk.Label(root,text='Use your voice to calculate',font=("arial 15 bold")).pack(pady=5)
ttk.Label(root,text='or just type in',font=("arial 15 bold")).pack()
command = StringVar()
e1 = ttk.Entry(root, width=30, textvariable = command)
e1.pack(pady=50)
photo=PhotoImage(file="D:\\Python projects\\smart_calculater\\mic.png")
b2=ttk.Button(root,text='Speak',image=photo,command=speak)
b2.pack()
root.bind('<Return>', calculate)
b1=ttk.Button(root,text='Calculate',command=calculate)
b1.pack()

ttk.Label(root,text='Result:',font=("arial 18")).pack()
box=Listbox(root,width=30,height=5)
box.pack()

root.mainloop()