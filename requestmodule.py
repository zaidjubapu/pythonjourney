import requests
r=requests.get("https://financialmodelingprep.com/api/company/price/AAPL")
a=r.text # show all the conntensts in the site
print(a)

# url="www.something.com"
# data= {
#     "p1":2,
#     "p2":3
# }
# r2=requests.post(url=url,data=data)
# print(r2)