# class Ave:
#     def volar(self):
#         return "estoy volando"
# class Pinguino(Ave):
#     def volar(self):
#         return "no puedo volar"

class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        return "estoy volando"
class AveNoVoladora(Ave):
    def volar(self):
        return "no puedo volar"
    