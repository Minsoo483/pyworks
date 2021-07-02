from libs.db.dbconn import getconn


def select_one():
    conn = getconn()
    cur = conn.cursor()
    # 1명 검색 sql

    sql = "select * from member where name='성춘향'"
    cur.execute(sql)
    print("성춘향 검색")
    '''rs = cur.fetchmany()
    print(rs)'''
    rs = cur.fetchone()
    print(rs)

    conn.close()


if __name__ == "__main__":
    select_one()