import pymysql
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
import json
import base64

# データベースからメールアドレスを取得
def get_email_addresses():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='yu07fgS14Pla',
        database='mydb'
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT email FROM users")
            result = cursor.fetchall()
            return [email[0] for email in result]
    finally:
        connection.close()


# メールを送信
def send_email(to_address, password, subject, html_content, img):
    from_address = 'shun74855@gmail.com'

    msg = MIMEMultipart('alternative')  

    # メール設定
    msg['Subject'] = subject
    msg['From'] = from_address
    msg['To'] = to_address

    html_part = MIMEText(html_content, 'html')
    msg.attach(html_part)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(from_address, password)
        server.sendmail(from_address, msg['To'], msg.as_string())

# メイン処理
def main():
    # 記事の読み込み(JSONファイル)
    with open('article/history_ja.json', 'r', encoding='utf-8') as file:
        article_data = json.load(file)

    # JSONデータをHTMLフォーマットに変換
    subject = article_data[1]['title']
    html_content = '<html><body>'

    html_content += f'<h1>{subject}</h1>'

    # 外部リンクを利用し画像を添付
    # img = ''
    # html_content += f'<img src="https://gift-life.com/{img}.jpg" width="500" alt="{img}">'

    for article in article_data[1]['sections']:
        html_content += f"<h2>{article['heading']}</h2>"
        html_content += f"<p>{article['content']}</p>"

    html_content += '</body></html>'
    
    
    # # タイトルを抽出
    # subject = ''
    # for article in articles:
    #     title = article['title']
    #     subject = title

   
    # # 本文を抽出
    # body = ''
    # for section in article['sections']:
    #     heading = section['heading']
    #     content = section['content']
    #     body += heading + content

    # 添付画像
    img = 'kohfukuji-temple.jpg'

    gmail_password = "rmiu xnqu ppsn htgk"
    email_addresses = get_email_addresses()
    for email in email_addresses:
        send_email(email, gmail_password, subject, html_content, img)

# スクリプトとして実行された場合のみmain()を呼び出す
if __name__ == "__main__":
    main()
