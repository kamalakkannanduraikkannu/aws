import webbrowser 
url=["http://www.google.com","http://www.yahoo.com","http://www.thatstamil.com"]
url_size = len(url)
for i in range(url_size):
    webbrowser.open_new(url[i])

