# coding:utf-8
 
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
 
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
 
plt.figure() # 实例化作图变量
plt.title('single variable') # 图像标题
plt.xlabel('x') # x轴文本
plt.ylabel('y') # y轴文本
plt.axis([30, 400, 100, 400])
plt.grid(True) # 是否绘制网格线
 
X = [[07],[17],[27],[37], [47],[57],[69],[77], [87],[97], [107], [117], [127],[137],[147], [157], [167],[177],[187],[198],[202], [217], [227], [237], [247], [257], [267], [277]]       
     
y = [[1.5223], [1.5223], [1.5203], [1.5203], [1.5203],[1.5203],[1.5223], [1.5223], [1.5201], [1.5201], [1.5201], [1.5201],[1.5201],[1.5201],[1.521], [1.521],[1.521], [1.521],  [1.5211],   [1.5211],  [1.5211], [1.5211],[1.5211], [1.522], [1.522],         [1.5223],         [1.5223],         [1.5223]]

X_test = [[287]] # 用来做最终效果测试
y_test = [[1.5223]] # 用来做最终效果测试
plt.plot(X, y, 'k.')
 
model = LinearRegression()
model.fit(X, y)
X2 = [[287]]
y2 = model.predict(X2)
plt.plot(X2, y2, 'g-')
 
xx = np.linspace(30, 400, 100) # 设计x轴一系列点作为画图的x点集
quadratic_featurizer = PolynomialFeatures(degree=2) # 实例化一个二次多项式特征实例
X_train_quadratic = quadratic_featurizer.fit_transform(X) # 用二次多项式对样本X值做变换
xx_quadratic = quadratic_featurizer.transform(xx.reshape(xx.shape[0], 1)) # 把训练好X值的多项式特征实例应用到一系列点上,形成矩阵
regressor_quadratic = LinearRegression() # 创建一个线性回归实例
regressor_quadratic.fit(X_train_quadratic, y) # 以多项式变换后的x值为输入，代入线性回归模型做训练
plt.plot(xx, regressor_quadratic.predict(xx_quadratic), 'r-') # 用训练好的模型作图
 
print '一元线性回归 r-squared', model.score(X_test, y_test)
X_test_quadratic = quadratic_featurizer.transform(X_test)
print '二次回归     r-squared', regressor_quadratic.score(X_test_quadratic, y_test)
 
plt.show() # 展示图像