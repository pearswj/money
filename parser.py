# -*- coding: utf-8 -*-
import re

def tocsv(file):
    """Turns plain-text bank statements into a csv string."""

    date = None
    desc = None
    amou = None
    bala = None

    print "date,description,amount,balance"

    SPLIT_CHR = u'\xa0' # '†'

    for line in file.readlines():
        try:
            line = line.decode('windows-1252') # 'utf-8'
        except:
            print 'Error decoding unicode input.'
            return
        #if line.startswith("From"):
            #print line.strip().split('\xa0')
        if line.startswith("Date"):
            date = line.strip().split(SPLIT_CHR)[1]
        if line.startswith("Description"):
            desc = re.split(',[0-9]', line.strip().split(SPLIT_CHR)[1])[0]
        if line.startswith("Amount"):
            amou = line.strip().split(SPLIT_CHR)[1].encode('ascii', 'ignore')
        if line.startswith("Balance"):
            bala = line.strip().split(SPLIT_CHR)[1].encode('ascii', 'ignore')
        if (date and desc and amou and bala):
            print '"%s","%s","%s","%s"' % (date, desc, amou, bala)
            date = None
            desc = None
            amou = None
            bala = None
