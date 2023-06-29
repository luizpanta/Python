def fizzBuzz(numero):

    if numero % 3 == 0 and numero % 5 != 0:
        saida = "Fizz"

    elif numero % 5 == 0 and numero % 3 != 0:
        saida = "Buzz"

    elif numero % 5 == 0 and numero % 3 == 0:
        saida = "FizzBuzz"

    else:
        saida = numero

    return saida