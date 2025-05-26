#!/usr/bin/env python3
print('--------------------------------')
print('area triangulo area cuadrado')
print('--------------------------------')

# def computeAreasquare(side):
#     return side*side

# def computerAreaCircle(radius):
#     pi=3.1415
#     return pi*radius**2

# print(f'the area of an square with side 3cm is {computeAreasquare(3)}')

# print(f'the area of an circle with radius 3cm is {computerAreaCircle(3):.2f}')


class geometry:
    pi=3.1415
    def __init__(self,side,radius):
        self.side=side
        self.radius=radius
        print('the object was crate successfully')
    
    def area(self):
        squarearea=self.side*self.side
        circlearea=geometry.pi*self.radius**2
        return[squarearea,circlearea]


areasquarecircle=geometry(3,3)
result=list()
result=areasquarecircle.area()
print(len(result))
print(f'the area of the square and circle are: {result[0]},{result[1]:.2f}')

print('--------------------------------')
print('rectangulo')
print('--------------------------------')

class rectangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
        print('objeto creado')
    
    def arear(self):
        arearectangulo=self.base*self.altura
        return[arearectangulo]
    
areares=rectangulo(5,4)
respuesta=areares.arear()
print(f'respuesta {respuesta}')


print('--------------------------------')
print('student')
print('--------------------------------')
import statistics
class Student:
    def __init__(self,name,grades):
        self.name=name
        self.grades=grades
    
    def avrg_grade(self):
        scoore=statistics.mean(self.grades)
        return scoore

wilmerStudent=Student('wilmer',[5,6,4.5,10])
millerStudent=Student('miller',[7,5.5,7.5,10])
eddyStudent=Student('eddy',[7,10,8.5,10])

print(f'the score of wilmer is {wilmerStudent.avrg_grade():.2f}')
print(f'the score of miller is {millerStudent.avrg_grade():.2f}')
print(f'the score of eddy is {eddyStudent.avrg_grade():.2f}')

print('--------------------------------')