def shift(word, num):
    alph = "abcdefghijklmnopqrstuvwxyz"
    indices = [alph.index(char) + num for char in word]
    indices = [index - (index // 26) * 26 if index >= 26 else index for index in indices]
    crypto = "".join([alph[index] for index in indices])
    return crypto


def isalpha(word):
    has_num = False
    for char in word:
        try:
            char = int(char)
            has_num = True
        except ValueError:
            pass
    return not has_num

print("""Sezar sifrelmesi:
Lutfen bir kelime ve bir kaydirma sayisi saglayiniz.\n""")

while True:
    num = input("Sayi: ")
    try:
        num = int(num)
        break
    except ValueError:
        print("Lutfen bir sayi giriniz")

result = []
go_on = True
while go_on is True:
    word = "123"
    while not isalpha(word):
        word = input("Kelime: ")
        if isalpha(word) == False:
            print("Lutfen kelimenizde sayi ya da ozel karakter kullanmayiniz!")
    word = word.lower()
    result.append(shift(word, num))
    while True:
        try:
            go_on = bool(int(input("Devam etmek icin herhangi bir sayiya,\nDurmak icin 0a basiniz: ")))
            break
        except ValueError:
            print("Lutfen sadece sayi giriniz!")
print(" ".join(result))
