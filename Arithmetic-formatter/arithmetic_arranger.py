def arithmetic_arranger(problems, answer = False):
  Firstl = ""
  Secondl = ""
  Thirdl = ""
  Fourl = ""
  operators = ("+", "-")
  opcount = 0
  if len(problems) > 5:
    return "Error: Too many problems."
  for operation in problems:
    opcount += 1
    words = operation.split()
    if words[1] in operators:
      if not words[0].isdigit() or not words[2].isdigit(): 
        return "Error: Numbers must only contain digits."

      greater = len(words[0]) 
      if len(words[0]) < len(words[2]): greater = len(words[2])

      if greater > 4: return "Error: Numbers cannot be more than four digits."

      Firstl += "  " + " " * (greater - len(words[0]))+ words[0]
      Secondl += words[1] + " " + " " * (greater - len(words[2])) + words[2]
      Thirdl += "-" * (greater+2)
      ans = str(eval(operation))
      Fourl += " " * (greater+2 - len(ans)) + ans 
      if opcount<len(problems):
        Firstl += "    "
        Secondl += "    "
        Thirdl += "    "
        Fourl += "    "
    else:
      return "Error: Operator must be '+' or '-'."
  if answer:
    return Firstl + "\n" + Secondl + "\n" + Thirdl + "\n" + Fourl
  else:
    return Firstl + "\n" + Secondl + "\n" + Thirdl