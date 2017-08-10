import requests
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def main():
	return render_template('home.html')

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)