import math
import json
import datetime
import csv
import os
import sys

def round_down(value, decimals):
    return math.trunc(value*(10**decimals))/(10**decimals)

def themore(price_dollar, exrate):
    visa_rate = 0.011
    shinhan_rate = 0.0018
    
    # from visa to shinhan
    visa_fee = round_down(price_dollar * visa_rate,2)
    charge_dollar = price_dollar + visa_fee
    
    # from shinhan to user
    charge_won = round_down(charge_dollar * exrate, 0)
    shinhan_fee = round_down(price_dollar * shinhan_rate * exrate, 0)
    charge_final = charge_won + shinhan_fee
    return charge_final

today = datetime.datetime.today().strftime('%Y%m%d')

base_dir = os.path.dirname(os.path.abspath(__file__))

# Load 'recent.json'
with open(os.path.join(base_dir, 'recent.json')) as f:
    recent = json.load(f)
    f.close()

# Check for rencent update
if recent['date'] == today:
    exit()
else:
    import rate2
    exrate = rate2.exrate

temp = round_down((5988 / exrate) * 0.989, 2)

while themore(temp, exrate) <= 5999:
    temp = (temp*100 + 1) / 100

temp = (temp*100 - 1) / 100

out = [today, exrate, temp, themore(temp, exrate)]
out2 = {
    "date":today,
    "exrate":exrate,
    "dollar":temp,
    "won":themore(temp, exrate)
}

with open(os.path.join(base_dir, 'history.csv'), 'a') as f:
    writer = csv.writer(f)
    writer.writerow(out)
    
with open(os.path.join(base_dir, 'recent.json'), 'w') as f:
    json.dump(out2, f, indent = 2)
