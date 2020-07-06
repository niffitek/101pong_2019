#! /usr/bin/env python3
import sys
import math


def error_checker():
    error = 0;
    if len(sys.argv) != 8:
        sys.stderr.write("error wrong number of arguments")
        exit(84)
    for i in range(1, 8):
        try:
            float(sys.argv[i])
        except ValueError:
            sys.stderr.write("error invalid input at argument: ")
            sys.stderr.write(str(i))
            exit(84)
    else:
        return 0


def inputs():
    try:
        my_try = error_checker()
        if my_try == 84:
            exit(84)
        p1 = [float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])]
        p2 = [float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6])]
        t = int(sys.argv[7])
        p3 = []
        angle = -1

        if t < 0:
            sys.stderr.write("error: negativ time shift")
            exit(84)
        vec = calc_vector(p1, p2)
        p3 = get_point(vec, p2, t)
        if (p2[2] < 0 and p3[2] > 0) or (p2[2] > 0 and p3[2] < 0) or (p3[2] == 0):
            angle = get_angle(vec)
        outputs(vec, p3, angle, t)
        return my_try
    except ValueError:
        sys.stderr.write("error: not all numbers")
        exit(84)


def calc_vector(p1, p2):
    vec = []
    for i in range(0, 3):
        vec.append(p2[i] - p1[i])
    return vec


def get_point(vec, p2, t):
    p3 = []
    for i in range(0, 3):
        p3.append(p2[i] + vec[i] * t)
    return p3


def get_angle(vec):
    absolute = vec[0] ** 2 + vec[1] ** 2 + vec[2] ** 2
    root = math.sqrt(float(absolute))
    sin = (math.fabs(vec[2]) / root)
    asin = math.degrees(math.asin(sin))
    while asin > 90:
        asin -= 90
    return asin


def outputs(vec, p3, angle, t):
    print("The velocity vector of the ball is:")
    print("(%.2f, %.2f, %.2f)" % (vec[0], vec[1], vec[2]))
    print("At time t + %i, ball coordinates will be:" % t)
    print("(%.2f, %.2f, %.2f)" % (p3[0], p3[1], p3[2]))
    if angle == -1:
        print("The ball won't reach the paddle.")
    else:
        print("The incidence angle is:")
        print("%.2f degrees" % angle)


inputs()
