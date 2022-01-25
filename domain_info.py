#Program to get domain information
import whois as w

#Check the domain is registered or not and return as bool
def resCheck(_domain_):
	try:
		reg = w.whois(_domain_)
	except Exception:
		return False
	else:
		return bool(reg.domain_name)

 
#Get info from the domain if registered
def infoGet(domain):
	if resCheck(domain) == True:
		info = w.whois(domain)
		print('The domain is registred in', info.registrar)
		print('The domain was created on', info.creation_date)
		print('This domain will expire on', info.expiration_date)
	else:
		print('The domain address does not exist')

infoGet(input('Enter a domain address\n'))	
