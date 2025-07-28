class Empleado:
    def __init__(self,codigo_empleado, nombre_completo, departamento, antiguedad):
        self.codigo_empleado = codigo_empleado
        self.nombre_completo = nombre_completo
        self.departamento = departamento
        self.antiguedad = antiguedad

class Evaluacion:
    def __init__(self, puntualidad, trabajo_equipo, productividad, observacion):
        self.puntualidad = puntualidad
        self.trabajo_equipo = trabajo_equipo
        self.productividad = productividad
        self.observacion = observacion
    def Promedio(self):
        promedio = self.puntualidad + self.trabajo_equipo + self.productividad/ 3
        return promedio
    def Estado(self,promedio):
        if promedio >= 7:
            return "Satisfactorio"
        elif promedio <= 6:
            return "Mejorar"

class InformacionPersonal:
    def __init__(self, telefono, correo_electronico):
        self.telefono = telefono
        self.correo_electronico = correo_electronico


def Menu():
    print("---Menu---")
    print("1. Agregar Empleado")
    print("2. Lista de Empleados")
    print("3. Buscar Empleado")
    print("4. Empleados satisfactorio")
    print("5. Mejores Empleados")
    print("6. Salir")

empleados = {}
while True:
    Menu()
    try:
        opcion = int(input("Ingrese una opcion: "))
        match opcion:
            case 1:
                print("\nAgregar Empleado")
                cantidad_empleados = int(input("Cuantos empleados desea agregar: "))
                if cantidad_empleados <= 0:
                    print("La cantidad debe ser mayor a 0")
                else:
                    for empleado in range(cantidad_empleados):
                        codigo_empleado=int(input(f"Ingrese el codigo del empleado #{empleado+1}"))
                        if codigo_empleado not in empleados:
                            nombre_completo=input(f"Ingrese el nombre completo del empleado #{empleado+1}: ")
                            departamento=input(f"Ingrese el departamento del empleado #{empleado+1}: ")
                            antiguedad=int(input(f"Ingrese los años de antiguedad del empleado #{empleado+1}: "))
                            if antiguedad<= 0:
                                print("La cantidad debe ser mayor a 0")
                            else:
                                puntualidad = int(input(f"Ingrese la puntualidad del empleado #{empleado+1} (0-10): "))
                                if puntualidad <= 0:
                                    print("La cantidad debe ser mayor a 0")
                                else:
                                    trabajo_equipo = int(input(f"Ingrese el trabajo en equipo del empleado #{empleado + 1} (0-10): "))
                                    if puntualidad <= 0:
                                        print("La cantidad debe ser mayor a 0")
                                    else:
                                        productividad = int( input(f"Ingrese la productividad del empleado #{empleado + 1} (0-10): "))
                                        if puntualidad <= 0:
                                            print("La cantidad debe ser mayor a 0")
                                        else:
                                            observaciones = input(f"Ingrese alguna observaciones del empleado #{empleado+1}: ")
                                            evaluacion = Evaluacion(puntualidad, trabajo_equipo, productividad, observaciones)
                                            promedio = evaluacion.Promedio()
                                            telefono= int(input(f"Ingrese el numero de telefono del empleado #{empleado+1}: "))
                                            correo_electronico = input(f"Ingrese el correo electric del empleado #{empleado+1}: ")
                                            empleados[codigo_empleado] = {
                                                "datos_generales" : {
                                                    "nombre_completo": nombre_completo,
                                                    "departamento": departamento,
                                                    "antiguedad": antiguedad
                                                },
                                                "evaluacion" : {
                                                    "puntualidad": puntualidad,
                                                    "trabajo_equipo": trabajo_equipo,
                                                    "productividad": productividad,
                                                    "observacion": observaciones,
                                                    "promedio": promedio,
                                                    "estado": evaluacion.Estado(promedio)
                                                },
                                                "contacto":{
                                                    "telefono": telefono,
                                                    "correo_electronico": correo_electronico
                                                }
                                            }
                        else:
                            print("El codigo ya existe")


            case 2:
                print("Lista Empleado")
                for codigo_empleado, empleado in empleados.items():
                    print(f"Codigo del empleado: {codigo_empleado}")
                    print(f"Nombre completo: {empleado['datos_generales']['nombre_completo']}")
                    print(f"Departamento: {empleado['datos_generales']['departamento']}")
                    print(f"Antiguedad: {empleado['datos_generales']['antiguedad']}")
                    print(f"Puntualidad: {empleado['evaluacion']['puntualidad']}")
                    print(f"Trabajo equipo: {empleado['evaluacion']['trabajo_equipo']}")
                    print(f"Productividad: {empleado['evaluacion']['productividad']}")
                    print(f"Observacion: {empleado['evaluacion']['observacion']}")
                    print(f"Promedio: {empleado['evaluacion']['promedio']}")
                    print(f"Estado: {empleado['evaluacion']['estado']}")
                    print(f"Telefono: {empleado['contacto']['telefono']}")
                    print(f"Correo electronico: {empleado['contacto']['correo_electronico']}")

            case 3:
                print("Buscar Empleados")
                codigo_buscar = int(input("Ingrese el codigo del empleado a buscar: "))
                if codigo_buscar in empleados:
                    for codigo_empleado, empleado in empleados.items():
                        if codigo_empleado == codigo_buscar:
                            print(f"Codigo del empleado: {codigo_empleado}")
                            print(f"Nombre completo: {empleado['datos_generales']['nombre_completo']}")
                            print(f"Departamento: {empleado['datos_generales']['departamento']}")
                            print(f"Antiguedad: {empleado['datos_generales']['antiguedad']}")
                            print(f"Puntualidad: {empleado['evaluacion']['puntualidad']}")
                            print(f"Trabajo equipo: {empleado['evaluacion']['trabajo_equipo']}")
                            print(f"Productividad: {empleado['evaluacion']['productividad']}")
                            print(f"Observacion: {empleado['evaluacion']['observacion']}")
                            print(f"Promedio: {empleado['evaluacion']['promedio']}")
                            print(f"Estado: {empleado['evaluacion']['estado']}")
                            print(f"Telefono: {empleado['contacto']['telefono']}")
                            print(f"Correo electronico: {empleado['contacto']['correo_electronico']}")
                        else:
                            continue

                else:
                    print("El codigo no existe")
            case 4:
                print("Empleados satisfactorio")
            case 5:
                print("Mejores Empleados")
            case 6:
                print("Gracias por usar el programa")
            case _:
                print("Opcion invalida")
    except Exception:
        print("La entrada de valor debe ser numerica")