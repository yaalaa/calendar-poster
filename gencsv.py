"""
Usage:
    python -m gencsv >out\out.csv
"""

import csv
import sys


import calc


# write output
csv_params = {}
if not sys.stdout.isatty(): csv_params[ 'lineterminator' ] = '\n'
writer = csv.writer( sys.stdout, **csv_params )
writer.writerows( calc.data )


