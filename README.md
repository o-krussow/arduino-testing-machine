## Arduino Wagon Wheel Testing Scripts

The ser.py program reads from an arduino over serial to get temperature, then puts the data in test_data.csv

This data can then be read in by gnuplot using ./plot.sh to make a graph

smooth-plot.sh Is the same as plot.sh, except that it applys a smoothing filter to get rid of the jagged edges.

smooth.py reads the data that ser.py outputs, and smooths out the outliers. Below is a before and after comparison.


Raw data:
![preprocessed out.png](./processing_demo/out.png)
After processing by smooth.py:
![first processed out.png](./processing_demo/pre-gnuplot-filter.png)
After gnuplot smoothing:
![processed out.png](./processing_demo/processed-out.png)
Using both smooth.py and gnuplot smoothing:
![double processed out.png](./processing_demo/gnuplot-and-smoothpy-out.png)


I still need to add support for multiple "streams" over serial, I just need to figure out the best way to do that.