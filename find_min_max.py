import random
def min_eleman():

# Boş bir liste oluşturuyoruz
    liste = []

# 10 adet rastgele sayı oluşturup listeye ekliyoruz (1 ile 100 arasında)
    for _ in range(10):
        number = random.randint(1, 100)
        liste.append(number)

# Oluşturulan rastgele sayılar dizisini ekrana yazdırıyoruz
    print("Random Numbers List:", liste)

    minimum=liste[0]
    for i in range (len(liste)):
        if liste[i]<minimum:
                minimum=liste[i]
    return minimum

print("minimum:",min_eleman())

def find_max():
    # Boş bir liste oluşturuyoruz
    liste2 = []

# 10 adet rastgele sayı oluşturup listeye ekliyoruz (1 ile 100 arasında)
    for _ in range(10):
        number = random.randint(1, 100)
        liste2.append(number)

# Oluşturulan rastgele sayılar dizisini ekrana yazdırıyoruz
    print("Random Numbers List:", liste2)
    max=liste2[0]
    for i in range (len(liste2)):
        if liste2[i]>max:
            max=liste2[i]
    return max

print("max:",find_max())