websites = {
    1: "www.yahoo.com",
    2: "www.tsec.edu",
    3: "www.asp.net",
    4: "www.abcd.in"
}
website_suffixes = tuple(url.split(".")[-1] for url in websites.values())
print(website_suffixes)
