import numpy as np
import matplotlib.pyplot as pt

def plotVector2D(x,y):                                                
    pt.rcParams["figure.figsize"] = [10,10]
    pt.rcParams["figure.autolayout"] = True
    data = np.array([0,0,x,y])
    pt.figure() 
    ax = pt.gca() 
    ax.quiver(*data,angles='xy',scale_units='xy',scale=1,color='blue') 
    ax.set_xlim([-1,10])
    ax.set_ylim([-1,10])
    pt.draw()
    pt.show()

def plotVector3D(data):                      #This function will plot x,y,z as a vector in 3d plane.
    fig = pt.figure()
    ax = pt.axes(projection='3d')
    ax.set_xlim([-1,10])
    ax.set_ylim(-10,10)
    ax.set_zlim([0,10])
    start = [0,0,0]
    ax.quiver(start[0],start[1],start[2],data[0],data[1],data[2])
    pt.show()