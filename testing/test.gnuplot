set title 'Title'
set grid
set datafile separator ','
set xlabel 'Seconds'
set ylabel 'Degrees C'
set timefmt '%S'
set term png
set output 'output.png'
plot 'interpolated.csv' smooth csplines
