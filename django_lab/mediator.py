import re

class Mediator:
    def __init__(self, walidatortxt, walidatoralfa, walidatornum, walidatorpoint, walidatorbig, walidatoreven):
        self.walidatortxt = walidatortxt
        self.walidatortxt.mediator = self
        self.walidatoralfa = walidatoralfa
        self.walidatoralfa.mediator = self
        self.walidatornum = walidatornum
        self.walidatornum.mediator = self
        self.walidatorpoint = walidatorpoint
        self.walidatorpoint.mediator = self
        self.walidatorbig = walidatorbig
        self.walidatorbig.mediator = self
        self.walidatoreven = walidatoreven
        self.walidatoreven.mediator = self
        self.walidatory = {
            "TXT": self.walidatortxt,
            "ALFA": self.walidatoralfa,
            "NUM": self.walidatornum,
            "POINT": self.walidatorpoint,
            "BIG": self.walidatorbig,
            "EVEN": self.walidatoreven,
        }
    def notify(self, tekst):
        if len(tekst) >= 2:
            walidator = tekst.pop()
            self.walidatory[walidator].przetworz(tekst)
        else:
            print("True")

class PodstawowyWalidator:
    def __init__(self, mediator = None):
        self.mediator = mediator
class WalidatorTXT(PodstawowyWalidator):
    def przetworz(self, tekst):
        if re.match('^[a-zA-Z_\ .,]+$', tekst[0]):
            self.mediator.notify(tekst)
        else:
            print("False")
class WalidatorALFA(PodstawowyWalidator):
    def przetworz(self, tekst):
        if re.match('^[a-zA-Z_\ .,0-9]+$', tekst[0]):
            self.mediator.notify(tekst)
        else:
            print("False")
class WalidatorNUM(PodstawowyWalidator):
    def przetworz(self, tekst):
        if re.match('^[0-9]+$', tekst[0]):
            self.mediator.notify(tekst)
        else:
            print("False")
class WalidatorPOINT(PodstawowyWalidator):
    def przetworz(self, tekst):
        if re.match('^-', tekst[0]):
            self.mediator.notify(tekst)
        else:
            print("False")
class WalidatorBIG(PodstawowyWalidator):
    def przetworz(self, tekst):
        if re.match('^[^a-z]+$', tekst[0]):
            self.mediator.notify(tekst)
        else:
            print("False")
class WalidatorEVEN(PodstawowyWalidator):
    def przetworz(self, tekst):
        if re.match('^[0,2,4,6,8]+$', tekst[0]):
            self.mediator.notify(tekst)
        else:
            print("False")

if __name__ == "__main__":
    m = Mediator(WalidatorTXT(), WalidatorALFA(), WalidatorNUM(), WalidatorPOINT(), WalidatorBIG(), WalidatorEVEN())
    with open("testowy.txt", 'r') as file:
        for line in file.readlines():
            line = line.replace("\n","").split(";")
            m.notify(line)
