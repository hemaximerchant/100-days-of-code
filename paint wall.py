#define function
def paint_wall(height,width,cover):
  cans=(height*width)/cover
  print(round(cans)+1)
  
#main code  
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_wall(height=test_h, width=test_w, cover=coverage)
