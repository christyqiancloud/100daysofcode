from turtle import *
# import another_module
# print(another_module.another_varible)

myscreen = Screen()
color('pink')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
# end_fill()
ming = Turtle()
print(ming)
ming.setpos(100,10)
ming.shape('turtle')
ming.color('DarkSeaGreen3')

myscreen.exitonclick()