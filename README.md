# calendar-poster

## new year support - for example 2023 

* open `calc.py`
* set `YEAR` to `2023`
* scroll down to `is_holiday`
* make a copy of the `if YEAR == 2022:` if-block in front
* correct header to `if YEAR == 2023:` + adjust holidays
* adjust `if YEAR == 2022:` to `elif YEAR == 2023:`
* run `gensvg.py` (from Py console: `exec( open( 'gensvg.py' ).read() )`)
* copy `out/out.svg` to `artifacts/out_2023.svg`
* commit changes `calc.py` with message `calc: support 2023`