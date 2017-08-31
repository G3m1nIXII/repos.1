import sys, random, argparse
import numpy as np
import math
import turtle
import random
from PIL import Image
from datetime import datetime
from fractions import  gcd

#a class that draws a spirograph
class Spiro:
	# a constructor
	def __init__(self, xc, yc, col, R, r, l):

		#create a turtle object
		self.t = turtle.Turtle()
		# set the cursor shape
		self.t.shape('turtle')

		# set the step in degrees
		self.step = 5
		self.drawingComplete = False

		self.setparams(xc, yc, col, R, r, l)

		self.restart()

	def setparams(self, xc, yc, col, R, r, l):
		self.xc = xc
		self.yc = yc
		self.R = int(R)
		self.r = int(r)
		self.l = l
		self.col = col
		gcdVal = gcd(self.r, self.R)
		self.nRot = self.r//gcdVal
		self.k = r/float(R)
		self.t.color(*col)
		self.a = 0



	def restart(self):
		self.drawingComplete = False
		self.t.showTurtle()
		self.t.up()
		R, k, l = self.R, self.k, self.l
		a = 0.0
		x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
		y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
		self.t.setpos(self.xc + x, self.yc + y)
		self.t.down()
