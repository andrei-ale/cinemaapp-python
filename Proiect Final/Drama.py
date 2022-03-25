from Film import Film


class Drama(Film):
    def __init__(self, titlu, durata, varsta):
        super().__init__(titlu, durata)
        self.varsta = varsta

    def __str__(self):
        return f"Titlu: {self.titlu}\nDurata: {self.durata}\nVarsta minima: {self.varsta}\n"
