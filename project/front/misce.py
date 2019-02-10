import requests

def send_contact_message(request):
	'''
	function to send the message
	'''
	data = ['name', 'position', 'company', 'location', 'email', 'telephone', 'service', 'message']
	msg = ''
	email = ''
	for row in data:
		value = request.POST.get(row, '')
		msg += row + ": " + value + '<br />'
		if row == 'email':
			email = value

	payload = {
		'from': email,
		'subject': 'Mensaje desde forma de contacto',
		'message': msg
	}

	response = requests.post("http://node-api-mint:3030/email?account=focusmx", data=payload)
	return response

