import ast

def findPhoneNumber(request):
	cookie_dict=ast.literal_eval(request.COOKIES['goalstar'])
	phone_number=cookie_dict['accountkit_data'][1]
	return phone_number

def findDevice(request):
	device=''
	if request.user_agent.is_mobile:
		device='mobile'

	elif request.user_agent.is_tablet :
		device='tablet'

	elif request.user_agent.is_pc:
		device='pc'
		
	else:
		device='unknown'

	return device