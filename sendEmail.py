import smtplib

sender_email = "shaneywaris118@gmail.com"
sender_password = "yawaris@786"

receiver_email = "shaneywaris118@gmail.com"

subject = "Test Subject"
msg = "This is message body"

message = "Subject: {}\n\n{}".format(subject, msg)

server = smtplib.SMTP("smtp.gmail.com")
server.starttls()

# Please allow secure apps in this url: https://myaccount.google.com/lesssecureapps
try:
    server.login(sender_email, sender_password)
    print("Login Success")
    server.sendmail(sender_email, receiver_email, message)
    print("Email is sent succesfully to ", receiver_email)

except (smtplib.SMTPAuthenticationError):
    print("Either Username or Password is Incorrect!!")

finally:
    server.quit()