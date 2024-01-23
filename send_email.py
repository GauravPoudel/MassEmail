
import csv 
from invitation_edit import edit_image
import connection as conn

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
from email.message import EmailMessage

myemail = "077bch024.gaurav@pcampus.edu.np"

subject = "Invitation to Farewell Party"


with open("D:\Committees\SSOChE\Font\C_2076.csv", "r") as registration:
        conn.server_connection(myemail)
        reader = csv.reader(registration)
        for row in reader:
            roll = row[0].lower()
            fullname = row[1].lower()
            image = edit_image(fullname.title())
            Name = fullname.split()[0].capitalize()
            print(Name)
            
            
            Email = f"{roll}.{Name.lower()}@pcampus.edu.np"
            # Email = "gauravpoudel49@gmail.com"
            
            body = f"Dear {Name.capitalize()}\n I hope this message finds you in good health.\nWishing you an auspicious Makar Sakranti, It is my utmost honor and pleasure to invite you to the Chemical farewell Party, 2080.\nAs the academic year draws to a close, we are gearing up to bid farewell to our graduating seniors. As our immediate and only senior, you have consistently been more than just a senior – you have been a guiding sibling, leading us through uncharted territories.\nThis event is a sincere attempt on our part to repay, in some measure, the camaraderie and support you've generously offered. Let us make some more memories to recall, more stories to tell and some more moments to cherish as we spend the day together. \nWe cordially invite you to join us for this heartwarming occasion, filled with nostalgia, reflections, and expressions of gratitude. Your presence would undoubtedly enhance the significance of this memorable evening.\nWe look forward to sharing this special moment with you.\n\nBest Regards\nGaurav Poudel\nBCH077 "
            
            msg = MIMEMultipart()
            msg["From"] = myemail
            msg["To"] = Email
            msg["Subject"] = subject
            with open(image, 'rb') as image:
                image_data = image.read()
                image = MIMEImage(image_data)
                image.add_header('Content-ID', '')
                image.add_header('Content-Disposition', 'inline', filename='image.jpg')
            msg.attach(image)
            msg.attach(MIMEText(body, 'plain'))
            # msg = msg.as_string()
            # print(f"Sending email to: {Name}...")
            conn.send_mail(myemail, Email, msg, Name)
        
        conn.close_connection()

