import random

print("Juego PIEDRA - PAPEL - TIJERA");
print("=" * 40);

options = ("piedra", "papel", "tijera")
rounds = 1
pcPoints = 0
userPoints = 0

while True:

  print("ROUND ==>", rounds);
  
  user_option = input("Porfavor elije piedra papel o tijera ==>").lower()
  pc_option = random.choice(options);
  
  if not user_option in options:
    print("Esa no es una Opcion valida")
    continue
  
  
  print("Elegiste: ", user_option);
  print("La PC ha elegido: ", pc_option);
  
  print("-" * 30);
  
  if user_option == pc_option :
    print("El resultado es: Empate")
    
  elif user_option == "tijera" and pc_option == "papel":
    print("=== Ganaste ===")
    userPoints += 1
  elif user_option == "tijera" and pc_option == "piedra":
    print("=== Perdiste ===")
    pcPoints += 1     
  elif user_option == "piedra" and pc_option == "tijera":
    print("=== Ganaste ===")
    userPoints += 1
  elif user_option == "piedra" and pc_option == "papel":
    print("=== Perdiste ===")
    pcPoints += 1
  elif user_option == "papel" and pc_option == "piedra":
    print("=== Ganaste ===")
    userPoints += 1
  else:
    print("=== Perdiste ===")
    pcPoints += 1

  print("Usuario: ", userPoints);
  print("PC: ", pcPoints);
  print("=" * 30);
  rounds += 1
  
  if pcPoints == 3: 
    print("RESULTADOS:")
    print("PC: ", pcPoints)
    print("Usuario: ", userPoints)
    print("==== GANA LA PC =====")
    break
          
  if userPoints == 3: 
    print("RESULTADOS:")
    print("PC: ", pcPoints)
    print("Usuario: ", userPoints);
    print("==== GANA EL USER =====")
    break