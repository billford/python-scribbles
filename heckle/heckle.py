splunk = 'https://SPLUNK-SERVER-HERE'
port = 'SPLUNK-HEC-PORT-HERE'
token = "SPLUNK-HEC-TOKEN-HERE"


def heckle(splunk, port, message, token):
    token = "Splunk " + token
    req = requests.post(splunk + ":"+ port + "/services/collector/raw", headers = { 'Authorization':  token }, data = message)
    if req.status_code == 200:
        return True
    else :
        return req.text
