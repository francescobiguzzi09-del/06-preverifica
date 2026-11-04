from sensore import Sensore
from satellite import Satellite
if __name__=="__main__":
    satellite = Satellite("CubeSat Aurora")
    satellite.aggiungi_sensore(Sensore("TMP-01", "temperatura", "C", 45))
    satellite.aggiungi_sensore(Sensore("BAT-01", "tensione batteria", "V", 8.4))
    satellite.aggiungi_sensore(Sensore("GYR-01", "velocita angolare", "deg/s", 12))
    satellite.registra_lettura("TMP-01", 50)
    print(satellite.lettura_allarme())
    satellite.riepilogo()