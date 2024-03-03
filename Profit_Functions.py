import Max_Regen_Yield_Function as mryf
import Crop_Data as cd
# function that calls the max_regen_yield function to calculate the profit of a regenerative crop
# eventually: new function that loops through the dictionary, calls calculate_regen_profit and returns the list
# then maybe sort it?

'''
These functions ultimately create a list of crops in order from most to least profitable 
given a plant-date and the season
'''


def calculate_non_regen_profit(date, crop_name):
    if crop_name in cd.SpringCropData:
        # s = standard_sales
        # c = cost
        crop = cd.SpringCropData[crop_name]  # crop is the sub-dictionary for crop_name in the parameters
        ld = crop.get('last_day', 0)
        if date > ld:
            # crop won't produce in time
            # print('crop wont produce in time')
            s = 0
            c = crop.get('cost', 0)
            p = s - c
            return p
        else:
            s = crop.get('standard_sales', 0)
            c = crop.get('cost', 0)
            p = s - c
            return p
    # what is this function capable of outputting? Should I set bounds?


def calculate_regen_profit(date, crop_name):
    # p = profit = max_yield * standard_sales - cost
    # c = cost
    # s = standard_sales
    s, c = 0, 0
    # do i need the below line if the same if statement is in the main function?
    # if crop_name in SpringCropData:
    crop = cd.SpringCropData[crop_name]
    c = crop.get('cost', 0)
    s = crop.get('standard_sales', 0)
    p = mryf.max_regen_yield(date, crop_name) * s - c
    return p
    # what is this function capable of outputting? Should I set bounds? I don't think I need to


def calculate_profit(date, crop_name):
    if crop_name in cd.SpringCropData:
        # if the crop doesn't regrow
        if cd.SpringCropData[crop_name]['days_to_regrow'] == 0:
            p = calculate_non_regen_profit(date, crop_name)
        else:
            p = calculate_regen_profit(date, crop_name)
        return p
    else:
        print(crop_name, "is not in the list of available crops")


def create_sorted_profit_list(date, crop_dict):
    profit_dict = {}
    for crop_name in crop_dict:
        profit_dict[crop_name] = calculate_profit(date, crop_name)
    # put the values in a dictionary
    # sort the dictionary by profit
    profit_dict = {k: v for k, v in sorted(profit_dict.items(), key=lambda item: item[1], reverse=True)}
    # I chat-gpt-ed the above line and I don't fully understand it, I'll figure it out later
    return profit_dict


# def croptimize(date, season):  # season is probably gonna go something like "if season is spring, use springCropData"
# rn we're just dealing with Spring
