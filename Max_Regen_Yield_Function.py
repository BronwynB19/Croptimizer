import math
import Crop_Data as cd

'''
This function calculates the maximum yield of a regenerative crop given a plant-date
'''


def max_regen_yield(date, crop_name):  # what do the parameters need to be?
    # x = date planted = date
    # g = days to grow = crop_dict[not sure][days_to_grow]
    # r = days to regrow = crop_dict[not sure][days_to_regrow]
    # m = max yield
    x = date
    g, r, m = 0, 0, 0
    # if the name of the crop is in the dictionary
    if crop_name in cd.SpringCropData:
        # assign it to a new variable called crop_info (not entirely sure of why here)
        crop_info = cd.SpringCropData[crop_name]
        g = crop_info.get('days_to_grow', 0)
        r = crop_info.get('days_to_regrow', 0)
        # Should I make an "if days to regrow = 0"?
        # I'm struggling slightly because I'm doing this as I go, it might be a good practice to pseudocode it first
        m = (1/r)*(28-(g+x))+1
        m = math.floor(m)
    else:
        print("There is no", crop_name, 'in the dictionary')
    # set m to zero if the initial calculation produces a negative number
    if m < 0:
        m = 0
    return m

# rn it's case-sensitive, but since this is going to be an automation problem, i don't think i need to worry
# ask friends what kind of errors they think could arise
