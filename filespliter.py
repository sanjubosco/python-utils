
import os

def splitfile(INPUT_FILE, OUT_FILE_FORMAT, BATCH_SIZE):
    FILE_SIZE = os.stat(INPUT_FILE).st_size
    with open(INPUT_FILE) as fl:
        for i in range(0,round(FILE_SIZE/BATCH_SIZE)+1):
            out = open(OUT_FILE_FORMAT+str(i), "w+")
            lines = fl.readlines(BATCH_SIZE)
            print ("Writing batch %d - Output file is %s" %(i,OUT_FILE_FORMAT+str(i)))
            for line in range(0,len(lines)):
                out.write(lines[line] + "\n")
            out.close()


def main():    
    INPUT_FILE = r'C:\Users\yyy\inputfile.txt' ## put path to the file to be split
    ## put output file format
    ## eg ...if output files needs to be in thr format output_1, output_2, then put the fomrat as output_
    OUT_FILE_FORMAT = r'C:\Users\yyy\output_' ## put output file format
    BATCH_SIZE = 50000000 ## 50MB. chaneg as required
    splitfile(INPUT_FILE, OUT_FILE_FORMAT, BATCH_SIZE)

if __name__ == "__main__":
    main()