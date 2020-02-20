import winsound
import time
def Morze(word):
    morze={
            'а': '.-',
            'б': '-...',
            'в': '.--',
            'г': '--.',
            'д': '-..',
            'е': '.',
            'ж': '...-',
            'з': '--..',
            'и': '..',
            'й': '.---',
            'к': '-.-',
            'л': '.-..',
            'м': '--',
            'н': '-.',
            'о': '---',
            'п': '.--.',
            'р': '.-.',
            'с': '...',
            'т': '-',
            'у': '..-',
            'ф': '..-.',
            'х': '....',
            'ц': '-.-.',
            'ч': '---.',
            'ш': '----',
            'щ': '--.-',
            'ъ': '.--.-.',
            'ы': '-.--',
            'ь': '-..-',
            'э': '..-..',
            'ю': '..--',
            'я': '.-.-'}
    #word = input().lower()
    result = []
    for elem in word:
        result.append(morze[elem])
    print(result)
    return result
frequency = 1000
while True:
    cont = Morze(input().lower())
    for s in cont:
        for symbol in s:
            if symbol == '.':
                winsound.Beep(frequency, 100)
            elif symbol == '-':
                winsound.Beep(frequency, 700)
        time.sleep(0.2)













