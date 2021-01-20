from tkinter import Tk, Label, Entry, Button, PhotoImage

window = Tk()
window.title('Tic-Tac-Toe FuckUp')
window.minsize(width=400, height=400)
window.config(padx=50, pady=50)

turn = 'first'
ximage = PhotoImage(file='images/x.png')
oimage = PhotoImage(file='images/o.png')

def press(arg):
    global turn
    if turn == 'first':
        arg.config(image=ximage, width=100, height=100)
        arg.grid()
        arg['state'] = 'disabled'
        turn = 'second'
    elif turn == 'second':
        arg.config(image=oimage, width=100, height=100)
        arg.grid()
        arg['state'] = 'disabled'
        turn = 'first'

right_image = PhotoImage(file='images/sq.png', width=100, height=100)
button1 = Button(image=right_image, highlightthickness=0, command=lambda: press(button1))
button1.grid(column=0, row=0)
button2 = Button(image=right_image, highlightthickness=0, command=lambda: press(button2))
button2.grid(column=0, row=1)
button3 = Button(image=right_image, highlightthickness=0, command=lambda: press(button3))
button3.grid(column=0, row=2)
button4 = Button(image=right_image, highlightthickness=0, command=lambda: press(button4))
button4.grid(column=1, row=0)
button5 = Button(image=right_image, highlightthickness=0, command=lambda: press(button5))
button5.grid(column=1, row=1)
button6 = Button(image=right_image, highlightthickness=0, command=lambda: press(button6))
button6.grid(column=1, row=2)
button7 = Button(image=right_image, highlightthickness=0, command=lambda: press(button7))
button7.grid(column=2, row=0)
button8 = Button(image=right_image, highlightthickness=0, command=lambda: press(button8))
button8.grid(column=2, row=1)
button9 = Button(image=right_image, highlightthickness=0, command=lambda: press(button9))
button9.grid(column=2, row=2)


window.mainloop()