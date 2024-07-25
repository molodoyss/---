import time
import functions
import variables
import random



while True:
    print(f"Твои очки хомячка: {variables.score}")
    user_input = input("""
тыкай на хомячкка
        *-----------*
        |           |
        |  хомячок  |
        |           |
        *-----------*
shop - магазин
exit - выход
vivod - вывести деньги
> """)

    if(user_input == 'shop'):
        time.sleep(0.5)
        functions.shop()
    if(user_input == 'exit'):
        time.sleep(0.5)
        break
    if(user_input == 'vivod'):
        time.sleep(0.5)
        print(f"вы вывели {round(variables.score / random.randint(25, 50))}")
        input("> ")

    else:
        variables.score += variables.multiplier

