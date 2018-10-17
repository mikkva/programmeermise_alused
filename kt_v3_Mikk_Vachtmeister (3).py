# KT - variant 3
# Mikk Vactmeister
# 03.10.2018

# Ülesanne 1
# Palindroom on keelend, mis on nii päri- kui ka tagurpidi lugedes täpselt samasugune. "Tema amet" on palindroom.
# Kirjutage funktsiooni palindrom(string) mis võtab argumendiks lause, kontrollib iga sõna eraldi ja tagastab neid,
# mis on palindroomid csv (comma-separated values) formaadis
def reverse(string):
    #keerab stringi teisipidi
    return string[::-1]

def palindrom (text):
    # võtab sisse kasutaja sisestatud teksti ja tagastab palindroomid
    words=[]
    words=text.split(" ") # paneb iga sõna lausest eraldi listi
    teistpidi="" # muutuja sõnade tagurpidiseks salvestamiseks
    palindroomid=[] #muutuja kuu salvestatakse palindroomid
    for i in range(len(words)):
        teistpidi=reverse(words[i]) # kutsub välja abifunktsiooni, mis keerab sõna teisipidi

        if words[i] == teistpidi: # kui sõna ühte ja teistpidi on võrdsed, siis on tegemist palindroomiga
            palindroomid.append(words[i])
    return palindroomid # tagastab kasutajale palindroomid

#Ülesanne 2
#Kirjutage funktsiooni population(X) mis võtab argumendiks meeste arvu linnas (väärtus X).
# On teada, et igal mehel on X naist ja igal naisel on X last. Arvutage mitu elanikut on linnas kokku.

def population(x):
    # arvutab mitu elaniku elab linnas, koodiloetavuse huvides on rolli järgi lahku löödud, saaks ka lihtsalt x+x*x+x*x*x
    if x > 0:   
        womenPopulation=x*x # naiste arv
        childPopulation=womenPopulation*x # laste arv
        totalPopulation=x+womenPopulation+childPopulation # kõikide elanike arv kokku
    else:
        totalPopulation=0
    return totalPopulation

#Ülesanne 3
#Kirjutage funktsiooni most_unique(string) mis võtab argumentiks lause (tühikuga jagatud sõnad) ja tagastab sõna,
#  kus on kõige rohkem unikaalseid tähti.
# Kui kahes sõnas on sama palju unikaalseid tähte tagastage esimese. Juhul kui sisend on tühi, tagastage None Näide:

def most_unique_string(string):
    # see funktsiooni otsib, millises sõnas on kõige rohkem erinevaid tähti.
    if string.isspace() or string=="":  # kui on tühi string kaasa antud, siis tagastab "none"
        return "None"
    words=[]    # tühi list kuhu pannakse kõik sõnad eraldi
    words=string.split(" ")     #eraldab lausest sõnad listi
    unical_charac_count=[]  # iga sõna unikaalsete tähemärkide arv
    helper=[]   #abimuutuja, sõnade võrdlemiseks
    for i in words:     # käib läbi iga sõna sisestatud sõnadest
        word=i
        for j in word:
            if j not in helper:
                helper.append(j) #lisab iga unikaalse tähemärgi muutujasse
        unical_charac_count.append(len(helper)) # salvestab unikaalsete tähemärkide arvu
        helper=[] # tühjendab abi listi järgmise sõna jaoks.

    # index funktsiooniga leian maximum pikkuse indexi ja tagastan selle sõna, index leiab alati esimese
    return words[((unical_charac_count.index(max(unical_charac_count))))]


# ei muutnud midagi
