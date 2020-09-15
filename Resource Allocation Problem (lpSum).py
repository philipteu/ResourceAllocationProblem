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

from pulp import *
import pandas as pd

#initalize the model 
model = LpProblem('Resource Allocation Problem', LpMinimize)

#Define the decision Variable
plant =['A', 'B']
farm  =['1', '2']
cost= {('A','1'): 90, ('A','2'): 50, ('B','1'): 75, ('B','2'): 80 }
grow = {('A','1'): 420, ('A','2'): 300, ('B','1'): 200, ('B','2'): 250 }
demand= {'A': 21000, 'B': 25000}
area = {'1': 100, '2': 75}

area_p = LpVariable.dicts("Area",[(p,f) for p in plant for f in farm],
                        lowBound=0, cat='Integer')

#Define Objective Function
model += lpSum([cost[(p,f)] * area_p[(p,f)] for p in plant for f in farm])

#Define Constraints
for f in farm:
    model += lpSum([area_p[('A', f)]] + [area_p[('B', f)]])== area[f]  
    
for p in plant: 
    model += lpSum([area_p[(p, '1')]* grow[(p,'1')]] + [area_p[(p, '2')] * grow[(p,'2')]])== demand[p] 



#Solve the model
model.solve()
print ("Status:", LpStatus[model.status])
o = [{'Farm_1':area_p[(p,'1')].varValue, 'Farm_2':area_p[(p,'2')].varValue }for p in plant]
o= pd.DataFrame(o, index = plant)
o = o.rename(index = lambda x: 'Plant_'+ x)
print(o)
print("Total Cost Expected of meeting demands = RM{}".format(value(model.objective)))
print ("Status:", LpStatus[model.status])