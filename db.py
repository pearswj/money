#!/usr/bin/python

import sqlite3
import sys
import csv
import time

con = sqlite3.connect('bank.db')#,detect_types=sqlite3.PARSE_DECLTYPES)

with con:
    cur = con.cursor()
    #cur.execute("DROP TABLE IF EXISTS transactions")
    cur.execute("CREATE TABLE Transactions(date TIMESTAMP, description TEXT, amount REAL, balance REAL, UNIQUE(date, description, amount, balance))")
    
    # read csv from stdin
    fails = 0
    data = sys.stdin.readlines()
    if data:
        found = len(data) - 1
        print "Found: " + str(found)
        reader = csv.reader(data)
        reader.next()
        for row in reader:
            
            # fix date format
            date = time.strptime(row[0], "%d/%m/%Y")
            date = time.strftime("%Y-%m-%d", date)
            row[0] = date
            
            # insert row into database, being careful not to create duplicates
            try:
                cur.execute("INSERT OR FAIL INTO Transactions VALUES(?, ?, ?, ?)", row)
            except:
                fails += 1
        print "Added: " + str(found - fails) + " (" + str(fails) + " duplicates)"
    
    '''
    cur.execute("SELECT * FROM Transactions")
    rows = cur.fetchall()
    rows=zip(*rows)[0]

    for row in rows:
        print row
    '''
    #for row in csv.reader(iter(sys.stdin.readline, '')):
    #    print("Read: ({}) {!r}".format(time.time(), row))
    