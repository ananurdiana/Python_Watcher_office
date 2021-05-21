#!/bin/python

import os
import os.path
from datetime import datetime

file_receive = "receive"
file_complete = "complete"
current_location = os.getcwd()
full_location = os.path.join(current_location, file_receive)
full_location_complete = os.path.join(current_location, file_complete)
extention_list = ['xlsx', 'xls', 'docx', 'doc', 'pptx', 'ppt']
watcher_lot_file = "watcher.log"
watcher_lot_dir = "log"
watcher_lot_location = os.path.join(watcher_lot_dir, watcher_lot_file)

#print(full_location)

def write_log(message):
    f = open(watcher_lot_location, "a+")
    t = datetime.now()
    f.write( t.strftime("%Y-%m-%d %H:%M:%S") + " : " + message + "\n")
    f.close()

def convert_to_pdf(location, full_location, filename):
    # convert to pdf
    cmd = "soffice --headless --convert-to pdf --outdir " + location + " \"" + full_location + "\""
    #print(cmd)
    os.system(cmd)
    # rename
    os.rename(full_location, os.path.join(location, filename))
    # write log
    write_log(cmd)

with os.scandir(full_location) as list:
    for e in list:
        if e.is_file():
            extention = os.path.splitext(e.name)[1][1:]
            #print(e.name + " " + extention)
            if extention in extention_list:
                #print(e.name + " harus di convert jadi pdf ")
                convert_to_pdf( full_location_complete, os.path.join(full_location, e.name), e.name )
            else:
                msg = e.name + " ga usah di ubah "
                #print(msg)
                # write log
                write_log(msg)

