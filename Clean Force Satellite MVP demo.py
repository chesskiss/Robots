Voice = None
x = None
 
 
while not (changeV2T(0)):
  tankEv3On(-10,10)
tankEv3Off(1)
Voice = True
while Voice:
  if changeV2T(0):
    Voice = False
    waitFaceName(2,"hello")
    resetSensor("AngleAccreset")
    T2V(0,'Initiating satellite course. Beginning lunch sequence',100,0)
    while not ((compareSensor("AngleScalarCompare",0,4,20)) and (compareSensor("AngleScalarCompare",0,2,(-20))) and (fdcpp_compare(0,4,15)) and (fdcpp_compare(0,2,(-15)))):
      tankEv3On(((0 - (fdcpp()[0])) * 0.4),((0 + (fdcpp()[0])) * 0.4))
      if (fdcpp_compare(0,2,(-10))) and (fdcpp_compare(0,4,10)):
        while not ((fdcpp_compare(0,4,(-10))) or (fdcpp_compare(0,2,10))):
          tankEv3Off(1)
x = 2
while not (x === 80):
  steeringEv3On(0,x)
  x = x + 1
tankEv3Off(0)