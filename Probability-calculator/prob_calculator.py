import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self,**colors):
    self.contents = []
    for color in colors.keys():
      self.contents += [color]*int(colors[color])

  def draw(self, amount):
    if amount >= len(self.contents):
      return self.contents
    else:
      return [self.contents.pop(random.randint(0, len(self.contents)-1)) for i in range(amount)]

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  ocurrencies = 0
  for i in range(num_experiments):
    initial_contents = copy.copy(hat.contents)
    draw = hat.draw(num_balls_drawn)
    match = True
    for color in expected_balls:
      if draw.count(color) < expected_balls[color]:
        match = False
    if match == True: ocurrencies +=1
    hat.contents = copy.copy(initial_contents)
  return ocurrencies/num_experiments