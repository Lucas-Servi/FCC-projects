class Category:

  def __init__(self, name):
    self.name = name
    self.ledger = []
  
  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    else:
      return True


  def deposit(self, amount, description = ""):
    self.ledger.append({"amount": amount, "description": description})
  
  def withdraw(self, amount, description = ""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False
    
  def get_balance(self):
    tot = 0
    for i in self.ledger:
      tot += i["amount"]
    return tot

  def transfer(self, amount, objname):
    if not self.check_funds(amount):
      return False

    tranfw = "Transfer to " + objname.name
    self.withdraw(amount, tranfw)

    tranfd = "Transfer from " + self.name
    objname.deposit(amount, tranfd)
    return True

  def __str__(self):
    title = f"{self.name:*^30}\n"
    items = ""
    for i in self.ledger:
      print(i)
      items += f"{i['description'][0:23]:23}" + f"{i['amount']:>7.2f}" + "\n"
    return title + items + "Total: " + str(self.get_balance())




def create_spend_chart(categories):
  title = "Percentage spent by category\n"
  balance = []
  chart = []
  names = []
  tot_spent = 0
  longest = 0
  for cate in categories:
    if len(cate.name) > longest:longest = len(cate.name)
    cate_spent = sum((value['amount'] for value in cate.ledger if value['amount'] < 0))
    balance.append(cate_spent)
    tot_spent += cate_spent
    names += [cate.name.capitalize()]
    
  print(balance)
  percentages = [(i/tot_spent)*100 for i in balance] 
  print(percentages)
  f = list(x/tot_spent for x in balance)
  print(f)
  
  for i in range(12 + longest):
    line = ''
    if i < 11:
      value = (10-i)*10
      line += f"{value:>3}|"
      dots = ("   " if elem < value else " o " for elem in percentages)
      line += "".join(dots) + " "
    elif i == 11:
        line = "    " + "---"*len(percentages) + "-"
    else:
        letters = list(" "+ name[i-12] +" " if len(name) > i-12 else "   " for name in names)
        line += "    "+ "".join(letters) + " "
    chart.append(line)
    
  return title + "\n".join(chart)