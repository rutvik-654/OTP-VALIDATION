# OTP Email Sender

This Python script sends a One-Time Password (OTP) via email for verification purposes. Users receive an OTP and must enter it to complete validation.

## Features
- Sends OTPs to multiple email addresses.
- Uses Gmail SMTP for email delivery.
- Validates user-entered OTPs against sent ones.

## Prerequisites
- Python 3.x installed.
- A Gmail account with **App Passwords** enabled.

## Setup Instructions

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/yourusername/otp-email-sender.git
   cd otp-email-sender
   ```

2. **Install Required Libraries:**
   ```sh
   pip install smtplib email.mime
   ```

3. **Set Up Your Email Credentials Securely:**
   - Enable **2-Step Verification** on your Gmail account.
   - Generate an [App Password](https://myaccount.google.com/apppasswords) for the script.
   - Store credentials in environment variables:
     ```sh
     export EMAIL_ADDRESS='your-email@gmail.com'
     export EMAIL_PASSWORD='your-app-password'
     ```

4. **Run the Script:**
   ```sh
   python otp_sender.py
   ```

## Security Warning
⚠️ **Never hardcode your email and password in the script!** Always use environment variables for security.

## License
This project is open-source and available under the MIT License.

# OTP-VALIDATION
