
## About
Portfolio website example with the back-end implemented with Flask.
\
\
Univers template from [Mashup Template](http://www.mashup-template.com/templates.html) where the contact section was modified to send information (email, subject, and message) to the server and store it in a CSV file.
\
\
Web App deployed to [pythonanywhere](https://www.pythonanywhere.com/): Take a look [here](https://sanede.pythonanywhere.com/).
\
&nbsp;

## How to run this project (macOS/Linux)
* Clone the project: **`git clone https://github.com/jemtca/Python-Development.git`**
* Go to the project folder: **`cd Python-Development/Web\ Development/`**
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
* Export the FLASK_APP environment variable: **`export FLASK_APP=server.py`**
* Debug Mode ON: **`export FLASK_ENV=development`**
* Run the application: **`flask run`**
* Open a browser tab and copy the address (http://127.0.0.1:5000/) where the flask app is running on.
\
&nbsp;
* Exit (in the terminal): **`control + c`**
\
&nbsp;
* Deactivate environment: **`deactivate`**
\
&nbsp;
* templates folder: for HTML files.
* static folder: for CSS files, js files, favicon file, and images.
\
&nbsp;

> **Modules used:** cvs, datetime.
\
> **Packages used:** Flask.
