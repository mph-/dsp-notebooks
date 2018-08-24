# M. P. Hayes UCECE

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from ipywidgets import interact

@interact(n=(1000,2000))
def plot_test2(n=1000):
    ts = pd.Series(np.random.randn(n), index=pd.date_range('1/1/2000', periods=n))
    ts = ts.cumsum()
    ts.plot()
    plt.show()
    

