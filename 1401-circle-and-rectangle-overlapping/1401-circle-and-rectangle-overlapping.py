class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if x1>xCenter:
            xnear = x1
        elif x2<xCenter:
            xnear = x2
        else:
            xnear = xCenter
        if y1>yCenter:
            ynear = y1
        elif y2<yCenter:
            ynear = y2
        else:
            ynear = yCenter
        dist = math.sqrt(((xnear-xCenter)*(xnear-xCenter))+((ynear-yCenter)*(ynear-yCenter)))
        if dist<=radius:
            return True
        else:
            return False