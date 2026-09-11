#Responsable: Torrico Copali Jorge David(eq04)

def dividir_por_multiplicacion(dividendo, divisor):
    if divisor == 0:
        raise ValueError("No se puede dividir entre cero")
    
    signo = 1
    if (dividendo < 0) != (divisor < 0):
        signo = -1
    
    dividendo = abs(dividendo)
    divisor = abs(divisor)
    
    cociente = 0
    acumulado = 0
    
    while acumulado + divisor <= dividendo:
        cociente += 1
        acumulado = divisor * cociente
    
    return cociente * signo, dividendo - acumulado


dividendo = float(input("Ingresa el dividendo: "))
divisor = float(input("Ingresa el divisor: "))

cociente, residuo = dividir_por_multiplicacion(dividendo, divisor)
print(f"Cociente: {cociente}")
print(f"Residuo: {residuo}")