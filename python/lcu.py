

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


