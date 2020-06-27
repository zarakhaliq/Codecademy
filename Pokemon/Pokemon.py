class Pokemon:
#Max health is determined by level and currentHealth at the start is the maxHealth:
  def __init__(self, name, type, level):
    self.name=name
    self.level=level
    self.type=type
    self.maxHealth=level*4
    self.currentHealth=level*4
    self.is_knocked_out=False
    self.experience=0

  def gainExperience(self, amount):
    self.experience+=amount
    #maximum levels in game are 10
    if((self.experience>=3) and (self.level<10)):
      self.levelUp()
      print(f'{self.name} moved up to level {self.level}')

  def levelUp(self):
    self.level+=1
    #reset experience to zero
    self.experience=0



  def loseHealth(self, amount):
    self.currentHealth-=amount
    print(f'{self.name} now has {self.currentHealth} health')
    if(self.currentHealth<=0):
      self.currentHealth=0
      self.KnockOut()

  def gainHealth(self, amount):
    if(self.currentHealth==0):
      self.Revive()
    self.currentHealth+=amount
    if(self.currentHealth>self.maxHealth):
      self.currentHealth=self.maxHealth

    print(f'{self.name} now has {self.currentHealth} health')
    

  def KnockOut(self):
    if(self.currentHealth==0):
      self.is_knocked_out==True
      print(f'K.O. {self.name} is knocked out!')
  
  def Revive(self):
    self.is_knocked_out==False
    print(f'Alive! Health {self.currentHealth}')
    if(self.currentHealth==0):
      self.currentHealth==1
    
    
  
  def attack(self, opponent):

    #listOfTypes=["Fire", "Water", "Grass"]

  # If Pokemon is of type Fire:
    opponentName=opponent.name 
    print(f'{self.name} is attacking {opponentName}!')
    if((self.type=="Fire") and (opponent.type=="Grass")):
      damage=2*self.level 
      opponent.loseHealth(damage)
      print(f'Great job! {opponentName} lost {damage} health.')
    elif((self.type=="Fire") and (opponent.type=="Water")):
      damage=0.5*self.level
      opponent.loseHealth(damage)
      print("Not so effective")
    elif((self.type=="Fire") and (opponent.type=="Fire")):
      damage=0.5*self.level
      opponent.loseHealth(damage)
      print("Do better next time")
#If Pokemon is of type Water:

    if((self.type=="Water") and (opponent.type=="Fire")):
      damage=2*self.level
      opponent.loseHealth(damage)
      print("Wait a go! That was a big hit.")
    elif((self.type=="Water") and (opponent.type=="Grass")):
      damage=0.5*self.level
      opponent.loseHealth(damage)
      print("Could do better..")
    elif((self.type=="Water") and (opponent.type=="Water")):
      damage=0.5*self.level
      opponent.loseHealth(damage)
      print("That was ok..")
  #If Pokemon is of type Grass:

    elif((self.type=="Grass") and (opponent.type=="Fire")):
      damage=0.5*self.level
      opponent.loseHealth(damage)
      print("Ineffective")
    elif((self.type=="Grass") and (opponent.type=="Water")):
      damage=2*self.level
      opponent.loseHealth(damage)
      print("Good hit!")
    elif((self.type=="Grass") and (opponent.type=="Grass")):
      damage=0.5*self.level
      opponent.loseHealth(damage)
      print("So and so..")
    self.gainExperience(1)
    print(f'Experience: {self.experience}')

#Create subclasses:
#We don't need to add name and type parameters because we will inherit these from Pokemon class using super():

class Misty(Pokemon):
  def __init__(self, level):
    super().__init__("Misty", "Water", level)

class Gloom(Pokemon):
  def __init__(self, level):
    super().__init__("Gloom", "Grass", level)

class Bruno(Pokemon):
  def __init__(self, level):
    super().__init__("Bruno", "Fire", level)

 #Trainer class: 

class Trainer:
  def __init__(self, pokemons, name, potions):
    self.pokemons=pokemons
    self.name=name
    self.potions=potions
    self.currentlyActive=0

#currentlyActive is a number or index of the pokemons list that represents the active pokemon.

#Funtion for using a potion
  def Heal(self):
    activePokemon=self.pokemons[self.currentlyActive]
    if(self.potions>0):
      print(f'You used a potion on {activePokemon.name}')
      activePokemon.gainHealth(5)
      self.potions-=1
    else:
      print("Sorry, no more potions left.")


#Function for trainer attacking another trainer:

  def trainerAttack(self, otherTrainer):
    otherTrainerActivePokemon=otherTrainer.pokemons[otherTrainer.currentlyActive]
    activePokemon=self.pokemons[self.currentlyActive]
    activePokemon.attack(otherTrainerActivePokemon)
    

#Function for switching currently Active:
  def SwitchPokemon(self, newPokemonIndex):
    
    activePokemon=self.pokemons[0]
    
    if(newPokemonIndex==self.currentlyActive):
      print("This Pokemon is already active")
    elif(newPokemonIndex > len(self.pokemons)):
      print("Pokemon does not exist")
    elif(self.pokemons[newPokemonIndex].is_knocked_out):
      print("Pokemon is knocked out")
    else:
      newPokemon=self.pokemons[newPokemonIndex]
      self.currentlyActive=newPokemonIndex
      Newname=newPokemon.name
      print(f'{Newname} is now active.')
#Calling the subclasses and trainer class to make the 4 pokemons and 2 trainers. 2 pokemons for each trainer. Each trainer can have up to 6 pokemons.
#Pokemon Misty on level 1, Pokemon Gloom on level 2,Pokemon Bruno on level 3 and Misty on level 2 .

misty=Misty(1)
gloom=Gloom(2)
bruno=Bruno(3)
misty2=Misty(2)

trainer1=Trainer([misty, gloom], "Red", 2)
trainer2=Trainer([bruno, misty2], "Blue", 3)

#Testing trainer methods:

trainer1.trainerAttack(trainer2)
trainer2.Heal()
trainer1.SwitchPokemon(1)
trainer1.SwitchPokemon(0)
trainer1.SwitchPokemon(4)
trainer2.trainerAttack(trainer1)



