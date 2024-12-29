from flask import Flask, render_template, request, redirect
import csv


app = Flask(__name__)
print(__name__)


@app.route("/")
def my_home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database_file2:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        # we create a csv writer object with specific parameters to control how data is written to a CSV file.
        csv_writer = csv.writer(
            database_file2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, subject, message])


# this method is used to send data to a server, and we will transfer  data from the server back to the python application

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            # the thankyou.html is handled by the html_page function in the sense that it will render the thankyou.html page
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong. Try again!'
