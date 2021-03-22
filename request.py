import requests
import json

def search_pi_name (first_name, middle_name,last_name, limit):
	request_body = {
	     "criteria": {
	       "pi_names": [
	         {
	           
	           "first_name": first_name,
	           "middle_name": middle_name,
	           "last_name": last_name
	         }
	       ]

	     },
	     "include_fields":[
	           "principal_investigators","is_active","program_officers","org_name","org_state",
	           "org_country","agency_ic_fundings"],
	     
	     "offset": 0,
	     "limit": limit,
	     
	 }
	r = requests.post('https://api.reporter.nih.gov/v1/projects/Search', json = request_body)
	results = json.loads(r.text)['results']
	number = 0
	for result in results:
		number = number + 1
		print("-------------------------------------")
		print(number)
		pi_name = result['principal_investigators']
		pi_names = list()
		for name in pi_name:
			full_name = name['full_name']
			pi_names.append(full_name)
		print("pi names",pi_names)
		is_active = result['is_active']
		print("is active:",is_active)
		po_name = result['program_officers']
		po_names = list()
		for name in po_name:
			full_name = name['full_name']
			po_names.append(full_name)
		print("po name:",po_names)
		org_name = result['org_name']
		print("org name:",org_name)
		org_state = result['org_state']
		print("org state:",org_state)
		org_country = result['org_country']
		print("org country:", org_country)
		is_agency_funding = True if result['agency_ic_fundings'] else False
		print("is agency funding:", is_agency_funding)
def main():
	first_name = input('first name > ')
	middle_name = input('middle name > ')
	last_name = input('last name > ')
	limit = input('limit > ')
	search_pi_name(first_name, middle_name, last_name, limit)

if __name__ == "__main__":
    main()

	
	
	
	
	
	
	
