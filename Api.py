import random
import json

import urllib3

class Account:
    ID = None
    Name = ''
    Address = ''
    Email = ''
    CreditScore = 0
    RiskScore = 0
    ApprovalState = False

    transactionContext = None
    transactions = []

    def __init__(self, tcon, **kwargs):
        self.Name = kwargs['data']['firstname'] + " " + kwargs['data']['lastname']
        self.Address = kwargs['data']['homeAddress']
        self.Email = kwargs['data']['email']
        self.CreditScore = kwargs['data']['creditScore']
        self.RiskScore = kwargs['data']['riskScore']
        self.ID = kwargs['data']['accountId']
        self.transactionContext = tcon

        self.transactionContext.Create(random.randrange(0, 5))


class Transaction:
    ID, Merchant, Category, Amount, Timestamp, Currency, Status = None, None, None, None, None, None, None

    def __init__(self, **kwargs):
        self.Merchant = kwargs['data']['merchant']['name']
        self.Category = kwargs['data']['merchant']['category']
        self.Amount = kwargs['data']['amount']
        self.Timestamp = kwargs['data']['timestamp']
        self.Currency = kwargs['data']['currency']
        self.Status = kwargs['data']['status']


class API:
    url = "https://sandbox.capitalone.co.uk/developer-services-platform-pr/api/data/"

    headers = {
        'Content-Type': 'application/json',
        'Version': '1.0',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJuYmYiOjE2OTYwMzIwMDAsImFwaV9zdWIiOiIwYmFjZjQ0NWM5ZjI3NTYxZGQzOTA4ZWQ5YmNkNzZkMjRjNGIyNWY3MTMwZDk0ZjNhNGIyOTZmNGIzYjEwMzZkMTcxNzIwMDAwMDAwMCIsInBsYyI6IjVkY2VjNzRhZTk3NzAxMGUwM2FkNjQ5NSIsImV4cCI6MTcxNzIwMDAwMCwiZGV2ZWxvcGVyX2lkIjoiMGJhY2Y0NDVjOWYyNzU2MWRkMzkwOGVkOWJjZDc2ZDI0YzRiMjVmNzEzMGQ5NGYzYTRiMjk2ZjRiM2IxMDM2ZCJ9.FGzp87wXv9MzgkcoxrIgTut0W9jj-_NlqvfSRXi3sv88tIIRmdsDRDkysDTkJnvlRORTsgA00XPolJBoxEs8dZySfFeEwDkoLz3u88DMyAOmhVzbC5qyRQTiHIOuVUu-Cb99vhEd68tgsMj7r5L6gHaIxhinhdkiD2iTw_micYbU_GknW-2VIUUOzqZoh5ot7IBBOPv-uIW4XgdSracXeg_qaBjKHS2Twh-BpZkuYGv2qjxe_PzgoJ27cXs7WiYqknezL95XlKpWJD-Ms1U7o4QN9f3w0pNszWFcovwrAWQEJnIy-Eh8E1P3gtd64Y7FNkIgPe4QKmAFKi_raXDmUw',
        'Cookie': 'AWSALB=n0ox8HP18bUphDm3YdaFFKRHwwhmKazwJeJizl4qRhcX6AicOfDOvwXeE/C72TSvxUCWEJPvQ4PPyuyGhMWLSqyTVcS6LYQF7N2Fd6J2L5AUbXZtBmov+TEy5PwW; AWSALBCORS=n0ox8HP18bUphDm3YdaFFKRHwwhmKazwJeJizl4qRhcX6AicOfDOvwXeE/C72TSvxUCWEJPvQ4PPyuyGhMWLSqyTVcS6LYQF7N2Fd6J2L5AUbXZtBmov+TEy5PwW'
    }

    class aContext:
        headers = None
        url = None
        accountID = None
        transactions = None

        class tContext:
            accId = None

            def __init__(self, accountID, headers):
                self.headers = headers
                self.accId = accountID
                

            def Create(self, amount):
                ret = []

                http = urllib3.PoolManager()

                payload = json.dumps({
                    "quantity": amount
                }).encode('utf-8')

                THISURL = "https://sandbox.capitalone.co.uk/developer-services-platform-pr/api/data/transactions/accounts/"+ self.accId + "/create"

                response = http.request('POST', THISURL, headers=self.headers, body=payload)
                if response.status == 200:
                    for transaction in response.json()["Transactions"]:
                        ret.append(Transaction(data=transaction))
                else:
                    print(response.data.decode('utf-8'))

                return ret

        def __init__(self, url, headers):
            self.headers = headers
            self.url = url + 'accounts/'

        def Create(self, amount):
            ret = []

            http = urllib3.PoolManager()
            
            payload = json.dumps({
                "quantity": amount,
                "state": "open"
            }).encode('utf-8')

            THISURL = self.url + "create"
            response = http.request('POST', THISURL, headers=self.headers, body=payload)
            for acc in response.json()['Accounts']:
                account = Account(self.tContext(accountID=acc['accountId'], headers=self.headers), data=acc)
                account.transactions = account.transactionContext.Create(5)
                ret.append(account)
            return ret

    aCtx = aContext(url, headers)
    accounts = []

    def Generate(self, count):
        return self.aCtx.Create(count)
