#!/usr/bin/env python3
import sys 

def deviation_from_average(average, value):
    return 1 - (value / average)

def deviation_from_previous(previous, value):
    return 1 - (value / previous)


def smooth_results(old_file, new_file):
    temp_sum = 0
    temp_count = 0
    float_prev_temp = 0
    prev_temp = ""
    deviation_detected = False

                        #deviation, sec
    highest_av_deviation = [0, ""]
    highest_prev_deviation = [0, ""]

    with open(old_file, "r") as of:
        of_contents = of.read()

    with open(new_file, "w+") as nf:
        for of_line in of_contents.split("\n"):
            try:
                sec, temp = of_line.split(",")
                float_temp = float(temp)
                temp_sum += float_temp
                temp_count += 1

                if temp_count == 1:
                    float_prev_temp = float_temp

                av_deviation = deviation_from_average((temp_sum/temp_count), float_temp)
                prev_deviation = deviation_from_previous(float_prev_temp, float_temp)

                if av_deviation > highest_av_deviation[0]:
                    highest_av_deviation[0] = av_deviation
                    highest_av_deviation[1] = sec
                if prev_deviation > highest_prev_deviation[0]:
                    highest_prev_deviation[0] = prev_deviation
                    highest_prev_deviation[1] = sec


                if -0.12 <= prev_deviation <= 0.12:
                    if not deviation_detected:
                        nf.write(sec+","+temp+"\n")
                        #print(sec+","+temp)
                    #else:
                    #    nf.write(sec+","+temp+"\n")
                    #    print(sec+","+temp)

                else:                                   #If current temperature exceeds deviation quota, then just write the previous temperature to smooth things out
                    if deviation_detected:
                        deviation_detected = False
                    else:
                        deviation_detected = True
                    #print("DEVIATION AT",sec)

                prev_temp = str(float_temp)
                float_prev_temp = float_temp
                
            except ValueError:
                continue
    
    print(highest_av_deviation)
    print(highest_prev_deviation)

def main(args):
    try:
        input_file, output_file = args[1:3]
        smooth_results(input_file, output_file)
    except ValueError:
        print("Usage: ./smooth.py <input-file> <output-file>")

if __name__ == "__main__":
    args = sys.argv
    main(args)








