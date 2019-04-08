import os
import json as js


def mk_dir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    else:
        print("Directory " + dir_name + " Exists")


def mk_file(file_name, mode):
    f = open(file_name, mode)
    return f


def write_file(file_name, data, json=True):
    if not json == True:
        f = mk_file(file_name, 'w+')
        f.write(data)
    else:
        f = mk_file(file_name, 'w+')
        js.dump(data, f)
        return


def read_json_file(file_name):
    f = mk_file(file_name, 'r')
    data = js.load(f)
    return data
