"""
Ali has two farms that grow plant A and plant B. Because of differing soil conditions, there are
differences in the yields and costs of growing crops on the two farms. The yields and costs are as
follows:
                         Farm 1    Farm 2
Plant A yield/acre (kg)    420    300
Cost/acre of plant A (RM)   90     50
Plant B yield/acre (kg)    200   250
Cost/acre of plant B (RM)   75   80

Farm 1 and farm 2 have 100 and 75 acres respectively available for cultivation. 21000 kg of plant A and
25000 kg of plant B must be grown. Determine a planting plan that will minimize the cost of meeting
these demands. 
"""

#Let
#W = the area of Farm 1 for planting plant A(acres)
#X = the area of Farm 1 for planting plant B(acres)
#Y = the area of Farm 2 for planting plant A(acres)
#Z = the area of Farm 2 for planting plant B(acres)
#model = the cost expected of meeting demands


#Objective Function = 90 *W + 75*X + 50*Y + 80 *Z
#Subject to 
# W + X <= 100
# Y + Z <= 75
# 420 * W + 300*Y >= 21000
# 200 * X + 250*Z >= 25000

from pulp import *

#initalize the model 
model = LpProblem('Resource Allocation Problem', LpMinimize)

#Define the decision Variable
W = LpVariable('Area_W', lowBound=0, cat ='Integer')
X = LpVariable('Area_X', lowBound=0, cat='Integer')
Y = LpVariable('Area_Y', lowBound=0, cat = 'Integer')
Z = LpVariable('Area_Z', lowBound=0, cat='Integer')


#Define Objective Function
model += 90 *W + 75*X + 50*Y + 80 *Z

#Define Constraints
model += W + X <= 100
model += Y + Z <= 75
model += 420 * W + 300*Y >= 21000
model += 200 * X + 250*Z >= 25000

#Solve the model
model.solve()
print("Growing {} acres of plant A in Farm 1". format(W.varValue))
print("Growing {} acres of plant A in Farm 2". format(X.varValue))
print("Growing {} acres of plant B in Farm 1". format(Y.varValue))
print("Growing {} acres of plant B in Farm 2". format(Z.varValue))
print("Total Cost Expected of meeting demands = RM{}".format(value(model.objective)))
print ("Status:", LpStatus[model.status])
