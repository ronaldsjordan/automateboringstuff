# Generate Collatz sequence.
def collatz(number):
    if number % 2 == 0:
        return int(number / 2)
    else:
        return 3 * number + 1

counter = 0
while True:
    print('Enter a positive integer to start with')
    try:
        number = int(input())
        if number < 1:
            continue
        else:
            break
    except ValueError:
        print('Invalid Input')
        continue

while number != 1:
    number = collatz(number)
    print(str(number))
    counter += 1

print('It took ' + str(counter) + ' times to reach 1')


