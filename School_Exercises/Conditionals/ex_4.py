import random
weather = ['rainy', 'sunny', 'cloudy', 'snowy', 'icy']
weather_shuffle = random.sample(weather, len(weather))
print(weather_shuffle)
if weather_shuffle[0] == 'rainy':
    print('Grab your umbrella.')
elif weather_shuffle[0] == 'sunny':
    print("It's a beautiful day!")
else:
    print("Let's stay inside.")
