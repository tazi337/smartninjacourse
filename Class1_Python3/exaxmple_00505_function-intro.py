# nach dem def kann man die Bezeichnung beliebig wählen.
# In die runde Klammer kommen die Argumente, die man mitgeben möchte.
# die Variablen im Funktionsblock, gibt es nur in dem einen Block. Hier: result gibt es nur hier
# Hier: mit float hinter der variabel, kann ich definieren, welcher Typ erlaubt ist -> welche Lösung zurückkommt

def subtraction(number_1: float, number_2: float) -> float:
  result = number_1 - number_2
  return result


def difference(number_1, number_2):
    result = number_1 - number_2
    if result>=0:
        return result
    else:
        return -result


assert subtraction(12, 14)==-2, subtraction(12, 14)==-2
assert difference(12, 14)==2, difference(12, 14)
assert difference(14, 12)==2, difference(14, 12)==2
assert difference(0, 0)==0, difference(0, 0)==0

print("Success!")



# Lösungen vor def differencec
# difference = subtraction(12, 14)
# print(difference)

#Alernativlösung für print - ohne Zwischenspeicherung in difference
# print(subtraction(12, 14))
