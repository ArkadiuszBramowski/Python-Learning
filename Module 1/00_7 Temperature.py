temperature = float(input('How many degrees we have today'))

if temperature <= 10:
    print('Stay home')
elif 10 < temperature < 20:
    print('Take jacket')
else:
    print('Have fun')
