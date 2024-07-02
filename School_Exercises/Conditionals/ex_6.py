import random
weather = ['sunny', 'cloudy', 'rainy', 'snow', 'windy']
weather_shuffle = random.sample(weather, len(weather))
match weather_shuffle[0]:
    case 'sunny':
        print('')