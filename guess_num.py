import os, random

while 1:
    menu = int(input('Elige una opción\n1.Iniciar\n2.Salir\n...\n'))
    if menu == 1:
        os.system("clear")
        numrand = random.randint(1,100)
        guess = int(input('Adivina un número del 1 al 100\n'))
        vidas = 5
        
        while guess != numrand:
            if guess > numrand: 
                vidas -= 1
                print('Pista: menor\n')
            elif guess < numrand: 
                print('Pista: mayor\n')
                vidas -= 1
            if vidas == 0:  
                os.system("clear")
                print(f'luser sin vidas\nel numero era {numrand}\n...\n\n¿Jugar de nuevo?\n')
                break
            print(f'tienes {vidas} vidas')
            guess = int(input('Intenta de nuevo\n'))
            
        if guess == numrand: print('si\n...\n\n¿Jugar de nuevo?\n')

    elif menu == 2:
        break
        os.system("clear")
    else: 
        os.system("clear")
        print('Elige una opción válida')
    
    