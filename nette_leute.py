liste=["Andreas", "Peter", "Tina", "Anna"]
anzahl=0
cool=0
for name in liste:
  anzahl = anzahl+1
  print("Ist", name, "eine nette Person? (j/n)")
  antwort=input("(j/n)")
  if antwort=="j":
    cool=cool+1
prozent=cool/anzahl*100
print(prozent, "% deiner Bekannten sind nette Leute.")

