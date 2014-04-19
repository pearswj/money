#!/usr/bin/python

import sqlite3
import csv
import time
import json

db_name = 'bank.db'

def append(file):
    """Takes bank transactions from a csv file and adds them to the database.
    Ignores duplicates."""

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

def get_json():
    """Gets all the transactions as a JSON string."""

    con = sqlite3.connect(db_name)
    
    with con:
        #TODO: print contents of database
        #TODO: package in JSON string and return
        cur = con.cursor()
        #cur.execute("")
        cur.execute("SELECT * FROM Transactions")
        r = [dict((cur.description[i][0], value) \
            for i, value in enumerate(row)) for row in cur.fetchall()]
        return json.dumps(r)