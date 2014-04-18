#!/usr/bin/env python

import sys
import argparse

argparser = argparse.ArgumentParser(description='Analyse some bank statements.')
argparser.add_argument('mode', choices=['parse','append','help'])

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