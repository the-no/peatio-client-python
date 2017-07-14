import matplotlib.pyplot as plt  
import numpy as np  
import scipy as sp  
from scipy.stats import norm  
from sklearn.pipeline import Pipeline  
from sklearn.linear_model import LinearRegression  
from sklearn.preprocessing import PolynomialFeatures  
from sklearn import linear_model  
  
#x = np.arange(0, 1, 0.002)
#y = norm.rvs(0, size=500, scale=0.1)  
#y = y + x**2  
s = [07,  17, 27, 37, 47,57, 69, 77,87, 97,107,117,127,137,147,157,167,177,197,198,202,217,227,237,247,257,267,277,287] 
d = [1.5223, 1.5223, 1.5203, 1.5203, 1.5203, 1.5203, 1.5223, 1.5223, 1.5201, 1.5201, 1.5201, 1.5201, 1.5201, 1.5201, 1.521, 1.521, 1.521, 1.521, 1.5211, 1.5211, 1.5211, 1.5211, 1.5211, 1.522, 1.522, 1.5223, 1.5223, 1.5223, 1.5223]
x = np.array(s) 
y = np.array(d) 

def rmse(y_test, y):  
    return sp.sqrt(sp.mean((y_test - y) ** 2))  
  
def R2(y_test, y_true):  
    return 1 - ((y_test - y_true)**2).sum() / ((y_true - y_true.mean())**2).sum()  
  
  
def R22(y_test, y_true):  
    y_mean = np.array(y_true)  
    y_mean[:] = y_mean.mean()  
    return 1 - rmse(y_test, y_true) / rmse(y_mean, y_true)  
  

plt.scatter(x, y, s=5)  
degree = [1,2,5]  
y_test = []  
y_test = np.array(y_test)  
  
  
for d in degree:  
    clf = Pipeline([('poly', PolynomialFeatures(degree=d)),  
                    ('linear', LinearRegression(fit_intercept=False))])  
    clf.fit(x[:, np.newaxis], y)  
    y_test = clf.predict(x[:, np.newaxis])  
  
    print(clf.named_steps['linear'].coef_)  
    print('rmse=%.2f, R2=%.2f, R22=%.2f, clf.score=%.2f' %  
      (rmse(y_test, y),  
       R2(y_test, y),  
       R22(y_test, y),  
       clf.score(x[:, np.newaxis], y)))
      # clf.score(x, y)))        
      
    plt.plot(x, y_test, linewidth=2)  
      
plt.grid()  
plt.legend(['1','2','100'], loc='upper left')  
plt.show()  