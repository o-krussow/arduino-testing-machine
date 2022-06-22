import serial
import time

def begin_test(duration):

    start = time.time()
    s = serial.Serial("/dev/ttyACM0", 9600)

    with open("test_results.csv", "w+") as f: 
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


    
if __name__ == "__main__":
    begin_test(30)



