from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'data not stored'
    else:
        return 'somthing wrong'


def write_to_csv(data):

    with open('data_base.csv', newline='', mode='a') as datbase:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(datbase, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
