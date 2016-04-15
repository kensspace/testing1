#!/usr/bin/env python


class SumFile:

    def __init__(self, filename):
        self.filename = filename

    def sum_file(self):
        with open(self.filename, 'rb') as f:
            result = sum([sum([float(x) for x in line.split()]) for line in f])
            f.close()
        return result
