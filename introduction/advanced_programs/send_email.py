import smtplib
import ssl


def send_email(message):
    port = 465  # SSL
    smtp_server = 'smtp.gmail.com'
    sender_email = 'sender@gmail.com'
    receiver_email = 'recipient@gmail.com'
    password = 'your password'

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(sender_email, password)
            res = server.sendmail(sender_email, receiver_email, message)
            print('E-mail sent!')
        except:
            print("It was impossible to send the e-mail, check your password.")
