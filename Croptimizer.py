import Croptimize_Function as cf
import Crop_Data as cd

'''
This file collects input and runs the croptimize function on said input
'''

# for now this is just gonna be full of comments, but it will eventually be part of the working project
# the below steps are subject to change -
# - and are what the program will do in what order, not my personal plan, ig this is my pseudocode

# Goal: Create a dictionary of key-value pairs of "crop"-"count" given a budget and a date
# things to account for: if it's the e.g., 20th, not all crops will grow in time, so not every one can be used -
# - (this would be where 'last_day' comes in handy, it's not something the code needs to calculate)

# Step 1: [DONE] Calculate the max yield of each crop given a date
# - in a previous version i found the cheapest crop, is that something i'd even need?

# Step 2: [DONE] Calculate the profit of each crop given a date -
# - and order them in a list/dictionary from most to least profitable -
# - I'll call it something like "crop_profit_list"

# Step 3: Generate a new list/dictionary containing the permutations of the most profitable purchases given a budget -
# - the basis of how this would work would go like: find the most profitable crop, -
# - buy that until you can't afford it, -
# - then repeat for the next affordable most profitable crop until you can't afford anymore

# I'm wondering if it's as simple as "there will only be one most profitable crop until you can't afford it" -
# - Like, you buy 10 parsnips or buy 5 cauliflower, even tho a single cauliflower is more profitable, will there -
# - ever be a case where more of a cheaper crop is the better choice? What math would I need to figure this out?

# Regarding the above line, for now, I think I'm gonna stick with my original idea, would it be different if i -
# - did one for the day of vs a larger span of time?

'''
# Get the season
season = input('What season is it? \n')
season = season.lower()
if season == 'spring':
    season = cd.SpringCropData
elif season == 'summer':
    season = cd.SummerCropData
elif season == 'fall':
    season = cd.FallCropData
elif season == 'winter':
    season = cd.WinterCropData
'''

# get the date
date = input('What is the date? \n')
date = int(date)

# Get the players budget
budget = input('What is your budget? \n')
budget = int(budget)

# Print the shopping list and how much money you have left
print(cf.croptimize(budget, date))

