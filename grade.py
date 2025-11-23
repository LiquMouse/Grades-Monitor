import requests
import json

def get_grades(url, cookies=""):
    html = requests.post(url, cookies=cookies).text
    data = json.loads(html)
    grades = {}
    for course in data['content']:
        grades[course['kcmc']] = course['zzcj']
    return grades