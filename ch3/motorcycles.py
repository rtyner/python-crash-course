motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(first_owned)
print(f"The first motorcycle I owned was a {first_owned.title()}")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)