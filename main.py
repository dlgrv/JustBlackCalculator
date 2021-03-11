from tkinter import *
from decimal import *

root = Tk()
root.title('Calculator by dlgrv')
root["bg"] = '#000000'
root.resizable(width=False, height=False)

buttons_list = [
    ['7', '8', '9', '+'],
    ['4', '5', '6', '-'],
    ['1', '2', '3',  '*'],
    ["0", ".", "=",  '/']
]

global stack
stack = ['', '', '']
global result
result = '0'
global output_text
output_text = Label(root, text='', font=f'Courier 35', fg='#ffffff', bg='#000000')
output_text.grid(row=1, column=0, columnspan=5)

def draw_buttons():
    counter_x = 1
    counter_y = 3
    size_btn_x = 30
    size_btn_y = 30
    for btn_y in buttons_list:
        for btn_x_y in btn_y:
            com = lambda x=btn_x_y: logicalc(x)
            btn = Button(text=btn_x_y,
                         background='#000000',
                         foreground='#ffffff',
                         padx=str(size_btn_x),
                         pady=str(size_btn_y),
                         font='Courier 20',
                         command=com)
            btn.grid(row=counter_y, column=counter_x)
            counter_x += 1
        counter_x = 1
        counter_y += 1

def output_update():
    global output_text
    global result
    Label(root, text='', font='Courier 12', fg='#ffffff', bg='#000000').grid(row=0, column=0, columnspan=5)
    Label(root, text='', font='Courier 12', fg='#ffffff', bg='#000000').grid(row=2, column=0, columnspan=5)
    result = str(result)
    if len(result) <= 13:
        font_size = 35
    elif len(result) <= 16:
        font_size = 30
    else:
        font_size = 25
    output_text.config(text=result, font = f'Courier {font_size}')

def logicalc(operation):
    global stack
    global result
    if operation.isdigit() or operation == '.':
        if stack[1] == '' and len(stack[0]) < 9:
            if operation.isdigit():
                stack[0] += operation
            elif operation == '.':
                if stack[0] != '':
                    stack[0] += '.'
                elif stack[0] == '':
                    stack += '0.'
        if stack[1] != '' and len(stack[2]) < 9:
            if operation.isdigit():
                stack[2] += operation
            elif operation == '.':
                if stack[2] != '':
                    stack[2] += '.'
                elif stack[2] == '':
                    stack += '0.'
    elif operation in ['+', '-', '*', '/']:
        if operation == '-' and stack[0] == '':
            stack[0] += '-'
        else:
            stack[1] = operation
    result = stack[0] + stack[1] + stack[2]
    if operation == '=' and (stack[0] != '' and stack[1] != '' and stack[2] != ''):
        calculate()
    output_update()

def calculate():
    global stack
    global result
    operand_2 = Decimal(stack.pop())
    operation = stack.pop()
    operand_1 = Decimal(stack.pop())
    stack = ['', '', '']
    if operation == '+':
        result = operand_1 + operand_2
    elif operation == '-':
        result = operand_1 - operand_2
    elif operation == '*':
        result = operand_1 * operand_2
    elif operation == '/':
        result = operand_1 / operand_2

output_update()
draw_buttons()
root.mainloop()