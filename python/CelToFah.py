fahrenheit = int(input('Please enter your fahrenheit: '))

def to_celsius(fahrenheit):
    temp_f = (5/9) * (fahrenheit - 32)
    return temp_f

tempature = to_celsius(fahrenheit)
print(tempature)    

# Converts temp to celsius
