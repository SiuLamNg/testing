#Function: MOA_Calculator
# User will be prompted to enter the following(s):
# 1. Target Distance
# 2. Vertical Shift
# 3. Horizontal Shift
# 4. MOA Adjustment Unit(per click) 
# 
# Output Requirment:
# [The calculator will be output the needed
# moves(clicks) to the user based on their 
# zeroing result.] - # int clicks

import math
Ratio = 1.0936132983 # 1 meter equals to = 1.0936132983 yards.

def MetricsToImperial(input):
  Yard = Ratio*input
  return Yard

def ImperialToMetrics(input):
  Meter = 1/Ratio
  return Meter

def UserInput():
  TargetDistance = float(input("What's your zeroing distance?"))
  VerticalShift = float(input("What's the vertical distance(by avg.)?"))  
  HorizontalShift = float(input("What's the horizontal distance(by avg.)?"))
  MoaPerClick = float(input("What's the MOA per click on the optics?"))
  return TargetDistance, VerticalShift, HorizontalShift, MoaPerClick

#def DistanceConversion(TargetDistance):
    Hundredyards = 100
    ConvertedDistance = TargetDistance/Hundredyards 
    return ConvertedDistance

    
#def AdjustmentCalculation(VerticalShift, HorizontalShift):
    Shift = ConvertedDistance/MoaPerClick
    return Shift
    



## 1 MOA = 1 inches in 100 yards
## 1 cm =  0.393701 inches
## 1 inches = 2.5399986284cm

## 500 yards, 5 inches, 4 inches, 0.5 moa per click
## 
## 100yards/TargetDiatance => converted distance
## 5
## converted distance/MoaPerClick - > (VerticalShift, Horizontal Shift)
## 5/0.5
## 10
##
