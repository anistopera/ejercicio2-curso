#Responsable: Franz Orellana (eq04)
class DivisionExacta:
    @staticmethod
    def dividir(x, y):
        if y == 0:
            return "el denominador no puede ser 0"
        return x // y