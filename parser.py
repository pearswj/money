import re
import sys

date = None
desc = None
amou = None
bala = None

print "date,description,amount,balance"

for line in sys.stdin.readlines():
    #if line.startswith("From"):
        #print line.strip().split('\xa0')
    if line.startswith("Date"):
        date = line.strip().split('\xa0')[1]
    if line.startswith("Description"):
        desc = re.split(',[0-9]', line.strip().split('\xa0')[1])[0]
    if line.startswith("Amount"):
        amou = line.strip().split('\xa0')[1]
    if line.startswith("Balance"):
        bala = line.strip().split('\xa0')[1]
    if (date and desc and amou and bala):
        print '"%s","%s","%s","%s"' % (date, desc, amou, bala)
        date = None
        desc = None
        amou = None
        bala = None