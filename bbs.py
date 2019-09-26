import csv
import os

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    u_list = []
    with open("bbs.csv", mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row['user']
            message = row['message']
            u_list.append(f'{name}: {message}')

    if request.method == 'GET':
        return render_template('index.html', u_list=u_list)

    if request.method == 'POST':
        username = request.form['username']
        message = request.form['message']
        if username == '':
            username = '名無しさん'
        with open("bbs.csv", mode='a') as f:
            writer = csv.writer(f)
            writer.writerow([username, message])
        u_list.append(f'{username}: {message}')

        return render_template('index.html', u_list=u_list)


def main():
    if os.path.isfile('bbs.csv') == False:
        with open("bbs.csv", mode='w') as f:
            writer = csv.writer(f)
            writer.writerow(['user', 'message'])


if __name__ == '__main__':
    main()
    app.run(debug=True, port=3333)
