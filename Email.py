import smtplib


class Email:

    def __init__(self):
        self.body = ""

    def send_email(self, login, password, subject, to_addr):
        with smtplib.SMTP("smtp-mail.outlook.com", port=587) as connection:
            connection.starttls()
            connection.login(user=login, password=password)
            connection.sendmail(from_addr=login, to_addrs=to_addr,
                                msg=f"Subject:{subject}\n\n{self.body}\n")

    def add_to_body(self, message=""):
        self.body += message + "\n"
        print(self.body)
