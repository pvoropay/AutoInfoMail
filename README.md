# AutoInfoEmail

AutoInfoEmail is a simple Python program designed to automatically send computer parameters and IP address to a specified email address upon computer startup.

## Features

- Automatically gathers system information upon startup.
- Sends an email containing system parameters and IP address.
- Customizable email recipient and message content.
- Compatible with Windows operating systems.

## Requirements

- Python 3.x
- Additional Python libraries:
  - `psutil`: Used for retrieving system information.
  - `win32com`: Used for interacting with Windows services.
  - `smtplib`: Used for sending emails.
  - `socket`: Used for retrieving the IP address.

## Installation

1.Initialize Git in your folder
   ```bash
   git init
   ```
3. Clone or download the repository to your local machine.
   ```bash
   git clone <url>
   ```
4. Install the required Python libraries:

    ```bash
    pip install psutil win32com
    ```

5. Configure the script:
   - Open `mail.py` and specify the email settings such as sender email, recipient email, SMTP server, and port.
   **Note**: When setting up the script to run on startup, keep in mind that you may need to input your email login credentials. Ensure that you're comfortable with this setup and consider using a less important email account for this purpose due to security considerations.  
6. Optionally, customize the email message in `mail.py`.

7. Set up the script to run on computer startup:
   
   -Open add_to_startup.py script  
   -Choose the path to your mail.py script   
   -Run add_to_startup.py script 

## Usage

Simply run the script to ensure that it will automatically gather system information and send an email upon computer startup.

```bash
python mail.py
```

License: This project is licensed under the MIT License.

