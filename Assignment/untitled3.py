import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
x=np.linspace(0,10,1000)
plt.plot(x,np.sin(x),color='black')
plt.xlabel('x',size=30,color='green')
plt.ylabel('y',size=30,color='green')
plt.title('Sine-wave',size=30)