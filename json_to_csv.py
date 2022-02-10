
import csv
import json
import os
columns = ['wx_nickname', 'wx_name', 'nickname_id', 'posttime', 'wx_title', 'url', 'add_time', 'readnum', 'likenum', 'old_like_num', 'top']


def eachFiles(filepath):
    child_file = []
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s\%s' % (filepath, allDir))
        if os.path.isfile(child):
            if child.endswith(".log"):
                child_file.append(child)
    return child_file


def readFile(file):
    data = open(file, encoding="utf_8_sig")
    res = []
    for i in data:
        if i.endswith("\n"):
            i = i.replace("\n", "").replace("\r", "")
        d = json.loads(i)
        temp_dict = {}
        for item in columns:
            temp_dict[item] = d.get(item, None)
        # print(d.keys())
        res.append(temp_dict)
    return res


def generateCsv(file):
    file_new_name = file.split(".log")[0] + ".csv"
    print(file_new_name)
    csv_file = open(file_new_name, 'w', encoding="utf_8_sig", newline="")
    json_list = readFile(file)
    json_values = []
    for one in json_list:
        json_values.append(one.values())
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(columns)
    csv_writer.writerows(json_values)
    csv_file.close()


if __name__ == '__main__':
    all_file = eachFiles(r"D:\桌面\微信top200")
    for item in all_file:
        generateCsv(item)