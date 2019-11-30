from __future__ import division
import scipy as sci
import scipy.special as sp
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm, colors

def spherharm(l,m):
    PHI, THETA = np.mgrid[0:2*np.pi:200j, 0:np.pi:100j] #arrays of angular variables
    R = np.abs(sp.sph_harm(m, l, PHI, THETA)) #Array with the absolute values of Ylm
    #Now we convert to cartesian coordinates
    # for the 3D representation
    X = R * np.sin(THETA) * np.cos(PHI)
    Y = R * np.sin(THETA) * np.sin(PHI)
    Z = R * np.cos(THETA)
        
    N = R/R.max()    # Normalize R for the plot colors to cover the entire range of colormap.
    fig, ax = plt.subplots(subplot_kw=dict(projection='3d'), figsize=(10,8))
    im = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, facecolors=cm.jet(N))
    ax.set_title(r'$|Y^2_ 4|$', fontsize=20)
    m = cm.ScalarMappable(cmap=cm.jet)
    m.set_array(R)    # Assign the unnormalized data array to the mappable
    #so that the scale corresponds to the values of R
    fig.colorbar(m, shrink=0.8);
    fig.show()
    return fig



