import requests
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

URL = "http://search.ams.usda.gov/farmersmarkets/v1/data.svc/zipSearch?zip={}"

MARKET = "http://search.ams.usda.gov/farmersmarkets/v1/data.svc/mktDetail?id="

def market_id_function(results):
	market_details = []
	for result in results['results']:
		id = result['id']
		details = requests.get(MARKET + id).json()
		market_details.append(details['marketdetails']['GoogleLink'])
	return marketdetails

"""
for result in results['results']:
    print result


"""
@app.route('/')
@app.route('/farm', methods=['GET', 'POST'])
def main():
	if request.method == 'GET':
		return render_template('index.html')
	else:
		# the request is POST
		zip = request.form['zip_input']
		# insert user-provided zipcode in url
		submit_url = URL.format(zip)
		# run requests.get function call; retrieve response as url
		url = requests.get(submit_url)
		# work with response json
		results = url.json()
		farm_results = results['results']
		googlelinks = market_id_function(results)

		return render_template('index.html', results=farm_results, googlelinks=googlelinks)

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)