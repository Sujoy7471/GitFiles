import numpy as np
import matplotlib.pyplot as plt

##initial position
x = 0.5
y = 0.2
##initial velocity
vx = 0.05554624495
vy = 0.03846116546
##number variables
n = 300                                                         ##Variable that controls number of iterations
##direction variables
dir_x = 1
dir_y = 1
##Trail
trail_x = [x]
trail_y = [y]


plt.figure()
for i in range(n):
    if x >= 0.925 or x <= -0.925:
        dir_x = -1*dir_x                                        ##Changing the x direction

    if y >= 0.95 or y <= -0.925:
        dir_y = -1*dir_y                                        ##Changing the y direction

    x = x + vx*dir_x                                            ##Update x co-ordinate
    y = y + vy*dir_y                                            ##Update y co-ordinate


    ##Print position
    if x <0: 
        print(f"x_position:{x:0.4f}       y_position: {y:0.4f}")
    if x >0:
        print(f"x_position: {x:0.4f}       y_position: {y:0.4f}")

    plt.clf()

    ##Trail adding
    trail_x.append(x)
    trail_y.append(y)
    if len(trail_x) > 10:
        trail_x = trail_x[-10:]
        trail_y = trail_y[-10:]
    plt.plot(trail_x, trail_y, ls='',marker = 'o', ms = 10, mfc = 'red', color='black', alpha=0.1)

    plt.title(f"Motion of a Ball in a rigid box in the horizontall plane")
    ##Plotting the ball
    plt.plot(x,y,marker='o',ms = 10, mfc = 'red', color = 'black')
    ##Box
    plt.vlines(x=1, ymin=-1.01, ymax=1.01, color='k', ls='-', linewidth=4)
    plt.hlines(y=1, xmin=-1.01, xmax=1.01, color='k', ls='-', linewidth=4)
    plt.vlines(x=-1, ymin=-1.01, ymax=1.01, color='k', ls='-', linewidth=4)
    plt.hlines(y=-1, xmin=-1.01, xmax=1.01, color='k', ls='-', linewidth=4)
    plt.xlim([-1.1,1.1])
    plt.ylim([-1.1,1.1])
    ##Time interval adjustment
    plt.pause(0.01)

plt.show()
