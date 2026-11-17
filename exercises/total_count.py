total = 0.0
count = 0
while True:
    number = input('Enter a number: ')
    if number == 'done':
        break
    try: 
            number = float(number)
            total += number
            count += 1
    except:
        print('Invalid input')
        continue
if count > 0:
    average = total / count
    print(total, count, average)
else:
     print('No numbers were entered.')