from display import *

def draw_line(x0, y0, x1, y1, screen, color):
    # make sure everything is an integer
    x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)

    # check steepness (replaces x with y if the slope is steep)
    steep = abs(y1 - y0) > abs(x1 - x0)
    if steep:
        x0, y0 = y0, x0
        x1, y1 = y1, x1

    # reordering (make sure A is positive)
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    A = x1 - x0
    B = y1 - y0

    # increment for y
    sB = 1

    # flip slope
    if B < 0:
        sB = -sB
        B = abs(B)

    D = 2*B - A

    # not necessary but neat
    y = y0

    # iterate
    for x in range(x0, x1 + 1):

        # plot depending on steepness
        if steep:
            plot(screen, color, y, x)
        else:
            plot(screen, color, x, y)

        if D > 0:
            y += sB
            D -= 2*A # effectively D += 2* (B - A)
        D += 2*B

    pass