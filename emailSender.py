import smtplib
import ssl
import os
# Setup port number and servr name

smtp_port = 587                 # Standard secure SMTP port
smtp_server = "smtp.gmail.com"  # Google SMTP Server

email_from = ''
email_to = ''
pswd = ""

# content of message

message = "Dear god, please help!!!"

# Create context
simple_email_context = ssl.create_default_context()


try:
    # Connect to the server
    print("Connecting to server...")
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls(context=simple_email_context)
    TIE_server.login(email_from, pswd)
    print("Connected to server :-)")
    
    # Send the actual email
    print()
    print(f"Sending email to - {email_to}")
    TIE_server.sendmail(email_from, email_to, message)
    print(f"Email successfully sent to - {email_to}")

# If there's an error, print it out
except Exception as e:
    print(f'Error!!!!!!!: {e}' )

# Close the port
finally:
    TIE_server.quit()

##############################################################################################################

import os
import datetime
from email.message import EmailMessage
import ssl
import smtplib

date = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

email_sender = ''
email_receiver = ''
email_password = os.environ.get("EMAIL_PASSWORD")

subject = f"OpenAI Motivational quotes {date}"
body = "Check this new motivational quote"

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

except Exception as e:
        print(f"Puta mare oe!: {str(e)}")














