# nlp_base_skill
## crawling data
### HTTP(Hyper Text Transfer Protocol)
- defination: A protocol based on TCP/IP protocol to exchange data such as HTML, image file 
- Working priciple:
    + he default port is 80
    + tackle with one request every connection
    + any type of data is allowed
    + unkonwn to former information
    + transfer data with an uniform resource identitiers, URI
    + 8 actions for request: OPTIONS, HEAD, GET, POST, PUT, DELETE, TRACE, CONNECT
    + HTTP state codes like 404 representing NOT FOUND.
- Request
    + GET means getting data from the server.
    + POST means sending data to the server.
    + HTTP content-type shows file transfering.
### urllib2
- Request Objects
    + urlopen(url) return file-like object with three additional methods
        * geturl()
        * info()
        * getcode()
        * use str function and encoding = 'utf-8' to get HTML code.
    + 