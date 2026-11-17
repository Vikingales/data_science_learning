# declare variables max_number = None and min_number = None
# request numbers from the user via input
# check whether the user entered 'done' and exiting the program via break
# try convert the input to a float number via try
# if this is not a number, display an error and return to the beginning of the loop
# if a number, compare with None (if None) and compare the number with the largest max_number (if >max_number)
# if true, write the resulting number to max_number
# compare with None and with min_number (if < min_number)
# if it is less, then write this number in min_number
# outside the loop display max_number and min_number

max_number = None
min_number = None
while True:
    number = input('Enter number: ')
    if number == 'done':
        break
    try:
        number = float(number)
        if max_number is None or number > max_number:
            max_number = number
        if min_number is None or number < min_number:
            min_number = number
    except:
        print('Input error')
        continue
print(max_number, min_number)