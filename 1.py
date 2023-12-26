"""
Вводиться рядок слів, розділених пропусками.
Знайти найдовше слово і вивести його на екран.
Розглянути випадок, коли найдовших неоднакових слів може бути кілька.
Автор: Мотовилець Марія
"""

n = input("Введіть рядок слів розділений пропусками: ")

words = n.split()

max_word = []
max_length = 0
for word in words:
    length = len(word)
    if length > max_length:
        max_length = length

for word in words:
    if len(word) == max_length:
        print(word,end=' ')
