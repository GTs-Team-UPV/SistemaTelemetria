import csv
import random
import time

xlength = 0
vel = 0
fren = 0
marcha = 0
revact = 0
comb = 100
xtime = 0

fieldnames = ["xlength" , "vel" , "fren" , "marcha" , "revact" , "comb" , "xtime"]


with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:
    
    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        info = {
            "xlength" : xlength,
            "vel" : vel,
            "fren" : fren,
            "marcha" : marcha,
            "revact" : revact,
            "comb" : comb,
            "xtime" : xtime
        }

        csv_writer.writerow(info)
        print(xlength, vel, fren, marcha, revact, comb, xtime)

        xlength += random.randint(20, 50)
        vel = random.randint(0, 200)
        fren = random.randint(0, 180)
        marcha = random.randint(-1, 6)
        revact = random.randint(0, 8000)
        comb -= 0.5
        xtime += 1
        

    time.sleep(1)
