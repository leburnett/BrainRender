def get_coords(obj):
    """[Get the XYZ coordinates of an object. Can take a dict, Pandas Dataframe or Series]
    
    Arguments:
        obj {[dict, DataFrame, Series]} -- [some variable with fields X Y Z from which the coordinates can be extracted]
    """
    if len(obj) == 0: raise ValueError

    try:
        z,y,x =  obj["z"].values[0], obj["y"].values[0], obj["x"].values[0]
    except:
        z,y,x = obj["z"], obj["y"], obj["x"]

    if not isinstance(z, float): raise ValueError("Could not extract coordinates from: {}".format(obj)) 
    else: 
        return z,y,x

def flatten_list(lst):
    flatten = []
    for item in lst:
        if isinstance(item, list):
            flatten.extend(item)
        else:
            flatten.append(item)
    return flatten


def get_slice_coord(bounds, n):
    """
        # Given the bounds of an actor, return the point that 
        # corresponds to the n% of the bounds range

        bounds should be a list of two floats
        n should be a float in range 0, 1
    """
    if not isinstance(bounds,(list, tuple)) or not isinstance(bounds[0],float) or not isinstance(bounds[1],float):
        raise ValueError("bounds should be a list or tuple of floats: {}".format(bounds))
    if not isinstance(n, (int, float)):
        raise ValueError("n should be a float")
    if n < 0 or n > 1:
        raise ValueError("n should be in range [0, 1]")


    b0, b1 = bounds
    delta = b1 - b0

    return b0 + delta*n