#!/usr/bin/env python
from app.CheckFile import CheckFile
from app.CountFile import CountFile
from app.SumFile import SumFile
import sys


if __name__ == "__main__":

    if(len(sys.argv) != 2):
        print "The command format: python ProcessFile.py <path_to_data_file>"
        exit()
    else:
        file_path = str(sys.argv[1])

    # Verify the file
    checkfile = CheckFile(file_path)
    # check file exit
    if not checkfile.check_file_path():
        print "The file path is not exist, please input a valid file"
        exit()

    sum_file = SumFile(file_path)
    sum_result = sum_file.sum_file()
    print "The total number sum: " + str(sum_result)

    count_file = CountFile(file_path)
    count_result = count_file.count_file()
    print "The total number count: " + str(count_result)
