from __future__ import division
import scipy as sci
import scipy.special as sp
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm, colors


def real(l,m):
    PHI, THETA = np.mgrid[0:2*np.pi:200j, 0:np.pi:100j]
    R = sp.sph_harm(m, l, PHI, THETA).real
    
    X = R * np.sin(THETA) * np.cos(PHI)
    Y = R * np.sin(THETA) * np.sin(PHI)
    Z = R * np.cos(THETA)
    
    #As R has negative values, we'll use an instance of Normalize
    #see http://stackoverflow.com/questions/25023075/normalizing-colormap-used-by-facecolors-in-matplotlib
    norm = colors.Normalize()
    fig, ax = plt.subplots(subplot_kw=dict(projection='3d'), figsize=(10,8))
    m = cm.ScalarMappable(cmap=cm.jet)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, facecolors=cm.jet(norm(R)))
    ax.set_title('real$(Y^2_ 4)$', fontsize=20)
    m.set_array(R)
    fig.colorbar(m, shrink=0.8);
    fig.show()
    return fig

