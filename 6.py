Schrauben = 0.07
Muttern = 0.04
Unterlegscheiben = 0.02

Menge_Schrauben = int(input("Wie viele Schrauben?: "))
Menge_Muttern = int(input("Wie viele Muttern?: "))
Menge_Unterlegscheiben = int(input("Wie viele Unterlegscheiben?: "))

Schraubenpreis = Schrauben * Menge_Schrauben 
Mutternpreis = Muttern * Menge_Muttern
Unterlegscheibenpreis = Unterlegscheiben * Menge_Unterlegscheiben

Gesamtpreis = Schraubenpreis + Mutternpreis + Unterlegscheibenpreis

print("Gesamtpreis: ", Gesamtpreis, "€")