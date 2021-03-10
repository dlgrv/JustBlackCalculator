from tkinter import *
from decimal import *

root = Tk()
root.title('Calculator by dlgrv')
root["bg"] = '#000000'
root.resizable(width=False, height=False)


# МАССИВ С КНОПКАМИ
buttons_list = [
    ['7', '8', '9', '+'],
    ['4', '5', '6', '-'],
    ['1', '2', '3',  '*'],
    ["0", ".", "=",  '/']
]

def output_window():
    Label(root, text='', font='Courier 12', fg='#ffffff', bg='#000000').grid(row=0, column=0, columnspan=5)
    Label(root, text='Hello word', font='Courier 30', fg='#ffffff', bg='#000000').grid(row=1, column=0, columnspan=5)
    Label(root, text='', font='Courier 12', fg='#ffffff', bg='#000000').grid(row=2, column=0, columnspan=5)


def draw_buttons():
    counter_x = 1
    counter_y = 3
    size_btn_x = 30
    size_btn_y = 30
    for btn_y in buttons_list:
        for btn_x_y in btn_y:
            btn = Button(text=btn_x_y,
                         background='#000000',
                         foreground='#ffffff',
                         padx=str(size_btn_x),
                         pady=str(size_btn_y),
                         font='Courier 20')
            btn.grid(row=counter_y, column=counter_x)
            counter_x += 1
        counter_x = 1
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
output_window()
draw_buttons()
root.mainloop()