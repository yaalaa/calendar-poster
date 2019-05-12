"""
Usage:
    python -m gencsv >out\out.csv
"""

import csv
from   datetime import datetime, timedelta
import sys


# calculate constants
YEAR           = 2019
MONTH_COLS     = 6
ITEM_COLS      = MONTH_COLS + 1
WEEK_ROWS      = 7
LINE_ROWS      = WEEK_ROWS + 3

COLS           = 1
COL_WEEK_LEFT  = COLS; COLS += 2
COL_MONTH      = COLS; COLS += 6 * ITEM_COLS
COL_WEEK_RIGHT = COLS; COLS += 2


ROWS           = 1
ROW_TITLE      = ROWS; ROWS += 2
ROW_WEEK       = ROWS; ROWS += WEEK_ROWS
ROWS          *= 2
ROWS          += 1


data           = [
    [ '' ] * COLS
    for _ in range( ROWS )
]


MONTH_TITLES   = [
    'Январь',
    'Февраль',
    'Март',
    'Апрель',
    'Май',
    'Июнь',
    'Июль',
    'Август',
    'Сентябрь',
    'Октябрь',
    'Ноябрь',
    'Декабрь',
]

WEEKDAY_TITLES = [
    'пн',
    'вт',
    'ср',
    'чт',
    'пт',
    'сб',
    'вс',
]

# fill the weekdays
for idx in range( 7 ):
    title = WEEKDAY_TITLES[ idx ]
    data[ ROW_WEEK             + idx ][ COL_WEEK_LEFT ] = data[ ROW_WEEK            + idx ][ COL_WEEK_RIGHT ] = title
    data[ ROW_WEEK + LINE_ROWS + idx ][ COL_WEEK_LEFT ] = data[ ROW_WEEK + LINE_ROWS+ idx ][ COL_WEEK_RIGHT ] = title

# fill the month titles
for idx in range( 6 ):
    data[ ROW_TITLE             ][ COL_MONTH + idx * ITEM_COLS ] = MONTH_TITLES[ idx     ]
    data[ ROW_TITLE + LINE_ROWS ][ COL_MONTH + idx * ITEM_COLS ] = MONTH_TITLES[ idx + 6 ]

# fill days
for idx in range( 12 ):

    row_base = ROW_WEEK              + ( 0   if idx < 6 else LINE_ROWS )
    col_base = COL_MONTH + ITEM_COLS * ( idx if idx < 6 else idx - 6   )

    col      = col_base

    day      = 1
    dt       = datetime( YEAR, idx + 1, day )
    while dt.month == idx + 1:

        weekday = dt.weekday()
        data[ row_base + weekday ][ col ] = '{}'.format( day )
        day += 1
        dt  += timedelta( days = 1 )
        if weekday == 6: col += 1


# write output
csv_params = {}
if not sys.stdout.isatty(): csv_params[ 'lineterminator' ] = '\n'
writer = csv.writer( sys.stdout, **csv_params )
writer.writerows( data )


