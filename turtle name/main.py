import turtle

t = turtle.Turtle()
t.penup()
t.goto(0,200)
t.pendown()
t.color('green')
style = ('Courier',60,'italic')
t.write('KHUSH',font=style,align='left',move=True)
t.hideturtle()


turtle.done()
