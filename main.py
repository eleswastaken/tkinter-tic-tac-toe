from tkinter import Tk, Label, Entry, Button, PhotoImage

window = Tk()
window.title('Tic-Tac-Toe FuckUp')
window.minsize(width=400, height=400)
window.config(padx=50, pady=50)

# turn is first player's
turn = 'first'
# prepare X and O images, so it won't get garbaged in the process
oimage = PhotoImage(file='images/o.png')
ximage = PhotoImage(file='images/x.png')

# define all win possibilities. #in the future write an algorithm searching by pattern#
sets = [
    {1,4,7},
    {2,5,8},
    {3,6,9},
    {1,2,3},
    {4,5,6},
    {7,8,9},
    {1,5,9},
    {3,5,7}
]

# in case of the DRAW; to be able to check if the number of moves has been exeeded
times = 0

activated_squares = []

# create list to disable all buttons later in case of player wins
buttons = []

# player_moves to compare later with the win_moves 
f_moves = []
s_moves = []

# button objects at the corners
corners = []

def check_win(player):
    global times
    # get hold of every win_situation
    times += 1
    if times == 9:
        label.config(text='DRAW!', fg='red')
        pass
    for win in sets:
        # either first or second
        if player == 'first':
            # check if the intersection of the win_set and player_moves_set 
            # is bigger than 3, which means 3 images got in the right positions
            if len(win.intersection(set(f_moves))) >= 3:
                label.config(text='FIRST WINS!', fg='green')
                # disable all buttons imitating victory
                for button in buttons:
                    button['state'] = 'disabled'
        else:
            # check if the intersection of the win_set and player_moves_set 
            # is bigger than 3, which means 3 images got in the right positions
            if len(win.intersection(set(s_moves))) >= 3:
                label.config(text='SECOND WINS!', fg='green')
                # disable all buttons imitating victory
                for button in buttons:
                    button['state'] = 'disabled'

def check_win_comb():
    for win in sets:
        if len(win.intersection(set(s_moves))) > 1:
            third_sq = int(str(win-set(s_moves))[1])
            button = buttons[third_sq-1]
            if button not in activated_squares:
                button.config(image=oimage, width=100, height=100)
                button.grid()
                s_moves.append(int(button._name))
                button['state'] = 'disabled'

def comp_block_move():
    for win in sets:
        if len(win.intersection(f_moves)) >= 2:
            third_sq = int(str(win - set(f_moves))[1])
            button = buttons[third_sq-1]
            button.config(image=oimage, width=100, height=100)
            button.grid()
            s_moves.append(int(button._name))
            button['state'] = 'disabled'
            return True

def comp_move():
    # if len(corners) > 0:
    if len(f_moves) >= 2:
        comp_block_move()
    elif len(s_moves) >= 2 and comp_block_move():
        check_win_comb()
    else:
        corners[0].config(image=oimage, width=100, height=100)
        corners[0].grid()
        s_moves.append(int(corners[0]._name))
        activated_squares.append(corners[0])
        corners[0]['state'] = 'disabled'
        corners.remove(corners[0])


def press(button):
    # create two lists of moves of players, so i could check the intersection
    f_moves.append(int(button._name))
    # change the image and put it to its coordinates
    button.config(image=ximage, width=100, height=100)
    button.grid()
    # change the state of the button, so it won't be pressed
    button['state'] = 'disabled'
    # check for active buttons
    activated_squares.append(button)
    if button in corners:
        corners.remove(button)
    check_win('first')

    comp_move()
    check_win('second')


# defining all buttons and getting them functioning
label = Label(text='First to go!', font=('Arial', 15))
label.grid(column=0, row=3, columnspan=3)
right_image = PhotoImage(file='images/sq.png', width=100, height=100)
button1 = Button(name='1',image=right_image, highlightthickness=0, command=lambda: press(button1))
button1.grid(column=0, row=0)
buttons.append(button1)
corners.append(button1)
button2 = Button(name='2',image=right_image, highlightthickness=0, command=lambda: press(button2))
button2.grid(column=0, row=1)
buttons.append(button2)
button3 = Button(name='3',image=right_image, highlightthickness=0, command=lambda: press(button3))
button3.grid(column=0, row=2)
buttons.append(button3)
corners.append(button3)
button4 = Button(name='4',image=right_image, highlightthickness=0, command=lambda: press(button4))
button4.grid(column=1, row=0)
buttons.append(button4)
button5 = Button(name='5',image=right_image, highlightthickness=0, command=lambda: press(button5))
button5.grid(column=1, row=1)
buttons.append(button5)
button6 = Button(name='6',image=right_image, highlightthickness=0, command=lambda: press(button6))
button6.grid(column=1, row=2)
buttons.append(button6)
button7 = Button(name='7',image=right_image, highlightthickness=0, command=lambda: press(button7))
button7.grid(column=2, row=0)
buttons.append(button7)
corners.append(button7)
button8 = Button(name='8',image=right_image, highlightthickness=0, command=lambda: press(button8))
button8.grid(column=2, row=1)
buttons.append(button8)
button9 = Button(name='9',image=right_image, highlightthickness=0, command=lambda: press(button9))
button9.grid(column=2, row=2)
buttons.append(button9)
corners.append(button9)


window.mainloop()