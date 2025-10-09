
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def plotsquare(C, half_width, color):
    """
    Plot a square centered at C with given half-width and color.
    
    Parameters:
    C: list or array with [x, y] coordinates of center
    half_width: half of the side length of the square
    color: color specification (e.g., 'w' for white, 'r' for red)
    """
    ax = plt.gca()
    square = patches.Rectangle(
        (C[0] - half_width, C[1] - half_width),
        2 * half_width,
        2 * half_width,
        facecolor=color,
        edgecolor=color
    )
    ax.add_patch(square)


def sierp_carpet(C, L, it):
    if (it <= 0):
        return
    
    plotsquare(C, L/2, 'w')
    
    plotsquare([C[0]-L/3, C[1]-L/3], L/6, 'r')
    sierp_carpet([C[0]-L/3, C[1]-L/3], L/3, it-1)
    
    plotsquare([C[0], C[1]-L/3], L/6, 'r')
    sierp_carpet([C[0], C[1]-L/3], L/3, it-1)
    
    plotsquare([C[0]+L/3, C[1]-L/3], L/6, 'r')
    sierp_carpet([C[0]+L/3, C[1]-L/3], L/3, it-1)
    
    
    plotsquare([C[0]+L/3, C[1]], L/6, 'r')
    sierp_carpet([C[0]+L/3, C[1]], L/3, it-1)
    
    
    
    plotsquare([C[0]+L/3, C[1]+L/3], L/6, 'r')
    sierp_carpet([C[0]+L/3, C[1]+L/3], L/3, it-1)
    
    plotsquare([C[0], C[1]+L/3], L/6, 'r')
    sierp_carpet([C[0], C[1]+L/3], L/3, it-1)
    
    plotsquare([C[0]-L/3, C[1]+L/3], L/6, 'r')
    sierp_carpet([C[0]-L/3, C[1]+L/3], L/3, it-1)
    
    plotsquare([C[0]-L/3, C[1]], L/6, 'r')
    sierp_carpet([C[0]-L/3, C[1]], L/3, it-1)
    
    plt.axis('off')
    
    

# plotsquare([C[0]/2, 3*C[1]/2], L/3, 'w')
# plotsquare([3*C[0]/2, C[1]/2], L/3, 'w')
# plotsquare([3*C[0]/2, 3*C[1]/2], L/3, 'w')


plt.close('all')
plt.figure()
sierp_carpet([0, 0], 1, 5)
plt.axis('equal')
plt.show()


