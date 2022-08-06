############################ Process Data

def average(Array,idx,offset):
    return (Array[(idx)]+Array[(idx-offset)])/2

def D(Array,idx,offset):
    return (Array[(idx)]-Array[(idx-offset)])/(offset)
