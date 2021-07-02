from libs.db.dbconn import getconn


def select_data():
    conn = getconn()
    cur = conn.cursor()
    # 자료 조회
    sql = "select * from member"
    cur.execute(sql)

    print("데이터 전체 조회")
    rs = cur.fetchall() # 꺼내온 자료 객체
    for i in rs:
        print(i)
    # commit 은 불필요 ( select 문이기 때문에)
    conn.close()


if __name__ == "__main__":
    select_data()