import numpy as np
from scipy.interpolate import splev
from scipy.interpolate import splprep
from scipy import float64
import matplotlib.pyplot as plt
from hull_functions import hull, diameter


if __name__ == '__main__':
    # Create a hi-res sample spline. Start with some
    # low-res points and then resample at a higher
    # res.
    x = [0.0,  1.0,  2.0, 3.0, 2.0, 1.0, 0.0]
    y = [0.0, -1.0, -0.5, 0.0, 2.5, 1.2, 2.0]
    XY = np.array([x,y])
    tck, u = splprep(XY, s=0)

    fig, ax = plt.subplots()
    ax.plot(x,y,'o')
    
    dXY = splev(np.linspace(0, 1, 400), tck,der = 1)
    XY = splev(np.linspace(0, 1, 400), tck)

    DYDX = [dy/dx for dx,dy in zip(*dXY)]


    thickness = 0.1*0.1
    pX = [x+np.sign(dXY[0][ind])*DYDX[ind]*np.sqrt(thickness/(pow(DYDX[ind],2)+1)) for ind,x in enumerate(XY[0])]
    pY = [y-np.sign(dXY[0][ind])*np.sqrt(thickness/(pow(DYDX[ind],2)+1)) for ind,y in enumerate(XY[1])]

    
    (x1,y1),(x2,y2) = diameter(zip(pX,pY))
    print np.sqrt(pow(x2-x1,2)+pow(y2-y1,2))
    
    
    ax.plot(*XY)
    ax.plot(pX,pY)

    ax.axis('equal')
    ax.grid()
    plt.show()

