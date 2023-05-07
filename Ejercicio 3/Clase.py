class Registro:
    def __init__(self, dia, hora, temperatura, humedad, presion):
        self.dia = dia
        self.hora = hora
        self.temperatura = temperatura
        self.humedad = humedad
        self.presion = presion

registros_mensuales = [[] for _ in range(31)]  
with open('datos_mensuales.txt', 'r') as archivo:
    for linea in archivo:
        datos = linea.strip().split(',')
        dia = int(datos[0])
        hora = int(datos[1])
        temperatura = float(datos[2])
        humedad = float(datos[3])
        presion = float(datos[4])
        registro = Registro(dia, hora, temperatura, humedad, presion)
        registros_mensuales[dia-1].append(registro)  
def max_min_variable(registros, variable):
    max_valor = float('-inf')
    min_valor = float('inf')
    max_dia = max_hora = min_dia = min_hora = None
    for registro in registros:
        valor = getattr(registro, variable)
        if valor > max_valor:
            max_valor = valor
            max_dia, max_hora = registro.dia, registro.hora
        if valor < min_valor:
            min_valor = valor
            min_dia, min_hora = registro.dia, registro.hora
    return max_valor, max_dia, max_hora, min_valor, min_dia, min_hora


def temperatura_promedio(registros, hora):
    temperatura_total = 0
    num_registros = 0
    for registro in registros:
        if registro.hora == hora:
            temperatura_total += registro.temperatura
            num_registros += 1
    if num_registros > 0:
        return temperatura_total / num_registros
    else:
        return None

def listar_valores(registros, dia):
    print(f"Valores registrados para el día {dia}:")
    for registro in registros:
        if registro.dia == dia:
            print(f"Hora {registro.hora}: temperatura = {registro.temperatura}, humedad = {registro.humedad}, presion = {registro.presion}")

# menú de opciones
while True:
    print("\nMenú de opciones:")
    print("1. Mostrar máximos y mínimos de variables")
    print("2. Mostrar temperatura promedio por hora")
    print("3. Listar valores de variables para un día")
    print("4. Salir")
    opcion = input("Ingrese la opción deseada: ")
    
    if opcion == '1':
        max_temperatura, max_temperatura_dia, max_temperatura_hora, min_temperatura, min_temperatura_dia, min_temperatura_hora = max_min_variable(sum(registros_mensuales, []), 'temperatura')
        print(f"Máximo valor de temperatura: {max_temperatura} en el día {max_temperatura_dia} hora {max_temperatura_hora}")
        print(f"Mínimo valor de temperatura: {min_temperatura} en el día {min_temperatura_dia} hora {min_temperatura_hora}")
        
        max_humedad, max_humedad_dia, max_humedad_hora, min_humedad, min_humedad_dia, min_humedad_hora = max_min_variable(sum(registros_mensuales, []), 'humedad')
        print(f"Máximo valor de humedad: {max_humedad} en el día {max_humedad_dia} hora {max_humedad_hora}")
        print(f"Mínimo valor de humedad: {min_humedad} en el día {min_humedad_dia} hora {min_humedad_hora}")
        
        max_presion, max_presion_dia, max_presion_hora, min_presion, min_presion_dia, min_presion_hora = max_min_variable(sum(registros_mensuales, []), 'presion')
        print(f"Máximo valor de presión: {max_presion} en el día {max_presion_dia} hora {max_presion_hora}")
        print(f"Mínimo valor de presión: {min_presion} en el día {min_presion_dia} hora {min_presion_hora}")
        
    elif opcion == '2':
        for hora in range(24):
            temperatura_prom = temperatura_promedio(sum(registros_mensuales, []), hora)
            if temperatura_prom is not None:
                print(f"Temperatura promedio para la hora {hora}: {temperatura_prom}")
                
    elif opcion == '3':
        dia = int(input("Ingrese el número de día: "))
        if dia < 1 or dia > 31:
            print("Número de día inválido")
        else:
            listar_valores(registros_mensuales[dia-1], dia)
            
    elif opcion == '4':
        break
        
    else:
        print("Opción inválida")

