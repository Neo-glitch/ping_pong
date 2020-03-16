from tkinter import *
import random
import time

counter = 0
counter1 = 0

root = Tk()
root.title('Ping_Pong')
root.resizable(0, 0)
root.wm_attributes('-topmost', 1)
drawingpad = Canvas(root, width=500, height=400, bd=0, highlightthickness = 0)
drawingpad.config(bg='black')
drawingpad.pack()
root.update()

drawingpad.create_line(250, 0, 250, 400, fill='white')


class Ball:
    def __init__(self, drawingpad, color, paddle, paddle1):
        self.drawingpad = drawingpad
        self.paddle = paddle
        self.paddle1 = paddle1
        self.id= drawingpad.create_oval(10, 10, 25, 25, fill=color)
        self.drawingpad.move(self.id, 235, 200)
        start = [-5, 5]
        random.shuffle(start)
        self.x= start[0]
        self.y= -5
        self.drawingpad_height = 400
        self.drawingpad_width = 500



    def draw(self):
        self.drawingpad.move(self.id, self.x, self.y)
        pos = self.drawingpad.coords(self.id)
        if pos[1] <= 0:
            self.y = 5
        if pos[3] >= self.drawingpad_height:
            self.y = -5
        if pos[0] <= 0:
            self.x = 5
            self.score(True)

        if pos[2] >= self.drawingpad_width:
            self.x = -5
            self.score(False)

        if self.hit_paddle(pos) == True:
            self.x = 5
        if self.hit_paddle1(pos) == True:
            self.x = -5


#****code block for the score
    def score(self, value):
        global counter
        global counter1

        if value == True:
            w = self.drawingpad.create_text(125, 40, text = counter, font =('Aral', 60), fill ='white')
            drawingpad.itemconfig(w, fill='black')
            counter += 1
            w = self.drawingpad.create_text(125, 40, text=counter, font=('Aral', 60), fill='white')

        if value == False:
            w = self.drawingpad.create_text(375, 40, text=counter1, font=('Aral', 60), fill='white')
            drawingpad.itemconfig(w, fill='black')
            counter1 += 1
            w = self.drawingpad.create_text(375, 40, text=counter1, font=('Aral', 60), fill='white')

    def hit_paddle(self, pos):
        paddle_pos = self.drawingpad.coords(self.paddle.id)
        if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[0] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                return True
            return False

    def hit_paddle1(self, pos):
        paddle_pos = self.drawingpad.coords(self.paddle1.id)
        if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[2] >= paddle_pos[0] and pos[2] <= paddle_pos[2]:
                return True
            return False


class Paddle:
    def __init__(self, drawingpad, color):
        self.drawingpad = drawingpad
        self.id = drawingpad.create_rectangle(0, 150, 30, 250, fill=color)
        self.y = 0
        self.drawingpad_height = self.drawingpad.winfo_height
        self.drawingpad_width = self.drawingpad.winfo_width
        self.drawingpad.bind_all('w', self.Turn_Left)
        self.drawingpad.bind_all('s', self.Turn_Right)


    def draw(self):
        self.drawingpad.move(self.id, 0, self.y)
        pos = self.drawingpad.coords(self.id)
        if pos[1] <= 0:
            self.y=0
        if pos[3] >= 400:
            self.y = 0

    def Turn_Left(self, event):
        self.y = -5

    def Turn_Right(self, event):
        self.y = 5

class Paddle1:
    def __init__(self, drawingpad, color):
        self.drawingpad = drawingpad
        self.id = drawingpad.create_rectangle(470, 150, 500, 250, fill=color)
        self.draeingpad_height = self.drawingpad.winfo_height
        self.drawingpad_width = self.drawingpad.winfo_width
        self.y = 0
        self.drawingpad.bind_all('<KeyPress-Up>', self.Move_Up)
        self.drawingpad.bind_all('<KeyPress-Down>', self.Move_Down)


    def draw(self):
        self.drawingpad.move(self.id, 0, self.y)
        pos = self.drawingpad.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= 400:
            self.y = 0

    def Move_Up(self, event):
        self.y = -5

    def Move_Down(self, event):
        self.y = 5



paddle = Paddle(drawingpad, 'blue')
paddle1 = Paddle1(drawingpad, 'red')
ball = Ball(drawingpad, 'orange', paddle, paddle1)


while 1:
    ball.draw()
    paddle.draw()
    paddle1.draw()
    if counter == 2:
        ball.x = 0
        ball.y = 0
        paddle.y = 0
        drawingpad.create_text(250, 200, text = 'Congrats Player 1! You win', font = 32, fill = 'red')
        drawingpad.create_text(250, 215, text = 'Score:' + str(counter) + '.' + str(counter1), font=32, fill = 'red')

    if counter1 == 2:
        ball.x = 0
        ball.y = 0
        paddle.y = 0
        drawingpad.create_text(250, 200, text = 'Congrats Player 2! You win', font = 32, fill = 'red')
        drawingpad.create_text(250, 215, text = 'Score:' + str(counter) + '.' + str(counter1), font=32, fill = 'red')

    root.update_idletasks()
    root.update()
    time.sleep(0.05)
# **** code block to end the game***
    if counter == 2 or counter1 == 2:
        time.sleep(10000)





























#root.mainloop()





























