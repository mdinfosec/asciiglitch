import random

while True: 
    print('')
    input('Glitch Me!')
 
    sym = ' ░▒▓█■▄•'
 
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    num3 = random.randint(1, 6)
    num4 = random.randint(1, 6)
	
    art1 = ''.join(random.sample(sym, len(sym)))
    art2 = ''.join(random.sample(sym, len(sym)))
    art3 = ''.join(random.sample(sym, len(sym)))
    art4 = ''.join(random.sample(sym, len(sym)))
    art5 = ''.join(random.sample(sym, len(sym)))
    art6 = ''.join(random.sample(sym, len(sym)))
 
    a = random.choice([art1, art2, art3, art4, art5, art6]) * num1
    b = random.choice([art1, art2, art3, art4, art5, art6]) * num2
    c = random.choice([art1, art2, art3, art4, art5, art6]) * num3
    d = random.choice([art1, art2, art3, art4, art5, art6]) * num4
 
    print('')
    for i in range(random.randint(2, 5)):
        print(' ',a)
        print(' ',b)
        print(' ',c)
        print(' ',d)
    print('')
