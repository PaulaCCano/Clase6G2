from sistemaVet import *

def main():
    servicio_hospitalario = sistemaV()
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Salir 
                       \nUsted ingresó la opción: ''' ))

        if menu == 1:
            tipo_ = print('Seleccione: 1.Felino 2.Canino.  =>')
            if tipo_ == '1':
                if servicio_hospitalario.verNumeroMascotasF() >= 7:
                    print("No hay espacio disponible para felinos...")
                    continue
            elif tipo_ == '2':
                if servicio_hospitalario.verNumeroMascotasC() >= 7:
                    print("No hay espacio disponible para caninos...")
                    continue                
            
            historia = int(input(" ingrese la historia clinica de la mascota: "))
            if servicio_hospitalario.verificarExiste(historia) == False:
                nombre=input("Ingrese el nombre de la mascota: ")
                tipo= tipo_
                if tipo == '1':
                    tipo = 'Felino'
                elif tipo == '2':
                    tipo = 'Canino'
                peso=int(input("Ingrese el peso de la mascota: "))
                fecha=input("Ingrese la fecha de ingreso (dia/mes/año): ")
                nm = int(input('Ingrese la cantidad de medicamentos de la mascota: '))
                lista_med = []

                for i in range (0,nm):
                    nombre_medicamento = input('Ingrese el nombre: ')
                    dosis = int(input('Ingrese la dosis: '))

                    medicamento=Medicamento()
                    medicamento.asignarNombre(nombre_medicamento)
                    medicamento.asignarDosis(dosis)
                    lista_med.appen(medicamento)
                
                mas = Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarMedicamento(medicamento)
                
                if tipo == 'Felino':
                    servicio_hospitalario.ingresarMascotaF(mas)
                elif tipo == 'Canino':
                    servicio_hospitalario.ingresarMascotaC(mas)

            else:
                print("Ya existe una mascota con el numero de historia clínica ingresado.") 

            
        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            if fecha != None:  
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
          
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4:
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento=servicio_hospitalario.verMedicamento(q)
            if medicamento != None: 
                print(f"El medicamento suministrado es: {medicamento.verNombre()} con dosis {medicamento.verDosis()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")

        elif menu==6:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")



if __name__ == "__main__":
    main()