import math

f = open('data_batch.conf', 'r')
k = 0
points = []
for line in f:
    line.replace("\n", "")
    if k % 4 == 0:
        l = line.split(' ')
        cn = int(l[-1].replace("\n", ""))
        if cn == 2: cn = -1
    elif k % 4 == 3:
        l = line.split(';') 
        for i in range(len(l)-1):
            l1 = l[i][0:-2]
            l2 = l1.split(',')
            if cn == -1:
                l2[0] = float(l2[0]) * (-1)
                l2[1] = float(l2[1]) * (-1)
            points.append([float(l2[0]), float(l2[1]), int(cn)])
    k += 1

x = []
y = []

for i in range(len(points)):
    if points[i][2] == 1:
        x.append([points[i][0], points[i][1]])
    else:
        y.append([points[i][0], points[i][1]])

def Metrica_Ev(x, y):
    rast = []
    for i in range(len(x)):
        rast.append(math.sqrt(sum([(x[i][j] - y[i][j])**2 for j in range(len(x[i]))])))
    return rast
print("Evklid ")
print(Metrica_Ev(x, y))
print("\n")

def Metrica_Manh(x, y):
    rast = []
    for i in range(len(x)):
        rast.append(sum([abs(x[i][j] - y[i][j]) for j in range(len(x[i]))]))
    return rast
print("Manhattan ")
print(Metrica_Manh(x, y))
print("\n")

def Metrica_Ravno(x, y):
    rast = []
    for i in range(len(x)):
        rast.append(max(x[i][j] - y[i][j] for j in range(len(x[i]))))
    return rast
print("Ravnomern ")
print(Metrica_Ravno(x, y))
print("\n")

def Metrica_Mink(x, y):
    rast = []
    for i in range(len(x)):
        rast.append((sum([(x[i][j] - y[i][j])**5 for j in range(len(x[i]))]))**(1/5))
    return rast

print("Minkovsk ")
print(Metrica_Mink(x, y))
print("\n")
