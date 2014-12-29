#!/usr/bin/env python

import sys
import argparse

from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)

import codecs
UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

argparser = argparse.ArgumentParser(description='Analyse some bank statements.')
argparser.add_argument('mode', choices=['parse','append','serve','help'])

args = argparser.parse_args()

if args.mode == 'help':
    argparser.print_help()
    sys.exit()
elif args.mode == 'parse':
    import parser
    parser.tocsv(sys.stdin)
elif args.mode == 'append':
    import db
    db.append(sys.stdin)
elif args.mode == 'serve':
    import server
    server.start()
