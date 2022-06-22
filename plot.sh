gnuplot -e "set terminal png size 1200,600; set output 'out.png'; set datafile separator ','; set xlabel 'Seconds'; set ylabel 'Degrees C'; set timefmt '%S'; plot 'test_results.csv' with lines"
