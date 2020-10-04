'''
Author: Sofia Gutierrez
Lab #1: The purpose of this lab is to draw a series of figures using recursion
'''

import numpy as np
import matplotlib.pyplot as plt
import math

def draw_squares(ax,n,p,w):
    if n > 0:
        ax.plot(p[:,0],p[:,1],linewidth=0.5,color='k') #draws out first square
        i1 = [1,2,3,0,1]
        q = p*(1-w) + p[i1]*w  
        draw_squares(ax,n-1,q,w)

################################ ################################

def circle(center,rad):
    # Returns the coordinates of the points in a circle given center and radius
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def draw_four_circles(ax,n,center,rad):
    if n > 0:
        x,y = circle(center,rad)
        ax.plot(x,y,linewidth=0.5,color='k')
        draw_four_circles(ax,n-1,[center[0],center[1]+rad],rad/2)
        draw_four_circles(ax,n-1,[center[0],center[1]-rad],rad/2)
        draw_four_circles(ax,n-1,[center[0]+rad,center[1]],rad/2)
        draw_four_circles(ax,n-1,[center[0]-rad,center[1]],rad/2)

################################ ################################

def draw_circles(ax,n,center,rad,w):
    if n > 0:
        x, y = circle(center, rad)
        ax.plot(x, y, color='k')
        rad = rad * .7
        center = [0,0]
        draw_circles(ax,n-1,center,rad,w)

################################ ################################

def ilum(ax,n,p):
    if n > 0:
        ax.plot(p[:,0],p[:,1],linewidth=0.5,color='k')
        #point 1
        p1a = ((p[0][0]+p[1][0])/2)
        p1b = ((p[0][1]+p[1][1])/2)
        #point 2
        p2a = ((p[1][0]+p[2][0])/2)
        p2b = ((p[1][1]+p[2][1])/2)
        #point 3
        p3a = ((p[2][0]+p[3][0])/2)
        p3b = ((p[2][1]+p[3][1])/2)
        #point 4
        p4a = p1a
        p4b = p1b
        
        new_p = np.array([[p1a,p1b],[p2a,p2b],[p3a,p3b],[p4a,p4b]])
        ilum(ax,n-1,new_p)

################################ ################################

def draw_triangle_grid(ax,n,p):
    if n > 0:
        ax.plot(p[:,0],p[:,1],linewidth=0.5,color='k')
        #point 1
        p1a = ((p[0][0]+p[1][0])/2)
        p1b = ((p[0][1]+p[1][1])/2)
        #point 2
        p2a = ((p[1][0]+p[2][0])/2)
        p2b = ((p[1][1]+p[2][1])/2)
        #point 3
        p3a = ((p[2][0]+p[3][0])/2)
        p3b = ((p[2][1]+p[3][1])/2)
        #point 4
        p4a = p1a
        p4b = p1b
        
        new_p1 = np.array([[p1a,p1b],[p2a,p2b],[p3a,p3b],[p4a,p4b]])
        draw_triangle_grid(ax,n-1,new_p1)

################################ ################################

def squares(ax,center,w):
    mid = w / 2
    x = np.array([[center[0] - mid, center[1] + mid], [center[0] + mid, center[1] + mid],
                 [center[0] + mid, center[1] - mid], [center[0] - mid, center[1] - mid],
                 [center[0] - mid, center[1] + mid]])
    ax.plot(x[:,0],x[:,1],linewidth=0.5,color='k')

def draw_square_pattern(ax,center,n,w):
    mid = w / 2
    if n > 0:
        squares(ax,center,w)
        p1 = [center[0] - mid, center[1] + mid]
        p2 = [center[0] + mid, center[1] + mid]
        p3 = [center[0] + mid, center[1] - mid]
        p4 = [center[0] - mid, center[1] - mid]
        
        draw_square_pattern(ax,p1,n-1,w/2)
        draw_square_pattern(ax,p2,n-1,w/2)
        draw_square_pattern(ax,p3,n-1,w/2)
        draw_square_pattern(ax,p4,n-1,w/2)

################################ ################################

def upsidedown_tree(ax,n,mainL,x,y):
    if n > 0:
        right = [mainL[0] + x, mainL[1] - y]
        left = [mainL[0] - x, mainL[1] - y]
        ax.plot([mainL[0],left[0]],[mainL[1],left[1]],[mainL[0],right[0]],[mainL[1],right[1]],linewidth=0.5,color='k')
        upsidedown_tree(ax,n-1,right, x/2, y*0.9)
        upsidedown_tree(ax,n-1,left, x/2, y*0.9)

################################ ################################

def tree(ax,n,mainL,x,y):
    if n > 0:
        right = [mainL[0] + x, mainL[1] + y]
        left = [mainL[0] - x, mainL[1] + y]
        ax.plot([mainL[0],left[0]],[mainL[1],left[1]],[mainL[0],right[0]],[mainL[1],right[1]],linewidth=0.5,color='k')
        tree(ax,n-1,right,x/2,y)
        tree(ax,n-1,left,x/2,y)
        
        #x array and y array
        #x cos
        #y sin
        #left and right branch
        #parameters will include starting angle

################################ ################################

if __name__ == "__main__":  
    
    plt.close("all") #Close all figures
    
    ###################### ######################
    
    orig_size = 1000.0
    p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
    print('Points in original square:')
    print(p)
    
    fig, ax = plt.subplots() #figure, axis
    draw_squares(ax,6,p,.1)
    ax.set_aspect(1.0)
    #ax.axis('off')
    plt.show()
    fig.savefig('squaresa.png')
    
    fig, ax = plt.subplots()
    draw_squares(ax,10,p,.2)
    ax.set_aspect(1.0)
    #ax.axis('off')
    plt.show()
    fig.savefig('squaresb.png')
    
    fig, ax = plt.subplots()
    draw_squares(ax,5,p,.3)
    ax.set_aspect(1.0)
    #ax.axis('off')
    plt.show()
    fig.savefig('squaresc.png')
    
    ###################### ######################
    
    fig, ax = plt.subplots() 
    draw_four_circles(ax, 2, [0,0], 100)
    ax.set_aspect(1.0)
    #ax.axis('off')
    plt.show()
    fig.savefig('four_circlesa.png')
    
    fig, ax = plt.subplots() 
    draw_four_circles(ax, 3, [0,0], 100)
    ax.set_aspect(1.0)
    #ax.axis('off')
    plt.show()
    fig.savefig('four_circlesb.png')
    
    fig, ax = plt.subplots() 
    draw_four_circles(ax, 4, [0,0], 100)
    ax.set_aspect(1.0)
    #ax.axis('off')
    plt.show()
    fig.savefig('four_circlesc.png')
    
    ###################### ######################
    
    mainL = np.array([0, 0])
    
    fig, ax = plt.subplots()
    upsidedown_tree(ax,4,mainL,150,40)
    ax.set_aspect(1.0)
    ax.axis('off')
    plt.show()
    fig.savefig('treea.png')
    
    fig, ax = plt.subplots()
    upsidedown_tree(ax,5,mainL,150,40)
    ax.set_aspect(1.0)
    ax.axis('off')
    plt.show()
    fig.savefig('treeb.png')
    
    fig, ax = plt.subplots()
    upsidedown_tree(ax,6,mainL,150,40)
    ax.set_aspect(1.0)
    ax.axis('off')
    plt.show()
    fig.savefig('treec.png')
    
    ###################### ######################
        
    fig, ax = plt.subplots()
    draw_square_pattern(ax, [0, 0], 2, 10)
    ax.set_aspect(1.0)
    #ax.axis('off')
    plt.show()
    fig.savefig('draw_square_patterna.png')
    
    fig, ax = plt.subplots()
    draw_square_pattern(ax, [0, 0], 3, 10)
    ax.set_aspect(1.0)
    #ax.axis('off')
    plt.show()
    fig.savefig('draw_square_patternb.png')
    
    fig, ax = plt.subplots()
    draw_square_pattern(ax,[0, 0], 4, 10)
    ax.set_aspect(1.0)
    #ax.axis('off')
    plt.show()
    fig.savefig('draw_square_patternc.png')
    
    ###################### ######################
    
    fig, ax = plt.subplots()
    draw_circles(ax, 3, [0, 0], 50, 5)
    ax.set_aspect(1.0)
    #ax.axis('off')
    plt.show()
    fig.savefig('circlea.png')
    
    fig, ax = plt.subplots()
    draw_circles(ax, 6, [0, 0], 50, 5)
    ax.set_aspect(1.0)
    ax.axis('off')
    plt.show()
    fig.savefig('circleb.png')
    
    fig, ax = plt.subplots()
    draw_circles(ax, 9, [0, 0], 50, 5)
    ax.set_aspect(1.0)
    ax.axis('off')
    plt.show()
    fig.savefig('circlec.png')

    ###################### ######################
    
    p = np.array([[0,0],[500,1000],[1000,0],[0,0]])
    #p2 = np.array([[250,500],[750,500],[500,0],[250,500]])
    #p3 = np.array([[625,250],[375,250],[500,500],[625,250]])
    
    #print("testing: ",(p[1]+p[2])/2)
    #print((p[0]+p[1])/2)
    #print((p[0]+p[2])/2)
    #print((p[1]+p[2])/2)
    
    fig, ax = plt.subplots()
    ilum(ax,3,p)
    ax.set_aspect(1.0)
    #ax.axis('off')
    plt.show()
    fig.savefig('trianglesa.png')
    
    fig, ax = plt.subplots()
    ilum(ax,5,p)
    ax.set_aspect(1.0)
    #ax.axis('off')
    plt.show()
    fig.savefig('trianglesb.png')
    
    fig, ax = plt.subplots()
    ilum(ax,6,p)
    ax.set_aspect(1.0)
    #ax.axis('off')
    plt.show()
    fig.savefig('trianglesc.png')
    
    ###################### ######################
    
    p = np.array([[0,0],[500,1000],[1000,0],[0,0]])
    
    fig, ax = plt.subplots()
    draw_triangle_grid(ax,1,p)
    ax.set_aspect(1.0)
    #ax.axis('off')
    plt.show()
    fig.savefig('triangle_grida.png')
    
    fig, ax = plt.subplots()
    draw_triangle_grid(ax,2,p)
    ax.set_aspect(1.0)
    #ax.axis('off')
    plt.show()
    fig.savefig('triangle_gridb.png')
    
    fig, ax = plt.subplots()
    draw_triangle_grid(ax,7,p)
    ax.set_aspect(1.0)
    #ax.axis('off')
    plt.show()
    fig.savefig('triangle_gridc.png')
    
    ###################### ######################
    
    mainL = np.array([0, 0])
    
    fig, ax = plt.subplots()
    tree(ax,4,mainL,150,40)
    ax.set_aspect(1.0)
    ax.axis('off')
    plt.show()
    fig.savefig('treeea.png')
    
    fig, ax = plt.subplots()
    tree(ax,5,mainL,150,40)
    ax.set_aspect(1.0)
    ax.axis('off')
    plt.show()
    fig.savefig('treeeb.png')
    
    fig, ax = plt.subplots()
    tree(ax,6,mainL,150,40)
    ax.set_aspect(1.0)
    ax.axis('off')
    plt.show()
    fig.savefig('treeec.png')