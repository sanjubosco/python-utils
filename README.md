# python-utils
Utility tools using python

filespliter
-----------
Splits a large text file into smaller files. Update the below variables based on needs.
INPUT_FILE - Give the full path to the file that has to be split.
eg: INPUT_FILE = r'C:\Users\yyy\inputfile.txt' ## put path to the file to be split

OUT_FILE_FORMAT -Provide the file output name format. if output files needs to be in thr format output_1, output_2, then put the format as output_
eg: OUT_FILE_FORMAT = r'C:\Users\yyy\output_' ## put output file format

BATCH_SIZE - Size of the split file in bytes. The input files will be split into smaller files of this size.
eg: BATCH_SIZE = 50000000 ## 50MB
