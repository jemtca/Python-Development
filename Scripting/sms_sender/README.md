
## About
A script that sends SMS texts to mobile phones.
\
&nbsp;

## How to run this script (macOS/Linux)
- Clone the project: **`git clone https://github.com/jemtca/Python-Development.git`**
- Go to the project folder: **`cd Python-Development/Scripting/sms_sender/`**
\
&nbsp;
- Create an environment: **`python3 -m venv ./`**
- Activate environment (fish shell): **`. bin/activate.fish`**
    - If different shell: check this [website](https://docs.python.org/3/library/venv.html).
\
&nbsp;
- Install dependencies: **`pip3 install -r requirements.txt`**
\
&nbsp;
- [Log In](https://www.twilio.com/) to use Twilio API.
- Create a new project: New Project / Products / Programmable SMS
- Get a Twilio phone number.
- Verify a number (your phone number): Phone Numbers / Verified Caller IDs / Verify a number
- Copy your personal ACCOUNT SID and paste it in the script file: account_sid = 'paste_it_in_here'
- Copy your personal AUTH TOKEN and paste it in the script file: auth_token = 'paste_it_in_here'
- Type the message that you would like to send (line 17).
\
&nbsp;
- Open the Terminal/Console and execute the script: **`python3 sms_sender.py`**
\
&nbsp;
- Deactivate environment: **`deactivate`**
\
&nbsp;

> **Packages used:** twilio.
