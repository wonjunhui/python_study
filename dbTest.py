import pymysql.cursors
 
conn = pymysql.connect(host='junhee.czmeph7testl.ap-northeast-2.rds.amazonaws.com',
        user='root',
        password='wnsgml159',
        db='crawlingtest',
        charset='utf8mb4')
 
try:
    with conn.cursor() as cursor:
        # sql = 'SELECT * FROM crawling'
        sql = 'INSERT INTO crawling (date,close,diff,open,low,volume) VALUES (%s,%s,%s,%s,%s,%s)'
        cursor.execute(sql, ('2010-03-01','23234','234234','5346','645645','6334'))
        # result = cursor.fetchone()
        conn.commit()
        # print(result)
        # (1, 'test@test.com', 'my-passwd')
finally:
    conn.close()

