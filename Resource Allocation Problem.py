# -*- coding: utf-8 -*-

#Resource Allocation Problem (Simple Linear Programming)
#We’re consulting for a boutique car manufacturer, producing luxury cars.
#They run on one month (30 days) cycles, we have one cycle to show we can provide value.
#There is one robot, 2 engineers and one detailer in the factory. The detailer has some holiday off, so only has 21 days available.

#The 2 cars need different time with each resource:

#Robot time: Car A – 3 days; Car B – 4 days.
#Engineer time: Car A – 5 days; Car B – 6 days.
#Detailer time: Car A – 1.5 days; Car B – 3 days.

#Car A provides $30,000 profit, whilst Car B offers $45,000 profit.
#At the moment, they produce 4 of each cars per month, for $300,000 profit. Not bad at all, but we think we can do better for them.

#Objective Function = 30000A + 45000B
#Subject to 
# 3A + 4B <= 30 
# 5A + 6B <= 60
# 1.5A + 3B <= 21
# A >= 0
# B>= 0

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
print("Total Cost Estimated = ${}".format(value(model.objective)))
print ("Status:", LpStatus[model.status])
