import pygal
from dice import Dice
dd=Dice()

results=[]
for roll in range(1000):
    result=dd.roll()
    results.append(result)

frequencies=[]
for v in range(1,dd.num_sides+1):
    frequency=results.count(v)
    frequencies.append(frequency)
 
hist=pygal.Bar()
hist.title='CCAV'
hist.x_labels=[1,2,3,4,5,6]
hist.x_tile='result'
hist.y_title='frequence of result'
hist.add('D6',frequencies)
#hist.render_to_png('Dice_png')
hist.render_to_file('dice_re.svg')