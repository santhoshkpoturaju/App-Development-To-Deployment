from django.http import HttpResponse

def hello_world(request):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello World Site</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <p>Welcome to your Django Hello World site. this is version 3.0 app</p>
    </body>
    </html>
    """
    return HttpResponse(html_content)