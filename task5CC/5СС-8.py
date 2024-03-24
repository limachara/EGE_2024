def Luhn(card):
    card = str(card)
    checksum = 0
    cardnumbers = list(map(int, card))
    for count, num in enumerate(cardnumbers):
        if count % 2 == 0:
            buffer = num * 2
            if buffer > 9:
                buffer -= 9
            checksum += buffer
        else:
            checksum += num
    return checksum % 25 == 0

for i in range(1000000000000000, 2234567891011121):
    if Luhn(i):
        print(i % 1000000)
        break