import random

class Handler:

    next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler
    def handle(self, wiadomosc):
        if self.next_handler:
            return self.next_handler.handle(wiadomosc)
        return None


class SpamHandler(Handler):
    def handle(self, napis):
        if napis.kategoria == "spam":
            napis.wiadomosc = "UWAGA! TO JEST SPAM. " + napis.wiadomosc
            return super().handle(napis)
        else:
            napis.wiadomosc += "To nie jest spam. "
            return super().handle(napis)
class WazneHandler(Handler):
    def handle(self, napis):
        if napis.kategoria == "ważne":
            napis.wiadomosc = "UWAGA! WAŻNA WIADOMOŚĆ. " + napis.wiadomosc
            return super().handle(napis)
        else:
            napis.wiadomosc += "To nie jest ważna wiadomość. "
            return super().handle(napis)
class InneHandler(Handler):
    def handle(self, napis):
        if napis.kategoria == "inne":
            return super().handle(napis)
        else:
            napis.wiadomosc += "To nie jest wiadomość z kategorii inne. "
            return super().handle(napis)
class Napis:
    wiadomosc = ""
    kategoria = ""

def losuj(string):
    Napis.wiadomosc = string
    Napis.kategoria = random.choice(KATEGORIE)
    return Napis

if __name__=="__main__":

    KATEGORIE = ["spam", "ważne", "inne"]

    spam = SpamHandler()
    wazne = WazneHandler()
    inne = InneHandler()
    spam.set_next(wazne).set_next(inne)

    print("INPUT: 'Przykładowa wiadomość.', kategoria -> "+losuj("Przykładowa wiadomość. ").kategoria)
    spam.handle(Napis)
    print("OUTPUT: "+Napis.wiadomosc)
