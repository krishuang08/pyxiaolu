import requests
import json
s=requests.Session()
cj=requests.cookies.RequestsCookieJar()
cj.set('SERVERID','s1',path='/',domain='xiaolu.newlandcxfzzx.com')
s.cookies.update(cj) 

def login(username,password):
    payload={"username":username,"password":password,"forceLoginFlag":1}
    r=s.post('https://xiaolu.newlandcxfzzx.com/newland-ai-education/sys/loginByUsername',json=payload,headers={'Referer':'https://xiaolu.newlandcxfzzx.com/admin/'})
    if json.loads(r.text)['success']:
        return json.loads(r.text)['result']['token']
    else:
        return False

def execute(code,token):
    payload={'code':code}
    r=s.post('https://xiaolu.newlandcxfzzx.com/newland-ai-education/xiaoluPythonWorks/xiaoluPythonWorks/run',json=payload,headers={'Referer':'https://xiaolu.newlandcxfzzx.com/admin/','X-Access-Token':token})
    if json.loads(r.text)['success']:
        return json.loads(r.text)['result']['stdOut']
    else:
        return json.loads(r.text)['success']