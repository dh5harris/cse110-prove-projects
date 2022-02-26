# inputs from user
temp = int(input('What is the tempterature outside? '))
scale = input('Fahrenheit or Celsius (F/C)? ')

# function to change from celsius to fehrenheit
def temperature(scale, temp):
    # fahrenheit = (celsius * 9/5) + 32 
    # celsius = (fahrenheit - 32) * (5/9)
    if scale.lower() == 'c':
        fahrenheit = (temp * 9/5) + 32
        #print(fahrenheit)
    elif scale.lower() == 'f':
        fahrenheit = float(temp)
    return fahrenheit


fahrenheit = temperature(scale, temp)

# function to find the windchill
# t = temp in fahrenheit, v = windspeed in mph
def wind_chill(t, v):
    return 35.74 + (0.6215 * t) - (35.75 * (v ** 0.16)) + (0.4275 * t * (v ** 0.16))

    
for wind_speed in range(5, 61 ,5):
    windchill = wind_chill(fahrenheit, wind_speed)
    print(f'At temperature {fahrenheit}F, and the wind speed {wind_speed} mph, the windchill is: {windchill:.2f}F')