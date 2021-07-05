from libs.db.dbconn import getconn


def drop_table():
    conn = getconn()
    cur = conn.cursor()

    sql = "drop table member"
    cur.execute(sql)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    drop_table()