##############

## If Algorithm Returns 1 Then buy
## Else IF it REturns -1 Then Sell
## If it Returns 0 Dont Do Anything


def algo1(Acceleration,Velocity):
    if(Acceleration>0):
        if(Velocity>1):
            return 1
        if(Velocity<0):
            return -1
    else:
        return 0