from turtle import forward, circle, setpos, penup, pendown, done, speed, home, right, left
from math import  asin, pi

speed(10) 

penup() #Pen up to avoid a line.
setpos(0,-330) #Lowering the start point of the drawing, for better visibility.
pendown() 


def calculator(): #Defining the calculator function, this function is going to generate a list of 3 different values that will be used to graph the crop circles.
    list_radius1 = []
    for x in range(0, 7):

        radius1 = 150*(0.7**x)     #My outer circles will be decreasing at a rate of 0.7
        list_radius1.append(radius1)
    
    list_angle1 = []    #Creating empty lists.
    list_angle_tilt= []
    
    for x in range(0, 7):   #For the value 0 up until 7, the following for loop occurs.
        if x == 0:      #This is an exception, since I am start from the top, i only need to devide by 2. This is because if I go straight up, I am directly encountering the center of my circle, unlike the other cases where I encounter the side of a circle.
            angle1 = asin((list_radius1[x]/2)/285)*(180/pi)*2     #Using (180/pi) to convert radians to degrees
            list_angle1.append(angle1)      #Adding the result to a list, building a list that I will use later on to draw my circles with
            
            angle_tilt = angle1/2
            list_angle_tilt.append(angle_tilt) 
            
        if x > 0:
            angle1 = asin((list_radius1[x]/2)/285)*(180/pi)*4 
            list_angle1.append(angle1)
            
            angle_tilt = angle1/2       #This value corresponds to the tilt my circles have to do in order to touch eachother and overlap slightly.
            list_angle_tilt.append(angle_tilt) 
    
    list_angle_total = [] 
    
    for item in range(0,7):
        angle_total = my_sum(list_angle1[0:(item+1)]) #Summing all of the previous angles together for each index. That becomes my new angle value. This is done because I later reset turtle facing straight up every time.
        list_angle_total.append(angle_total) #Append to add items to the new list.
 
    list_radius = list_radius1[1:]  #I don't need the first value for the drawing of the outer circle as I drew the largest circle first and ''manually''.
    list_angle = list_angle_total
    list_tilt = list_angle_tilt
    
    return list_radius, list_angle, list_tilt


def my_sum(list_to_sum):    #Defining a sum function, this function will aid me when adding up all of the angle values together.
    total = 0
    for item in list_to_sum:
        total += item
    return total    
    
    

def innerCircles():     #Defining my inner circles function.
    for x in range(1,2):    #My second circle is twice the radius of my first one.
        circle(15*x) 
    for x in range(2,14):   #I found the number 14 by doing 7*2 because there are 7 circles.
        if x % 2 == 0:  #If the number is even, a circle is drawn, if it is odd, nothing is drawn.
            circle(15*x) 
        else:
            pendown()    #This does nothing.

innerCircles()   #This calls my function and runs it.



def outerCirclesLeft():     #Defining my outer circles function.
    
    penup()
    setpos(0,(-330+570-150))   #I am returning to the center of my guiding circle, which has a 285 radius.
    pendown()
    circle(150)    #This is my first and largest outer circle, it's also a reference point.
    

    for x in range(0,6):
        radius = list_radius[x]
        angle = list_angle[x]
        tilt = list_tilt[x]
        
        penup()
        setpos(0,(-330+285))    #The turtle is being repositioned at the center
        left(90)    #Turtle is in standard mode, meaning the right side corresponds to 0 degrees, to face up, it must go left 90 degrees.
        left(angle)
        forward(285) 
        left(tilt)  #I am turning left to a void a gap that would happen otherwise
        
        pendown()
        circle(radius)      #Different circles are drawn for each value present in my list_radius
        
        right(tilt)     #Undo-ing
        right(90)   #Undo-ing
        right(angle)    #Undo-ing
        
        
def outerCirclesRight():    #Defining my outer circles function.
    right(180)
    penup()
    setpos(0,(-330+570-150))    #I am returning to the center of my guiding circle, which has a 285 radius.
    pendown()
    
    for x in range(0,6):    #For each value, from 0 to 6, a circle is drawn using the following values:
        radius = list_radius[x] #These are the values used to draw my circles
        angle = list_angle[x]
        tilt = list_tilt[x]
        
        penup()
        setpos(0,(-330+285))     #The turtle is being repositioned at the center
        right(90)       #Turtle is in standard mode, meaning the right side corresponds to 0 degrees, to face up, it must go left 90 degrees.
        right(angle)
        forward(285)
        right(tilt+180)  #I am turning left to a void a gap that would happen otherwise
        
        pendown()
        circle(radius)  #Different circles are drawn for each value present in my list_radius
        
        left(tilt+180)   #Undo-ing
        left(90)    #Undo-ing
        left(angle)     #Undo-ing       
    done()      #The crop circles drawing is complete! Thanks turtle c:
        
        
list_radius, list_angle, list_tilt = calculator()

outerCirclesLeft() 
outerCirclesRight()     #Running my functions
