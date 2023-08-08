# -*- coding: utf-8 -*-
"""
Vessel Simulator

@authors: Gabriela Copetti Maccagnan, Jean Schmith, Marcia Cunha dos Santos and Rodrigo Marques de Figueiredo
"""

# LIBRARIES
import numpy as np
import random
from numpy import ones, vstack
from numpy.linalg import lstsq
import math
from PIL import Image, ImageDraw, ImageFilter

def make_line(a, b, width):
    '''
    Returns the points for a line vessel.    

    Parameters
    ----------
    a : float
        Slope of the line.
    b : float
        Interceptor of the line.
    width : int
        The width in image of the vessel.

    Returns
    -------
    result : list
        The points of the line y = a*x + b.

    '''
    
    x = np.arange(width)
    y = np.arange(width)

    result = []
    for i in range(1, width):
        x[i] = i
        y[i] = a * x[i] + b
        result.append(tuple([x[i], y[i]]))

    return result


def make_line_v2(xys):
    '''
    Returns the points for a line vessel.

    Parameters
    ----------
    xys : list
        The start and the end of the line. Example: [(0,0),(10,10)].

    Returns
    -------
    result : list
        The points of the line between A and B.

    '''
    
    p_a, p_b = xys

    if p_b[0] != p_a[0]:
        width = abs(p_b[0] - p_a[0])
    else:
        width = abs(p_b[1] - p_a[1])

    x = np.arange(width)
    y = np.arange(width)
    points = [p_a, p_b]
    x_coords, y_coords = zip(*points)
    A = vstack([x_coords, ones(len(x_coords))]).T
    a, b = lstsq(A, y_coords)[0]

    result = []
    for i in range(0, width):
        if p_b[0] != p_a[0]:
            if p_a[0] < p_b[0]:
                x[i] = p_a[0] + i
                y[i] = a * x[i] + b
            else:
                x[i] = p_b[0] + i
                y[i] = a * x[i] + b
        else:
            x[i] = p_a[0]
            if (p_b[1] - p_a[1]) < 0:
                y[i] = p_a[1] + i
            else:
                y[i] = p_a[1] - i

        result.append(tuple([x[i], y[i]]))

    return result


def make_second_degree(xys, width):
    '''
    Returns the points for a second degree vessel.

    Parameters
    ----------
    xys : list
        Three points that intersects the second degree equation. Example: [(0,920),(700,1100),(1080,1920)].
    width : int
        The max width in image to start and to end the second degree vessel.

    Returns
    -------
    result : list
        The points of the second degree vessel.

    '''
    
    p_a, p_b, p_c = xys

    denom = (p_a[0] - p_b[0]) * (p_a[0] - p_c[0]) * (p_b[0] - p_c[0])
    a = (p_c[0] * (p_b[1] - p_a[1]) + p_b[0] * (p_a[1] - p_c[1]) + p_a[0] * (p_c[1] - p_b[1])) / denom
    b = (p_c[0] * p_c[0] * (p_a[1] - p_b[1]) + p_b[0] * p_b[0] * (p_c[1] - p_a[1]) + p_a[0] * p_a[0]
         * (p_b[1] - p_c[1])) / denom
    c = (p_b[0] * p_c[0] * (p_b[0] - p_c[0]) * p_a[1] + p_c[0] * p_a[0] * (p_c[0] - p_a[0]) * p_b[1] + p_a[0] *
         p_b[0] * (p_a[0] - p_b[0]) * p_c[1]) / denom

    x = np.arange(width)
    y = np.arange(width)

    result = []
    for i in range(p_a[0], p_c[0]):
        y[i] = (a * (x[i] ** 2)) + (b * x[i]) + c
        result.append(tuple([x[i], y[i]]))

    return result


def make_sine(xys, A, f, phi=0):
    '''
    Returns the points for a sine vessel.

    Parameters
    ----------
    xys : list
        The start and the end of the sine. Example: [(0,0),(100,0)].
    A : float
        Amplitude of the sine signal.
    f : float
        frequency of the sine signal.
    phi : float, optional
        Phase of the sine signal. The default is 0.

    Returns
    -------
    result : list
        The points of the sine vessel.

    '''
        
    p_a, p_b = xys

    if p_b[0] != p_a[0]:
        width = abs(p_b[0] - p_a[0])
    else:
        width = abs(p_b[1] - p_a[1])

    x = np.linspace(0, 1, width, endpoint=False)
    y = np.linspace(0, 1, width, endpoint=False)

    Fs = width  # sampling frequency
    Ts = 1.0 / Fs  # sampling period
    t = np.arange(0, 1, Ts)  # time vector
    t = t[:width]  # to guarantee the same size

    ysin = A * np.sin(2 * np.pi * f * t + phi)
    line = make_line_v2([p_a, p_b])

    result = []
    for i in range(0, len(t)):
        y[i] = (line[i][1] + ysin[i])
        x[i] = line[i][0]

        result.append([x[i], y[i]])

    return result


def make_bezier(xys):
    '''
    Returns the points for a bezier vessel.

    Parameters
    ----------
    xys : list
        Points for Bezier function.

    Returns
    -------
    result : list
        The points of the bezier vessel.
    '''
    
    # xys should be a sequence of 2-tuples (Bezier control points)
    n = len(xys)
    combinations = __pascal_row(n - 1)
    ts = [t / 300.0 for t in range(301)]

    # This uses the generalized formula for bezier curves
    # http://en.wikipedia.org/wiki/B%C3%A9zier_curve#Generalization
    result = []
    for t in ts:  # B(t)=(1-t)^(3) P0 + 3(1-t)^(2) t P1 + 3(1-t) t^(2) P2 + t^(3) P3
        tpowers = (t ** i for i in range(n))
        upowers = reversed([(1 - t) ** i for i in range(n)])
        coefs = [c * a * b for c, a, b in zip(combinations, tpowers, upowers)]
        result.append(
            tuple(sum([coef * p for coef, p in zip(coefs, ps)]) for ps in zip(*xys)))

    return result


def __pascal_row(n):
    # This returns the nth row of Pascal's Triangle
    # https://en.wikipedia.org/wiki/Pascal%27s_triangle
    result = [1]
    x, numerator = 1, n
    for denominator in range(1, n // 2 + 1):
        x *= numerator
        x /= denominator
        result.append(x)
        numerator -= 1
    if n & 1 == 0:
        result.extend(reversed(result[:-1]))
    else:
        result.extend(reversed(result))

    return result


def make_end_vessel(xys, A, alpha=-2, f=3):
    '''
    Returns the points for a end of vessel.

    Parameters
    ----------
    xys : list
        the start and the end of the vessel.
    A : float
        Amplitude of the signal.
    alpha : float, optional
        Decay of the signal. The default is -2.
    f : TYPE, optional
        Main fequency of the signal. The default is 3.

    Returns
    -------
    result : list
        The points of the end of vessel.

    '''

    p_a, p_b = xys

    # width = abs(point_a[0] - point_b[0])
    if p_b[0] != p_a[0]:
        width = abs(p_b[0] - p_a[0])
    else:
        width = abs(p_b[1] - p_a[1])

    x = np.linspace(0, 1, width, endpoint=False)
    y = np.linspace(0, 1, width, endpoint=False)

    Fs = width
    Ts = 1.0 / Fs
    t = np.arange(0, 1, Ts)

    if f == -1:
        f = random.randint(2, 4)

    ysin = A * (np.sin(2 * np.pi * f * t) + 2 * np.sin(2 * np.pi * 0.5 * t)) * (np.exp(alpha * t))

    line = make_line_v2([p_a, p_b])

    result = []
    for i in range(0, len(line)):
        y[i] = (line[i][1] + ysin[i])
        x[i] = line[i][0]

        result.append([x[i], y[i]])

    return result


def __draw_gradient(image):
    inner_color = random.randint(25, 50)
    outer_color = random.randint(85, 105)
    center = [random.randint(-image.width, image.width * 2), random.randint(-image.height, image.height * 2)]

    for y in range(image.height):
        for x in range(image.width):
            # Find the distance to the center
            distance_to_center = math.sqrt((x - center[0]) ** 2 + (y - center[1]) ** 2)
            # Make it on a scale from 0 to 1
            distance_to_center = float(distance_to_center) / (math.sqrt(2) * image.width / 2)
            # Calculate r, g, and b values
            color = outer_color * distance_to_center + inner_color * (1 - distance_to_center)
            # Place the pixel
            image.putpixel((x, y), int(color))


def __add_white_noise(image, delta):
    for x in range(0, image.width):
        for y in range(0, image.height):
            col = random.randint(-delta, delta)
            color = image.getpixel((x, y))
            image.putpixel((x, y), color + col)


def __draw_vessel(image, points_width):
    color = (0, 0, 0, random.randint(100, 100))
    poly = Image.new('RGBA', (image.width, image.height))
    pdraw = ImageDraw.Draw(poly)

    for index, point in enumerate(points_width):
        pdraw.ellipse(point, fill=color)

    image.paste(poly, mask=poly)


def draw_vessel_image(width, height, noise_grade, points_width):
    '''
    Draw the final vessel image.    

    Parameters
    ----------
    width : int
        The width of the image.
    height : int
        The height of the image.
    noise_grade : float
        The quantity of noise between 0 and 1.
    points_width : int
        The size of the points.

    Returns
    -------
    image : image
        The image with the vessel structure in points_width.

    '''

    image = Image.new('L', (width, height), 80)

    __draw_gradient(image)

    __draw_vessel(image, points_width)

    initial_size = 100 / noise_grade
    __add_white_noise(image, 16 + image.height // initial_size)
    image = image.filter(ImageFilter.GaussianBlur(
        random.randint(7 + image.width // initial_size, 8 + image.width // initial_size) * 0.2))
    __add_white_noise(image, 1 + image.width // initial_size)

    return image


def make_stenosis_aneurysm(points, position_stenosis, stenosis_len, stenosis_grade, vessel_width, type_disease):
    '''
    Compute the width of the vessel for stenosis or aneurysm.    

    Parameters
    ----------
    points : list
        Points of the vessel.
    position_stenosis : int
        The position in points to start the stenosis/aneurysm.
    stenosis_len : int
        The len of stenosis.
    stenosis_grade : float
        The grade of the stenosis/aneurysm between 0 and 1.
    vessel_width : int
        The width of the vessel.
    type_disease : string
        "stenosis" or "aneurysm".

    Returns
    -------
    points_width : list
        The points with the respective width for the vessel with disease..

    '''

    points_width = []

    t = 0
    for index, point in enumerate(points):

        stenosis_factor = 1
        if (index > position_stenosis) and (index < position_stenosis + stenosis_len):
            stenosis_factor = np.cos(2 * np.pi * (1 / stenosis_len) * t)
            t += 1

            if type_disease == "aneurysm":
                stenosis_factor = __map_values(stenosis_factor, -1, 1, (1 + stenosis_grade), 1)
            if type_disease == "stenosis":
                stenosis_factor = __map_values(stenosis_factor, -1, 1, (1 - stenosis_grade), 1)

        stenosis_width = vessel_width * stenosis_factor

        points_width.append([point[0] - stenosis_width, point[1] - stenosis_width, point[0] + stenosis_width,
                             point[1] + stenosis_width])

    return points_width


def make_normal(points, vessel_width):
    '''
    Compute the width of the vessel.    

    Parameters
    ----------
    points : list
        Points of the vessel.
    vessel_width : int
        The width of the vessel.

    Returns
    -------
    points_width : list
        The points with the respective width for the vessel.

    '''

    points_width = []

    for index, point in enumerate(points):
        points_width.append(
            [point[0] - vessel_width, point[1] - vessel_width, point[0] + vessel_width, point[1] + vessel_width])

    return points_width


def make_thinning(points, factor, alpha = 1, left_to_right = True):
    '''
    Compute the width of the vessel for thining.    

    Parameters
    ----------
    points : list
        Points of the vessel.
    factor : float
        Value between 1 and 0 to start the thinning. .
    alpha : float, optional
        Decay of the thinning. The default is 1.
    left_to_right : bool, optional
        The direction of the thinning in image. The default is True.

    Returns
    -------
    points_width : list
        The points with the respective thinning for the vessel.

    '''

    points_width = []

    width = len(points)
    factor = width - factor * width

    Fs = width
    Ts = 1.0 / Fs
    t = np.arange(0, 1, Ts)
    if (left_to_right == False):
        t = -t
        t=np.sort(t)
        t = -t
        
    thinning = np.exp(- alpha * t)

    i = 0
    for index, point in enumerate(points):
        if index < factor:
            points_width.append([point[0], point[1], point[2], point[3]])
        else:
            ellipse_new_radius = ((point[2] - point[0])/2)*thinning[i]
            
            pos_x = (point[2] + point[0])/2
            pos_y = (point[3] + point[1])/2
                       
            points_width.append([pos_x - ellipse_new_radius, pos_y - ellipse_new_radius,
                                 pos_x + ellipse_new_radius, pos_y + ellipse_new_radius])
                        
            i += 1

    return points_width


def __map_values(x, in_min, in_max, out_min, out_max):
    # Linear conversion
    return ((x - in_min) * (out_max - out_min) / (in_max - in_min)) + out_min


def mask_fundus_border(img, width, height, blur_radius=0, offset=0):
    '''
    Still in development.

    Parameters
    ----------
    img : TYPE
        DESCRIPTION.
    width : TYPE
        DESCRIPTION.
    height : TYPE
        DESCRIPTION.
    blur_radius : TYPE, optional
        DESCRIPTION. The default is 0.
    offset : TYPE, optional
        DESCRIPTION. The default is 0.

    Returns
    -------
    TYPE
        DESCRIPTION.

    '''
    
    background = Image.new('L', (width, height), 0)

    mask = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((offset, offset, width - offset, height - offset), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(blur_radius))

    return Image.composite(img, background, mask)


def mask_fundus_details(im, width, height, point, color, alpha, blur_radius):
    '''
    Still in development.

    Parameters
    ----------
    img : TYPE
        DESCRIPTION.
    width : TYPE
        DESCRIPTION.
    height : TYPE
        DESCRIPTION.
    blur_radius : TYPE, optional
        DESCRIPTION. The default is 0.
    offset : TYPE, optional
        DESCRIPTION. The default is 0.

    Returns
    -------
    TYPE
        DESCRIPTION.

    '''
    
    w, h = width, height
    a, b = point[0], point[1]

    # TODO: remover hardcode
    shape = [(50, 55), (w - 750, h - 745)]
    color = (color, color, color, alpha)
    img = Image.new("RGBA", (w, h))
    img1 = ImageDraw.Draw(img)
    img1.ellipse(shape, fill=color)
    img = img.filter(ImageFilter.GaussianBlur(blur_radius))

    return im.paste(img, (a - 125, b - 105), mask=img)
