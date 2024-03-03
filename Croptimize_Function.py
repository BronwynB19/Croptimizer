# I might eventually copy/paste this function into Croptimizer.py and delete this one
# It depends on the level of organization I want
import Crop_Data as cd
import Profit_Functions as p
'''
This function takes a budget and a date, and uses the profit functions to create a list of how much of each crop 
you should buy to make the most money.
Additionally, it also returns the amount of money left over if there's any
'''

'''
Rn the plan is buy most profitable crop until you can't anymore, buy next one until you can't, etc.
I don't know for a fact if that's the most profitable solution, but it's what I'm going with for now.
I will test it in the future
'''


# creates and returns a dictionary of key:value pairs -
# - where the key is the name of the crop and the value is the quantity of that crop
def croptimize(budget, date):
    # Initialize the return value
    shopping_list = {}
    leftover = budget
    for crop in cd.SpringCropData:
        shopping_list[crop] = 0
    # Initialize the dictionary of most profitable crops
    profitable_crop_dictionary = p.create_sorted_profit_list(date, cd.SpringCropData)
    # print(profitable_crop_dictionary)
    for crop, data in profitable_crop_dictionary.items():
        cost = cd.SpringCropData[crop]['cost']
        last_day = cd.SpringCropData[crop]['last_day']
        # while you can afford the most profitable crop
        if last_day >= date:
            while budget >= cost:
                # add one to the value of the most profitable crop you can afford
                shopping_list[crop] += 1
                # subtract the cost from budget
                budget -= cost
                leftover -= cost
    return shopping_list, leftover


'''
# use budget = 200, date = i to see if the output is the correct information (1-28; i+1)
# budget = i, date = 10 also seems to be a good test case (0-500; i+25)
i = 0
while i <= 5000:
    print('budget:', i, croptimize(i, 10))
    i += 25
'''

"""
shop_list = croptimize(1000, 15)
print(shop_list)
shop_list = croptimize(1500, 16)
print(shop_list)
"""
