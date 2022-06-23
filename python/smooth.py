#!/usr/bin/env python3

'''
Written by Owen Krussow
June 22nd, 2022

This program removes weird spikes from data

It works by looking through the data, then comparing the current value to the previous value. If the new value deviates greater than +/-12%, then deviation_detected is set to true.
When deviation_detected is set to true, new data is ignored until another deviation happens, then deviation_detected is set to false.

The deviation percentage can be tweaked easily down below, the variable name is deviation_tolerance

We ignore data between deviations since any "spike" is going to have an upwards deviation before correcting with a downwards deviation.
'''

import lcu
import sys 

def deviation_from_average(average, value):
    if average == 0:
        average = 1
    return 1 - (value / average)

def deviation_from_previous(previous, value):
    if previous == 0:
        previous = 1
    return 1 - (value / previous)


def smooth_results(if_contents):
    temp_sum = 0
    temp_count = 0
    prev_temp = 0
    prev_temp = ""
    deviation_detected = False
    deviation_tolerance = 0.12

    highest_av_deviation = [0, 0]
    highest_prev_deviation = [0, 0]

    results = [] 

    for if_line in if_contents:
        try:
            sec, temp = if_line
            sec, temp = float(sec), float(temp)
            
            temp_sum += temp
            temp_count += 1

            if temp_count == 1:
                prev_temp = temp

            av_deviation = deviation_from_average((temp_sum/temp_count), temp)
            prev_deviation = deviation_from_previous(prev_temp, temp)

            if av_deviation > highest_av_deviation[0]:
                highest_av_deviation[0] = av_deviation
                highest_av_deviation[1] = sec
            if prev_deviation > highest_prev_deviation[0]:
                highest_prev_deviation[0] = prev_deviation
                highest_prev_deviation[1] = sec


            if (-deviation_tolerance <= prev_deviation <= deviation_tolerance):
                if not deviation_detected:
                    results.append([sec, temp])


            else: #If current temperature exceeds deviation quota, then just write the previous temperature to smooth things out
                if deviation_detected:
                    deviation_detected = False
                else:
                    deviation_detected = True
                print("DEVIATION AT",sec)

            prev_temp = temp
            
        except ValueError:
            continue
    
    print("Highest from average: ", highest_av_deviation)
    print("Highest from previous: ", highest_prev_deviation)

    return results

def main(args):
    try:
        input_file, output_file = args[1:3]
        
        if_to_list = lcu.read_into_list(input_file)

        final_data = smooth_results(if_to_list)

        lcu.list_to_csv(final_data, output_file)

    except ValueError:
        print("Usage: ./smooth.py <input-file> <output-file>")

if __name__ == "__main__":
    args = sys.argv
    main(args)








