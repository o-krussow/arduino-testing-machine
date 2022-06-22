gnuplot -e "set terminal png size 1200,600; set output 'out.png'; set datafile separator ','; set timefmt '%S'; plot 'test_results.csv' with lines"
