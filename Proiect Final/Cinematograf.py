from Drama import Drama
from Animatie import Animatie
import random


class Cinematograf:
    def __init__(self, denumire, locatie, lista_filme=[]):
        self.denumire = denumire
        self.locatie = locatie
        self.lista_filme = lista_filme

    def adaugare_film(self, film_nou):
        self.lista_filme.append(film_nou)

    def afisare(self):
        for film in self.lista_filme:
            print(film.__str__())

    def afisare_animatii(self):
        for film in self.lista_filme:
            if isinstance(film, Animatie):
                print(film.__str__())

    def alege_film(self):
        incearca_un_film = random.choice(self.lista_filme)
        print(f"Ai ales filmul: {incearca_un_film.titlu}")
        print(incearca_un_film.__str__())

    def salveaza_filme(self, fisier):
        with open(f"{fisier}.txt", mode="wt") as f:
            f.write("Cinematograful Popular ruleaza urmatoarele filme:\n\n")
            for film in self.lista_filme:
                if isinstance(film, Drama):
                    f.write(f"Titlu: {film.titlu} - Durata: {film.durata} - Varsta: {film.varsta}\n")
                elif isinstance(film, Animatie):
                    f.write(f"Titlu: {film.titlu} - Durata: {film.durata} - Limba dublarii: {film.limba_dublare}\n")
