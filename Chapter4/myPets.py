pets = ['Baxter', 'Misty', 'Alan', 'Kora', 'Venice', 'Dipsy']

print('Enter a pet name')
petName = input()

if petName not in pets:
    print('Not my pet')
else:
    print('That is my pet.')