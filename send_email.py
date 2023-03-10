import smtplib, ssl


def mail(message):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "pritamdas5370@gmail.com"  # Enter your address
    receiver_email = "dasp5370@gmail.com"  # Enter receiver address
    password = "vfwpogpvooegtfvi"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


