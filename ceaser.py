lang = input("""Ingilicce: EN
             Turkce: TR
             Kendi alfabeni tanimlamak icin: CUS
             giriniz\n""")
if lang == "EN":
    alph = "abcdefghijklmnopqrstuvwxyz"
elif lang == "TR":
    alph = "abcçdefgğhıijklmnoöprsştuüvyz"
if lang == "CUS":
    alph = input("Alfabenizi giriniz:\n")

def shift(word, num, way):
    if way is True:
        indices = [alph.index(char) + num for char in word]
    elif way is False:
        indices = [alph.index(char) - num for char in word]
    indices = [index - (index // len(alph)) * len(alph) if index >= len(alph) else index for index in indices]

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
    print(" ".join(result))


results = []
word_num = 0
word_count = 0
go_on = True
while go_on is True:
    if way is False:
        print("""Seazar Sifresi Cozme:
              Sifreli Kelimeyi giriniz
             Bilgisayar muhtemel sonuclari gosterecektir""")

        num = 1
        word = input("Kelime: ")
        word = word.lower()
        results.append([] * len(alph))
        while num <= len(alph):
            results[word_num].append(shift(word, num, way))
            num += 1
        while True:
            try:
                go_on = bool(int(input("Devam etmek icin herhangi bir sayiya,\nDurmak icin 0a basiniz: ")))
                word_count += 1
                break
            except ValueError:
                print("Lutfen sadece sayi giriniz!")
        num = 1
        word_num += 1
    else: break
if way is False:
    count = 0
    end_results = []
    while word_count >= 1:
        for result in results:
            end_results.append([])
            end_results[count].append(result[count])
            print(result[count])
            count += 1
        word_count -= 1
    for result in end_results:
        print(" ".join(result))
        num += 1

