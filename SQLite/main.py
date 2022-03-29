import sqlite3
import datetime

conn = sqlite3.connect('Z:\PycharmProjects\WIN\бд\data.db')
cur = conn.cursor()


# now=datetime.datetime.strftime(datetime.datetime.now(),'%d.%m.%y %H:%M:%S')
# cur.execute('insert into clients (`name`,`tel`,`dopPole`,`comment`,`dateAdd`) values (?,?,?,?,?)',
#             ('ИмяЯЯЯЯ', '1234554321', 'nu tipa dop', 'коммент23',now))
# conn.commit()


# now=str(datetime.datetime.now())
# now=(datetime.datetime.now())
#
# print(datetime.datetime.strftime(now,'%d.%m.%y %H:%M:%S'))



res=cur.execute('select * from clients -- where id=1')

for i in res.fetchall():
    print(i[0],i)

conn.close()
