from tkinter import *
from PIL import ImageTk,Image


def get_dig(digit):
    current= result_label["text"]
    new=current+ str(digit)
    result_label.config(text=new)

def clr():
    result_label.config(text="")

def delete():
    current = result_label["text"]
    new = current[:-1]
    result_label.config(text=new)

def clear_equalto():
    result_label.config(text="")

#declaration of number and operator

num1=num2=opertor1=None

def opertor(op):
    global num1,opertor1

    num1=float(result_label['text'])
    opertor1= op
    if (opertor1=='1/x'):
        div_1byx=round((1/num1),4)
        result_label.config(text=str(div_1byx))
    elif (opertor1=='x^2'):
        square=round((num1**2),6)
        result_label.config(text=str(square))
    elif (opertor1=='sqrt(x)'):
        sqrroot=round(num1**(1/2),6)
        result_label.config(text=str(sqrroot))
    elif (opertor1=='percent'):
        current=float(result_label["text"])
        percent=current/100
        rounded_result=round(percent,5)
        result_label.config(text=str(rounded_result))
    else:
        new_str=""
        result_label.config(text=new_str)
    

def plus_minus():
    current_num = float(result_label['text'])
    result_label.config(text=str(0 - current_num))

def result_equalto():
    global num1,num2,opertor1

    num2=int(result_label['text'])

    if (opertor1=='+'):
        addition=str(num1+num2)
        result_label.config(text=addition)
    elif (opertor1=='-'):
        substraction=str(num1-num2)
        result_label.config(text=substraction)
    elif (opertor1=='*'):
        product=str(num1*num2)
        result_label.config(text=product)
    elif (opertor1=='/'):
        if num2==0:
            result_label.config(text="Error")
        else:
            division = num1 / num2
            rounded_result = str(round(division, 6))
            result_label.config(text=(rounded_result))

  

root= Tk()
root.geometry("320x550")
root.resizable(0,0)
root.title("My Standard Calculator")
# root.iconbitmap("calculator_81497.ico")
root.config(bg="#888888")

# Result Section
result_label=Label(root,text="",bg="#888888",fg="black")
result_label.grid(row=0,column=0,padx=(0,0), columnspan=10, pady=(40,25), ipady=8, sticky="w")
result_label.config(font=("Verdana",30,"bold"))

#Button section
btn_percent=Button(root,text="%",bg="aqua",fg="black",width=5,height=2,command= lambda :opertor("percent"))
btn_percent.grid(row=1,column=0)
btn_percent.config(font=("Verdana",15,"bold"))

btn_CE=Button(root,text="CE",bg="aqua",fg="black",width=5,height=2,command= clear_equalto)
btn_CE.grid(row=1,column=1)
btn_CE.config(font=("Verdana",15,"bold"))

btnC=Button(root,text="C",bg="aqua",fg="black",width=5,height=2,command=clr)
btnC.grid(row=1,column=2)
btnC.config(font=("Verdana",15,"bold"))

btn_del=Button(root,text="del",bg="aqua",fg="black",width=5,height=2,command=delete)
btn_del.grid(row=1,column=3)
btn_del.config(font=("Verdana",15,"bold"))

btn_1div=Button(root,text="1/x",bg="aqua",fg="black",width=5,height=2,command=lambda :opertor("1/x"))
btn_1div.grid(row=2,column=0)
btn_1div.config(font=("Verdana",15,"bold"))

btn_xsq=Button(root,text="x^2",bg="aqua",fg="black",width=5,height=2,command=lambda :opertor("x^2"))
btn_xsq.grid(row=2,column=1)
btn_xsq.config(font=("Verdana",15,"bold"))

btnx_sqrt=Button(root,text="sqrt(x)",bg="aqua",fg="black",width=5,height=2,command=lambda :opertor("sqrt(x)"))
btnx_sqrt.grid(row=2,column=2)
btnx_sqrt.config(font=("Verdana",15,"bold"))

btn_div=Button(root,text="/",bg="aqua",fg="black",width=5,height=2,command=lambda :opertor("/"))
btn_div.grid(row=2,column=3)
btn_div.config(font=("Verdana",15,"bold"))

btn7=Button(root,text="7",bg="aqua",fg="black",width=5,height=2,command=lambda : get_dig(7))
btn7.grid(row=3,column=0)
btn7.config(font=("Verdana",15,"bold"))

btn8=Button(root,text="8",bg="aqua",fg="black",width=5,height=2,command=lambda : get_dig(8))
btn8.grid(row=3,column=1)
btn8.config(font=("Verdana",15,"bold"))

btn9=Button(root,text="9",bg="aqua",fg="black",width=5,height=2,command=lambda : get_dig(9))
btn9.grid(row=3,column=2)
btn9.config(font=("Verdana",15,"bold"))

btn_mul=Button(root,text="*",bg="aqua",fg="black",width=5,height=2,command=lambda :opertor("*"))
btn_mul.grid(row=3,column=3)
btn_mul.config(font=("Verdana",15,"bold"))

btn4=Button(root,text="4",bg="aqua",fg="black",width=5,height=2,command=lambda : get_dig(4))
btn4.grid(row=4,column=0)
btn4.config(font=("Verdana",15,"bold"))

btn5=Button(root,text="5",bg="aqua",fg="black",width=5,height=2,command=lambda : get_dig(5))
btn5.grid(row=4,column=1)
btn5.config(font=("Verdana",15,"bold"))

btn6=Button(root,text="6",bg="aqua",fg="black",width=5,height=2,command=lambda : get_dig(6))
btn6.grid(row=4,column=2)
btn6.config(font=("Verdana",15,"bold"))

btn_add=Button(root,text="+",bg="aqua",fg="black",width=5,height=2,command=lambda :opertor('+'))
btn_add.grid(row=4,column=3)
btn_add.config(font=("Verdana",15,"bold"))


btn1=Button(root,text="1",bg="aqua",fg="black",width=5,height=2,command=lambda : get_dig(1))
btn1.grid(row=5,column=0)
btn1.config(font=("Verdana",15,"bold"))

btn2=Button(root,text="2",bg="aqua",fg="black",width=5,height=2,command=lambda : get_dig(2))
btn2.grid(row=5,column=1)
btn2.config(font=("Verdana",15,"bold"))

btn3=Button(root,text="3",bg="aqua",fg="black",width=5,height=2,command=lambda : get_dig(3))
btn3.grid(row=5,column=2)
btn3.config(font=("Verdana",15,"bold"))

btn_sub=Button(root,text="-",bg="aqua",fg="black",width=5,height=2,command=lambda :opertor('-'))
btn_sub.grid(row=5,column=3)
btn_sub.config(font=("Verdana",15,"bold"))

btn_minus=Button(root,text="(-)",bg="aqua",fg="black",width=5,height=2,command=plus_minus)
btn_minus.grid(row=6,column=0)
btn_minus.config(font=("Verdana",15,"bold"))

btn0=Button(root,text="0",bg="aqua",fg="black",width=5,height=2,command=lambda : get_dig(0))
btn0.grid(row=6,column=1)
btn0.config(font=("Verdana",15,"bold"))

btn_decimal=Button(root,text=".",bg="aqua",fg="black",width=5,height=2,command=lambda : get_dig("."))
btn_decimal.grid(row=6,column=2)
btn_decimal.config(font=("Verdana",15,"bold"))

btn_equal=Button(root,text="=",bg="#cc8800",fg="black",width=5,height=2,command=result_equalto)
btn_equal.grid(row=6,column=3)
btn_equal.config(font=("Verdana",15,"bold"))

root.mainloop()