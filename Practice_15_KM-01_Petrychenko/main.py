def input_n(text):
    val = input(text)
    while type(val) != float:
        try:
            val = float(val)
        except:
            val = input("Enter correct number value:  ")
    return int(val)


def answer(val):
    print(f"Function value = {val}")


def main():
    greeting = '''
    Hello, please chooze funciton for calculate :
    1  -  fact 
    2  -  exp2
    3  -  exp3
    4  -  root2
    5  -  root3
    6  -  log
    7  -  ln
    8  -  lg
    
    '''
    print(greeting)
    while True:
        name = input('Enter the function number or its name (Example "8" or "exp2" ): ')
        if name == 'ln' or name == 'lg' or name == '7' or name == '8':
            b = input_n("Enter b (b>0): ")
            break
        elif name == 'log' or name == '6':
            a = input_n("Enter a (a>0, a!=1): ")
            b = input_n("Enter b (b>0): ")
            break
        elif name == "fact" or name == "exp2" or name == "exp3" or name == "root2" or name == "root3" \
                or name == '1' or name == '2' or name == '3' or name == '4' or name == '5':
            n = input_n("Enter natural number n: ")
            break
        else:
            print('You entered an invalid value for the function name')
            continue
    if name == '1' or name == 'fact':
        from factorial import factorial
        answer(factorial.fact(n))
    elif name == '2' or name == 'exp2':
        from exp__root import exponentiation
        answer(exponentiation.exp2(n))
    elif name == '3' or name == 'exp3':
        from exp__root import exponentiation
        answer(exponentiation.exp3(n))
    elif name == '4' or name == 'root2':
        from exp__root import root
        answer(root.root2(n))
    elif name == '5' or name == 'root3':
        from exp__root import root
        answer(root.root3(n))
    elif name == '5' or name == 'log':
        from logarithm import logarithm
        answer(logarithm.log(a, b))
    elif name == '6' or name == 'ln':
        from logarithm import logarithm
        answer(logarithm.ln(b))
    elif name == '7' or name == 'lg':
        from logarithm import logarithm
        answer(logarithm.lg(b))


main()
