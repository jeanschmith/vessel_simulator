# -*- coding: utf-8 -*-
"""
Vessel Simulator - Examples

@authors: Gabriela Copetti Maccagnan, Jean Schmith, Marcia Cunha dos Santos and Rodrigo Marques de Figueiredo
"""

import VesselSimulator as vs
import matplotlib.pyplot as plt
import random

#######################################################################################################################
#-------------------------------------------  EXAMPLE LINE FUNCTION  -------------------------------------------------#
#######################################################################################################################
def line_generator():
    points = []
    image_height = 1920
    image_width = 1920
    vessel_line_width = 30
    noise_grade = 0.9
    stenosis_grade = 0.6
    stenosis_length = 100
    pos_stenosis = 500

    points = vs.make_line(1.5, 430, image_width)

    points_width = vs.make_stenosis_aneurysm(points, pos_stenosis, stenosis_length, stenosis_grade, vessel_line_width,
                                             "stenosis")

    points_width = vs.make_thinning(points_width, 1, left_to_right=False)
    
    im = vs.draw_vessel_image(image_width, image_height, noise_grade, points_width)

    plt.figure()
    plt.imshow(im, cmap="gray")
    plt.axis('off')
    plt.show()

#######################################################################################################################
#-----------------------------------------  EXAMPLE LINE FUNCTION  V2 ------------------------------------------------#
#######################################################################################################################
def line_v2_generator():
    points = []
    image_height = 1920
    image_width = 1920
    vessel_line_width = 30
    noise_grade = 0.9
    stenosis_grade = 0.6
    stenosis_length = 100
    pos_stenosis = 500

    point_a = (0, 0)
    point_b = (image_width, image_height)
    
    points = vs.make_line_v2([point_a, point_b])
    
    points_width = vs.make_stenosis_aneurysm(points, pos_stenosis, stenosis_length, stenosis_grade, vessel_line_width,
                                             "stenosis")
    
    im = vs.draw_vessel_image(image_width, image_height, noise_grade, points_width)

    plt.figure()
    plt.imshow(im, cmap="gray")
    plt.axis('off')
    plt.show()

#######################################################################################################################
#---------------------------------------  EXAMPLE SECOND DEGREE FUNCTION  --------------------------------------------#
#######################################################################################################################
def sec_degree_generator():
    points = []
    image_height = 1920
    image_width = 1920
    vessel_line_width = 30
    noise_grade = 0.9
    stenosis_grade = 0.6
    stenosis_length = 100
    pos_stenosis = 50

    point_a = (0, 920)
    point_b = (700, 1100)
    point_c = (1080, 1920)

    points = vs.make_second_degree([point_a, point_b, point_c], image_width)

    points_width = vs.make_stenosis_aneurysm(points, pos_stenosis, stenosis_length, stenosis_grade, vessel_line_width,
                                             "stenosis")

    im = vs.draw_vessel_image(image_width, image_height, noise_grade, points_width)

    plt.figure()
    plt.imshow(im, cmap="gray")
    plt.axis('off')
    plt.show()

#######################################################################################################################
#-----------------------------------------  EXAMPLE SINE FUNCTION  ---------------------------------------------------#
#######################################################################################################################
def sine_generator():
    points = []
    image_height = 1920
    image_width = 1920
    vessel_line_width = 30
    noise_grade = 0.9
    stenosis_grade = 0.6
    stenosis_length = 100
    pos_stenosis = 50
    
    point_a = (0, int(image_height * .5))
    point_b = (image_width, int(image_height * .5))
    
    points = vs.make_sine([point_a, point_b], int(image_width * .1), 1)
    
    points_width = vs.make_stenosis_aneurysm(points, pos_stenosis, stenosis_length, stenosis_grade, vessel_line_width,
                                             "stenosis")

    im = vs.draw_vessel_image(image_width, image_height, noise_grade, points_width)

    plt.figure()
    plt.imshow(im, cmap="gray")
    plt.axis('off')
    plt.show()

#######################################################################################################################
#-----------------------------------------  EXAMPLE BEZIER FUNCTION  -------------------------------------------------#
#######################################################################################################################
def bezier_generator():
    points = []
    image_height = 1920
    image_width = 1920
    vessel_line_width = 30
    noise_grade = 0.9
    stenosis_grade = 0.6
    stenosis_length = 100
    pos_stenosis = 50
    
    point_a = (random.randint(-image_width, image_width * 2), 0)
    inter_point = (random.randint(0, image_width), random.randint(0, image_height))
    inter_point2 = (random.randint(0, image_width), random.randint(0, image_height))
    point_b = (random.randint(-image_width, image_width * 2), image_height)
    
    points = vs.make_bezier([point_a, inter_point, inter_point2, point_b])
    
    points_width = vs.make_stenosis_aneurysm(points, pos_stenosis, stenosis_length, stenosis_grade, vessel_line_width,
                                             "stenosis")
    
    im = vs.draw_vessel_image(image_width, image_height, noise_grade, points_width)
    
    plt.figure()
    plt.imshow(im, cmap="gray")
    plt.axis('off')
    plt.show()

#######################################################################################################################
#--------------------------------------  EXAMPLE END VESSEL FUNCTION  ------------------------------------------------#
#######################################################################################################################
def end_vessel_generator():
    points = []
    image_height = 920
    image_width = 920
    vessel_line_width = 18
    noise_grade = 0.6
    stenosis_grade = 0.4
    stenosis_length = 100
    pos_stenosis = 250

    point_a = (0, int(image_height * .5))
    point_b = (image_width, int(image_height * .5))

    points = vs.make_end_vessel([point_a, point_b], int(image_width * .1))

    points_width = vs.make_stenosis_aneurysm(points, pos_stenosis, stenosis_length, stenosis_grade, vessel_line_width,
                                             "stenosis")
    
    im = vs.draw_vessel_image(image_width, image_height, noise_grade, points_width)

    plt.figure()
    plt.imshow(im, cmap="gray")
    plt.axis('off')
    plt.show()

#######################################################################################################################
#-------------------------------------  EXAMPLE LEFT CORONARY SET OF VESSELS  ----------------------------------------#
#######################################################################################################################
def lca_generator():
    points_width = []
    variation_tax = 0.025
    image_div = 8
    image_height = 1920
    image_width = 1920
    vessel_line_width = 30
    noise_grade = 0.9
    stenosis_grade = 0.6
    stenosis_length = 100
    pos_stenosis = 200
    thinning_factor = 1

    y_a = int(image_height / image_div) + random.randint(-int(image_height * variation_tax),
                                                         int(image_height * variation_tax))

    x_b = int(image_width / image_div) + random.randint(-int(image_width * variation_tax), 
                                                        int(image_width * variation_tax))
    y_b = int(image_height / image_div) + random.randint(-int(image_height * variation_tax),
                                                         int(image_height * variation_tax))

    x_c = int(image_width / image_div) * 2 + random.randint(-int(image_width * variation_tax),
                                                            int(image_width * variation_tax))
    y_c = int(image_height / image_div) * 2 + random.randint(-int(image_height * variation_tax),
                                                             int(image_height * variation_tax))

    x_d = int(image_width / image_div) * 3 + random.randint(-int(image_width * variation_tax),
                                                            int(image_width * variation_tax))
    y_d = int(image_height / image_div) * 5 + random.randint(-int(image_height * variation_tax),
                                                             int(image_height * variation_tax))

    x_e = int(image_width / image_div) * 5 + random.randint(-int(image_width * variation_tax),
                                                            int(image_width * variation_tax))
    y_e = int(image_height / image_div) * 7 + random.randint(-int(image_height * variation_tax),
                                                             int(image_height * variation_tax))

    x_f = int(image_width / image_div) + random.randint(-int(image_width * variation_tax), int(image_width * variation_tax))
    y_f = int(image_height / image_div) * 5 + random.randint(-int(image_height * variation_tax),
                                                             int(image_height * variation_tax))

    x_g = int(image_width / image_div) * 3 + random.randint(-int(image_width * variation_tax),
                                                            int(image_width * variation_tax))
    y_g = int(image_height / image_div) * 7 + random.randint(-int(image_height * variation_tax),
                                                             int(image_height * variation_tax))

    x_h = int((x_g + x_e) / 2) + random.randint(-int(image_width * variation_tax), int(image_width * variation_tax))
    y_h = int(image_height / image_div) * 7 + random.randint(-int(image_height * variation_tax),
                                                             int(image_height * variation_tax))

    x_i = int(image_width / image_div) * 5 + random.randint(-int(image_width * variation_tax),
                                                            int(image_width * variation_tax))
    y_i = int((y_c + y_d) / 2) + random.randint(-int(image_height * variation_tax), int(image_height * variation_tax))

    x_j = int(image_width / image_div) * 5 + random.randint(-int(image_width * variation_tax),
                                                            int(image_width * variation_tax))
    y_j = int((y_d + y_e) / 2) - random.randint(-int(image_height * variation_tax), int(image_height * variation_tax))
    
    x_k = int(image_width / image_div) * 4 + random.randint(-int(image_width * variation_tax),
                                                            int(image_width * variation_tax))
    y_k = int(image_height / image_div) + random.randint(-int(image_height * variation_tax),
                                                         int(image_height * variation_tax))

    x_l = int(image_width / image_div) * 6 + random.randint(-int(image_width * variation_tax),
                                                            int(image_width * variation_tax))
    y_l = int(image_height / image_div) * 7 - random.randint(-int(image_height * variation_tax),
                                                             int(image_height * variation_tax))

    x_m = int(image_width / image_div) * 7.5
    y_m = int(image_height / image_div) * 4.5 + random.randint(-int(image_height * variation_tax),
                                                               int(image_height * variation_tax))

    point_a = (0, y_a)
    point_b = (x_b, y_b)
    point_c = (x_c, y_c)
    point_d = (x_d, y_d)
    point_e = (x_e, y_e)
    point_f = (x_f, y_f)
    point_g = (x_g, y_g)
    point_h = (x_h, y_h)
    point_i = (x_i, y_i)
    point_j = (x_j, y_j)
    point_k = (x_k, y_k)
    point_l = (x_l, y_l)
    point_m = (x_m, y_m)
    
    C1 = vs.make_sine([point_a, point_b], int(image_width * .01), 1)
    C1 = vs.make_normal(C1, vessel_line_width)
    points_width.extend(C1)
    
    C2 = vs.make_sine([point_b, point_c], int(image_width * .01), 1)
    C2 = vs.make_normal(C2, vessel_line_width)
    points_width.extend(C2)
    
    C3 = vs.make_sine([point_b, point_k], int(image_width * .01), 1)
    C3 = vs.make_normal(C3, vessel_line_width)
    points_width.extend(C3)
    
    C4 = vs.make_sine([point_c, point_d], int(image_width * .04), 1)
    C4 = vs.make_normal(C4, vessel_line_width)
    points_width.extend(C4)
    
    C5 = vs.make_end_vessel([point_d, point_e], int(image_width * .04))
    C5 = vs.make_normal(C5, vessel_line_width)
    C5 = vs.make_thinning(C5, thinning_factor)
    points_width.extend(C5)
    
    C6 = vs.make_end_vessel([point_c, point_i], int(image_width * .05))
    C6 = vs.make_stenosis_aneurysm(C6, pos_stenosis, stenosis_length, stenosis_grade, vessel_line_width, "stenosis")
    C6 = vs.make_thinning(C6, thinning_factor)
    points_width.extend(C6)

    C7 = vs.make_end_vessel([point_d, point_j], int(image_width * .04))
    C7 = vs.make_normal(C7, vessel_line_width)
    C7 = vs.make_thinning(C7, thinning_factor)
    points_width.extend(C7)

    inter_point_1 = (int(point_k[0] * 1.4), int(point_k[1] * 0.9))
    inter_point_2 = (int(point_l[0] * 1.1), int(point_l[1] * 0.9))
    C8 = vs.make_bezier([point_k, inter_point_1, inter_point_2, point_l])
    C8 = vs.make_normal(C8, vessel_line_width)
    C8 = vs.make_thinning(C8, thinning_factor)
    points_width.extend(C8)
    
    inter_point_1 = (int(point_k[0] * 1.4), int(point_k[1] * 0.9))
    inter_point_2 = (int(point_m[0]), int(point_m[1] * 0.9))
    C9 = vs.make_bezier([point_k, inter_point_1, inter_point_2, point_m])
    C9 = vs.make_normal(C9, vessel_line_width)
    C9 = vs.make_thinning(C9, thinning_factor)
    points_width.extend(C9)
    
    inter_point_1 = (point_b[0] * 1.1, int(abs(point_b[1] - point_f[1]) / 3))
    inter_point_2 = (point_b[0] * 0.9, int(abs(point_b[1] - point_f[1]) / 3) * 2)
    C10 = vs.make_bezier([point_b, inter_point_1, inter_point_2, point_f])
    C10 = vs.make_normal(C10, vessel_line_width)
    points_width.extend(C10)
    
    C11 = vs.make_end_vessel([point_f, point_g], int(image_width * .04))
    C11 = vs.make_normal(C11, vessel_line_width)
    C11 = vs.make_thinning(C11, thinning_factor)
    points_width.extend(C11)
    
    C12 = vs.make_end_vessel([point_f, point_h], int(image_width * .04))
    C12 = vs.make_normal(C12, vessel_line_width)
    C12 = vs.make_thinning(C12, thinning_factor)
    points_width.extend(C12)
    
    im = vs.draw_vessel_image(image_width, image_height, noise_grade, points_width)
    
    plt.figure()
    plt.imshow(im, cmap="gray")
    plt.axis('off')
    plt.show()    


#######################################################################################################################
#------------------------------------  EXAMPLE LEFT CORONARY SET OF VESSELS V2 ---------------------------------------#
#######################################################################################################################
def lca_v2_generator():
    points_width = []
    variation_tax = 0.04
    image_div = 8
    image_height = 1920
    image_width = 1920
    vessel_line_width = 30
    noise_grade = 1
    stenosis_grade = 3.0
    stenosis_length = 100
    pos_stenosis = 100
    thinning_factor = 1
    
    x_a = 0
    y_a = 0
    
    x_d = int(image_width / image_div) * 1.7 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_d = int(image_height / image_div) * 1.2 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_g = int(image_width / image_div) * 3 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_g = int(image_height / image_div) * 3.95 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_ga = int(image_width / image_div) * 1.8 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_ga = int(image_height / image_div) * 6.7 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_gb = int(image_width / image_div) * 6.5 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_gb = int(image_height / image_div) * 5.25 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax))
    
    x_i = int(image_width / image_div) * 5 + random.randint(-int(image_width * variation_tax), int(image_width * 0.03)) 
    y_i = int(image_height / image_div) * 5.9 + random.randint(-int(image_height * variation_tax), int(image_height * 0.03)) 
    
    x_ia = int(image_width / image_div) * 5.5 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_ia = int(image_height / image_div) * 7.4 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_l = int(image_width / image_div) * 6 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_l = int(image_height / image_div) * 6.3 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_m = int(image_width / image_div) * 6.2 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_m = int(image_height / image_div) * 6.5 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_mb = int(image_width / image_div) * 6.95 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_mb = int(image_height / image_div) * 6.75 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_mc = int(image_width / image_div) * 7.9 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_mc = int(image_height / image_div) * 6.5 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_r = int(image_width / image_div) * 7.9 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_r = int(image_height / image_div) * 6 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_t = int(image_width / image_div) * 3.9 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_t = int(image_height / image_div) * 0.5 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_tb = int(image_width / image_div) * 5.1 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_tb = int(image_height / image_div) * 0.9 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_td = int(image_width / image_div) * 5.96 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_td = int(image_height / image_div) * 1.8 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_tf = int(image_width / image_div) * 6.95 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_tf = int(image_height / image_div) * 3.2 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_th = int(image_width / image_div) * 7.6 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_th = int(image_height / image_div) * 4.5 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_ti = int(image_width / image_div) * 2.6 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_ti = int(image_height / image_div) * 1.9 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_tia = int(image_width / image_div) * 2.2 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_tia = int(image_height / image_div) * 3.3 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_tib = int(image_width / image_div) * 1.5 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_tib = int(image_height / image_div) * 3.25 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_tj = int(image_width / image_div) * 5.4 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_tj = int(image_height / image_div) * 1.64 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_tja = int(image_width / image_div) * 5.8 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_tja = int(image_height / image_div) * 2.95 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_tjb = int(image_width / image_div) * 6.4 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_tjb = int(image_height / image_div) * 3.3 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_u = int(image_width / image_div) * 5.2 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_u = int(image_height / image_div) * 0.6 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_ua = int(image_width / image_div) * 3.3 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_ua = int(image_height / image_div) * 2.9 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_ub = int(image_width / image_div) * 5.5 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   0.03)) 
    y_ub = int(image_height / image_div) * 0.5 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   0.03)) 
    
    x_uc = int(image_width / image_div) * 7.8 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   0.03)) 
    y_uc = int(image_height / image_div) * 2.3 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   0.03))
    
    x_v = int(image_width / image_div) * 2.8 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_v = int(image_height / image_div) * 3.2 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_x = int(image_width / image_div) * 7.8 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_x = int(image_height / image_div) * 3.2 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax))
    
    point_a = (int(x_a), int(y_a))
    point_d = (int(x_d), int(y_d))
    point_g = (int(x_g), int(y_g))
    point_ga = (int(x_ga), int(y_ga))
    point_gb = (int(x_gb), int(y_gb))
    point_i = (int(x_i), int(y_i))
    point_ia = (int(x_ia), int(y_ia))
    point_l = (int(x_l), int(y_l))
    point_m = (int(x_m), int(y_m))
    point_mb = (int(x_mb), int(y_mb))
    point_mc = (int(x_mc), int(y_mc))
    point_r = (int(x_r), int(y_r))
    point_t = (int(x_t), int(y_t))
    point_tb = (int(x_tb), int(y_tb))
    point_td = (int(x_td), int(y_td))
    point_tf = (int(x_tf), int(y_tf))
    point_th = (int(x_th), int(y_th))
    point_ti = (int(x_ti), int(y_ti))
    point_tia = (int(x_tia), int(y_tia))
    point_tib = (int(x_tib), int(y_tib))
    point_tj = (int(x_tj), int(y_tj))
    point_tja = (int(x_tja), int(y_tja))
    point_tjb = (int(x_tjb), int(y_tjb))
    point_u = (int(x_u), int(y_u))
    point_ua = (int(x_ua), int(y_ua))
    point_ub = (int(x_ub), int(y_ub))
    point_uc = (int(x_uc), int(y_uc))
    point_v = (int(x_v), int(y_v))
    point_x = (int(x_x), int(y_x))
    
    x_b = int(image_width / image_div) * 0.9 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) #56
    y_b = int(image_height / image_div) * 1.2 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) #75
    point_b = (int(x_b), int(y_b))
    x_c = point_d[0] * 0.75
    y_c = point_d[1] * 0.54
    point_c = (int(x_c), int(y_c))
    C1 = vs.make_bezier([point_a, point_b, point_c, point_d])
    C1 = vs.make_normal(C1, vessel_line_width)
    points_width.extend(C1)
    
    x_e = point_d[0] * 1.1 
    y_e = point_d[1] * 2.15 
    point_e = (int(x_e), int(y_e))
    x_f = point_g[0] * 0.98 
    y_f = point_g[1] * 0.65
    point_f = (int(x_f), int(y_f))
    C2 = vs.make_bezier([point_d, point_e, point_f, point_g])
    C2 = vs.make_normal(C2, vessel_line_width)
    points_width.extend(C2)
    
    C3 = vs.make_sine([point_g, point_ga], 40, -2)
    C3 = vs.make_normal(C3, 10)
    C3 = vs.make_thinning(C3, thinning_factor, False)
    points_width.extend(C3)
    
    C4 = vs.make_sine([point_g, point_gb], 20, 4)
    C4 = vs.make_normal(C4, 10)
    C4 = vs.make_thinning(C4, thinning_factor)
    points_width.extend(C4)
    
    x_h = point_g[0] * 1.27 
    y_h = point_g[1] * 1.41 
    point_h = (int(x_h), int(y_h))
    C5 = vs.make_bezier([point_g, point_h, point_i])
    C5 = vs.make_normal(C5, vessel_line_width)
    C5 = vs.make_stenosis_aneurysm(C5, pos_stenosis, stenosis_length, stenosis_grade, vessel_line_width, "aneurysm")
    points_width.extend(C5)
    
    C6 = vs.make_sine([point_i, point_ia], 20, 2)
    C6 = vs.make_normal(C6, 11)
    C6 = vs.make_thinning(C6, thinning_factor)
    points_width.extend(C6)
    
    x_j = point_i[0] * 1.12 
    y_j = point_i[1] * 1.01 
    point_j = (int(x_j), int(y_j))
    x_k = point_l[0] * 0.92 
    y_k = point_l[1] * 1.06
    point_k = (int(x_k), int(y_k))
    C7 = vs.make_bezier([point_i, point_j, point_k, point_l])
    C7 = vs.make_normal(C7, vessel_line_width)
    points_width.extend(C7)
    
    C8 = vs.make_bezier([point_l, point_m])
    C8 = vs.make_normal(C8, vessel_line_width)
    points_width.extend(C8)
    
    x_ma = point_m[0] * 1.01
    y_ma = point_m[1] * 1.08
    point_ma = (int(x_ma), int(y_ma))
    C9 = vs.make_bezier([point_m, point_ma, point_mb])
    C9 = vs.make_normal(C9, 10)
    points_width.extend(C9)
    
    C10 = vs.make_end_vessel([point_mb, point_mc], 10)
    C10 = vs.make_normal(C10, 10)
    C10 = vs.make_thinning(C10, thinning_factor)
    points_width.extend(C10)
    
    x_n = point_m[0] * 1.11
    y_n = point_m[1] * 0.9 
    point_n = (int(x_n), int(y_n))
    x_o = point_m[0] * 1.13 
    y_o = point_m[1] * 1.12 
    point_o = (int(x_o), int(y_o))
    x_p = point_r[0] * 0.93 
    y_p = point_r[1] * 0.94 
    point_p = (int(x_p), int(y_p))
    x_q = point_r[0] * 0.96
    y_q = point_r[1] * 1.04
    point_q = (int(x_q), int(y_q))
    C11 = vs.make_bezier([point_m, point_n, point_o, point_p, point_q, point_r])
    C11 = vs.make_normal(C11, vessel_line_width)
    C11 = vs.make_thinning(C11, thinning_factor)
    points_width.extend(C11)
    
    x_s = point_d[0] * 1.73
    y_s = point_d[1] * 0.2
    point_s = (int(x_s), int(y_s))
    C12 = vs.make_bezier([point_d, point_s, point_t])
    C12 = vs.make_normal(C12, vessel_line_width)
    points_width.extend(C12)
    
    C13 = vs.make_line_v2([point_t, point_u])
    C13 = vs.make_normal(C13, vessel_line_width)
    points_width.extend(C13)
    
    C14 = vs.make_sine([point_u, point_ua], 15, -2)
    C14 = vs.make_normal(C14, 10)
    C14 = vs.make_thinning(C14, thinning_factor, False)
    points_width.extend(C14)
    
    C15 = vs.make_second_degree([point_u, point_ub, point_uc], image_width)
    C15 = vs.make_normal(C15, 10)
    C15 = vs.make_thinning(C15, thinning_factor)
    points_width.extend(C15)
    
    C16 = vs.make_second_degree([point_u, point_v, point_x], image_width)
    C16 = vs.make_normal(C16, vessel_line_width)
    C16 = vs.make_thinning(C16, thinning_factor)
    points_width.extend(C16)
    
    x_ta = point_t[0] * 1.32
    y_ta = 0
    point_ta = (int(x_ta), int(y_ta))
    C17 = vs.make_bezier([point_t, point_ta, point_tb])
    C17 = vs.make_normal(C17, vessel_line_width)
    points_width.extend(C17)
    
    x_tc = point_tb[0] * 1.21
    y_tc = point_tb[1] * 1.2
    point_tc = (int(x_tc), int(y_tc))
    C18 = vs.make_bezier([point_tb, point_tc, point_td])
    C18 = vs.make_normal(C18, vessel_line_width)
    points_width.extend(C18)
   
    x_tda = point_td[0] * 0.95
    y_tda = point_td[1] * 1.44
    point_tda = (int(x_tda), int(y_tda))
    x_te = point_tf[0] * 0.99 
    y_te = point_tf[1] * 0.6
    point_te = (int(x_te), int(y_te))
    C19 = vs.make_bezier([point_td, point_tda, point_te, point_tf])
    C19 = vs.make_normal(C19, vessel_line_width)
    points_width.extend(C19)
    
    x_tfa = point_tf[0] * 1
    y_tfa = point_tf[1] * 1.25
    point_tfa = (int(x_tfa), int(y_tfa))
    x_tg = point_th[0] * 1
    y_tg = point_th[1] * 0.73
    point_tg = (int(x_tg), int(y_tg))
    C20 = vs.make_bezier([point_tf, point_tfa, point_tg, point_th])
    C20 = vs.make_normal(C20, vessel_line_width)
    C20 = vs.make_thinning(C20, thinning_factor)
    points_width.extend(C20)
    
    C21 = vs.make_end_vessel([point_t, point_ti], 20, -2, -4)
    C21 = vs.make_normal(C21, 12)
    points_width.extend(C21)
    
    x_tiaa = point_ti[0] * 1.07
    y_tiaa = point_ti[1] * 1.4
    point_tiaa = (int(x_tiaa), int(y_tiaa))
    C22 = vs.make_bezier([point_ti, point_tiaa, point_tia])
    C22 = vs.make_normal(C22, 10)
    C22 = vs.make_thinning(C22, thinning_factor, False)
    points_width.extend(C22)
    
    x_tiba = point_ti[0] * 0.74
    y_tiba = point_ti[1] * 1.3
    point_tiba = (int(x_tiba), int(y_tiba)) 
    C23 = vs.make_bezier([point_ti, point_tiba, point_tib])
    C23 = vs.make_normal(C23, 10)
    C23 = vs.make_thinning(C23, thinning_factor, False)
    points_width.extend(C23)
    
    C24 = vs.make_sine([point_t, point_tj], 20, 2)
    C24 = vs.make_normal(C24, 12)
    points_width.extend(C24)
   
    C25 = vs.make_sine([point_tj, point_tja], 20, 2)
    C25 = vs.make_normal(C25, 10)
    C25 = vs.make_thinning(C25, thinning_factor)
    points_width.extend(C25)
    
    C26 = vs.make_sine([point_tj, point_tjb], 20, -2)
    C26 = vs.make_normal(C26, 10)
    C26 = vs.make_thinning(C26, thinning_factor)
    points_width.extend(C26)
    
    im = vs.draw_vessel_image(image_width, image_height, noise_grade, points_width)

    plt.figure()
    plt.imshow(im, cmap="gray")
    plt.axis('off')
    plt.show()
    

#######################################################################################################################
#-------------------------------------  EXAMPLE RIGHT CORONARY SET OF VESSELS  ---------------------------------------#
#######################################################################################################################
def rca_generator():
    points_width = []
    variation_tax = 0.025
    image_div = 8
    image_height = 1920
    image_width = 1920
    vessel_line_width = 30
    noise_grade = 0.9
    stenosis_grade = 0.6
    stenosis_length = 100
    pos_stenosis = 200
    thinning_factor = 1

    x_a = int(image_width / image_div) * 4 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax))

    x_b = int(image_width / image_div) * 1.5 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                     variation_tax))
    y_b = int(image_height / image_div) * 2 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                     variation_tax))

    x_c = int(image_width / image_div) + random.randint(-int(image_width * variation_tax), int(image_width * variation_tax))
    y_c = int(image_height / image_div) + random.randint(-int(image_height * variation_tax),
                                                         int(image_height * variation_tax))

    x_d = int(image_width / image_div) * 6 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax))
    y_d = int(image_height / image_div) * 5.5 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                       variation_tax))

    x_e = int(image_width / image_div) * 7.9 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                     variation_tax))
    y_e = int(image_height / image_div) * 6 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                     variation_tax))

    x_f = int(image_width / image_div) * 7.7 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                     variation_tax))
    y_f = int(image_height / image_div) * 5.5 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                       variation_tax))

    point_a = (x_a, 0)
    point_b = (x_b, y_b)
    point_c = (x_c, y_c)
    point_d = (x_d, y_d)
    point_e = (int(x_e), int(y_e))
    point_f = (x_f, y_f)

    inter_point_1 = (int(point_a[0] * 0.9), int(point_b[1] * 0.9))
    inter_point_2 = (int(point_b[0] * 1.2), int(point_b[1] * 0.4))
    RC1 = vs.make_bezier([point_a, inter_point_1, inter_point_2, point_b])
    RC1 = vs.make_stenosis_aneurysm(RC1, pos_stenosis - 30, stenosis_length, 0.5, vessel_line_width, "aneurysm")
    points_width.extend(RC1)

    inter_point_1 = (160, 80)
    inter_point_2 = (220, 50)
    RC2 = vs.make_bezier([point_b, inter_point_1, inter_point_2, point_c])
    RC2 = vs.make_normal(RC2, vessel_line_width - 8)
    points_width.extend(RC2)

    inter_point_1 = (int(point_b[0] * 0.6), int(point_b[1] * 2.2))
    inter_point_2 = (int(point_b[0] * 0.7), int(point_d[1] * 1.3))
    RC3 = vs.make_bezier([point_b, inter_point_1, inter_point_2, point_d])
    RC3 = vs.make_stenosis_aneurysm(RC3, 30, 40, stenosis_grade, vessel_line_width, "stenosis")
    points_width.extend(RC3)

    RC4 = vs.make_end_vessel([point_d, point_e],  int(image_width * .01))
    RC4 = vs.make_normal(RC4, vessel_line_width)
    RC4 = vs.make_thinning(RC4, thinning_factor)
    points_width.extend(RC4)

    inter_point_1 = (int(point_d[0] * 1.2), int(point_d[1] * 0.8))
    inter_point_2 = (int(point_f[0] * 0.85), int(point_f[1] * 0.95))
    RC5 = vs.make_bezier([point_d, inter_point_1, inter_point_2, point_f])
    RC5 = vs.make_normal(RC5, vessel_line_width)
    RC5 = vs.make_thinning(RC5, thinning_factor)
    points_width.extend(RC5)

    im = vs.draw_vessel_image(image_width, image_height, noise_grade, points_width)

    plt.figure()
    plt.imshow(im, cmap="gray")
    plt.axis('off')
    plt.show()


#######################################################################################################################
#------------------------------------  EXAMPLE RIGHT CORONARY SET OF VESSELS V2  -------------------------------------#
#######################################################################################################################
def rca_v2_generator():
    points_width = []
    variation_tax = 0.04
    image_div = 8
    image_height = 512
    image_width = 512
    vessel_line_width = random.randint(7, 10)
    noise_grade = 0.01
    stenosis_grade = 0.6
    stenosis_length = 100
    pos_stenosis = 200
    thinning_factor = 1
    
    x_a = int(image_width / image_div) * 4.6 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_a = 0
    
    x_c = int(image_width / image_div) * 4 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_c = int(image_height / image_div) * 1.3 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_cba = int(image_width / image_div) * 2.4 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_cba = int(image_height / image_div) * 1.1 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_cae = int(image_width / image_div) * 2.8 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_cae = int(image_height / image_div) * 2.9 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_cag = int(image_width / image_div) * 3.8 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_cag = int(image_height / image_div) * 4.5 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_cbc = int(image_width / image_div) * 3.4 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_cbc = int(image_height / image_div) * 0.9 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_cbe = int(image_width / image_div) * 4.6 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_cbe = int(image_height / image_div) * 1.4 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_cbf = int(image_width / image_div) * 5.4 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_cbf = int(image_height / image_div) * 0.2 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_e = int(image_width / image_div) * 3.7 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_e = int(image_height / image_div) * 2.7 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_g = int(image_width / image_div) * 1.8 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_g = int(image_height / image_div) * 3.7 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
        
    x_hac = int(image_width / image_div) * 1.5 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_hac = int(image_height / image_div) * 4.9 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_had = int(image_width / image_div) * 2.3 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_had = int(image_height / image_div) * 6 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 

    x_hag = int(image_width / image_div) * 3.8 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_hag = int(image_height / image_div) * 6.3 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_hah = int(image_width / image_div) * 2.9 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_hah = int(image_height / image_div) * 6.6 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_i = int(image_width / image_div) * 4.6 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax))  
    y_i = int(image_height / image_div) * 5.2 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_iac = int(image_width / image_div) * 7.5 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_iac = int(image_height / image_div) * 5.6 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_k = int(image_width / image_div) * 5.9 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_k = int(image_height / image_div) * 5.3 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_kaa = int(image_width / image_div) * 7.4 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_kaa = int(image_height / image_div) * 6.1 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_kbc = int(image_width / image_div) * 6.7 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_kbc = int(image_height / image_div) * 4.5 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_kbe = int(image_width / image_div) * 7.6 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_kbe = int(image_height / image_div) * 4.4 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_kbf = int(image_width / image_div) * 7.9 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_kbf = int(image_height / image_div) * 4 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_kbg = int(image_width / image_div) * 7.9 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_kbg = int(image_height / image_div) * 4.8 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax)) 
    
    x_kbh = int(image_width / image_div) * 7.9 + random.randint(-int(image_width * variation_tax), int(image_width *
                                                                                                   variation_tax)) 
    y_kbh = int(image_height / image_div) * 5.3 + random.randint(-int(image_height * variation_tax), int(image_height *
                                                                                                   variation_tax))
    
    point_a = (int(x_a), int(y_a))
    point_c = (int(x_c), int(y_c))
    point_cae = (int(x_cae), int(y_cae))
    point_cag = (int(x_cag), int(y_cag))
    point_cba = (int(x_cba), int(y_cba))
    point_cbc = (int(x_cbc), int(y_cbc))
    point_cbe = (int(x_cbe), int(y_cbe))
    point_cbf = (int(x_cbf), int(y_cbf))
    point_e = (int(x_e), int(y_e))
    point_g = (int(x_g), int(y_g))
    point_hac = (int(x_hac), int(y_hac))
    point_had = (int(x_had), int(y_had))
    point_hag = (int(x_hag), int(y_hag))
    point_hah = (int(x_hah), int(y_hah))
    point_i = (int(x_i), int(y_i))
    point_iac = (int(x_iac), int(y_iac))
    point_k = (int(x_k), int(y_k))
    point_kaa = (int(x_kaa), int(y_kaa))
    point_kbc = (int(x_kbc), int(y_kbc))
    point_kbe = (int(x_kbe), int(y_kbe))
    point_kbf = (int(x_kbf), int(y_kbf))
    point_kbg = (int(x_kbg), int(y_kbg))
    point_kbh = (int(x_kbh), int(y_kbh))
        
    x_b = point_a[0] * 1.04
    y_b = point_c[1] * 1.3
    point_b = (int(x_b), int(y_b))
    C1 = vs.make_bezier([point_a, point_b, point_c])
    C1 = vs.make_normal(C1, vessel_line_width)
    points_width.extend(C1)

    x_d = point_e[0] * 0.5 
    y_d = point_c[1] * 0.7 
    point_d = (int(x_d), int(y_d))
    x_f = point_e[0] * 0.6
    y_f = point_c[1] * 2.2
    point_f = (int(x_f), int(y_f))
    C2 = vs.make_bezier([point_c, point_d, point_e, point_f, point_g])
    C2 = vs.make_stenosis_aneurysm(C2, pos_stenosis, stenosis_length, stenosis_grade, vessel_line_width, 'stenosis')
    points_width.extend(C2)
    
    x_h = point_g[0] * 0.8
    y_h = point_g[1] * 1.8
    point_h = (int(x_h), int(y_h))
    C3 = vs.make_bezier([point_g, point_h, point_i])
    C3 = vs.make_normal(C3, vessel_line_width)
    points_width.extend(C3)
    
    x_j = point_i[0] * 1.1
    y_j = point_i[1] * 0.96
    point_j = (int(x_j), int(y_j))
    C4 = vs.make_bezier([point_i, point_j, point_k])
    C4 = vs.make_normal(C4, vessel_line_width)
    C4 = vs.make_thinning(C4, thinning_factor)
    points_width.extend(C4)
    
    x_kba = point_k[0] * 1.1
    y_kba = point_k[1] * 0.96
    point_kba = (int(x_kba), int(y_kba))
    x_kbb = point_kbc[0] * 0.9
    y_kbb = point_kbc[1] * 1.01
    point_kbb = (int(x_kbb), int(y_kbb))
    C5 = vs.make_bezier([point_k, point_kba, point_kbb, point_kbc])
    C5 = vs.make_normal(C5, 5)
    points_width.extend(C5)
        
    x_kbd = point_kbc[0] * 1.1
    y_kbd = point_kbc[1] * 0.99
    point_kbd = (int(x_kbd), int(y_kbd))
    C6 = vs.make_bezier([point_kbc, point_kbd, point_kbe])
    C6 = vs.make_normal(C6, 5)
    points_width.extend(C6)
    
    C7 = vs.make_sine([point_kbe, point_kbf], 15, 1.5)
    C7 = vs.make_normal(C7, 5)
    C7 = vs.make_thinning(C7, thinning_factor, 1.1, left_to_right=True)
    points_width.extend(C7)
    
    C8 = vs.make_end_vessel([point_kbd, point_kbg], 2)
    C8 = vs.make_normal(C8, 5)
    C8 = vs.make_thinning(C8, thinning_factor, 1.1, left_to_right=True)
    points_width.extend(C8)
    
    C9 = vs.make_end_vessel([point_k, point_kaa], 2)
    C9 = vs.make_normal(C9, 5)
    C9 = vs.make_thinning(C9, thinning_factor, 1.1, left_to_right=True)
    points_width.extend(C9)
    
    C10 = vs.make_end_vessel([point_kbc, point_kbh], 2)
    C10 = vs.make_normal(C10, 5)
    C10 = vs.make_thinning(C10, thinning_factor, 1.1, left_to_right=True)
    points_width.extend(C10)
   
    x_hab = point_g[0] * 0.74
    y_hab = point_g[1] * 1.01
    point_hab = (int(x_hab), int(y_hab))
    C11 = vs.make_bezier([point_g, point_hab, point_hac])
    C11 = vs.make_normal(C11, 3)
    points_width.extend(C11)
    
    C12 = vs.make_sine([point_hac, point_had], 15, 1.5)
    C12 = vs.make_normal(C12, 3)
    points_width.extend(C12)
    
    x_hae = point_had[0] * 1.3
    y_hae = point_had[1] * 1.05
    point_hae = (int(x_hae), int(y_hae))
    x_haf = point_hag[0] * 0.84
    y_haf = point_hag[1] * 0.97
    point_haf = (int(x_haf), int(y_haf))
    C13 = vs.make_bezier([point_had, point_hae, point_haf, point_hag])
    C13 = vs.make_normal(C13, 3)
    C13 = vs.make_thinning(C13, thinning_factor, 1.1, left_to_right=True)
    points_width.extend(C13)
    
    C14 = vs.make_end_vessel([point_had, point_hah], 1)
    C14 = vs.make_normal(C14, 3)
    C14 = vs.make_thinning(C14, thinning_factor, 1.1, left_to_right=True)
    points_width.extend(C14)
    
    x_iaa = point_i[0] * 1.17
    y_iaa = point_i[0] * 1.2
    point_iaa = (int(x_iaa), int(y_iaa))
    x_iab = point_iac[0] * 0.93
    y_iab = point_iac[1] * 1.1
    point_iab = (int(x_iab), int(y_iab))
    C15 = vs.make_bezier([point_i, point_iaa, point_iab, point_iac])
    C15 = vs.make_normal(C15, 3)
    C15 = vs.make_thinning(C15, thinning_factor, 1.1, left_to_right=True)
    points_width.extend(C15)
    
    x_caa = point_c[0] * 0.86
    y_caa = point_c[1] * 0.7
    point_caa = (int(x_caa), int(y_caa))
    x_cab = point_cba[0] * 1.4
    y_cab = point_cba[1] * 0.2
    point_cab = (int(x_cab), int(y_cab))
    C16 = vs.make_bezier([point_c, point_caa, point_cab, point_cba])
    C16 = vs.make_normal(C16, 3)
    points_width.extend(C16)
    
    x_cac = point_cba[0] * 0.71
    y_cac = point_cba[1] * 1.3
    point_cac = (int(x_cac), int(y_cac))
    x_cad = point_cae[0] *  1.07
    y_cad = point_cae[0] * 0.76
    point_cad = (int(x_cad), int(y_cad))
    C17 = vs.make_bezier([point_cba, point_cac, point_cad, point_cae])
    C17 = vs.make_normal(C17, 3)
    points_width.extend(C17)
    
    C18 = vs.make_end_vessel([point_cae, point_cag], 2)
    C18 = vs.make_normal(C18, 3)
    C18 = vs.make_thinning(C18, thinning_factor, 1.1, left_to_right=True)
    points_width.extend(C18)
    
    x_cbb = point_cba[0] * 1.3
    y_cbb = point_cba[1] * 2.2 
    point_cbb = (int(x_cbb), int(y_cbb))
    x_cbd = point_cbe[0] *  0.88
    y_cbd = point_cbe[1] * 1.6
    point_cbd = (int(x_cbd), int(y_cbd))
    C19 = vs.make_bezier([point_cba, point_cbb, point_cbc, point_cbd, point_cbe])
    C19 = vs.make_normal(C19, 2)
    points_width.extend(C19)
    
    C20 = vs.make_sine([point_cbe, point_cbf], 15, 1.5)
    C20 = vs.make_normal(C20, 3)
    C20 = vs.make_thinning(C20, thinning_factor, 1.1, left_to_right=True)
    points_width.extend(C20)
    
    im = vs.draw_vessel_image(image_width, image_height, noise_grade, points_width)

    plt.figure()
    plt.imshow(im, cmap="gray")
    plt.axis('off')
    plt.show()

