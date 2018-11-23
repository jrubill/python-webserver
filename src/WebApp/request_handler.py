
SUCCESS_HEADER = "HTTP/1.1 200 OK\r\n\r\n "
FAIL_HEADER = "HTTP/1.1 404 NOT FOUND\r\n\r\n "

def handle_request(request):
    r_type = request.split("\n")[0]
    print(r_type)
    if "GET" in r_type:
        if r_type.split(' ')[1] == '/':
            try:
                with open("index.html", "r") as f:
                    return SUCCESS_HEADER + f.read()
            except:
                with open("html/404.html", "r") as f:
                    return FAIL_HEADER + f.read()
        else:
            with open("html/404.html", "r") as f:
                return FAIL_HEADER + f.read()
 
