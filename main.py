import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
label = tk.Label(root, text="Tkinter Calculator", fg="#FF8000")
label.pack()

expression = ""

input_text = tk.StringVar()

def click_btn(number):
    global expression
    expression += str(number)
    input_text.set(expression)


def clear_btn():
    global expression
    expression = ""
    input_text.set(expression)


def equal_btn():
    global expression
    result =  eval(expression)
    input_text.set(result)
    expression = ""


frame = tk.Frame(root, width=400)
frame.pack(padx=6, pady=3)

input_field = tk.Entry(frame, textvariable=input_text, width=25, font=("Arial", 32), bg="#123", fg="#fff")
input_field.pack()


btn_frame = tk.Frame(root, width=400,)
btn_frame.pack()
    


clear_button = tk.Button(btn_frame, text="Clear", command=lambda: clear_btn(), width=15, height=3, bg="#123", fg="#fff").grid(row=0, column=0)

invert_button = tk.Button(btn_frame, text="+/-", width=15, height=3, bg="#123", fg="#fff").grid(row=0, column=1)

button_seven = tk.Button(btn_frame, text="7", command=lambda: click_btn(7), width=15, height=3, bg="#FF8000", fg="#fff").grid(row=1, column=0)

button_eight = tk.Button(btn_frame, text="8", command=lambda: click_btn(8), width=15, height=3, bg="#FF8000", fg="#fff").grid(row=1, column=1)

button_nine = tk.Button(btn_frame, text="9", command=lambda: click_btn(9), width=15, height=3, bg="#FF8000", fg="#fff").grid(row=1, column=2)

button_four = tk.Button(btn_frame, text="4", command=lambda: click_btn(4), width=15, height=3, bg="#FF8000", fg="#fff").grid(row=2, column=0)

button_five = tk.Button(btn_frame, text="5", command=lambda: click_btn(5), width=15, height=3, bg="#FF8000", fg="#fff").grid(row=2, column=1)

button_six = tk.Button(btn_frame, text="6", command=lambda: click_btn(6), width=15, height=3, bg="#FF8000", fg="#fff").grid(row=2, column=2)

button_one = tk.Button(btn_frame, text="1", command=lambda: click_btn(1), width=15, height=3, bg="#FF8000", fg="#fff").grid(row=3, column=0)

button_two = tk.Button(btn_frame, text="2", command=lambda: click_btn(2), width=15, height=3, bg="#FF8000", fg="#fff").grid(row=3, column=1)

button_three = tk.Button(btn_frame, text="3", command=lambda: click_btn(3), width=15, height=3, bg="#FF8000", fg="#fff").grid(row=3, column=2)

button_equal = tk.Button(btn_frame, text="=", command=lambda: equal_btn(), width=15, height=3, bg="#123", fg="#fff").grid(row=4, column=2)

button_zero = tk.Button(btn_frame, text="0", command=lambda: click_btn(0), width=15, height=3, bg="#FF8000", fg="#fff").grid(row=4, column=0)

button_plus = tk.Button(btn_frame, text="+", command=lambda: click_btn("+"), width=15, height=3, bg="#123", fg="#fff").grid(row=3, column=3)

button_minus = tk.Button(btn_frame, text="-", command=lambda: click_btn("-"), width=15, height=3, bg="#123", fg="#fff").grid(row=2, column=3)

button_delit = tk.Button(btn_frame, text="/", command=lambda: click_btn("/"), width=15, height=3, bg="#123", fg="#fff").grid(row=0, column=2,)

button_umnojit = tk.Button(btn_frame, text="*", command=lambda: click_btn("*"), width=15, height=3, bg="#123", fg="#fff").grid(row=1, column=3)

button_zapitaya = tk.Button(btn_frame, text=",", command=lambda: click_btn(","), width=15, height=3, bg="#123", fg="#fff").grid(row=4, column=1)


root.mainloop()