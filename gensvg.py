# import os


import svgwrite


import calc


PAGE_WIDTH_PHYS  = '420mm'
PAGE_HEIGHT_PHYS = '594mm'

PAGE_WIDTH       = 420
PAGE_HEIGHT      = 594

TITLE_FONT_SIZE  = 6
DAY_FONT_SIZE    = 6

FILL_USUAL       = 'black'
FILL_HOLIDAY     = '#a00000'

PAD_OUTER_HORZ   = 20
PAD_OUTER_VERT   = 20
PAD_INTER_VERT   =  3
PAD_TITLE_VERT   = 10
PAD_LINE_VERT    = 20
PAD_ITEM_HORZ    = 1
PAD_WEEK_HORZ    = 10


HEIGHT_INTER     = DAY_FONT_SIZE + PAD_INTER_VERT
HEIGHT_LINE      = TITLE_FONT_SIZE + PAD_TITLE_VERT + 7 * DAY_FONT_SIZE + 6 * PAD_INTER_VERT
HEIGHT_LINE2     = HEIGHT_LINE + PAD_LINE_VERT
HEIGHT_ALL       = HEIGHT_LINE * 2 + PAD_LINE_VERT

WIDTH_WEEKDAY    = 10
WIDTH_ITEM       = ( PAGE_WIDTH - 2 * PAD_OUTER_HORZ - 2 * WIDTH_WEEKDAY - 2 * PAD_WEEK_HORZ - PAD_ITEM_HORZ * 5 ) / 6.0
WIDTH_ITEM2      = WIDTH_ITEM + PAD_ITEM_HORZ
WIDTH_COL        = WIDTH_ITEM / calc.MONTH_COLS


TOP              = PAGE_HEIGHT - PAD_OUTER_VERT - HEIGHT_ALL
TOP_TITLE        = TOP; TOP += TITLE_FONT_SIZE + PAD_TITLE_VERT
TOP_WEEK         = TOP

LEFT             = PAD_OUTER_HORZ
LEFT_WEEKDAY     = LEFT; LEFT += WIDTH_WEEKDAY + PAD_WEEK_HORZ
RIGHT            = PAGE_WIDTH - PAD_OUTER_HORZ
RIGHT_WEEKDAY    = RIGHT; RIGHT -= WIDTH_WEEKDAY + PAD_WEEK_HORZ
LEFT_ITEM        = LEFT

print( 'Top part height: {}'.format( TOP ) )

dwg = svgwrite.Drawing( 'out/out.svg', size = ( PAGE_WIDTH_PHYS, PAGE_HEIGHT_PHYS ) )
dwg.viewbox( 0, 0, PAGE_WIDTH, PAGE_HEIGHT )

# draw weekdays
for idx in range( 7 ):

    fill = FILL_USUAL if idx < 5 else FILL_HOLIDAY

    dwg.add( dwg.text( calc.WEEKDAY_TITLES[ idx ], insert = ( RIGHT_WEEKDAY - WIDTH_WEEKDAY, TOP_WEEK + idx * HEIGHT_INTER                ), font_size = DAY_FONT_SIZE, fill = fill ) )
    dwg.add( dwg.text( calc.WEEKDAY_TITLES[ idx ], insert = ( LEFT_WEEKDAY                 , TOP_WEEK + idx * HEIGHT_INTER + HEIGHT_LINE2 ), font_size = DAY_FONT_SIZE, fill = fill ) )
    dwg.add( dwg.text( calc.WEEKDAY_TITLES[ idx ], insert = ( LEFT_WEEKDAY                 , TOP_WEEK + idx * HEIGHT_INTER                ), font_size = DAY_FONT_SIZE, fill = fill ) )
    dwg.add( dwg.text( calc.WEEKDAY_TITLES[ idx ], insert = ( RIGHT_WEEKDAY - WIDTH_WEEKDAY, TOP_WEEK + idx * HEIGHT_INTER + HEIGHT_LINE2 ), font_size = DAY_FONT_SIZE, fill = fill ) )


# draw months
for idx in range( 12 ):

    top  = TOP_TITLE +               ( 0   if idx < 6 else HEIGHT_LINE2 ) - TITLE_FONT_SIZE / 2
    left = LEFT_ITEM + WIDTH_ITEM2 * ( idx if idx < 6 else idx - 6      )

    dwg.add(
        dwg.text(
            calc.MONTH_TITLES[ idx ],
            insert      = ( left + WIDTH_ITEM / 2, top ),
            font_size   = TITLE_FONT_SIZE,
            fill        = 'black',
            text_anchor = 'middle',
            font_weight = 'bold'
        )
    )

    dwg.add(
        dwg.text(
            calc.MONTH_SUBTITLES[ idx ],
            insert      = ( left + WIDTH_ITEM / 2, top + TITLE_FONT_SIZE * 3 / 2 ),
            font_size   = TITLE_FONT_SIZE,
            fill        = 'green', #'blue',
            text_anchor = 'middle',
            font_weight = 'bold'
        )
    )

# draw days
for idx in range( 12 ):

    row_base = calc.ROW_WEEK                   + ( 0   if idx < 6 else calc.LINE_ROWS )
    col_base = calc.COL_MONTH + calc.ITEM_COLS * ( idx if idx < 6 else idx - 6        )

    top_base  = TOP_WEEK                + ( 0   if idx < 6 else HEIGHT_LINE2 )
    left_base = LEFT_ITEM + WIDTH_ITEM2 * ( idx if idx < 6 else idx - 6      )

    for row in range( 7 ):
        for col in range( calc.MONTH_COLS ):

            text = calc.data[ row_base + row ][ col_base + col ]
            if not text: continue

            top  = top_base  + HEIGHT_INTER * row
            left = left_base + WIDTH_COL    * col

            if row >= 5: is_holiday = True
            else: is_holiday = calc.is_holiday( idx + 1, int( text ) )

            fill = FILL_USUAL if not is_holiday else FILL_HOLIDAY

            dwg.add( dwg.text( text, insert = ( left + WIDTH_COL, top ), font_size = DAY_FONT_SIZE, fill = fill, text_anchor = 'end' ) )




dwg.save( pretty = True )

