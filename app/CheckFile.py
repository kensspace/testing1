#!/usr/bin/env python
import os


class CheckFile:

    def __init__(self, file_path):
        self.file_path = file_path

    def check_file_path(self):
        return os.path.isfile(self.file_path)
