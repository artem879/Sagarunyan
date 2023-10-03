import numpy as np
import matplotlib.pyplot as plt
from math import pi
import random

class TREUGOLNIC:
    """creates TREUGOLNIC based on the data provided in the \
            class_data.conf"""
    def __init__(self, x, y, x1, y1, x2, y2):
        self.x_batch = []
        self.y_batch = []
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.batch_size = 6
        self.gen_class()

    def gen_class(self):
        for i in range(self.batch_size):
            s, t = sorted([random.random(), random.random()])
            u = 1 - t
            x = u * self.x + t * (u * self.x1 + t * self.x2)
            y = u * self.y + t * (u * self.y1 + t * self.y2)
            self.x_batch.append(x)
            self.y_batch.append(y)

    def get_batch_data(self):
        return self.x_batch, self.y_batch 

    def get_class_data(self):
        return self.x, self.y, self.x1 , self.y1, self.x2, self.y2 

def draw_triangle(points): 
    x = [point[0] for point in points]
    y = [point[1] for point in points]
    
    x.append(x[0])
    y.append(y[0])  
    plt.plot(x, y) 
 
    print((x,y))

classes = []
colors = ['cyan', 'blue', 'purple', 'red', 'gray']

try:
    with open('class_data.conf','r') as data:
        counter = 0
        for line in data:
            values=line.split(' ')
            values[len(values)-1]=values[len(values)-1].replace('\n','')
            x, y, x1, y1, x2, y2 = [float(values[i]) for i in range(len(values))]
            classes.append(TREUGOLNIC(x,y,x1,y1,x2,y2))
            counter+=1
                 
except FileNotFoundError:
    print('File not found! Manual data input...\n')
    counter = int(input('Class quantity = '))
    for i in range(counter):
        print('Class '.join(str(counter+1)).join('\n'))
        x = float(input('x = '))
        y = float(input('y = '))
        x1 = float(input('x1 = '))
        y1 = float(input('y1 = '))
        x2 = float(input('x2 = '))
        y2 = float(input('y2 = '))
        classes.append(TREUGOLNIC(x,y,x1,y1,x2,y2))


result = open('data_batch.conf', 'w')
for i in range(counter):
    x_dat, y_dat = classes[i].get_batch_data()
    x,y,x1,y1,x2,y2 = classes[i].get_class_data()
    result.write("Class %s\n" % (i+1,))
    result.write("Class Info: %s, %s, %s, %s, %s, %s\n" % (x,y,x1,y1,x2,y2))
    for j in range(len(x_dat)):
        result.write("%s, %s; " % (x_dat[j],y_dat[j]))
    result.write('\n')
    plt.scatter(x_dat, y_dat, c=colors[i])
    draw_triangle([(x,y),(x1,y1),(x2,y2)])
result.close()

plt.grid(color='lightgray', linestyle='--')
plt.show()
