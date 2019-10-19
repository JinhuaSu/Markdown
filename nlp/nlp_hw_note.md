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
    + urlopen(url) returns file-like object with three additional methods
        * geturl()
        * info()
        * getcode()
        * use str function and encoding = 'utf-8' to get HTML code.
    + practice with cookies
        * What is cookie? a name-value pair sent to the clients by the server at the first time, it helps the server recognize the client for the next time.
        * Type: conversation cookie and simple cookie
        * attribution:
            - NAME = Value
            - Expires
            - Domain
            - Path
            - Secure: return the cookie only when connecting using SSH(secure shell)
    + introduction of 0-1 travelling in the internet
        * client, server
        * LAN local area network with the rounter
        * enterprise network with interchanger
        * proxy server will let clients see the same IP, or help clients use virtual private network
        * firewall
        * request and response
        * package transportation: flow work for current 
### tricks for efficiency
- target: to cheat the cops of the server anti_crawling organization
- VPN: different position
- cookie: different clients
- user_agent: Mozilla, window NT
### re
### file management
- with grammar
- os module
    