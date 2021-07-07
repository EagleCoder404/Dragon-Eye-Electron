import csv
import os
import cv2
from pathlib import Path
class Logger:

    def __init__(self, path_to_file):
        
        log_dir = Path("facial/logs")
        if not log_dir.exists():
            os.mkdir(log_dir)
        had_existed = os.path.exists(path_to_file)

        self.file_write = open(path_to_file, 'a')
        self.file_read = open(path_to_file, 'r')

        self.writer = csv.writer(self.file_write)
        self.reader = csv.reader(self.file_read)
        self.frame_id = 0

        if not had_existed:
            self.writer.writerow(["frame_id","face_detection","multiple_face", "face_recognition", "face_alignment", "eye_position"])
        else:
            next(self.reader)
            for row in self.reader:
                self.frame_id = int(row[0])

    def log(self, log_data):
        self.frame_id += 1
        row = [self.frame_id] + log_data
        self.writer.writerow(row)
        return self.frame_id 


