#!/bin/sh
#Written by Owen Krussow
#June 22nd, 2022

#I probably SHOULD make a .gnuplot file with this information, but I want to run/use gnuplot from only one file. (this one)
gnuplot -e "set terminal png size 1200,600; set output '$2'; set datafile separator ','; set xlabel 'Seconds'; set ylabel 'Degrees C'; set timefmt '%S'; plot '$1' smooth csplines"
