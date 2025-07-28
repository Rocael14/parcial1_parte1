class Empleado:
    def __init__(self, nombre_completo, departamento, antiguedad):
        self.nombre_completo = nombre_completo
        self.departamento = departamento
        self.antiguedad = antiguedad

class Evaluacion:
    def __init__(self, puntualidad, trabajo_equipo, productividad, observacion):
        self.puntualidad = puntualidad
        self.trabajo_equipo = trabajo_equipo
        self.productividad = productividad
        self.observacion = observacion

    def promedio(self):
        promedio = self.puntualidad + self.trabajo_equipo + self.productividad/3
        return promedio

class InformacionPersonal:
    def __init__(self, telefono, correo_electronico):
        self.telefono = telefono
        self.correo_electronico = correo_electronico
