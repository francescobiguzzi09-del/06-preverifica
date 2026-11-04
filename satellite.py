from sensore import Sensore
class Satellite:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.sensori = {}
        self.letture = []
        
    def aggiungi_sensore(self, sensore: Sensore) -> None:
        if sensore.codice in self.sensori:
            raise ValueError("error")
        self.sensori[sensore.codice] = sensore
        
    def registra_lettura(self, codice: str, valore: float) -> None:
        if codice not in self.sensori:
            raise KeyError("error key")
        self.letture.append({
            "codice": codice,
            "valore": valore,
            "unità": self.sensori[codice].unita,
            "allarme": valore > self.sensori[codice].soglia_massima
        })
    def lettura_allarme(self) -> list[dict]:
        allarm_list=[]
        for lettura in self.letture:
            if lettura["allarme"] == True:
                allarm_list.append(lettura)
        return allarm_list
    def riepilogo(self) -> None:
        for lettura in self.letture:
            allarmati = "ALLARME" if lettura["allarme"] else "ok"
            print(f"codice: {lettura['codice']}, unita: {lettura['unità']}, valore: {lettura['valore']}, stato: {lettura['allarme']}")

