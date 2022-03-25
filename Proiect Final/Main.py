from Cinematograf import Cinematograf
from Drama import Drama
from Animatie import Animatie


if __name__ == "__main__":
    cinema = Cinematograf("Popular", "Constanta")
    print("Bine ati venit la cinematograful Popular din Constanta !")
    while True:
        try:
            op = input("Introduceti o optiune: ").strip()
            op_list = op.split()
            if len(op_list) == 4:
                op_list[2] = int(op_list[2])
                if op_list[0] == "adauga_drama":
                    op_list[3] = int(op_list[3])
                if op_list[2] > 180:
                    raise ValueError("Durata filmelor trebuie sa fie de cel mult 180 de minute."
                                     " Va rugam introduceti o valoare corecta.")
        except ValueError as e:
            print(e)
            continue
        if op_list[0] == "adauga_drama":
            film_nou = Drama(op_list[1], op_list[2], op_list[3])
            cinema.adaugare_film(film_nou)
            print("Filmul a fost adaugat.")

        elif op_list[0] == "adauga_animatie":
            film_nou = Animatie(op_list[1], op_list[2], op_list[3])
            cinema.adaugare_film(film_nou)
            print("Filmul a fost adaugat.")

        elif op == "afisare":
            print("Cinematograful ruleaza urmatoarele filme: ")
            cinema.afisare()

        elif op == "afisare_animatii":
            cinema.afisare_animatii()

        elif op == "alege_film":
            cinema.alege_film()
            print("")

        elif op_list[0] == "salveaza_filme":
            cinema.salveaza_filme(op_list[1])
            print("Filmele adaugate au fost salvate.")

        elif op == "exit":
            break

        else:
            print("Comanda nerecunoscuta.\n")
