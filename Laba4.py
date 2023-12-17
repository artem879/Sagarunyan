import numpy as np

def create_out(y, x, k):
    out = 0
    for i in range(len(y[k])):  
        out += (y[k][i] * x[i])
    return out;

y1 = [1,0,1,0]
y2 = [1,1,1,0]              
y3 = [0,0,1,1]
y4 = [1,1,0,0]                        

y = np.array([y1,y2,y3,y4])     
x = np.array([0,0,0,0])         

k = 0
g = 0
flag = 0
while (flag < 4):
    flag = 0                     
    while k > 3:                
        k -= 4

    
    out = create_out(y, x, k)           
    
    if (k in (0,1) and out <= 0):
        x = np.add(x, y[k])              
    if (k in (2, 3) and out >= 0):
        x = np.add(x, -y[k])
   
    print ("Cледующий шаг")
    print(out)
    print(k)
    
    k += 1
    g += 1

    for i in range(4):
        if (i in [0, 1]) and (create_out(y, x, i) > 0):
            flag += 1                                               
        if (i in [2, 3]) and (create_out(y, x, i) < 0):
            flag += 1

    

print (" x = " + str(x))
print(" за " + str(g) + " шагов")
