import json
import sys
import os
import time

def menu_startowe():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("="*40)
        print("   WITAJ W QUIZIE Z 'MISTRZA I MAŁGORZATY'")
        print("="*40)
        print("1. Rozpocznij quiz")
        print("2. Zakończ program")
        print("="*40)

        wybor = input("Wybierz opcję (1/2): ").strip()
        if wybor in ["1", "2"]:
            return wybor
        print("Nieprawidłowy wybór. Wpisz 1 lub 2.")
        input("Naciśnij Enter, by spróbować ponownie...")

def wczytaj_pytania(plik: str):
 
    try:
        with open(plik, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        input(f"Błąd podczas wczytywania pytań. Wciśnij Enter, by zakończyć. ({e})")
        sys.exit(1)

def uruchom_quiz(pytania: list):
 
    wynik = 0
    suma = len(pytania)
    odpowiedzi_uzytkownika = []
    start_czas = time.time()

    print("\nRozpoczynasz quiz... Powodzenia!\n")
    czas_start = time.time()

    for numer, p in enumerate(pytania, start=1):
        klucze_odpowiedzi = sorted(p['odpowiedzi'].keys())
        
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Pytanie {numer}: {p['pytanie']}")
            for klucz in klucze_odpowiedzi:
                print(f"  {klucz}) {p['odpowiedzi'][klucz]}")

            odp = input("Twoja odpowiedź (a/b/c/d): ").strip().lower()
            if odp in klucze_odpowiedzi:
                break
            print("Nieprawidłowy wybór. Wpisz a, b, c lub d.")
            input("Naciśnij Enter, by spróbować ponownie")

        odpowiedzi_uzytkownika.append(odp)
        poprawna = p['poprawna'].lower()
        wybrany_tekst = p['odpowiedzi'][odp]
        poprawny_tekst = p['odpowiedzi'][poprawna]

        if odp == poprawna:
            print(f"Poprawnie! Wybrałeś '{odp}) {wybrany_tekst}'.\n")
            wynik += 1
        else:
            print(
                f"Źle. Wybrałeś '{odp}) {wybrany_tekst}'. "
                f"Poprawna odpowiedź to '{poprawna}) {poprawny_tekst}'.\n"
            )

        input("Naciśnij Enter, by kontynuować...")

    koniec_czas = time.time()
    czas_trwania = round(koniec_czas - start_czas, 2)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Podsumowanie twoich odpowiedzi:\n")

    for idx, p in enumerate(pytania, start=1):
        dane = odpowiedzi_uzytkownika[idx - 1]
        dane_tekst = p['odpowiedzi'][dane]
        poprawna = p['poprawna'].lower()
        poprawna_tekst = p['odpowiedzi'][poprawna]

        print(f"{idx}. {p['pytanie']}")
        print(f"   Twoja odpowiedź: {dane}) {dane_tekst}")
        print(f"   Poprawna odpowiedź: {poprawna}) {poprawna_tekst}\n")
    
    print("="*40)
    print(f"Twój wynik: {wynik}/{suma}")
    print(f"Czas trwania quizu: {czas_trwania} sekund.\n")
    print("="*40)

if __name__ == '__main__':
    try:
        while True:
            wybor = menu_startowe()
            if wybor == "1":
                pytania = wczytaj_pytania('questions.json')
                uruchom_quiz(pytania)
                input("\nNaciśnij Enter, by wrócić do menu...")
            else:
                print("Quiz nie rozpoczęty.")
                sys.exit(0)
    except KeyboardInterrupt:
        print("\nPrzerwano działanie programu.")
        sys.exit(0)
