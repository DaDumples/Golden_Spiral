from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import numpy as np


GOLDEN_RATIO = 1.61803398874989484820458683436563811772030917980576286213544862270526046281890
COLOR1 = (64,224,208)
COLOR2 = (138,43,226)


class WINDOW(QMainWindow):

	def __init__(self):
		QMainWindow.__init__(self)
		self.wid = QWidget()
		self.setCentralWidget(self.wid)

		self.main_layout = QVBoxLayout()
		self.screen = QLabel()

		self.pixmap = QPixmap(1080,720)
		self.pixmap.fill(Qt.white)
		self.screen.setPixmap(self.pixmap)

		self.main_layout.addWidget(self.screen)

		self.menu_bar = QHBoxLayout()
		self.slider1 = QSlider(Qt.Horizontal)
		self.slider1.setMaximum(2000)
		self.slider1.setMinimum(0)
		self.slider1.setTickInterval(1)
		self.slider1.valueChanged.connect(self.sl1)
		self.slider2 = QSlider(Qt.Horizontal)
		self.slider2.setMaximum(1000)
		self.slider2.setMinimum(0)
		self.slider2.setTickInterval(1)
		self.slider2.valueChanged.connect(self.sl2)

		self.slider3 = QSlider(Qt.Horizontal)
		self.slider3.setMaximum(100)
		self.slider3.setMinimum(0)
		self.slider3.setTickInterval(1)
		self.slider3.valueChanged.connect(self.sl3)

		self.menu_bar.addWidget(self.slider1)
		self.menu_bar.addWidget(self.slider2)
		self.menu_bar.addWidget(self.slider3)
		self.main_layout.addLayout(self.menu_bar)
		self.wid.setLayout(self.main_layout)

		self.drad = 1
		self.num_points = 100
		self.circle_rad = 3

		self.slider1.setValue(self.num_points)
		self.slider2.setValue(self.drad)
		self.slider3.setValue(self.circle_rad)
		self.show()
		self.draw()

	def sl1(self):
		self.num_points = self.slider1.value()
		self.draw()

	def sl2(self):
		self.drad = self.slider2.value()/1000
		self.draw()

	def sl3(self):
		self.circle_rad = self.slider3.value()
		self.draw()

	def draw(self):
		center = (self.screen.width()/2,self.screen.height()/2)
		radius = 0
		angle = 0

		painter = QPainter()
		painter.begin(self.pixmap)
		#painter.setBrush(Qt.blue)

		# rspace = np.linspace(COLOR1[0],COLOR2[0],self.num_points)
		# gspace = np.linspace(COLOR1[1],COLOR2[1],self.num_points)
		# bspace = np.linspace(COLOR1[2],COLOR2[2],self.num_points)
		colors = list(zip(*[np.linspace(c1,c2,self.num_points) for c1,c2 in zip(COLOR2,COLOR1)]))
		#colors = list(zip(rspace,gspace,bspace))
		dangle = GOLDEN_RATIO-1
		self.pixmap.fill(Qt.black)
		for i in range(self.num_points):
			rgb = colors[-i]
			painter.setBrush(QColor(*rgb))
			circumferance = 2*radius*np.pi
			x = radius*np.cos(angle) + center[0]
			y = radius*np.sin(angle) + center[1]
			radius += self.drad
			angle = (angle+dangle*2*np.pi)%(2*np.pi)
			painter.drawEllipse(QPoint(x,y),self.circle_rad,self.circle_rad)

		self.screen.setPixmap(self.pixmap)




if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = WINDOW()
	sys.exit(app.exec_())