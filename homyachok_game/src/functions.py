import variables

items = {
    '1': {
        "multiplier" : 5,
        "price" : 100
    }
}

def shop():
    user_input = input(f"""
вы хотите купить множитель {items['1']['multiplier']} за {items['1']['price']}?  
1 - да
2 - нет
> """)
    if user_input == '1':
        price = items['1']['price']
        if(variables.score >= price):
            variables.multiplier = items['1']['multiplier']
            variables.score -= price
            items['1']['multiplier'] += 10
            items['1']['price'] += 100
        else:
            input("""
недостаточно валюты
> """)


