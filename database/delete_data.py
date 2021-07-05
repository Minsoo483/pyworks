from libs.db.dbconn import getconn


def delete_data():
    conn = getconn()
    cur = conn.cursor()
    sql = "delete from member where mem_num = 103"
    cur.execute(sql)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    delete_data()