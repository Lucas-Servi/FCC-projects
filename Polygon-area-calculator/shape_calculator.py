import math
class Rectangle:

  def __init__(self, width, height):
    self.set_width(width)
    self.set_height(height)

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.height*self.width

  def get_perimeter(self):
    return self.height*2 + self.width*2

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    picture = []
    if self.width>50 or self.height>50:
      return "Too big for picture."
    else:
      for i in range(self.height):
        picture.append("*"*self.width)
    return "\n".join(picture) +"\n"

  def get_amount_inside(self, shape):
    return math.floor(self.width / shape.width) * math.floor(self.height / shape.height)

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):

  def __init__(self, side):
    self.set_side(side)
  
  def set_side(self, side):
    self.side = side
    self.width = side
    self.height = side

  def set_width(self, side):
    self.set_side(side)


  def set_height(self, side):
    self.set_side(side)


  def __str__(self):
    return f"Square(side={self.side})"