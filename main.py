import sys

#date
lista=[]
#lista de cuvinte
cuvinte=[]
#dictionar de stari
stari={}

stari["S"]=[]
stari["N"]=[]
stari["F"]=[]

#ca sa gasesc mai usor starile la validare
stari_neclasificate=set()

tranzitii=[]

def Citeste():
    f=open("date.in")

    #evita comentariile
    for linie in f:
        if linie[0]!='#':
         lista.append(linie.strip())

    f.close()

    poz=0
    n=len(lista)

    while poz<n:
        if lista[poz].find("Sigma")!=-1:
            poz+=1
            while lista[poz]!="End":
                cuvinte.append(lista[poz])
                poz+=1
            #sunt cu poz pe end
            poz+=1

        if lista[poz].find("States")!=-1:
            poz+=1
            #construiesc dictionar cu cheile S,F,N-normale si adaug starile
            while lista[poz]!="End":
                bucati=[]
                bucati=lista[poz].split(",")
                stari_neclasificate.add(bucati[0])
                if len(bucati)==1:
                    stari["N"].append(bucati[0])
                elif len(bucati)==2:
                        if bucati[1].strip()=="S":
                            stari["S"].append(bucati[0])
                        elif bucati[1].strip()=="F":
                            stari["F"].append(bucati[0])
                else: # are sigur lungime 3 -> stare intiala si stare finala
                    stari["F"].append(bucati[0])
                    stari["S"].append(bucati[0])

                poz+=1
            poz+=1 #sar peste end

        if lista[poz].find("Transitions") != -1:
            poz+=1
            while lista[poz] != "End":

                bucati=lista[poz].split(",")
                tranzitii.append(tuple(bucati))

                poz+=1
            poz+=1
        poz+=1

def AfisareDate():
    print("Starile introduse sunt:", stari)
    print("Tranzitiile introduse sunt:", tranzitii)
    print("Cuvintele introduse sunt:",  cuvinte)

def Validare():
    #are mai multe stari intiale
    if len(stari["S"])!=1:
        print("Exista mai multe stari initiale!")
        return 0
    #nu are stare finala
    if len(stari["F"])==0:
        print("Nu exista stare finala!")
        return 0
    for tranz in tranzitii:
        if tranz[1] not in cuvinte:
            print("A fost introdus un cuvant invalid!")
            return 0
        if tranz[0] not in stari_neclasificate:
            print("A fost introdusa o stare invalida!")
            return 0
        if tranz[2] not in stari_neclasificate:
            print("A fost introdusa o stare invalida!")
            return 0

    return 1

def ValidareDate():

  if Validare()==0:
    print("Datele nu sunt valide!")
  else:
    print("Datele sunt valide!")


def Verifica():

    s=sys.argv[1:]
    #s=input("cuvant:")
    lg=len(s)
    starecurenta=stari["S"][0]
    i=0
    rej=0 #daca a fost rejected de la abort
    lg_tranz=len(tranzitii)
    ok=0
    while i<lg:
      ok=0 #daca gasesc o tranzitie buna sau nu
      for j in range(lg_tranz):
          if tranzitii[j][0]==starecurenta: # am identificat o tranzitie care pleaca din starea mea curenta
             if s[i:].find(tranzitii[j][1])==0: #in aceasta tranzitie urmeaza o secventa/cuvant din s
                 # am gasit tranzitia
                ok=1
                starecurenta=tranzitii[j][2] #trec la urmatoarea tranzitie
                i=i+len(tranzitii[j][1]) #sar cuvantul
                break

      if ok==0: #abort
          print("Rejected")
          rej=1
          break

    if rej==0 and starecurenta not in stari["F"]:
        print("Rejected")
    elif starecurenta in stari["F"]:
        print("Accepted")


#main
Citeste()
AfisareDate()
ValidareDate()
Verifica()


