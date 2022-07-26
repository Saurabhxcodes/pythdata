'''from turtle import *


speed('slowest')
pencolor('red')
bgcolor('black')
pensize(10)
side = 12
size =200

begin_fill()
fillcolor('green')
for i in range(side):
    fd(size)
    lt(360/size)
    rt(100)


end_fill()
mainloop() '''


from turtle import *


speed('slowest')
pencolor('red')
bgcolor('black')
pensize(10)
side=2

begin_fill()
fillcolor('green')
for i in range(side):
    fd(50)
    lt(90)
    fd(50)
    rt(90)
    



end_fill()
mainloop()