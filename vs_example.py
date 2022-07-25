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

x_b = int(image_width / image_div) + random.randint(-int(image_width * variation_tax), int(image_width * variation_tax))
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

