from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

def write_to_file(data):
    with open('database.txt', "a") as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f"\n{email}, {subject}, {message}")

def write_to_csv(data):
    with open('database.csv', "a", newline='') as database2:
        # email = data['email']
        # subject = data['subject']
        # message = data['message']
        # csv_write = csv.writer(database2, delimiter=',', quotechar='|', newline='', quoting=csv.QUOTE_MINIMAL)
        # csv_write.writerow([email, subject, message]) 
        csv_write = csv.DictWriter(database2, fieldnames=data.keys())
        csv_write.writerow(data)

@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return render_template('submit_form.html')
    else:
        return 'something went wrong'
