# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from walk import Radomwalk
''' input_value=list(range(1,1001))
squares=[x**3 for x in input_value]
plt.plot(input_value,squares,linewidth=5) '''
while True:
    rw=Radomwalk(5000)
    rw.fill_walk()
    plt.title('我是标题,do u know')
    pointNumbers=list(range(rw.num_points))
    plt.scatter(0,0,c='green',s=200)    
    plt.scatter(rw.x_values[-1],rw.y_vaules[-1],s=200,c='red')
    #plt.scatter(rw.x_values,rw.y_vaules,s=1,edgecolors=None,c=pointNumbers,cmap=plt.cm.Blues)

    plt.plot(rw.x_values,rw.y_vaules,linewidth=1)
#plt.tick_params(axis='both',which='major',labelsize=14)
#plt.axis([0,1100,0,1110110])
    plt.axes().get_xaxis().set_visible(False)
    plt.show()

    keep_running=input('输入q去中止')
    if keep_running == 'q':
        break