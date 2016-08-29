# coding: utf-8

import exifread
import os

img_dir = 'E:\\Temp\\Camera\\'
# date_tag = 'Image DateTime'
original_date_tag = 'EXIF DateTimeOriginal'


def get_imgdate(filepath):
    f = open(filepath, 'rb')
    tags = exifread.process_file(f)

    if original_date_tag in tags:
        return tags[original_date_tag]

def read_all_images():
    img_datetime_list = []
    for x in os.listdir(img_dir):
        img_datetime = get_imgdate(img_dir + x)
        if img_datetime:
            img_datetime_list.append(img_datetime)

    return img_datetime_list

if __name__ == '__main__':
    for x in read_all_images():
        print x
