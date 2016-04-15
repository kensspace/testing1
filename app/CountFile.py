#!/usr/bin/env python


class CountFile:

    def __init__(self, filename):
        self.filename = filename

    def count_file(self):
        count = 0
        with open(self.filename, 'rb') as f:
            for line in f:
                for number in line.split():
                    count += 1
            f.close()
        return count
