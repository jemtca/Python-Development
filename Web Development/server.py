import csv
from datetime import datetime
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home_section():
	return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

# def write_to_file(data):
# 	with open('database.txt', mode='a') as database:
# 		date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# 		email = data['email']
# 		subject = data['subject']
# 		message = data['message']
# 		file = database.write(f'\nDate: {date}\nEmail: {email}\nSubject: {subject}\nMessage: {message}\n\n')

def write_to_csv(data):
	with open('database.csv', mode='a', newline='') as database:
		date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(database, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([date, email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()

			if len(data['email']) > 0 and len(data['subject']) > 0 and len(data['message']) > 0:
				# write_to_file(data)
				write_to_csv(data)
				return redirect('/thanks.html')
			else:
				return redirect('/missed.html')
		except:
			return redirect('/data.html')
	else:
		return redirect('/wrong.html')
