# -*- coding: utf-8 -*-
import random
import numpy
from change import Hexagram as Hex
from iching import IChing as IC

class Transfer():

	def __init__(self):
		self.num = 0

	# 我们先给“6、7、8、9”分阴阳：7、9都是奇数，为“阳”；6和8都是偶数，叫“阴”
	# 不止这么简单，还需继续分：6是老阴，8是少阴，7是少阳，9是老阳
	# 以四分法来看，这一卦是：“少阴、少阴、老阴、老阳、少阴、少阳”（8、8、6、9、8、8）
	# 呈现“豫卦”
	def yinYangTransfer(self, array):
		newArray = []
		for i in range (len(array)):
			if array[i]%2 == 1:
				newArray.append(1)
			else:
				newArray.append(0)
		return newArray

	def shaoTaiTransfer(self, array):
		newArray = []
		for i in range (len(array)):
			if array[i] == 6:
				newArray.append(8)
			elif array[i] = 9:
				newArray.append(7)
			else:
				newArray.append(array[i])
		return self.yinYangtransfer(array)



h = Hex().hexgram()
b = Read().yinYangtransfer(h)
b = Read().yinYangtransfer(h)
print IC().text(b)
print IC().text



# Weed = Cal.weed(49)
# print Weed, len(Weed)

# print TC.change(Weed)

# Weed1 = Cha.change(Weed)
# print Weed1, len(Weed1)

# Weed2 = Cha.change(Weed1)
# print Weed2, len(Weed2)

# Weed3 = Cha.change(Weed2)
# print Weed3, len(Weed3)

# print Cha.quarter(Weed3)