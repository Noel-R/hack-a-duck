#plswork.py
import json
import requests

def apiGenData():
    authJWT="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJuYmYiOjE2OTYwMzIwMDAsImFwaV9zdWIiOiIwYmFjZjQ0NWM5ZjI3NTYxZGQzOTA4ZWQ5YmNkNzZkMjRjNGIyNWY3MTMwZDk0ZjNhNGIyOTZmNGIzYjEwMzZkMTcxNzIwMDAwMDAwMCIsInBsYyI6IjVkY2VjNzRhZTk3NzAxMGUwM2FkNjQ5NSIsImV4cCI6MTcxNzIwMDAwMCwiZGV2ZWxvcGVyX2lkIjoiMGJhY2Y0NDVjOWYyNzU2MWRkMzkwOGVkOWJjZDc2ZDI0YzRiMjVmNzEzMGQ5NGYzYTRiMjk2ZjRiM2IxMDM2ZCJ9.FGzp87wXv9MzgkcoxrIgTut0W9jj-_NlqvfSRXi3sv88tIIRmdsDRDkysDTkJnvlRORTsgA00XPolJBoxEs8dZySfFeEwDkoLz3u88DMyAOmhVzbC5qyRQTiHIOuVUu-Cb99vhEd68tgsMj7r5L6gHaIxhinhdkiD2iTw_micYbU_GknW-2VIUUOzqZoh5ot7IBBOPv-uIW4XgdSracXeg_qaBjKHS2Twh-BpZkuYGv2qjxe_PzgoJ27cXs7WiYqknezL95XlKpWJD-Ms1U7o4QN9f3w0pNszWFcovwrAWQEJnIy-Eh8E1P3gtd64Y7FNkIgPe4QKmAFKi_raXDmUw"
    headers = {
        'Authorization': f'Bearer {authJWT}',
        'Content-Type': 'application/json',
        'version': '1.0'
    }
    quantity = 1
    numTransactions = 1
    liveBalance = False
    payload = json.dumps({"quantity": quantity, "numTransactions": numTransactions, "liveBalance": liveBalance})

    response = requests.post("https://sandbox.capitalone.co.uk/developer-services-platform-pr/api/data/accounts/create", headers=headers, data=payload).text
    d=json.loads(response)
    return jsonD
    jsonD=d["Accounts"][0]
    if "developerId" in jsonD:
        jsonD.pop("developerId")
    if "livebalance" in jsonD:
        jsonD.pop("livebalance")