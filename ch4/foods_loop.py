my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')

for i in my_foods:
    print(f"Some of the favorite foods are {i}")
for i in friend_foods:
    print(f"Some of my friends favorite foods are {i}")    
