#!/usr/bin/env python3

import serial
import time
import sys


def begin_test(duration, output_file):

    duration = int(duration)

    start = time.time()
    s = serial.Serial("/dev/ttyACM0", 115200)
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
                
                if len(split_line) == 1:
                    temperature = split_line[0]
                    elapsed_time = time.time() - start


                    f.write(str(elapsed_time)+","+temperature+"\n")
                    print(str(elapsed_time)+","+temperature)
                    

                    if elapsed_time > duration:
                        break

            except UnicodeDecodeError:
                continue

def main(args):
    try:
        duration, output_file = args[1:]
        begin_test(duration, output_file)
    except ValueError:
        print("Usage: ./ser.py <duration> <output-file>")
    
if __name__ == "__main__":
    args = sys.argv
    main(args)



