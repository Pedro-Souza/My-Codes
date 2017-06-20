#!/usr/bin/env python

import pygame as pg


class sound(object):
	def __init__(self, folder):
		self.toque = True
		self.folder = folder

	def Play(self):
	 	pg.mixer.init(44100, -16, 2, 2048)
	 	print(self.folder)
	 	pg.mixer.music.set_volume(.8)
	 	clock = pg.time.Clock()
	 	pg.mixer.music.load(self.folder)
	 	pg.mixer.music.play()
	 	print(self.toque)
	 	self.test = 0 
	 	while self.toque:
	 		print('ué')
	 		print(self.test)
	 		if(self.test == 100):
	 			self.toque = False
	 		clock.tick(30)
	 		self.test += 1


sound('toque.wav').Play()