from tkinter import *
from decimal import *

root = Tk()
root.title('Calculator by dlgrv')

# МАССИВ С КНОПКАМИ
buttons_list = [
    ['7', '8', '9', '+'],
    ['4', '5', '6', '-'],
    ['1', '2', '3',  '*'],
    ["0", ".", "=",  '/']
]
counter_x = 0
counter_y = 0
size_btn_x = 30
size_btn_y = 30
for btn_y in buttons_list:
    for btn_x_y in btn_y:
        btn = Button(text=btn_x_y,
                     background='#000000',
                     foreground='#ffffff',
                     padx=str(size_btn_x),
                     pady=str(size_btn_y),
                     font=('courier', 16))
        btn.grid(row=counter_y, column=counter_x)
        counter_x += 1
    counter_x = 0
    counter_y += 1

# ВВЕДЕНЫЕ ЧИСЛА И ОПЕРАЦИИ
stack = []

def calculate():
    global label
    global stack
    global result
    operand_2 = Decimal(stack.pop())
    operation = stack.pop()
    operand_1 = Decimal(stack.pop())

    # ВЫПОЛНЯЕМ ПОДСЧЕТЫ
    if operation == '+':
        result = operand_1 + operand_2
    elif operation == '-':
        result = operand_1 - operand_2
    elif operation == '*':
        result = operand_1 * operand_2
    elif operation == '/':
        result = operand_1 / operand_2

    # ППРИВОДИМ ЧИСЛО В КРАСИВЫЙ ВИД (ЕСЛИ ЦЕЛОЕ, ТО

root.mainloop()