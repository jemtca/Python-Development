
## About
A script that sends an email.
\
&nbsp;

## How to run this script (macOS/Linux)
* Clone the project: **`git clone https://github.com/jemtca/Python-Development.git`**
* Go to the project folder: **`cd Python-Development/Scripting/email_sender/`**
\
&nbsp;
* Create an environment: **`python3 -m venv ./`**
* Activate environment (fish shell): **`. bin/activate.fish`**
    * If different shell: check this [website](https://docs.python.org/3/library/venv.html).
\
&nbsp;
* Install dependencies: **`pip3 install -r requirements.txt`**
\
&nbsp;
* Before running the script, fill in every line of code that has a comment on it:
    * email (from)
    * email (to)
    * email subject
    * email content
    * SMTP function has two parameters: host (Gmail, Outlook, etc...) and port (587)
    * login function has two parameters: email address from where the email will be sent and email address password
\
&nbsp;
* Open the Terminal/Console and execute the script:
    * **`python3 email_sender_static.py`**
    * **`python3 email_sender_dynamic.py`**
\
&nbsp;
* Deactivate environment: **`deactivate`**
\
&nbsp;

> **Modules used:** smtplib, email.message, string, pathlib.
