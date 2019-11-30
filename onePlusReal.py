from __future__ import division
import scipy as sci
import scipy.special as sp
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm, colors


def oneplusreal(l,m):
    PHI, THETA = np.mgrid[0:2*np.pi:300j, 0:np.pi:150j]
    R = sp.sph_harm(m, l, PHI, THETA).real
    
    s = 1
    X = (s*R+1) * np.sin(THETA) * np.cos(PHI)
    Y = (s*R+1) * np.sin(THETA) * np.sin(PHI)
    Z = (s*R+1) * np.cos(THETA)
    
    norm = colors.Normalize()
    fig, ax = plt.subplots(subplot_kw=dict(projection='3d'), figsize=(10,8))
    m = cm.ScalarMappable(cmap=cm.jet)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, facecolors=cm.jet(norm(R)))
    ax.set_title('1 + real$(Y^2_ 4)$', fontsize=20)
    m.set_array(R)
    fig.colorbar(m, shrink=0.8);
    fig.show()
    return fig
