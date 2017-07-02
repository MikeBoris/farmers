import requests
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

URL = "http://search.ams.usda.gov/farmersmarkets/v1/data.svc/zipSearch?zip={}"

"""
for result in results['results']:
    print result

market = "http://search.ams.usda.gov/farmersmarkets/v1/data.svc/mktDetail?id="

for result in results['results']:
    id = result['id']
    details = requests.get(market + id).json()
    print details['marketdetails']['GoogleLink']
"""
@app.route('/')
@app.route('/farm', methods=['GET', 'POST'])
def main():
	if request.method == 'GET':
		return render_template('index.html')
	else:
		# the request is POST
		zip = request.form['zip_input']
		# apply user-provided zipcode in url
		submit_url = URL.format(zip)
		url = requests.get(submit_url)
		results = url.json()
		farm_results = results['results']
		return render_template('index.html', results=farm_results)

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)