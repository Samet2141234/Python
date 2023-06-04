from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        to = request.form['to']
        subject = request.form['subject']
        message = request.form['message']

        # Set up the SMTP connection
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        sender_email = 'ngozihenrychukwueweniwew@gmail.com'
        password = 'rmeclcqpkhuozlnf'

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, password)

            # Compose the email
            email_message = f"Subject: {subject}\n\n{message}"

            # Send the email
            server.sendmail(sender_email, to, email_message)

            # Close the connection
            server.quit()

            result = 'Email sent successfully'
        except smtplib.SMTPException as e:
            result = f'Error sending email: {str(e)}'

        return render_template('index.html', result=result)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()