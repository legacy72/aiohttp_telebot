from aiohttp import web

from telegram_bot import ask_eye_of_god_bot

routes = web.RouteTableDef()


@routes.get('/eye_of_god_bot')
async def eye_of_god_bot(request):
    phone_number = request.rel_url.query.get('phone_number')
    res = await ask_eye_of_god_bot(phone_number=phone_number)
    return web.json_response(res)


app = web.Application()
app.add_routes(routes)
web.run_app(app)
