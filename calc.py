
# konvertē datu mērvienības
def megabit_to_megabyte(megabit):
   result = megabit*8
   return result

# saskaiti degvielas patēriņu uz 100 km
def fuel_consumption(litres, kilometers):
   result = 0
   return result

# konvertē temperatūru
def celsius_to_fahrenheit(celsius):
    result = celsius*9/5+32
    return result

# saliec visus skaitļus pirms dota skaitļa (izmanto for)
def sigma(tail):
    result = 0
    return result

# nokonvertē svaru uz tuvāko mērvienību - grams, kilograms, tonna (izmanto if)
def weight(grams):
    if grams <1000:
        return str(grams) + "g"
    if grams >=1000:
        result = int(grams/1000)
        return str(grams) + "kg"
    if grams >= 100000:
        result = int(grams/100000)
        return str(grams) + "c"
    if grams >=1000000:
        result = int(grams/1000000)
        return str(grams) + "t"
