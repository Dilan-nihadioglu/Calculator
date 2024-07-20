from tkinter import*


w=Tk()
w.title("CALCULATOR")
w.geometry("230x320")
w.resizable(FALSE,FALSE)
w.tk_setPalette("#014D27")
header=Label(w,text="EXECUTE",font="algerian",fg="orange")
header.pack(side="top")
screen=Entry(w,fg="orange",font="Arial 20 bold",width=14,justify="right") #justify right deme yazı sağdan sola doğru ilerlesin demek
screen.pack()

result=""
def calculate(key):
    global result
    if key in "1234567890":
        screen.insert(END,key)
        result+=key

    if key in "+%*-(),/**":
        screen.insert(END,key)
        result+=key

    if key=="=":
        screen.delete(0,END)
        result=eval(result,{"__builtins__":None},{}) #eval fonksiyonu textin içerisindeki her sembolu ayırıp hesaplar.
        result=str(result)
        screen.insert(END,result)


    if key=="C":
        screen.delete(0,END)
        

a=0.05
b=0.22
symbols=["()","%","**","-","1","2","3","+","4","5","6","/","7","8","9","*","=","0","C",","]      
for i in symbols:
    y=lambda x=i : calculate(x)
    symbol=Button(w,text=i,relief="raised",font="algerian",fg="orange",bg="black",command=y) #relief tuş şekillendirmesi falan
    symbol.place(relx=a,rely=b)
    a+=0.25
    if(a>=1.0):
        b+=0.15
        a=0.05


















mainloop()