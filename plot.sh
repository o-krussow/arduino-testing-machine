gnuplot -e "set terminal png size 1200,600; set output '$2'; set datafile separator ','; set xlabel 'Seconds'; set ylabel 'Degrees C'; set timefmt '%S'; plot '$1' with lines"
