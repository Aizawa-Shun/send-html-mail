import pymysql
from email.mime.text import MIMEText



def create_connection():
    """データベースへの接続を作成し、接続オブジェクトを返す"""
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='your_database_password',
        database='your_database_name'
    )
    return connection


def create_users_table(cursor):
    """指定されたカーソルを使用してユーザーテーブルを作成する"""
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        password VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL UNIQUE
    )
    """)


def insert_user_data(cursor, password, email):
    """指定されたカーソルを使用してユーザーデータを挿入する"""
    sql = "INSERT INTO users (password, email) VALUES (%s, %s)"
    cursor.execute(sql, (password, email))


def delete_user_data(cursor, user_id):
    """指定されたIDのユーザーデータを削除する"""
    sql = "DELETE FROM users WHERE id = %s;"
    cursor.execute(sql, (user_id,))


def fetch_table_data(cursor, table_name):
    """指定されたテーブル内のデータを取得し表示する"""
    cursor.execute(f"SELECT * FROM {table_name};")
    rows = cursor.fetchall()
    print(f"Data in table '{table_name}':")
    for row in rows:
        print(row)


def describe_table(cursor, table_name):
    """指定されたテーブルの構造を確認する"""
    cursor.execute(f"DESCRIBE {table_name};")
    columns = cursor.fetchall()
    print(f"Structure of table '{table_name}':")
    for column in columns:
        print(column)


def main():
    """メインの実行関数"""
    connection = create_connection()  # データベースに接続

    try:
        with connection.cursor() as cursor:  # connectionオブジェクトからカーソルを取得。withステートメントがカーソルの管理を自動化
            # create_users_table(cursor)  # カーソルを引数にしてcreate_users_table関数を呼び出し、テーブルを作成

            # insert_user_data(cursor, 'password', 'shun49421@gmail.com')  # ユーザーデータをテーブルに挿入

            user_id_to_delete = 2  # ここに削除したいユーザのIDを指定
            delete_user_data(cursor, user_id_to_delete)  # 指定IDのユーザーデータを削除
            connection.commit()         # データベースに対する変更を確定

            describe_table(cursor, 'users')  # 'users'テーブルの構造を確認
            fetch_table_data(cursor, 'users')  # 'users'テーブル内のデータを取得し表示
        
    finally:
        connection.close()   # データベースとの接続を閉じる

# スクリプトとして実行された場合のみmain()を呼び出す
if __name__ == "__main__":
    main()

