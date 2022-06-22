#!/usr/bin/env python3
import sys 

def average_points(p1, p2):
    return (p1+p2)/2

def read_into_list(filename):
    retlist = []
    with open(filename, "r") as f:
        f_contents = f.read()
    
    line_list = f_contents.split("\n")
    for line in line_list:
        split_line = line.split(",")
        if len(split_line) > 0 and split_line[0] != "" and split_line[1] != "":
            retlist.append([float(split_line[0]), float(split_line[1])])
    
    return retlist

def list_to_csv(data, filename):
    with open(filename, "w+") as f:
        for element in data:
            f.write(str(element[0])+","+str(element[1])+"\n")


def interpolate_results(data):

    old_data = data
    interpolated_data = []
    
    for index in range(len(old_data)):
        back = index
        front = index+1
        if front < len(old_data):
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
        data = interpolate_results(data)
        print(time+1)
    return data


def main(args):
    try:
        input_file, output_file, numtimes = args[1:4]
        numtimes = int(numtimes)

        input_file_list = read_into_list(input_file)

        final_data = run_interpolate(numtimes, input_file_list)

        list_to_csv(final_data, output_file)
    except ValueError:
        print("Usage: ./interpolate.py <input-file> <output-file> <iterations>")

if __name__ == "__main__":
    args = sys.argv
    main(args)








