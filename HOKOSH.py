import numpy as np
import matplotlib.pyplot as plt

def kashyap(X, y, a=0.1, max_iter=10000):
    X = np.hstack([X, np.ones((X.shape[0], 1))]) 
    w = np.zeros(X.shape[1]) 
    b = 0

    for i in range(max_iter):
        z = np.dot(X, w) + b
        e = y - np.sign(z)
        w += a * np.dot(X.T, e)             
        b += a * np.sum(e)

        if np.all(np.abs(e) < 1e-6):    
            break

    return w, b

n_samples = 10
n_features = 5
X = np.random.rand(n_samples, n_features) * 10 - 5
y = np.random.choice([-1, 1], size=n_samples)              

w, b = kashyap(X, y)

print("Weight vector:", w)      
print("Bias term:", b)          


plt.scatter(X[:, 0], X[:, 1], c=y)
x1 = np.linspace(-5, 5, 100)
x2 = -(w[0] * x1 + b) / w[1]            
plt.plot(x1, x2)
plt.show()
