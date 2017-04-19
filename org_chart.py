# Assume there is a REST API available at "http://www.company.com/api" for accessing employee information The employee 
#   information endpoint is "/employee/<id>" Each employee record you retrieve will be a JSON object with the following keys:
#   - 'name'  refers to a String that contains the employee's first and last name
#   - 'title' refers to a String that contains the employee's job title
#   - 'reports' refers to an Array of Strings containing the IDs of the employee's direct reports
# Write a function that will take an employee ID and print out the entire hierarchy of employees under that employee.
# For example, suppose that Frank Michaels' employee id is 'A123456789' and his only direct reports are Walton Thames and 
#   Nancy Chadwick. If you provide 'A123456789' as input to your function, you will see the sample output below.
# 
# -----------Begin Sample Output--------------
# Frank Michaels - Senior VP of Engineering
#   Walton Thames - VP of UX
#     Ryan Kramer - Director of UX
#       Bethany Pfleger - Senior UX Engineer
#   Nancy Chadwick - VP of Engineering
#     Thomas Qix - Director of Engineering
#       Jillian Frampton - Website Manager
#         Luke Fillmore - Software Engineer
#       Steve Delli - Infrastructure Manager
#         Ying Ping - Site Reliability Engineer
# -----------End Sample Output--------------
# 
# GET /employee/A123456789
# {
#  "name": "Frank Michaels",
#  "title": "Senior VP of Engineering",
#  "reports": ["A123456793", "A1234567898"]
# }

# TODO: Get this tested and actually working.
    
import requests
import json
    
def request_api(emp_id):
    r = requests.get("http://www.linkedin.corp/api/employee/" + emp_id)
    request_json = json.loads(r.content())
    print(request_json['name'] + " - " + request_json['title'])
    if request_json['reports'] is '':
        return 0
    for direct_report in request_json['reports']:
        request_api(direct_report)
    
