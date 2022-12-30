from Chef import Chef
from ChineseChef import ChineseChef

myChef = Chef()
myChef.make_chicken()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_fried_rice()

# Accessing Chef class method using ChineseChef object
myChineseChef.make_special_dish()