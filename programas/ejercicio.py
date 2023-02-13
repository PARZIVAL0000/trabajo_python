#!/usr/bin/env python3
#_*_ coding:utf-8 _*_ 


import os, time


lista_usuarios = []


while(True):
    os.system("clear")
    
    print(""" 
                            1.- Ingresar informacion de usuarios

                            2.- Mostrar informacion de usuarios

                            3.- Editar Informacion de usuarios

                            4.- Eliminar informacion de usuarios

                            5.- Salir
    """)

    entrada = input("\n[>] Inserta tu entrada: ")

    match(entrada):
        case "1":
            os.system("clear")
            
            lista_usuarios.extend([lista_usuarios.append(input("[*] Cedula: ")), lista_usuarios.append(input("[*] Nombre: ")), lista_usuarios.append(input("[*] Apellido: ")), lista_usuarios.append(input("[*] Monto: ")), lista_usuarios.append(input("[*] Perfil: "))])
        
            time.sleep(2)
            
        case "2":
            
        
            
            for i in lista_usuarios:
                if(lista_usuarios.index(i)%5 == 0):
                    
                    m = lista_usuarios.index(i)

            
                    

        case "3":
            valor_indice = lista_usuarios.index(input("[*] Ingresa la cedula para buscar registro: "))
            nombre_nuevo = input("\n[*] Inserta el nombre nuevo: ")

            lista_usuarios[valor_indice+1] = nombre_nuevo

            print(lista_usuarios)

            time.sleep(5)
            



