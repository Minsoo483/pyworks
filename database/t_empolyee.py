from libs.db.dbconn import getconn


def select_emp():
    conn = getconn()
    cur = conn.cursor()

    sql = "select * from employee"
    cur.execute(sql)
    rs = cur.fetchall()
    for i in rs:
        print(i)

    conn.close()


def select_one():
    conn = getconn()
    cur = conn.cursor()

    sql = "select * from employee where emp_id = ?"
    cur.execute(sql, ('e103',))  # 튜플 삽입 - 1개만 입력시 ('',) 마지막에 콤마 필수!!!!!!
    rs = cur.fetchone() # fetchone - 1개만 가져오기 // fetchall은 모두 가져오기
    print(rs)

    conn.close()


def insert_emp():
    conn = getconn()
    cur = conn.cursor()

    sql = "insert into employee(emp_id, name, age, salary) values(?, ?, ?, ?)"
    cur.execute(sql, ('e104', '김산', 22, 5000))

    conn.commit()
    conn.close()


def update_emp():
    conn = getconn()
    cur = conn.cursor()

    sql = "update employee set salary = ? where emp_id =?"
    cur.execute(sql, (25000, 'e102'))

    conn.commit()
    conn.close()


def delete_emp():
    conn = getconn()
    cur = conn.cursor()

    sql = "delete from employee where emp_id =?"
    cur.execute(sql, ('e102',))

    conn.commit()
    conn.close()


if __name__ == "__main__":
    # select_one()
    # insert_emp()
    # update_emp()
    delete_emp()
    select_emp()