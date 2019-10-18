import urllib.request as urlopen

def convert():
    open=req.get("https://api.exchangerate-api.com/v4/latest/USD")
    cur=open.json()
    print(cur)
convert()