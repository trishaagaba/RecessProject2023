import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0,tk.END)
    entry.insert(tk.END, current + str(number))

    def button_clear():
        entry.delete(0, tk.END)

    def button_equal():
        expression = entry.get()
        try:
            result = eval(expression)
            entry.delete(0,tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0,tk.END)
            entry.insert(tk.END, "Error detected")

# For the main window to be seen by the user
mainwindow = tk.Tk()
mainwindow.title("Trisha's Simple Calculator")

# For an entry field
entry = tk.Entry(mainwindow,width=30)
entry.grid(row=0, column=0,columnspan= 5)

# Buttons for the different numbers and operators
button1 = tk.Button(mainwindow, text='1',padx=20, pady=10,command=lambda:
                    button_click(1))
button2 = tk.Button(mainwindow, text='2',padx=20, pady=10,command=lambda:
                    button_click(2))
button3 = tk.Button(mainwindow, text='3',padx=20, pady=10,command=lambda:
                    button_click(3))
button4 = tk.Button(mainwindow, text='4',padx=20, pady=10,command=lambda:
                    button_click(4))
button5 = tk.Button(mainwindow, text='5',padx=20, pady=10,command=lambda:
                    button_click(5))
button6 = tk.Button(mainwindow, text='6',padx=20, pady=10,command=lambda:
                    button_click(6))
button7 = tk.Button(mainwindow, text='7',padx=20, pady=10,command=lambda:
                    button_click(7))
button8 = tk.Button(mainwindow, text='8',padx=20, pady=10,command=lambda:
                    button_click(8))
button9 = tk.Button(mainwindow, text='9',padx=20, pady=10,command=lambda:
                    button_click(9))
button0 = tk.Button(mainwindow, text='0',padx=20, pady=10,command=lambda:
                    button_click(0))

buttonadd = tk.Button(mainwindow, text='+',padx=20, pady=10,command=lambda:
                    button_click("+"))
buttonsubtract = tk.Button(mainwindow, text='-',padx=20, pady=10,command=lambda:
                    button_click("-"))
buttonmultiply = tk.Button(mainwindow, text='*',padx=20, pady=10,command=lambda:
                    button_click("*"))
buttondivide = tk.Button(mainwindow, text='/',padx=20, pady=10,command=lambda:
                    button_click("/"))
buttonclear = tk.Button(mainwindow, text='C',padx=20, pady=10,command=buttonclear)
buttonequal = tk.Button(mainwindow, text='=',padx=20, pady=10,command= buttonequal)

# Putting the buttons on a right position on the grid
button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)

button0.grid(row=4,column=1)

buttonadd.grid(row=1,column=3)
buttonsubtract.grid(row=2,column=3)
buttonmultiply.grid(row=3,column=3)
buttondivide.grid(row=4,column=3)
buttonclear.grid(row=4,column=0)
buttonequal.grid(row=4,column=2)

# start the loop of the main event
mainwindow.mainloop()



