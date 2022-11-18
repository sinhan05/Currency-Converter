import math

language= input("Choose your language. E for English or G for German. Bitte geben Sie ihren Sprache ein. E für Englisch und G für Deutsch.")

if language == "E":
  currency = input("Please input the currency name that you want to change. Input D for the american dollar, Input P for the british pound, Input F for the swiss franc, Input R for the indian rupee, Input E for the european euro and Input Y for the chinese yen. ")
else:
  currency = input("Bitte geben Sie den Waehrungsnamen ein, den Sie aendern moechten. Geben Sie D für den amerikanischen Dollar ein, geben Sie P fuer das britische Pfund ein, geben Sie F fuer den Schweizer Franken ein, geben Sie R für die indische Rupie ein, geben Sie E für den europäischen Euro ein und geben Sie Y für den chinesischen Yen ein. ")

if currency=="D":
  print("OKAY")
if currency=="P":
  print("OK, THAT WORKS")
if currency=="F":
  print("DAS PASSCHT MIR")
if currency=="R":
  print("WO MENE TO KHAR SAKTA HOON")
if currency=="E":
  print("ICH AM GA PARA ROBYTY TOA...")
if currency=="Y":
  print("Wǒ néng zuò dào")

