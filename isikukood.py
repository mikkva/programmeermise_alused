
def id_kontroll(id):
    today=[2018, 10, 10]
    aasta = 0
    aa=""
    if len(id) != 11:
        return "ei ole õige pikkus"
    if not(id.isdigit()):
        return "ei ole ainult numbrid"
    if int(id[0])  not in range(1,7):
        return "esimene nr vale"
    #aasta arvutamine, kui aasta on 1800..1899
    if int(id[0]) in range(1,3):
        aa=id[1]+id[2]
        aa=int(aa)
        aasta= 1800 + aa
        print(aasta)
    #aasta arvutamine, kui aasta on 1900..1999
    if int(id[0]) in range(3,5):
        aa=id[1]+id[2]
        aa=int(aa)
        aasta= 1900 + aa
    #aasta arvutamine, kui aasta on 2000..2999
    if int(id[0]) in range(5,7):
        aa=id[1]+id[2]
        aa=int(aa)
        aasta= 2000 + aa

    kk=id[3]+id[4]
    kk=int(kk)

    #kohad 4. ja 5. peavad olema vahemikus 01..12
    if int(id[3]) not in range(0,2):
        return "Sünnikuupäeva 1 kuu on vigane"
    if not(((int(id[3]) == 0 and int(id[4]) in range(1,10))) or (int(id[3]) == 1 and int(id[4]) in range(0,3))):
        return "Sünnikuupäeva kuu on vigane"

    #kohad 6. ja 7. väärtused eavad olema vahemikus 01...31
    pp=id[5]+id[6]
    pp=int(pp)

    #Kui võll ei ole veel sündinud
    if ((aasta > today[0]) or (aasta == today[0] and kk>today[1])or (aasta == today[0] and kk==today[1] and pp>today[2])):
        return "Sa ei ole veel sündinud"

    if pp not in range(1,32):
        return "Kuupäev on vale"
    if (kk == 4 and pp==31) or (kk== 6 and pp==31) or (kk==9 and pp==31) or (kk==11 and pp==31):
        return "Kuupäev on vale 31"
    if (kk==2 and pp>29):
        return "Veebruaris on vähem päevi"
    if ((kk==2 and pp==29) and not(aasta%4==0 and (aasta%100 ==0 and aasta%400==0))):
        return "sellel aastal polnud liigaastat"

    jargud_i=[1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    jargud_ii= [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    # kontrollsumma
    summa=0
    for i in range(0,10):
        summa= summa+ int(id[i])*jargud_i[i]

    jaak=summa%11
    if jaak == 10:
        for i in range(0,10):
            summa= summa+ int(id[i])*jargud_i[i]

    if jaak != int(id[10]):
        return "kontrollsumma on vale"

    return "id kood on korrektne"
k=1
while k == 1:
    id=input("Sisesta isikukood (väljumiseks vajuta 0): ")
    if int(id)==0:
        k=0
    else:
        print(id_kontroll(id))