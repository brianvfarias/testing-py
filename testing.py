def show_hero_info(name, exp):
  level = ""
  if(exp < 1000):
    level= "Ferro"
  elif(exp < 5000):
    level= "Bronze"
  elif(exp < 7000):
    level= "Prata"
  elif(exp < 8000):
    level= "Ouro"
  elif(exp < 9000):
    level= "Platina"
  elif(exp < 10000):
    level= "Ascendente"
  elif(exp > 10000):
    level= "Radiante"
  return "O Herói de nome " + name  +" está no nível de " + level

print(show_hero_info("Brian", 100000))
