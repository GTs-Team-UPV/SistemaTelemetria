import serial
import struct
import csv
import random
import time

ser = serial.Serial('COM9', 57600, timeout=15, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
ser.write("radio get freq\r\n".encode())
print(ser.readline())
ser.write("radio set mod fsk\r\n".encode())
print(ser.readline())
ser.write("radio set bitrate 19000\r\n".encode())
print(ser.readline())
ser.write("mac pause\r\n".encode())
print(ser.readline())
radio_decoded = 'radio_err\r\n'
fieldnames = ["xlength" , "vel" , "fren" ,"rpm", "marcha", "comb" , "xtime", "x_cord", "y_cord"]

def listen():
    global radio_decoded
    
    with open('received_data.csv', 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
    while True:
        while radio_decoded == 'radio_err\r\n':
            ser.write("radio rx 0\r\n".encode())
            print(ser.readline())
            linea = ser.readline()
            print(linea)
            tamanyo = len(linea)
            print(tamanyo)
            if(len(linea) == 84):
                radio_decoded = linea.decode('utf-8')
                print(radio_decoded)
            
            
        #Cuando se salga del bucle, tendremos en radio 
        #decoded el data bueno que habrá que tratar
        #A lo mejor hay que quitar el radio rx antes de la trama
        radio_decoded = radio_decoded[10:]
        radio_decoded = radio_decoded[:72]
        hexList = reordenar_trama(radio_decoded)
        floatList = []
        for item in hexList:
            itemFloat = struct.unpack('!f', bytes.fromhex(item))[0]
            floatList.append(itemFloat)
        append_CSV(floatList)
        radio_decoded = 'radio_err\r\n'

            


def append_CSV(floatList):
    xlength = vel = fren = marcha = rpm = xtime = xcord = ycord = 0
    comb = 100
    print(floatList)
    global fieldnames
    with open('received_data.csv', 'a',newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        info = {
            "xlength" : round(floatList[0],2),
            "vel" : round(floatList[1],2),
            "fren" : round(floatList[2],2),
            "rpm" : round(floatList[3],2),
            "marcha" : int(floatList[4]),
            "comb" : int(floatList[5]),
            "xtime" : round(floatList[6],2),
            "x_cord": round(floatList[7],4),
            "y_cord": round(floatList[8],4)
        }

        csv_writer.writerow(info)

        # xlength += floatList[0]
        # vel = floatList[1]
        # fren = floatList[2]
        # rpm = floatList[3]
        # marcha = floatList[4]
        comb -= 0.5
        #xtime += 1

def reordenar_trama(trama):
    hexUnorderedList = [trama[i:i+8] for i in range(0, len(trama), 8)]
    print(hexUnorderedList)
    hexList = []
    for item in hexUnorderedList:
        newItem = str(item[0:4]+item[4:8])
        hexList.append(newItem)
    print(hexList)
    return hexList

if __name__ == '__main__':
    listen()
    # hexList = reordenar_trama('097444FE4ED0427D2F4C3EBD871A458A00004000')
    # floatList = []
    # for item in hexList:
    #     itemFloat = struct.unpack('!f', bytes.fromhex(item))[0]
    #     floatList.append(itemFloat)
    # append_CSV(floatList)
    