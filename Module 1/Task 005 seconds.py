# A certain program counts time only in seconds and resets itself every day. Try to write it in the classic form
# time presented in the format: 23400, 34200, 81000. The result should be: 6:30, 9:30, 22:30
# Prepare a program that will transform any value provided by the user into a readable form.

sec = int(input('Give a number: '))
hr = sec // 3600
minute = (sec % 3600) / 60
print(f'Hour after transferring minutes is {hr:02.0f}:{minute:02.0f}')
