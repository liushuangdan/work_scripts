# import psycopg2
# import random
# import datetime
# import pandas as pd
# from faker import Faker
# fake = Faker("zh_CN")
#
# ruyuanshijian_data = fake.date_time_between(start_date="-5y", end_date="now", tzinfo=None)
# id_card_data = random.choice([fake.ssn(),''])
# def patient_birth_date_data():  # 出生日期,有身份证按身份证提取，反正,随机生成。
#     if id_card_data == '':
#         return fake.date_between(start_date='-30y', end_date='today')
#     else:
#         return datetime.datetime.strptime(str(id_card_data[6:14]), '%Y%m%d')
# a = int(str(ruyuanshijian_data)[0:4]) - int(str(patient_birth_date_data())[0:4])
# print("入院时间：" + str(ruyuanshijian_data))
# print("身份证号" +  str(id_card_data))
# print("出生日期" + str(patient_birth_date_data()))
# print(fake.ean8())

import psycopg2
import pandas as pd
from faker import Faker
fake = Faker("zh_CN")
import random
import datetime
# 连接数据库
# conn = psycopg2.connect(database="rdr_new",user="postgres",
#                         password="12345678",
#                         host="postgres.bddev-malijun.svc.k8s.bjo.natureself.site",
#                         port="5432")
# cur = conn.cursor()
schema = 'ods'

# 查询全部表
# tab_all_sql = "SELECT table_name  FROM INFORMATION_SCHEMA.TABLES where table_schema = '" + schema + "';"
# table_name = pd.read_sql_query(tab_all_sql,conn)
# tab_name_list = table_name['table_name'].tolist()
# 清空当前全部数据
# for i in tab_name_list:
#     del_all_sql = "delete from " + schema + "." + i + ";"
#     cur.execute(del_all_sql)
#     conn.commit()


def insert_sql():
    for i in range(5):
        card_type_data = random.choice(['01', '02', '03', '04', '05', '06', '07', '99'])
        if card_type_data == '01':
            id_card = fake.ssn()
            in_patient_sql = "insert into " + schema + \
                             ".ods_mt_patient_info(card_type,id_card)values('{card_type_data}','{id_card}')".format(
                                 card_type_data=card_type_data,
                                 id_card=id_card
                             )
        else:
            # id_card = None
            in_patient_sql = "insert into " + schema + \
                             ".ods_mt_patient_info(card_type)values('{card_type_data}')".format(
                                 card_type_data=card_type_data
                             )
        # 插入患者信息
        print(in_patient_sql)
        # cur.execute(in_patient_sql)
        # conn.commit()


if __name__ == '__main__':
    insert_sql()