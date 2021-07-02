from libs.db.dbconn import getconn


def insert_data():
    conn = getconn()
    cur = conn.cursor()

    cur.execute("insert into member values ('황진이', 30)")
    cur.execute("insert into member values ('성춘향', 20)")
    conn.commit()
    conn.close()


if __name__ == "__main__":
    insert_data()