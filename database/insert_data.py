from libs.db.dbconn import getconn


def insert_data():
    conn = getconn()
    cur = conn.cursor()

    cur.execute("insert into member values (103, '황진이', 25)")
    cur.execute("insert into member values (104, '성춘향', 22)")
    conn.commit()
    conn.close()


if __name__ == "__main__":
    insert_data()