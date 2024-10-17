from enum import Enum
class HeroType(Enum):
  WARRIOR = "guerreiro"
  MAGE = "mago"
  MONK = "monge"
  NINJA = "ninja"

class Hero:
  name: str
  age: int
  type: HeroType


  def __init__(self, name: str, age: int, hero_type: str ):
    self.name = name
    self.age = age
    if hero_type.lower() == "guerreiro":
      self.type = HeroType.WARRIOR
    elif hero_type.lower() == "mago":
      self.type = HeroType.MAGE
    elif hero_type.lower() == "monge":
      self.type = HeroType.MONK
    elif hero_type.lower() == "ninja":
      self.type = HeroType.NINJA
    else:
      raise ValueError("Tipo de herói não reconhecido")
    
  def attack(self):
    attack_name = ""
    if self.type.value == "guerreiro":
      attack_name = "espada"
    if self.type.value == "mago":
      attack_name = "magia"
    if self.type.value == "monge":
      attack_name = "artes marciais"
    if self.type.value == "ninja":
      attack_name = "shuriken"
    return f"o {self.type.value} atacou usando {attack_name}"
  
heros = []

try:
  h1 = Hero("Brian", 25, "mago")
  heros.append(h1)
  h2 = Hero("Brian", 25, "guerreiro")
  heros.append(h2)
  h3 = Hero("Brian", 25, "ninja")
  heros.append(h3)

  h4 = Hero("Brian", 25, "monge")
  heros.append(h4)
  h5 = Hero("Brian", 25, "teste")
  heros.append(h5)
except ValueError as e:
  print(e)

for i in heros:
  print(i.attack())
