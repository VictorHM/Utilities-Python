import json, csv, datetime, time
import requests, sys
import threading, logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
litecoinUrlCZK = 'https://api.coinmarketcap.com/v1/ticker/litecoin/?convert=EUR'
bitcoinUrlCZK = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=CZK'

valueCZKLite = []


def checkPricesTreshold(value_lite, threshold_val):
    # TODO check the value against predetermined value
    iValue_lite = float(value_lite)
    if iValue_lite > threshold_val:
        send_alert(value_lite)

def getData():
    dt = datetime.datetime.now()
    valueCZKLite=[]
    try:
        while dt.hour < 18 and dt.hour >= 9:
            respoCZKLite = requests.get(litecoinUrlCZK)
            respoCZKLite.raise_for_status()
            liteCZKData = json.loads(respoCZKLite.text)

            # lista que recibe valor de moneda
            dt = datetime.datetime.now()
            valueCZKLite.append([dt, liteCZKData[0]['price_eur']])
            time.sleep(900)  # sleep for 15 min
        # END OF WHILE
    except KeyboardInterrupt:
        print("Done.\n")
    # TODO Salvar en archivo CSV con nombre [dia_mes_anio]_LiteCoinData.csv
    if valueCZKLite:
        date_string = datetime.datetime.now()
        filename = date_string.strftime('%d_%B_%Y') + '_' + 'LiteCoinData.csv'
        # outputFile = open(filename, 'w', newline='')
        outputFile = open(filename, 'w')
        outWriter = csv.writer(outputFile)
        for list in valueCZKLite:
            outWriter.writerow(list)
        outputFile.close()
    else:
        print('Fuera de horario')


# TODO Crear un daemon thread que compruebe la fecha constantemente y arranque el programa cada vez que llega el momento de tomar datos
def send_alert(price_now):
    print('ALERTA! valor de LiteCoin por encima de limite {}', price_now)


def main():
    try:
        dt = datetime.datetime.now()
        # thread1 = threading.Thread(target=getData)
        logging.debug('Hora actual %s' % dt.time())
        logging.debug('Hora %d' % dt.hour)

        while dt.hour > 19:
            if dt.hour < 9 or dt.hour >= 18:
                logging.debug('Fuera de horario. Dormir durante 15 minutos')
                time.sleep(3600)  # TODO calcular tiempo hasta siguiente dia a las 9 y sleep
            else:
                logging.debug('Dentro de horario. Recabar datos y lanzar hilos')
                respoCZKLite = requests.get(litecoinUrlCZK)
                respoCZKLite.raise_for_status()
                liteCZKData = json.loads(respoCZKLite.text)
                thread1 = threading.Thread(target=checkPricesTreshold, args=(liteCZKData[0]['price_eur'], 250))
                thread2 = threading.Thread(target=getData())
                thread1.start()
                thread2.start()
                logging.debug('El numero de hilos es %s' % threading.active_count())
                thread1.join()
                thread2.join()
                break
    except KeyboardInterrupt:
        print('Programa finalizado')


# Point of Entry
print('Empezamos')
main()
# input("Pulsa una tecla para continuar...")
