def fizzbuzz():
    for i in range(1, 101):
        fizz = 'fizz' if i % 3 == 0 else ''
        buzz = 'buzz' if i % 5 == 0 else ''
        print(f'{fizz}{buzz}' or i)


fizzbuzz()
