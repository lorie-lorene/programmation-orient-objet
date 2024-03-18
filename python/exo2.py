import random
from os import system

class Food_data:
    def __init__(self, date, food, nb_times, water_qty, qty_liquid, fruits_legumes, nb_bowel, health):
        self.date = date                        # String
        self.food = food                        # list
        self.nb_times = nb_times                # int
        self.water_qty = water_qty              # float /liter
        self.qty_liquid = qty_liquid            # float /liter
        self.fruits_legumes = fruits_legumes    # bool
        self.nb_bowel = nb_bowel                # int
        self.health = health                    # String
        self.next_f = None

    def __str__(self):
        val = "Date : "+self.date+"\nFood(s) : "

        for elt in self.food:
            val += elt+", "
        
        val += "\nNb of times food eaten per day : "+str(self.nb_times)+"\nQty of water drank : "+str(self.water_qty)+"L\nQty of other liquid drank : "+str(self.qty_liquid)+"L"
        
        if self.fruits_legumes:
            val += "\nEating fruits and legumes : yes"
        else:
            val += "\nEating fruits and legumes : no"
        
        val+= "\nNb of bowel movements : "+str(self.nb_bowel)+"\nHealth problems : "+self.health+"\n"
        
        return val




class Day:
    def __init__(self, date):
        self.date = date
        self.next = None

    def add_foodData(self, food_data):
        if self.next == None:
            self.next = food_data
        else:
            pt = self.next
            while pt.next_f != None:
                pt = pt.next_f
            pt.next_f = food_data

class compare_food:
    def __init__(self, food):
        self.food = []
        self.num = []
        for elt in food:
            self.food.append(elt)
            self.num.append(1)
    
    def add_food(self, food):
        for elt in food:
            if elt in self.food:
                i = self.food.index(elt)
                self.num[i]+=1
            else:
                self.food.append(elt)
                self.num.append(1)


"""----------------- Main program ----------------"""

def describe(graph):
    for elt in graph:
        pt = elt.next
        while pt != None:
            print(pt)
            pt = pt.next_f

def predict(graph, jour):
    for elt_day in graph:
        if elt_day.date.upper() == jour.upper():
            pt = elt_day.next

            if pt != None:
                cp = compare_food(pt.food)
                pt = pt.next_f

            while pt != None:
                cp.add_food(pt.food)
                pt = pt.next_f

            break

    i = 1
    max = cp.num[0]
    while i < len(cp.num):
        if max < cp.num[i]:
            max = cp.num[i]
        i+=1

    if max == 1:
        print("\nLa nouriture que vous allez manger "+jour+": "+cp.food[random.randint(0,len(cp.food)-1)])
        print("\n")
    else:
        if cp.num.count(max) == 1:
            j = cp.num.index(max)
            print("\nLa nouriture que vous allez manger "+jour+": "+cp.food[j])
            print("\n")
        else:
            ans = "\nLes nouriture que vous allez manger "+jour+": "

            i = 0
            while i < len(cp.num):
                if cp.num[i] == max:
                    ans += cp.food[i]+", "
                i+=1
                
            print(ans)
            print("\n")

def fill_max(graph):
    tab = [[],[],[],[],[],[],[]]
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    i = 0
    while i < 7:
        pt = graph[i].next
        while pt != None:
            if(pt.health == "RAS"):
                tab[i].append(pt)
            pt = pt.next_f
        i+=1

    i = 0
    while i < 7:
        print("\n")
        print("----------"+days[i]+"-----------")
        j = random.randint(0,len(tab[i])-1)
        k = 0
        print("Food(s) :", end='')
        while k < len(tab[i][j].food):
            print(" "+tab[i][j].food[k]+",", end='')
            k+=1
        print("\nNumber of times eaten : "+str(tab[i][j].nb_times))
        print("Quantity of water : "+str(tab[i][j].water_qty)+"L")
        i+=1
    print("\n")



fd = []
fd1 = Food_data("Mardi 1 Nov", ["Beignet haricot", "Banane malakse"], 3, 0.25, 0, True, 2, "RAS")
fd.append(fd1)
fd2 = Food_data("Mercredi 2 Nov", ["Beignet sucre", "Riz saute"], 3, 1, 0, True, 2, "RAS")
fd.append(fd2)
fd3 = Food_data("Jeudi 3 Nov", ["Bouilli avec le pain", "Okok avec le manioc"], 2, 0.3, 0, False, 3, "RAS")
fd.append(fd3)
fd4 = Food_data("Vendredi 4 Nov", ["Okok avec le manioc"], 3, 0.5, 0.1, True, 1, "RAS")
fd.append(fd4)
fd5 = Food_data("Samedi 5 Nov", ["Riz saute", "Bouilli avec le pain"], 3, 0.5, 0.1, False, 0, "RAS")
fd.append(fd5)
fd6 = Food_data("Dimanche 6 Nov", ["Pain oeuf", "Pile patate"], 3, 0.5, 0.3, False, 2, "Mal au ventre")
fd.append(fd6)
fd7 = Food_data("Lundi 7 Nov", ["Pile patate", "Spaghetti"], 3, 1, 0, True, 2, "RAS")
fd.append(fd7)
fd8 = Food_data("Mardi 8 Nov", ["Patate sauce bouillon", "Riz sauce pistache"], 3, 0.75, 0, False, 1, "RAS")
fd.append(fd8)
fd9 = Food_data("Mercredi 9 Nov", ["Riz sauce pistache", "Couscous nkuih"], 2, 0.5, 0, True, 2, "RAS")
fd.append(fd9)
fd10 = Food_data("Jeudi 10 Nov", ["Pain haricot", "Spaghetti"], 2, 1, 0, True, 2, "RAS")
fd.append(fd10)
fd11 = Food_data("Vendredi 11 Nov", ["Spaghetti", "Plantain frit", "Patate sauce pistache"], 2, 0.8, 0.15, False, 1, "RAS")
fd.append(fd11)
fd12 = Food_data("Samedi 12 Nov", ["Patate avocat", "Cafe", "Banane malakse"], 4, 1, 0, False, 2, "RAS")
fd.append(fd12)
fd13 = Food_data("Dimanche 13 Nov", ["Banane malakse", "Kondre", "Koki"], 4, 1, 0.3, False, 1, "RAS")
fd.append(fd13)
fd14 = Food_data("Lundi 14 Nov", ["Kondre", "Ndole"], 2, 1, 0, True, 0, "RAS")
fd.append(fd14)
fd15 = Food_data("Mardi 15 Nov", ["Ndole", "Beignet sucre", "Melon"], 3, 1, 0, True, 1, "Mal au ventre")
fd.append(fd15)
fd16 = Food_data("Mercredi 16 Nov", ["Beignet sucre", "Bignets mais", "Fufu sauce pistache"], 3, 1.5, 0, True, 2, "RAS")
fd.append(fd16)
fd17 = Food_data("Jeudi 17 Nov", ["Banane saute"], 1, 0.5, 0.1, True, 1, "RAS")
fd.append(fd17)
fd18 = Food_data("Vendredi 18 Nov", ["Banane saute", "Beignet sucre", "Pain avocat"], 3, 1, 0, True, 2, "RAS")
fd.append(fd18)
fd19 = Food_data("Samedi 19 Nov", ["Pain chocolat", "Pile banane"], 3, 1, 0.1, True, 2, "RAS")
fd.append(fd19)
fd20 = Food_data("Dimanche 20 Nov", ["Pile banane", "Spaghetti"], 2, 1.2, 0.35, True, 1, "RAS")
fd.append(fd20)
fd21 = Food_data("Lundi 21 Nov", ["Spaghetti", "Couscous sauce jaune"], 2, 1, 0.1, True, 2, "RAS")
fd.append(fd21)
fd22 = Food_data("Mardi 22 Nov", ["Beignet sucre", "Couscous sauce jaune", "Manioc pate d'arachide"], 2, 1.2, 0, True, 1, "RAS")
fd.append(fd22)
fd23 = Food_data("Mercredi 23 Nov", ["Pain oeuf", "Riz sauce pistache"], 3, 1, 0, True, 2, "RAS")
fd.append(fd23)
fd24 = Food_data("Jeudi 24 Nov", ["Riz sauce pistache", "Patate sauce bouillon"], 2, 1.5, 0.1, True, 1, "RAS")
fd.append(fd24)
fd25 = Food_data("Vendredi 25 Nov", ["Patate sauce bouillon", "Bouilli avec le pain"], 2, 1, 0.1, True, 2, "RAS")
fd.append(fd25)
fd26 = Food_data("Samedi 26 Nov", ["Baton avocat", "Fufu sauce d'arachide"], 3, 1, 0.5, True, 1, "RAS")
fd.append(fd26)
fd27 = Food_data("Dimanche 27 Nov", ["Bouilli avec le pain", "Ekomba", "Fufu sauce d'arachide"], 4, 0.7, 0.2, True, 2, "RAS")
fd.append(fd27)
fd28 = Food_data("Lundi 28 Nov", ["Baton sauce d'arachide", "Riz sauce d'arachide"], 2, 1.5, 0, True, 2, "RAS")
fd.append(fd28)
fd29 = Food_data("Mardi 29 Nov", ["Beignet sucre", "mes de pistache avec le baton"], 2, 0.7, 0.2, True, 1, "RAS")
fd.append(fd29)

day = []

day1 = Day("Lundi")
day.append(day1)
day2 = Day("Mardi")
day.append(day2)
day3 = Day("Mercredi")
day.append(day3)
day4 = Day("Jeudi")
day.append(day4)
day5 = Day("Vendredi")
day.append(day5)
day6 = Day("Samedi")
day.append(day6)
day7 = Day("Dimanche")
day.append(day7)

for fd_elt in fd:
    for day_elt in day:
        if fd_elt.date.split(" ")[0] == day_elt.date:
            day_elt.add_foodData(fd_elt)
            break
        


again = True
while again:
    system("clear")
    print("-------- Nutritional agenda --------")
    print("1 : D'ecrire l'habitude alimentaire")
    print("2 : Predire le plat du jour")
    print("3 : Fill max program")

    choice = input("\nFaire un choix en entrant le numero correspondant : ")
    choice = int(choice)

    if choice == 1:
        describe(day)
    elif choice == 2:
        jour = input("\nQuelle jour voulez vous predire : ")
        predict(day, jour)
    elif choice == 3:
        fill_max(day)
    else:
        print("Faire un choix entre 1 et 2")

    choix = input("Voulez vous retourner au menu principale (o/n) ? ")
    while choix != 'o' and choix != 'n':
        choix = input("choisir entre o (oui) ou n (non) : ")
    if choix == 'n':
        again = False


