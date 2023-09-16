# Create a tuple containing numbers divisible by 6 from 12 to 1024 and answer the following questions:
# How many of these numbers are there?
# Display first three numbers
# Penultimate number
# every sixth element counting from the fourth
# every third element counting from the end
# what is the average of the last ten values


numbers = tuple(range(12, 1024, 6))

print('Number of values', len(numbers))

print('First three numbers', numbers[:3])

print('Penultimate number', numbers[-2:])

print('Every sixth number', numbers[3::6])

print('Every third number', numbers[::-3])

print('Average of last numbers', sum(numbers[-10::]) / 10)
