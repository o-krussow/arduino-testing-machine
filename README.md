This program reads from an arduino over serial to get temperature, then puts the data in test_data.csv

This data can then be read in by gnuplot using ./plot.sh to make a graph

Example Graph:
![alt text](./out.png)

I still need to add support for multiple "streams" over serial, I just need to figure out the best way to do that.