from urllib.request import urlopen

url  = "http://www.seventeen.com/fashion/trends/g12063225/victorias-secret-fashion-show-model-lineup-2017/"

def get_webpage(url):

	print("Getting Request Object")
	request = urlopen(url)
	print("Reading Request Object")
	data = request.read()
	text = data.decode("utf-8")

	print("Web Page Downloaded")
	return text

text = get_webpage(url)

with open('html_text.txt', 'w') as f:
	f.write(text)

