m, k = input().split(' ')

card_suit = {
    "1": "spades",
    "2": "clubs",
    "3": "diamonds",
    "4": "hearts",
}

card_value = {
    "14": "ace",
    "13": "king",
    "12": "queen",
    "11": "jack",
    "10": "ten",
    "9": "nine",
    "8": "eight",
    "7": "seven",
    "6": "six"
}

print(f'the {card_value[k]} of {card_suit[m]}')
