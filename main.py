from aiohttp import web


async def index(request):
    cookie = request.cookies.get('default', None)
    if cookie:
        page = open('site.html').read()
        return web.Response(text=page, content_type='text/html')
    else:
        return web.HTTPFound(location='/loginpage')


async def login_page(request):
    resp = open('C:/users/balakris/aiohttp-login-session/login.html', 'r').read()
    return web.Response(text=resp, content_type='text/html')


async def login(request):
    form = await request.post()
    username = form.get('username')
    if username == 'hippod':
        password = form.get('password')
        if password == 'admin':
            response = web.HTTPFound(location='/')
            response.set_cookie('default', value=1, max_age=30*86400, path='/')
            return response
    else:
        resp = web.HTTPFound(location='/loginpage')
        return resp

app = web.Application()
app.router.add_get('/', index)
app.router.add_get('/loginpage', login_page)
app.router.add_post('/login', login)
web.run_app(app, host='127.0.0.1', port=8080)