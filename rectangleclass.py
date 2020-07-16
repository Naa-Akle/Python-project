class Point:  

    def _init_(rectp, x, y):
        rectp.x = x
        rectp.y = y


class rectangle: 
    def _init_(rectp, bottomLeftCorner = Point(0,0), topRightCorner=Point(4,4)):
        rectp.bottomLeftCorner = bottomLeftCorner
        rectp.topRightCorner = topRightCorner

        rectp.height = topRightCorner.y - bottomLeftCorner.y  
        rectp.width = topRightCorner.x - bottomLeftCorner.x  
        rectp.area = rectp.height * rectp.width  
        rectp.perimeter = 2 * (rectp.height + rectp.width)  

    def intersect(BLC_1, TRC_1, BLC_2, TRC_2):  
        return not (TRC_1.x < BLC_2.x or BLC_1.x > TRC_2.x or TRC_1.y < BLC_2.y or BLC_1.y > TRC_2.y)


rect = rectangle(Point(0, 0), Point(4, 4))  
print(rect.area)  
print(rect.perimeter)  


rectA = rectangle(Point(0, 0), Point(6, 6))
rectB = rectangle(Point(0, 2), Point(2, 6))


Rectangle.intersect(rectA.bottomLeftCorner, rectA.topRightCorner, rectB.bottomLeftCorner, rectB.topRightCorner)