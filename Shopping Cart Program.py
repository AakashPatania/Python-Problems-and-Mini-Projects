## Shopping Cart Program ####


# foods = []
# prices = []
# total = 0

# while True:
#     food = input("Enter the food you want to order: ")
#     if food.lower() == 'q':
#         break
#     else:
#         price = float(input("Enter the price of the food items you ordered: $"))
#         foods.append(food)
#         prices.append(price)
        
# print("---- YOUR CART -----")
# for i in foods:
#     print(i)
    
# for price in prices:
#     total = total + price

# print()
# print(f"Your total is: ${total}")


foods = []
prices = []
total = 0

while True:
    food = input("Enter the food you want to order: ")
    price = float(input("Enter the price of the food items you ordered: $"))
    foods.append(food)
    prices.append(price)
    

    ## Validation Loop
    while True:
        More = input("Anything else? (y/n): ") 
        if More.lower() in ["y","n"]:
            break      # breaking the validation loop if the input is correct and it continues to ask
        else:
            print("Enter the valid response")

    if More.lower() == 'n':
        break   # stop the main loop it times to print the informations which we got and the final shopping cart                   

        
print("---- YOUR CART -----")
for i in foods:
    print(i)
    
for price in prices:
    total = total + price

print()
print(f"Your total is: ${total}")
