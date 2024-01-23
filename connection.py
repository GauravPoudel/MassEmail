import smtplib


smtp_port = 587                 
smtp_server = "smtp.gmail.com"
password = "wlsu alqc mhfo abwi"
def server_connection(email):
    print("Connecting to server...")
    global TIE_server
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls()
    TIE_server.login(email, password)
    print("Succesfully connected to server")
    print()

def send_mail(myemail, email, msg, Name):
    print(f"Sending email to: {Name}...")
    TIE_server.sendmail(myemail, email, msg.as_string())
    print(f"Email sent to: {Name}")
    print()

def close_connection():
    TIE_server.quit()