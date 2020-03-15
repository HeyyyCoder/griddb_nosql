import tkinter as tk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def save():
    no1 = e1.get()
    no2 = e2.get()
    no3 = e3.get()
    no4 = e4.get()

    email = 'theofficialdoctorninja@gmail.com'
    password = 'april222007'
    send_to_email = 'theofficialdoctorninja@gmail.com'
    subject = 'This is the subject'
    message = "Who is the legend you use the most? " + str(
        no1) + "\n Who is the second legend you use the most? " + str(
        no2) + "\n who is the legend you occasionaly use? " + str(
        no3) + "\n Who is the legend you dont want to use?" + str(no4)

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, send_to_email, text)
    server.quit()
    exit()


root = tk.Tk()

question_1 = "Who is the legend you use the most?"
question_2 = "Who is the second legend you use the most?"
question_3 = "who is the legend you occasionaly use?"
question_4 = "Who is the legend you dont want to use?"

tk.Label(root, text="1. " + question_1).grid(row=0)
e1 = tk.Entry(root)
e1.grid(row=0, column=1)
tk.Label(root, text="2. " + question_2).grid(row=1)
e2 = tk.Entry(root)
e2.grid(row=1, column=1)
tk.Label(root, text="3. " + question_3).grid(row=2)
e3 = tk.Entry(root)
e3.grid(row=2, column=1)
tk.Label(root, text="4. " + question_4).grid(row=3)
e4 = tk.Entry(root)
e4.grid(row=3, column=1)

tk.Button(root, text="Send", command=save).grid(row=4, column=1, sticky=tk.W, pady=4)
tk.Button(root, text="Exit", command=exit).grid(row=4, column=2, sticky=tk.W, pady=4)

tk.mainloop()
