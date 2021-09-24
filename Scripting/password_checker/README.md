
## About
A script that checks if a password has been compromised.
\
&nbsp;

## How to run this script (macOS/Linux)
* Clone the project: **`git clone https://github.com/jemtca/Python-Development.git`**
* Go to the project folder: **`cd Python-Development/Scripting/password_checker/`**
\
&nbsp;
* Create an environment: **`python3 -m venv ./`**
* Activate environment (fish shell): **`. bin/activate.fish`**
    - If different shell: check this [website](https://docs.python.org/3/library/venv.html).
\
&nbsp;
* Install dependencies: **`pip3 install -r requirements.txt`**
\
&nbsp;
* The script allows checking as many passwords as wished.
* If a password contains any special character ($, &, *, etc...), it is recommended to wrap it with single/double-quotes.
\
&nbsp;
* Open the Terminal/Console and execute the script: **`python3 password_checker.py hello helloworld 123456`**
\
&nbsp;
* Deactivate environment: **`deactivate`**
\
&nbsp;

> **Modules used:** hashlib, sys.
\
> **Packages used:** requests.

&nbsp;
## Important note
Using the k-anonymity model which means, any typed password, is hashed and only the first five chars are sent to the API.
