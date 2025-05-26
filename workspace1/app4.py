#!/usr/bin/env python3
print('--------------------------------')
print('clases')
print('--------------------------------')
print('--------------------------------')
print('clases: vehiculos')
print('--------------------------------')

class vehicle:
    def __init__(self,maker,model):
        self.maker=maker
        self.model=model
    def printmessage(self):
        return(f'the maker is {self.maker}, the model is {self.model}')

class car(vehicle):
    def __init__(self,maker,model,doors):
        super().__init__(maker,model)
        self.doors=doors
    def infoprint(self):
        return(f'the maker is {self.maker}, the model is {self.model} and has {self.doors} doors')
        

class truck(vehicle):
    def __init__(self,maker,model,weight):
        super().__init__(maker,model)
        self.weight=weight

    def infoprint(self):
        return(f'the maker is {self.maker}, the model is {self.model} and has {self.weight} weight')
    

vehicleobject=vehicle('generic','model tx')
carobject=car('toyota', 'yaris',3)
truckobject=truck('hino','gh',120)

print(vehicleobject.printmessage())
print(carobject.infoprint())
print(truckobject.infoprint())

print('--------------------------------')
print('clases: libros')
print('--------------------------------')

print('--------------------------------')
print('--------------------------------')