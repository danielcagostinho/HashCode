import math

def get_score(tags1, tags2):
    common  = len(list(set(tags1) & set(tags2)))
    unique1 = len(set(tags1)) - common
    unique2 = len(set(tags2)) - common
    return min(common, unique1, unique2)





               
