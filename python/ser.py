#!/usr/bin/env python3

'''
Written by Owen Krussow
June 22nd, 2022

This program reads in temperature (and soon, current) data over serial from an arduino and writes it into a csv in relation to time.

serial_device and baud_rate as defined below are important, change as necessary.
'''

import serial
import time
import sys
import lcu

def begin_test(duration, output_file):
    #Change these as needed---------
    serial_device = "/dev/ttyACM0"
    baud_rate = 115200
    #-------------------------------

    duration = int(duration)
    start = time.time()
    s = serial.Serial(serial_device, baud_rate)

    previous_temperature = 0
    temp_sum = 0
    temp_count = 0
    float_temp = 0

    with open(output_file, "w+") as f: 
        while True:
            line_bytes = s.readline()
            try:
                line = line_bytes.decode('utf-8').strip() #line_bytes is a byte string, so we want to encode that byte string into utf-8 so it's easier to work with. strip() removes the \r\n from the end of the string.
                split_line = line.split(" ")
                
                elapsed_time = time.time() - start
                if len(split_line) == 1 and elapsed_time > 0.3:
                    temperature = split_line[0]


                    f.write(str(elapsed_time)+","+temperature+"\n")
                    print(str(elapsed_time)+","+temperature)
                    

                if elapsed_time > duration:
                    break

            except UnicodeDecodeError:
                continue

def main(args):
    try:
        output_file, duration = args[1:]
        begin_test(duration, output_file)
    except ValueError:
        print("Usage: ./ser.py <output-file> <duration>")
    
if __name__ == "__main__":
    args = sys.argv
    main(args)



