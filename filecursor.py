import hashlib
import datetime, time
import os
import pymssql

# init
m = hashlib.md5()
i = 0
st = time.time()


def sqlData(sql, dict=False):
    '''returns data from any sql query'''
    conn = pymssql.connect(host='server\sql2008', user='python',
                           password='sql', database='northwind',
                           as_dict='True')
    # conn = psycopg2.connect('dbname=postgres user=postgres')  #Postgre
    cur = conn.cursor()
    cur.execute('%s' % sql)
    return None # cur.fetchall()

def matchHash(Hash):
    query = 'select Hash from Obj_Hash where Hash = %h' % Hash
    results = sqlData(query)
    print results


for root, dirs, files in os.walk('C:\\Users\\Sean\\Desktop'):
    for name in files:
        i = i + 1

        hashname = hashlib.md5(os.path.join(root, name))
        raw = hashname.hexdigest()
        pts = os.path.join(root, name)
        # print hashname.hexdigest()
        # print os.path.join(root, name)
        query = 'insert into Obj_Hash (hash, path) values (cast({!r} as binary),{!r})'.format(raw, pts)
        sqlData(query)
        # print query


# deinit
et = time.time()
tt = et - st


print i
print str(datetime.timedelta(seconds=tt))
