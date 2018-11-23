from WebApp.routes import routes 
SUCCESS = "HTTP/1.1 200 OK\r\n\r\n "
NOT_FOUND = "HTTP/1.1 404 NOT FOUND\r\n\r\n "

def handle_request(request):
    r_type = request.split("\n")[0]
    print(request)
    if "GET" in r_type:
        route = r_type.split(' ')[1]
        if route in routes:
            try:
                print(routes[route])
                with open("../_html/"+routes[route], "r") as f:
                    return SUCCESS + f.read()
            except:
                with open("_html/errors/404.html", "r") as f:
                    return NOT_FOUND + "something went wrong :(" 
        else:
            with open("../_html/errors/404.html", "r") as f:
                return NOT_FOUND + f.read()
