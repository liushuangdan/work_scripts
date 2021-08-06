
import csv
import json
# fh = open(r"C:\Users\liushuangdan\Desktop\sfr_2021-08-06.csv", "w+")
# writer = csv.writer(fh)
# writer.writerow(["城市代码","城市名称"])
data = open(r"C:\Users\liushuangdan\Desktop\sfr_2021-08-06.txt", encoding="utf_8_sig")
res = []
columns = ['reposts_count', 'posttime', 'site_name', 'vid', 'fetch_time', 'title', 'url', 'author', 'play_count', 'comments_count', 'author_url', 'author_followers_count', 'favourites_count', 'author_id', 'subdomain', 'author_statuses_coun', 'author_favourites_count', 'author_img', 'album_id', 'author_name', 'album', 'reposts_coun', 'platform', 'album_url', 'albums_count', 'play_time', 'author_info', 'album_subscribe_count', 'author_favorite_count', 'album_play_count', 'album_item_num', 'author_statuses_count', 'coin_count', 'collection_count']
for i in data:

    if i.endswith("\n"):
        i = i.replace("\n", "").replace("\r", "")
    d = json.loads(i)
    temp_dict = {}
    for item in columns:
        temp_dict[item] = d.get(item, None)
    # print(d.keys())
    res.append(temp_dict)
# print(res)
csv_file = open(r"C:\Users\liushuangdan\Desktop\sfr_2021-08-06-new.csv", 'w', encoding="utf_8_sig", newline="")
json_list = res
json_values = []
for one in json_list:
    # print(one.keys())
    # print('**'*30)
    # print(len(one.values()), one.values())
    json_values.append(one.values())
csv_writer = csv.writer(csv_file)
csv_writer.writerow(columns)
csv_writer.writerows(json_values)
csv_file.close()