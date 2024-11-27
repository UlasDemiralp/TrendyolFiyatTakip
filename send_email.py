import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMail(toMail, subject, content):
    fromMail = "yasinaqbas1905@gmail.com"
    app_password = "kushpurxhtpioeou"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()


        server.login(fromMail, app_password)


        message = MIMEMultipart("alternative")
        message["From"] = fromMail
        message["To"] = toMail
        message["Subject"] = subject


        htmlContent = MIMEText(content, "html")
        message.attach(htmlContent)

        server.sendmail(fromMail, toMail, message.as_string())
        print("E-posta başarıyla gönderildi!")
    except Exception as e:
        print(f"E-posta gönderimi sırasında hata oluştu: {e}")
    finally:
     server.quit()