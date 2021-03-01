#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 20:11:19 2021

@author: heiko.langer
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0,(640,480))
while True:
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	out.write(frame)
	cv2.imshow('frame',frame)
	cv2.imshow('gray',gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
out.release()
cv2.destroyAllWindows()
#img = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)

#cv2.imshow('image', img)

#cv2.waitKey(0)
#cv2.destroyAllWindows()

