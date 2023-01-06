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
HundredYard = 100

def UserInput():
    TargetDistance = float(input("What's your zeroing distance?"))
    return TargetDistance

def MOAscaling():
    Input = UserInput()
    ConvertedDistance  = (HundredYard/Input) 
    return ConvertedDistance

Scaling = MOAscaling()

def VerticalShift():
    VerticalShift = float(input("What's the vertical distance(by avg.)?"))  
    return VerticalShift

VerticalLength = VerticalShift()

def HorizontalShift():
    HorizontalShift = float(input("What's the horizontal distance(by avg.)?"))
    return HorizontalShift

HorizontalLength = HorizontalShift()

def OpticsMOA():
    MoaPerClick = float(input("What's the MOA per click on the optics?")) 
    return MoaPerClick

OpticsNotch = OpticsMOA()
      
def VerticalMOA_adjustment(): 
    VerticalClicks = ((Scaling*VerticalLength)/OpticsNotch)
    AdjustedVerticalClicks = math.ceil(VerticalClicks)
    return AdjustedVerticalClicks

def HorizontalMOA_adjustment():
    HorizontalClicks = ((Scaling*HorizontalLength)/OpticsNotch)
    AdjustedHorizontalClicks = math.ceil(HorizontalClicks)
    return AdjustedHorizontalClicks

def intToString (moaclick):
    result = str(moaclick)
    return result

VerticalMOA_adjustment()
HorizontalMOA_adjustment()
VerticalAdjustment = VerticalMOA_adjustment()
HorizontalAdjustment = HorizontalMOA_adjustment()

def seperation():
    print("\n" + "Output:")
    
def template():
    AdjustedVertical = intToString(VerticalAdjustment)
    AdjustedHorizontal = intToString(HorizontalAdjustment)
    seperation()
    print("The needed vertical adjustment is: ", AdjustedVertical, " clicks.")
    print("The needed horizontal adjustment is: ", AdjustedHorizontal, " clicks.")
    
template()