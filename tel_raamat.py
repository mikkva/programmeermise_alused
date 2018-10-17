def ask_name():
    #Küsib nime ja eemaldab algusest ja lõpust tühikud
    new_name=input("Sisesta nimi: ")
    new_name=new_name.strip()
    return new_name

def check_name(name):
    # kontrollib, kas nimi on 1 sõna
    for i in name:
        if i==" ":
            print("nimi on vale, ei tohi sisestada tühikuga")
            return False
    return True

def existing_name(name):
    # kontrollib, kas selline nimi eksisteerib telefoniraamatus
    for i in tel_numbrid.keys():
        if i == name:
            return True
    return False

def ask_check_number():
    # Kontrollib ja küsib numbri, kuna numbrit on vaja alati nii küsida, kui ka kontrollida
    while True:
        try:
            new_number=int(input("Sisesta number: "))
        except TypeError:
            print("Vigane number")
            return False
        except ValueError:
            print("Vigane nr")
            return False
        return new_number


def add_new_contact(new_name, new_number):
    tel_numbrid[new_name]=new_number

def print_contacts():
    print("Teie telefoniraamatus on järgmised kontaktid:\n {}".format(tel_numbrid))

def delete_contact(delete_name):
    try:
        del tel_numbrid[delete_name]
    except KeyError:
        print("Sellist kontakti pole")

def update_number(update_name):
    for i in tel_numbrid.keys():
        if i == update_name:
            new_number=ask_check_number()
            if new_number != False:
                tel_numbrid[update_name]=new_number
                return
            else:
                return
    print ("sellist kontakti pole")

def update_name(old_name, new_name):
    number_helper=tel_numbrid[old_name]
    delete_contact(old_name)
    add_new_contact(new_name, number_helper)


tel_numbrid = {'Mikk': 54541010, 'Mart': 53531010}
valik=1
while True:
    try:
        valik = int(input("\nVali tegevus:\n 1 - Lisa kontakt\n 2 - Näita kontaktide nimekirja\n"
                      " 3 - Kustuta kontakt\n 4 - Uuenda number\n 5 - Muuda nimi\n 0 - lõpeta\n Valik:"))
    except ValueError:
        print("Sellist valikut polnud ju lollpea, sessioon l2bi!")
        break
    if valik == 1:
        new_name=ask_name()
        if check_name(new_name):
            new_number=ask_check_number()
            if new_number != False:
                add_new_contact(new_name, new_number)
    elif valik == 2:
        print_contacts()
    elif valik == 3:
        name=ask_name()
        if check_name(name):
            delete_contact(name)
    elif  valik == 4:
        name=ask_name()
        if check_name(name):
            update_number(name)
    elif valik == 5:
        print("Otsitava nime sisestamine!")
        old_name= ask_name()
        if check_name(old_name):
            if existing_name(old_name):
                print("Uue nime sisestamine!")
                new_name=ask_name()
                if check_name(new_name):
                    update_name(old_name, new_name)
    else:
        print("sessioon läbi")
        break
