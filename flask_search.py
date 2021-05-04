import json
import requests
from flask import Flask, request, redirect, url_for, render_template        
app = Flask(__name__)


def search_pi_name (pi_first_name, pi_middle_name, pi_last_name):
	request_body = {
	     "criteria": {
	       "pi_names": [
	         {	 
	           "first_name": pi_first_name,
	           "middle_name": pi_middle_name,
	           "last_name": pi_last_name
	         }
	       ]
	     },
	     "include_fields":[
	           "principal_investigators","is_active","program_officers","org_name","org_state",
	           "org_country","agency_ic_fundings"],	     
	     "offset": 0,
	     "limit": 500	     	   	     
	 }

	r = requests.post('https://api.reporter.nih.gov/v1/projects/Search', json = request_body)
	results = json.loads(r.text)
	number = 0
	content = []
	for result in results['results']:
		# print(result)
		# print("------")
		number = number + 1
		content.append(result)
		

	return number, content   



@app.route("/search", methods = ["POST", "GET"])
def search():
    if request.method == "POST":
    	first_name = request.form["fn"]
    	middle_name = request.form["mn"]
    	last_name = request.form["ln"]
    	my_input = first_name + "|" +  middle_name + "|" + last_name
    	return redirect(url_for("user", usr= my_input))
    else:
    	return render_template("search.html")

@app.route("/<usr>")
def user(usr):

	first_name, middle_name, last_name = usr.split("|")
	rv,content = search_pi_name(first_name,middle_name,last_name)
	my_result = ''
	for i in range (0, len(content)):
		my_result = '<p>' +  my_result + str(content[i]) + '<p>'
	if len(my_result) == 0:
		return "null"
	else: 
		return my_result


if __name__ == '__main__':
   app.run()
   # rv, content = search_pi_name ("Matthew", "D", "welch")
   # print(content)
   
		
	
	
	
	
	
	
