#!/usr/bin/env python3

import lcu

'''
Written by Owen Krussow
June 22nd, 2022

My initial thought was that this program would exist to create "higher resolution" data from the original data, since the original data appeared very jagged in the graphs.

I don't think this ended up being as necessary as I thought, gnuplot and smooth.py seem to do a good enough job.

Explanation for how this works:
    Lets say the original data looks like this: 
        1 second: 25C, 2 second: 26C, 3 second: 26.5C

        After being run once through this program:

        1 second: 25C, 1.5 second: 25.5C, 2 second: 26C, 2.5 second: 26.25C, 3 second: 26.5C

        A second time:

        1 second: 25C, 1.25 second: 25.25C, etc
'''

import sys 

def average_points(p1, p2):
    return (p1+p2)/2


def interpolate_results(data):

    old_data = data
    interpolated_data = []
    
    for index in range(len(old_data)):
        back = index
        front = index+1
        if front < len(old_data):
            '''
            I like to conceptualize this as:
             <back> <> <front>
               ^    ^    ^
               |    |    |
            index   |    |
                average  |
                      index+1
            where back and front are both elements of the list (data)
            And "average" is the element that we are making up    
            '''
            back_time = old_data[back][0]
            front_time = old_data[front][0]

            back_temp = old_data[back][1]
            front_temp = old_data[front][1]

            average_time = average_points(back_time, front_time)
            average_temp = average_points(back_temp, front_temp)

            interpolated_data.append(old_data[back])
            interpolated_data.append([average_time, average_temp])

    interpolated_data.append(old_data[-1]) #append last value because loop won't

    return interpolated_data



def run_interpolate(numtimes, data):
    for time in range(numtimes):
        print(time)
        data = interpolate_results(data)
    return data


def main(args):
    try:
        input_file, output_file, numtimes = args[1:4]
        numtimes = int(numtimes)

        input_file_list = lcu.read_into_list(input_file)

        final_data = run_interpolate(numtimes, input_file_list)

        lcu.list_to_csv(final_data, output_file)
    except ValueError:
        print("Usage: ./interpolate.py <input-file> <output-file> <iterations>")

if __name__ == "__main__":
    args = sys.argv
    main(args)








