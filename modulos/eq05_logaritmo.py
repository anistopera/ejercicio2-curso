## Responsable: Dayana Ibarra Zarate
import math


class Logaritmo:

    def logaritmo_base10(self, numero):
       
        if not isinstance(numero, (int, float)):
            raise ValueError(f"'{numero}' no es un número válido.")
        if numero <= 0:
            raise ValueError("El logaritmo solo está definido para números mayores que 0.")

        return math.log10(numero)

    def logaritmo_base_personalizada(self, numero, base):
       
        if not isinstance(numero, (int, float)) or not isinstance(base, (int, float)):
            raise ValueError("El número y la base deben ser valores numéricos.")
        if numero <= 0:
            raise ValueError("El logaritmo solo está definido para números mayores que 0.")
        if base <= 0 or base == 1:
            raise ValueError("La base debe ser mayor que 0 y distinta de 1.")

        return math.log(numero, base)

    def logaritmo_natural(self, numero):
        
        if not isinstance(numero, (int, float)):
            raise ValueError(f"'{numero}' no es un número válido.")
        if numero <= 0:
            raise ValueError("El logaritmo solo está definido para números mayores que 0.")

        return math.log(numero)


if __name__ == "__main__":
    operacion = Logaritmo()
    numero = 1000
    resultado = operacion.logaritmo_base10(numero)
    print(f"El logaritmo base 10 de {numero} es: {resultado}")