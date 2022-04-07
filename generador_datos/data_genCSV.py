import csv
import random
import time

xlength = vel = fren = rpm = marcha = comb = xtime = 0
comb = 100
x_cord = 40.614537
y_cord = -3.583129

# ESTO ESTÁ ALGO DESORDENADO, REVACT AHORA ES RPM. CORREGIR EN BASE A LO QUE HAY EN RECEPTOR.PY
fieldnames = ["xlength" , "vel" , "fren", "rpm" , "marcha", "comb" , "xtime", "x_cord","y_cord"]


with open('testData.csv', 'w',newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:
    
    with open('testData.csv', 'a',newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        info = {
            "xlength" : xlength,
            "vel" : vel,
            "fren" : fren,
            "rpm" : rpm,
            "marcha" : marcha,
            "comb" : comb,
            "xtime" : xtime,
            "x_cord": x_cord,
            "y_cord":y_cord
        }

        csv_writer.writerow(info)
    
        xlength += random.randint(20, 50)
        vel = random.randint(0, 200)
        fren = random.randint(0, 180)
        rpm = random.randint(0, 8000)
        marcha = random.randint(-1, 6)
        comb -= 0.5
        xtime += 1
        if(xtime % 2 == 1):
            x_cord=40.614536
            y_cord=-3.583130
        else:
            x_cord = 40.614537
            y_cord = -3.583129
        

    time.sleep(1)
