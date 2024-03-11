from tkinter import *
root = Tk()
root.title('zentience calculator')
def clear():
    db.delete(0,END)

def btn_clk(num):
    cur_num = db.get()
    clear()
    f_num = cur_num + num
    db.insert(0,f_num)

first_num =0 

def calc(math_type):
    global first_num,math
    math = math_type
    first_num =db.get()
    clear()

def equal():
    result = ''
    global first_num
    second_num = db.get()
    clear()
    if math == 'add':
        result = int(first_num) + int(second_num)
    elif math == 'sub':
        result = int(first_num) - int(second_num)
    elif math == 'mul':
        result = int(first_num) * int(second_num)
    elif math == 'div':
        result = int(first_num) / int(second_num)
        result =round(result,3)
    db.insert(0,str(result))

# Creating widgets
db = Entry(root,width=10,font=('Arial',28),justify=RIGHT)
# button height pady
btn_0 = Button(root,text ='0',padx =36,pady = 10,font=('Arial',14),command=lambda:btn_clk('0'))
btn_1 = Button(root,text ='1',padx =36,pady = 10,font=('Arial',14),command=lambda:btn_clk('1'))
btn_2 = Button(root,text ='2',padx =36,pady = 10,font=('Arial',14),command=lambda:btn_clk('2'))
btn_3 = Button(root,text ='3',padx =36,pady = 10,font=('Arial',14),command=lambda:btn_clk('3'))
btn_4 = Button(root,text ='4',padx =36,pady = 10,font=('Arial',14),command=lambda:btn_clk('4'))
btn_5 = Button(root,text ='5',padx =36,pady = 10,font=('Arial',14),command=lambda:btn_clk('5'))
btn_6 = Button(root,text ='6',padx =36,pady = 10,font=('Arial',14),command=lambda:btn_clk('6'))
btn_7 = Button(root,text ='7',padx =36,pady = 10,font=('Arial',14),command=lambda:btn_clk('7'))
btn_8 = Button(root,text ='8',padx =36,pady = 10,font=('Arial',14),command=lambda:btn_clk('8'))
btn_9 = Button(root,text ='9',padx =36,pady = 10,font=('Arial',14),command=lambda:btn_clk('9'))
btn_clear = Button(root,text ='clear',padx =70,pady = 10,font=('Arial',14),command=clear)
btn_div = Button(root,text ='/',padx =36,pady = 10,font=('Arial',14),command =lambda:calc('div'))
btn_mul = Button(root,text ='*',padx =36,pady = 10,font=('Arial',14),command =lambda:calc('mul'))
btn_sum = Button(root,text ='+',padx =36,pady = 10,font=('Arial',14),command =lambda:calc('add'))
btn_sub = Button(root,text ='-',padx =36,pady = 10,font=('Arial',14),command =lambda:calc('sub'))
btn_equal = Button(root,text ='=',padx=36,pady=35,font=('Arial',14),command=equal)

# showing widgets
btn_1.grid(row=1,column =0,pady=2)
btn_2.grid(row=1,column =1,pady=2)
btn_3.grid(row=1,column =2,pady=2)

btn_4.grid(row=2,column =0,pady=2)
btn_5.grid(row=2,column =1,pady=2)
btn_6.grid(row=2,column =2,pady=2)

btn_7.grid(row=3,column =0,pady=2)
btn_8.grid(row=3,column =1,pady=2)
btn_9.grid(row=3,column =2,pady=2)

btn_0.grid(row=4,column =0,pady=2)
btn_clear.grid(row=4,column=1,columnspan=2,pady=2)

btn_div.grid(row=5,column=0,pady=2)
btn_mul.grid(row=5,column=1,pady=2)

btn_sum.grid(row=6,column=0,pady=2)
btn_sub.grid(row=6,column=1,pady=2)
btn_equal.grid(row=5,rowspan=2,column=2,pady=2)

db.grid(row=0,column=0,padx=10, columnspan=3, pady=10)

root.mainloop()