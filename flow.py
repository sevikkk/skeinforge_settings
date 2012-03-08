#!/usr/bin/python
import math

h = 0.30
feed = 10

w = h * 1.5

d_infill = h * 1.31
s_infill = d_infill * d_infill * math.pi/4

d_fil = 1.75
s_fil = d_fil * d_fil * math.pi/4

head_len = 3200/104.0

rpm = s_infill / s_fil * feed / head_len * 60
print rpm
