def prime_game():
    print('welcome to priming!')
    print('what is your first number?')
    firstNumber = input()
    print('what is your second number?')
    secondNumber = input()
    print('do you want to start primin??')
    myAnswer = input()
    if myAnswer == 'yes':
        print('alright, alright, alright')
        int_firstNumber = int(firstNumber)
        int_secondNumber = int(secondNumber) + 1
        print('your range of numbers is ' + str(list(range(int_firstNumber, int_secondNumber))))
        print('Let\'s see what ones are prime shall we?')
        
        prime_numbers = 0
        def is_prime_number(x):
            if x >= 2:
                for y in range(2,x):
                    if not (x % y):
                        return False
            else:
                return False
            return True
        
        for i in range(int_firstNumber, int_secondNumber):
            if is_prime_number(i):
                prime_numbers += 1
                print(i)
                
        print('you have ' + str(prime_numbers) + ' prime numbers.')
    
    else:
        print('You\'re no fun.')

prime_game()