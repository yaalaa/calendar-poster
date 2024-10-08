from   datetime import datetime, timedelta


# calculate constants
YEAR           = 2025
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

MONTH_SUBTITLES   = [
    'Сечень',
    'Лютый',
    'Сухой',
    'Брезень',
    'Травень',
    'Червец',
    'Липец',
    'Серпень',
    'Вресень',
    'Листопад',
    'Листопад',
    'Студень',
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
    data[ ROW_TITLE                 ][ COL_MONTH + idx * ITEM_COLS ] = MONTH_TITLES   [ idx     ]
    data[ ROW_TITLE + LINE_ROWS     ][ COL_MONTH + idx * ITEM_COLS ] = MONTH_TITLES   [ idx + 6 ]
    data[ ROW_TITLE             + 1 ][ COL_MONTH + idx * ITEM_COLS ] = MONTH_SUBTITLES[ idx     ]
    data[ ROW_TITLE + LINE_ROWS + 1 ][ COL_MONTH + idx * ITEM_COLS ] = MONTH_SUBTITLES[ idx + 6 ]

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

def is_holiday( month, day ):

    if YEAR == 2025:
        if month == 1: # Jan
            return day <= 8
        # if month == 2: # Feb
        #     return day == 23
        # if month == 3: # Mar
        #     return day == 8
        # if month == 4: # April
        #     return day >= 29
        if month == 5: # May
            return day in { 1, 2, 8, 9, }
        if month == 6: # Jun
            return day in { 12, 13 }
        if month == 11: # Nov
            return day in { 3, 4 }
        if month == 12: # Dec
            return day >= 31
    elif YEAR == 2024:
        if month == 1: # Jan
            return day <= 8
        if month == 2: # Feb
            return day == 23
        if month == 3: # Mar
            return day == 8
        if month == 4: # April
            return day >= 29
        if month == 5: # May
            return day in { 1, 9, 10, }
        if month == 6: # Jun
            return day == 12
        if month == 11: # Nov
            return day == 4
        if month == 12: # Dec
            return day >= 30
    elif YEAR == 2023:
        if month == 1: # Jan
            return day <= 8
        if month == 2: # Feb
            return day == 23 or day == 24
        if month == 3: # Mar
            return day == 8
        if month == 5: # May
            return day in { 1, 8, 9 }
        if month == 6: # Jun
            return day == 12
        if month == 11: # Nov
            return day in { 6 }
        if month == 12: # Dec
            return day == 31
    elif YEAR == 2022:
        if month == 1: # Jan
            return day <= 8
        if month == 2: # Feb
            return day == 23
        if month == 3: # Mar
            return day == 8
        if month == 5: # May
            return day in { 2, 3, 9, 10 }
        if month == 6: # Jun
            return day == 13
        if month == 11: # Nov
            return day in { 4 }
        if month == 12: # Dec
            return day == 31
    elif YEAR == 2021:
        if month == 1: # Jan
            return day <= 8
        if month == 2: # Feb
            return day == 23 or day == 22
        if month == 3: # Mar
            return day == 8
        if month == 5: # May
            return day in { 1, 2, 3, 9, 10 }
        if month == 6: # Jun
            return day == 14
        if month == 11: # Nov
            return day in { 4, 5 }
        if month == 12: # Dec
            return day == 31
    elif YEAR == 2020:
        if month == 1: # Jan
            return day <= 8
        if month == 2: # Feb
            return 22 <= day <= 24
        if month == 3: # Mar
            return 7 <= day <= 9
        if month == 5: # May
            return day in { 1, 2, 3, 4, 5, 9, 10, 11 }
        if month == 6: # Jun
            return day == 12
        if month == 11: # Nov
            return day == 4
    elif YEAR == 2019:
        if month == 1: # Jan
            return day <= 8
        if month == 2: # Feb
            return day == 23
        if month == 3: # Mar
            return day == 8
        if month == 5: # May
            return day in { 1, 2, 3, 9, 10 }
        if month == 6: # Jun
            return day == 12
        if month == 11: # Nov
            return day == 4

    return False

