# J & K's Diner

dinnerMenu = ['STEAK', '15', 'CHICKEN', '12', 'PORK', '11', 'SALAD', '12']
sidesMenu = ['FRIES', 'RICE', 'VEGGIES', 'SOUP', '1']

dinnerSelect = input("Please select an entree: ").upper()

if dinnerSelect == dinnerMenu[0]:
  print("Excellent choice! The price for that entree is {}".format(dinnerMenu[1]))
  input("And how would you like your steak?")
  dinner_main = [dinnerMenu[0], dinnerMenu[1]]
elif dinnerSelect == dinnerMenu[2]:
  print("Wonderful! The price for that entree is {}".format(dinnerMenu[3]))
  dinner_main = [dinnerMenu[2], dinnerMenu[3]]
elif dinnerSelect == dinnerMenu[4]:
  print("Tasty! The price for that entree is {}".format(dinnerMenu[5]))
  dinner_main = [dinnerMenu[4], dinnerMenu[5]]
elif dinnerSelect == dinnerMenu[6]:
  print("One of our most popular! The price for that entree is {}".format(dinnerMenu[7]))
  dinner_main = [dinnerMenu[6], dinnerMenu[7]]
else:
  print("Please make a valid selection")
  

  
sidesSelect = input("You also have your choice of two sides to go with your meal. What is the first side you would like? ").upper()

if sidesSelect == sidesMenu[0] or sidesSelect == sidesMenu[1] or sidesSelect == sidesMenu[2] or sidesSelect == sidesMenu[3]:
  print("Ok.")
  first_side_price = sidesMenu[4]
else:
  print("We currently do not offer that on our menu.")
  

sidesSelect = input("And what would you like for your second side?").upper()

if sidesSelect == sidesMenu[0]:
  print("Very good! The price for those sides is {}".format(sidesMenu[4]))
  side_price = sidesMenu[4]
elif sidesSelect == sidesMenu[1]:
  print("Super! The price for those sides is {}".format(sidesMenu[4]))
  side_price = sidesMenu[4]
elif sidesSelect == sidesMenu[2]:
  print("Nice! The price for those sides is {}".format(sidesMenu[4]))
  side_price = sidesMenu[4]
elif sidesSelect == sidesMenu[3]:
  print("Sounds good! The price for those sides is {}".format(sidesMenu[4]))
  side_price = sidesMenu[4]
else:
  print("We currently do not offer that on our menu.")
  

dinnerTotal = int(dinner_main[1]) + int(side_price) + int(first_side_price)
print("The total cost for your dinner comes to {}".format(dinnerTotal))