# decrypt any given Vigener encrypted text without knowing the key
# decription is for a text in slovene language using the slovene 25-letter alphabet

import string
import numpy as np
alph = "ABCČDEFGHIJKLMNOPRSŠTUVZŽ"


poraz = [10.47, 1.94, 0.66, 1.48, 3.39, 10.71, 0.11, 1.64, 1.05, 9.04, 4.67, 3.70,
         5.27, 3.30, 6.33, 9.08, 3.37, 5.01, 5.05, 1.00, 4.33, 1.88, 3.76, 2.10, 0.65]


def isLetter(char):
    return (char in alph)


def countLetters(text):
    count = 0
    for i in text:
        if(isLetter(i)):
            count += 1
    return count


aha = []


def keylenIOC(text):
    arr = []
    for k in range(1, 20):
        text2 = text
        text2 = (text[::k])
        letterCounts = []
        for i in range(len(alph)):
            count = 0

            for j in text2:
                if j == alph[i]:
                    count += 1
            letterCounts.append(count)

        total = 0
        for i in range(len(letterCounts)):
            ni = letterCounts[i]
            total += ni * (ni - 1)

        N = countLetters(text2)

        total = float(total) / ((N * (N - 1)))
        arr.append(total)

    for k in range(0, 19):
        arr = np.array(arr, dtype='float')
        if(arr[k] > 0.0600):
            aha.append(arr[k])
            aha.append(k+1)

    print("Dolzina kljuca je: " + str(aha[1]) + " ; " + str(aha[3]))
    print("\n")
    return arr


def abc(list):
    list[:] = [round(x / 100, 3) for x in list]
    return list


keylist = []


def keyword(text, list):
    arr = []
    key = aha[1]
    abcslo = []
    abcslo = abc(list)
    keylist = []
    for k in range(0, key):
        text2 = text
        text2 = (text[k::key])
        letterCounts = []
        # print(text2)
        print(" -------------------  ")
        N = countLetters(text2)

        for i in range(len(alph)):
            count = 0
            for j in text2:
                if j == alph[i]:
                    count += 1
            letterCounts.append(count)

        letterCounts[:] = [round(x / N, 3) for x in letterCounts]

        sums = []

        for j in range(len(letterCounts)):
            letterCounts2 = letterCounts
            abcslo2 = abcslo
            arrnew = []
            letterCounts2 = np.roll(letterCounts, -j)
            arrnew = [((letterCounts2[i] - abcslo2[i])**2)/abcslo2[i]
                      for i in range(len(letterCounts))]

            sumo = sum(arrnew)
            sums.append(sumo)

        minval = min(sums)
        minind = sums.index(minval)
        print(minval, minind)
        keylist.append(alph[minind])

    print("\n")
    print(keylist)
    print("\n")

    key2 = key
    M = countLetters(text)
    lengg = int(M/key2)
    keystring = lengg * keylist

    orig_text = []
    for i in range(len(text)):
        a = "ABCČDEFGHIJKLMNOPRSŠTUVZŽ"
        t = text[i]
        k = keystring[i]
        b = a.index(t)
        c = a.index(k)

        x = (b - c + 25) % 25
        y = a[x]
        orig_text.append(y)

    tostring = ""
    for i in orig_text:
        tostring = tostring+i

    print("besedilo zapisano v novo - besedilo.txt - datoteko")
    print("\n")
    f = open("besedilo.txt", mode="w", encoding='utf-8')
    f.write(tostring)
    f.close


# -----------------------------------------------
# change the .txt  file you want to decrypt
with open('Decryptthistext.txt', encoding='utf-8') as file:
    text = file.read().replace('\n', '')

letsgo = keylenIOC(text)
letsgo2 = keyword(text, poraz)
