
from tkinter import *

root = Tk()
root.title('zentience calculator')
def clear():
    db.delete(0, END) # clear method

def btn_clk(char):
    cur_num = db.get()
    clear()
    f_num = cur_num + char
    db.insert(0, f_num) # click method

def evaluate(expression):
    # Stack for numbers
    numbers = []
    # Stack for operators
    operators = []
    i = 0
    while i < len(expression):
        # Ignore whitespaces
        if expression[i] == ' ':
            i += 1
            continue
        # If current character is a digit, push it to numbers stack
        if expression[i].isdigit():
            num = 0
            # Extract the whole number
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            numbers.append(num)
            continue
# If current character is an operator
        if expression[i] in '+-*/':
# If precedence of current operator is less than or equal to precedence of the operator
# on top of stack, perform the calculation and push result to numbers stack
            while operators and precedence(operators[-1]) >= precedence(expression[i]):
                apply_operator(numbers, operators)
            operators.append(expression[i])
        elif expression[i] == '(':
            operators.append(expression[i])
        elif expression[i] == ')':
            while operators and operators[-1] != '(':
                apply_operator(numbers, operators)
            operators.pop()  # Remove '('
        i += 1
# Perform the remaining calculations
    while operators:
        apply_operator(numbers, operators)
    return numbers[-1]

def precedence(operator):
    if operator in '+-':
        return 1
    elif operator in '*/':
        return 2
    return 0

def apply_operator(numbers, operators):
    num2 = numbers.pop()
    num1 = numbers.pop()
    operator = operators.pop()
    if operator == '+':
        numbers.append(num1 + num2)
    elif operator == '-':
        numbers.append(num1 - num2)
    elif operator == '*':
        numbers.append(num1 * num2)
    elif operator == '/':
        if num2 == 0:
            raise ValueError("Division by zero!")
        numbers.append(num1 / num2)

def equal():
    expression = db.get()
    try:
        result = evaluate(expression) #params
        db.delete(0, END)
        db.insert(0, str(result))
    except Exception as e: #expection handling
        db.delete(0, END)
        db.insert(0, "Error")

# # Creating widgets
db = Entry(root,width=12,font=('Arial',28),justify=RIGHT)
# buttons
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
btn_div = Button(root,text ='/',padx =36,pady = 10,font=('Arial',14),command =lambda: btn_clk('/'))
btn_mul = Button(root,text ='*',padx =36,pady = 10,font=('Arial',14),command =lambda: btn_clk('*'))
btn_sum = Button(root,text ='+',padx =36,pady = 10,font=('Arial',14),command =lambda: btn_clk('+'))
btn_sub = Button(root,text ='-',padx =36,pady = 10,font=('Arial',14),command =lambda: btn_clk('-'))
btn_equal = Button(root,text ='=',padx=36,pady=60,font=('Arial',14),command=equal)
btn_op = Button(root,text = '(',padx=36,pady=10,font =('Arial',14),command= lambda: btn_clk('('))
btn_clo = Button(root,text = ')',padx=36,pady=10,font =('Arial',14),command=lambda: btn_clk(')'))

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
btn_equal.grid(row=5,rowspan=3,column=2,pady=2)

btn_op.grid(row=7,column=0,pady=2)
btn_clo.grid(row=7,column=1,pady=2)

db.grid(row=0,column=0,padx=10, columnspan=3, pady=10)
root.mainloop()



