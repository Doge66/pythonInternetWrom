# -*- coding:utf-8 -*-
import re


def readFile(filename):
    f = open(filename, "r", encoding="utf8");
    ret = "".join(f.readlines())
    f.close()
    return ret


def consult(filename):
    str_ = readFile(filename)
    # print(str_)
    f = open(filename, mode="w", encoding="utf-8")
    data = re.sub("\(.*?\)", "", str_)
    data = re.sub("（.*?[a-zA-Z]+.*?）", "", data)
    print(data)
    f.write(data)
    f.flush()
    f.close()


consult("test.txt")
