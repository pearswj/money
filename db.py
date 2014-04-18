#!/usr/bin/python

import sqlite3
import csv
import time

def append(file):
    """Takes bank transactions from a csv file and adds them to the database.
    Ignores duplicates."""
    
    db_name = 'bank.db'

    con = sqlite3.connect(db_name)

    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS transactions( \
            date TIMESTAMP, description TEXT, amount REAL, balance REAL, \
            UNIQUE(date, description, amount, balance))")
    
        # read csv from stdin
        found = failed = 0
        data = file.readlines()
        if data:
            reader = csv.reader(data)
            reader.next()
            for row in reader:
                found += 1
                
                # fix date format
                date = time.strptime(row[0], "%d/%m/%Y")
                date = time.strftime("%Y-%m-%d", date)
                row[0] = date
            
                # insert row into database, being careful not to create duplicates
                try:
                    cur.execute("INSERT OR FAIL INTO transactions VALUES(?, ?, ?, ?)", row)
                except:
                    failed += 1
                    
            print "Found: " + str(found)
            print "Added: " + str(found - failed) + " (" + str(failed) + " duplicates)"
    