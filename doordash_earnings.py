import csv
import pandas as pd
import time

date = []
earnings = []
gas = []
miles = []
dash_time = []
active_time = []
deliveries = []

entries = int(input("How many entries would you like to make? "))

with open("doordash_earnings.csv", "a") as dde:
    writer = csv.writer(dde)
    writer.writerow(["", "Date", "Earnings", "Gas", "Miles", "Dash Time", "Active Time", "Deliveries"])


for i in range(entries):
    date.append(input("What was the date? "))
    earnings.append(float(input("What were your earnings? ")))
    gas.append(float(input("How much was gas? ")))
    mi = int(input("How many miles did you start with? "))
    mf = int(input("How many miles did you end with? "))
    mt = mf - mi
    miles.append(mt)
    dash_time.append(input("What was the dash time? "))
    active_time.append(input("What was the active time? "))
    deliveries.append(int(input("How many deliveries did you make? ")))
    print("\n")

    dict = {'date':date, 'earnings':earnings, 'gas':gas, 'miles':miles, 'dash_time':dash_time, 'active_time':active_time, "deliveries":deliveries}


class Dash:
    def __init__(self, date, earnings, miles, gas, dash_time, active_time, deliveries):
        self.date = date
        self.earnings = earnings
        self.miles = miles
        self.gas = gas
        self.dash_time = dash_time
        self.active_time = active_time
        self.deliveries = deliveries
                    

    def write_csv(self):
        df = pd.DataFrame(dict)
        df.to_csv('doordash_earnings.csv', mode="a", index=False)

    def net_income(self):
        for i in active_time:
            i *= 60
        net = sum(earnings)- sum(gas) / (sum(active_time) / 60)
        return net

    def per_hour(self):
        net = sum(earnings) - sum(gas) / (sum(active_time) / 60)
        per_hour = net / sum(active_time)
        return per_hour


def tires(miles):
    tires = (sum(miles) / 4000) * 600
    return tires
def oil(miles):
    oil = (sum(miles) / 3000) * 100
    return oil



e = Dash(date, earnings, miles, gas, dash_time, active_time, deliveries)
e.write_csv()


