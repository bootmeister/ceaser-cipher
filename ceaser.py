lang = input("""Ingilicce: EN
             Turkce: TR\n"""
def shift(word, num, way):
    if lang == "EN":
        alph = "abcdefghijklmnopqrstuvwxyz"
    elif lang == "TR":
        alph = "abc1defg2h3ijklmno4prs5tyvu6vyz"
    indices = [alph.index(char) + num for char in word]
    if way is True:
        indices = [index - (index // len(alph)) * len(alph) if index >= len(alph) else index for index in indices]
    elif way is False:
        indices = [index + (index // len(alph)) * len(alph) if index >= len(alph) else index for index in indices]

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

way = bool(int(input("Sifrelemek icin 1 e,\nSifre donusturmek icin 0 a basiniz")))


if way is True:
    print("""Sezar sifrelmesi:
    Lutfen bir kelime ve bir kaydirma sayisi saglayiniz.\n""")

    while True:
        num = input("Sayi: ")
        try:
            num = int(num)
            break
        except ValueError:
            print("Lutfen bir sayi giriniz\n")

    result = []
    go_on = True
    while go_on is True:
        word = "123"
        while not isalpha(word):
            word = input("Kelime: ")
            if isalpha(word) == False:
                print("Lutfen kelimenizde sayi ya da ozel karakter kullanmayiniz!")
        word = word.lower()
        result.append(shift(word, num, way))
        while True:
            try:
                go_on = bool(int(input("Devam etmek icin herhangi bir sayiya,\nDurmak icin 0a basiniz: ")))
                break
            except ValueError:
                print("Lutfen sadece sayi giriniz!")

if way is False:
    print("""Seazar Sifresi Cozme:
          Sifreli Kelimeyi giriniz
          Bilgisayar muhtemel sonuclari gosterecektir""")

    while go_on is True:
     while True:
        num = input("Sayi: ")
        try:
            num = int(num)
            break
        except ValueError:
            print("Lutfen bir sayi giriniz\n")

       word = "123"
        while not isalpha(word):
            word = input("Kelime: ")
            if isalpha(word) == False:
                print("Lutfen kelimenizde sayi ya da ozel karakter kullanmayiniz!")
        word = word.lower()
        result.append(shift(word, num, way))
        while True:
            try:
                go_on = bool(int(input("Devam etmek icin herhangi bir sayiya,\nDurmak icin 0a basiniz: ")))
                break
            except ValueError:
                print("Lutfen sadece sayi giriniz!")

print(" ".join(result))
