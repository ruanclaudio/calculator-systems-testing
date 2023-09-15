# temp video 1:13:09
from tkinter import * # Importing GUI TKInter libary
from tkinter import ttk
import util
import math

window = Tk()
window.title("Calculator")
window.geometry('330x460')

all_values = '' # DEFINE VARIAVEL COMO STRING VAZIA
# CREATE FUNCIOTION
def add_values(event_value):
    global all_values # KEPT AS A GLOBAL VARIABLE
    
    if event_value == '':
        all_values = all_values[:-1]
    elif event_value == '%':
        all_values += '({}/100)*100'.format(all_values)
    elif event_value == '√':
        all_values = 'math.sqrt({})'.format(all_values)
    elif event_value == '1/x':
        all_values = '1/({})'.format(all_values)
    elif event_value == '±':
        last_number = find_last_number(all_values)
        if last_number:
            if last_number.startswith('-'):
                all_values = all_values[:-len(last_number)] + last_number[1:]
            else:
                all_values = all_values[:-len(last_number)] + '-' + last_number
    else:
        all_values = all_values + str(event_value)
    
    text_value.set(all_values)
    
def find_last_number(expression):
    # Função para encontrar o último número na expressão
    tokens = expression.split()
    for token in reversed(tokens):
        if token.isdigit() or (token.startswith('-') and token[1:].isdigit()) or (token.count('.') == 1 and token.replace('.', '').isdigit()):
            return token
    return None
    
def calculate():
    try:
        global all_values # KEPT AS A GLOBAL VARIABLE
        
        all_values = all_values.replace('x','*')
        all_values = all_values.replace('÷','/')
        all_values = all_values.replace('²','**2')
        result = eval(all_values)
        text_value.set(str(result))
        if '**' in all_values:
            text_value.set('ERROR')
        if '*-+' in all_values:
            text_value.set('ERROR')
        if '*+-' in all_values:
            text_value.set('ERROR')
        else:
            result = eval(all_values)
            text_value.set(result)
    except SyntaxError:
        text_value.set('ERROR')
    except ZeroDivisionError:
        text_value.set('Impossível dividir por 0')

def clear_screen():
    global all_values # KEPT AS A GLOBAL VARIABLE
    
    all_values = ""
    text_value.set("")
    
    
# CREATE FRAMES
frame_screen = Frame(window, width=330, height=80, borderwidth=2, relief="solid", bg=util.color_dark)
frame_screen.grid(row=0, column=0)

frame_body = Frame(window,width=330, height=400, bg=util.color_dark)
frame_body.grid(row=1, column=0)

# CREATE LABEL
text_value = StringVar()
screen_label = Label(frame_screen, textvariable=text_value, width=18, height=3, padx=11, relief=FLAT, anchor="e", justify=RIGHT, font=("Ivy", 21, "bold"))
screen_label.place(x=0, y=0)

# CREATE BUTTONS
# LINE 1
b_1 = Button(frame_body, command= lambda:add_values('%'), text="%", width=6, height=2, fg=util.color_white, bg=util.color_lightdark, font=("Ivy", 13, "bold"))
b_1.place(x=3, y=3)
b_2 = Button(frame_body, command= clear_screen, text="CE", width=6, height=2, fg=util.color_white, bg=util.color_lightdark, font=("Ivy", 13, "bold"))
b_2.place(x=88, y=3)
b_3 = Button(frame_body, command= clear_screen, text="C", width=6, height=2, fg=util.color_white, bg=util.color_lightdark, font=("Ivy", 13, "bold"))
b_3.place(x=173, y=3)
b_4 = Button(frame_body, command= lambda:add_values(''), text="⌫", width=6, height=2, fg=util.color_white, bg=util.color_lightdark, font=("Ivy", 13, "bold"))
b_4.place(x=258, y=3)

# LINE 2
b_5 = Button(frame_body, command= lambda:add_values('1/x'), text="1/x", width=6, height=2, fg=util.color_white, bg=util.color_lightdark, font=("Ivy", 13, "bold"))
b_5.place(x=3, y=67)
b_6 = Button(frame_body, command= lambda:add_values('²'), text="x²", width=6, height=2, fg=util.color_white, bg=util.color_lightdark, font=("Ivy", 13, "bold"))
b_6.place(x=88, y=67)
b_7 = Button(frame_body, command= lambda:add_values('√'), text="²√x", width=6, height=2, fg=util.color_white, bg=util.color_lightdark, font=("Ivy", 13, "bold"))
b_7.place(x=173, y=67)
b_8 = Button(frame_body, command= lambda:add_values('÷'), text="÷", width=6, height=2, fg=util.color_white, bg=util.color_lightdark, font=("Ivy", 13, "bold"))
b_8.place(x=258, y=67)

# LINE 3
b_9 = Button(frame_body, command= lambda:add_values('7'), text="7", width=6, height=2, fg=util.color_white, bg=util.color_lightdark2, font=("Ivy", 13, "bold"))
b_9.place(x=3, y=131)
b_10 = Button(frame_body, command= lambda:add_values('8'), text="8", width=6, height=2, fg=util.color_white, bg=util.color_lightdark2, font=("Ivy", 13, "bold"))
b_10.place(x=88, y=131)
b_11 = Button(frame_body, command= lambda:add_values('9'), text="9", width=6, height=2, fg=util.color_white, bg=util.color_lightdark2, font=("Ivy", 13, "bold"))
b_11.place(x=173, y=131)
b_12 = Button(frame_body, command= lambda:add_values('x'), text="X", width=6, height=2, fg=util.color_white, bg=util.color_lightdark, font=("Ivy", 13, "bold"))
b_12.place(x=258, y=131)

# LINE 4
b_13 = Button(frame_body, command= lambda:add_values('4'), text="4", width=6, height=2, fg=util.color_white, bg=util.color_lightdark2, font=("Ivy", 13, "bold"))
b_13.place(x=3, y=195)
b_14 = Button(frame_body, command= lambda:add_values('5'), text="5", width=6, height=2, fg=util.color_white, bg=util.color_lightdark2, font=("Ivy", 13, "bold"))
b_14.place(x=88, y=195)
b_15 = Button(frame_body, command= lambda:add_values('6'), text="6", width=6, height=2, fg=util.color_white, bg=util.color_lightdark2, font=("Ivy", 13, "bold"))
b_15.place(x=173, y=195)
b_16 = Button(frame_body, command= lambda:add_values('-'), text="-", width=6, height=2, fg=util.color_white, bg=util.color_lightdark, font=("Ivy", 13, "bold"))
b_16.place(x=258, y=195)

# LINE 5
b_17 = Button(frame_body, command= lambda:add_values('1'), text="1", width=6, height=2, fg=util.color_white, bg=util.color_lightdark2, font=("Ivy", 13, "bold"))
b_17.place(x=3, y=259)
b_18 = Button(frame_body, command= lambda:add_values('2'), text="2", width=6, height=2, fg=util.color_white, bg=util.color_lightdark2, font=("Ivy", 13, "bold"))
b_18.place(x=88, y=259)
b_19 = Button(frame_body, command= lambda:add_values('3'), text="3", width=6, height=2, fg=util.color_white, bg=util.color_lightdark2, font=("Ivy", 13, "bold"))
b_19.place(x=173, y=259)
b_20 = Button(frame_body, command= lambda:add_values('+'), text="+", width=6, height=2, fg=util.color_white, bg=util.color_lightdark, font=("Ivy", 13, "bold"))
b_20.place(x=258, y=259)

# LINE 6
b_21 = Button(frame_body, command= lambda:add_values('±'), text="±", width=6, height=2, fg=util.color_white, bg=util.color_lightdark2, font=("Ivy", 13, "bold"))
b_21.place(x=3, y=323)
b_22 = Button(frame_body, command= lambda:add_values('0'), text="0", width=6, height=2, fg=util.color_white, bg=util.color_lightdark2, font=("Ivy", 13, "bold"))
b_22.place(x=88, y=323)
b_23 = Button(frame_body, command= lambda:add_values('.'), text=".", width=6, height=2, fg=util.color_white, bg=util.color_lightdark2, font=("Ivy", 13, "bold"))
b_23.place(x=173, y=323)
b_24 = Button(frame_body, command= calculate, text="=", width=6, height=2, fg=util.color_white, bg=util.color_orange, font=("Ivy", 13, "bold"))
b_24.place(x=258, y=323)



window.mainloop()