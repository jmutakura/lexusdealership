# import smtplib
# from email.mime.text import MIMEText


# def send_mail(customer, dealer, rating, comments):
#     port = 25
#     smtp_server = 'smtp.mailtrap'
#     login = 'b072176eba9ccf'
#     password = '1ef75289cd3993'
#     message = f"< h3 > New Feedback Submission/h3 > <ul > <li > Customer: {customer} < /li ><li > Dealer: {dealer} < /li ><li > Rating: {rating} < /li ><li > Comments: {comments} < /li > </ul >"

#     sender_email = 'email1@examole.com'
#     receiver_email = 'email2@example.com'
#     msg = MIMEText(message, 'html')
#     msg['Subject'] = 'Lexus Feedback'
#     msg['From'] = sender_email
#     msg['To'] = receiver_email

#     # Sending email
#     with smtplib.SMTP(smtp_server, port) as server:
#         server.login(login, password)
#         server.sendmail(sender_email, receiver_email, msg.as_string())
