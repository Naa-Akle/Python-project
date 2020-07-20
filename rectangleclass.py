'''A program that takes two coordinates(x,y) each of top right corner and bottom left corner'''
class Point:
    '''to initialize the rectangle'''
    def __init__(self,x, y):
        self.x = x
        self.y = y 

''' declaring the rectangle class'''
class rectangle: 
    def __init__(self, bottomLeftCorner = Point(0,0), topRightcorner=Point(6,6)):
        self.bottomLeftCorner = bottomLeftCorner
        self.topRightcorner = topRightcorner

        self.height = topRightcorner.y - bottomLeftCorner.y  
        self.width = topRightcorner.x - bottomLeftCorner.x 
        self.area = self.height * self.width  
        self.perimeter = 2 * (self.height + self.width)
        
    '''function to check for intersetion'''

    def intersect(bLC_1, tRC_1, bLC_2, tRC_2):

      if(tRC_1.x < bLC_2.x or bLC_1.x > tRC_2.x):
        return False

      if(tRC_1.y < bLC_2.y or bLC_1.y > tRC_2.y):
        return False
      
      return True
        
'''Creating an istance of the rectangle class to Calculate area and perimeter'''
rect = rectangle(Point(0, 0), Point(6, 6))  
print('The area of the rectangle is',rect.area)  
print('The perimeter of the rectangle is', rect.perimeter)

'''Creating two instances of the rectangle class'''
rectA = rectangle(Point(0, 4), Point(6, 6))
rectB = rectangle(Point(2, 5), Point(10, 6))

'''Conditional statement to check for overlapping''' 
if(rectangle.intersect(rectA.bottomLeftCorner, rectA.topRightcorner, rectB.bottomLeftCorner, rectB.topRightcorner)):
  print("Both rectangles do overlap") 
else: 
  print("Both rectangles don't overlap")