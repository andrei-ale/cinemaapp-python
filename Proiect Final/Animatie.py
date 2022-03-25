from Film import Film


class Animatie(Film):
    def __init__(self, titlu, durata, limba_dublare):
        super().__init__(titlu, durata)
        self.limba_dublare = limba_dublare

    def afiseaza_dublare(self):
        print(f"Filmul este dublat in limba: {self.limba_dublare}")

    def __str__(self):
        return f"Titlu: {self.titlu}\nDurata: {self.durata}\nLimba dublarii: {self.limba_dublare}\n"
