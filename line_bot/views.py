from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, JsonResponse

from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage, TextMessage,StickerMessage

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

@csrf_exempt
def callback(request):
    if (request.method == "POST"):
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')


        # 嘗試解密event
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
       
        for event in events:
            if isinstance(event, MessageEvent):
                print(event)
                
                if isinstance(event.message, TextMessage):
                    res_text = event.message.text
                    
                    if event.message.text=='@我要報到':
                       line_bot_api.reply_message(event.reply_token, StickerMessage(type="sticker",package_id = 789,sticker_id=10855))
                    elif event.message.text=='@我的名牌':
                       line_bot_api.reply_message(event.reply_token, TextSendMessage(text = res_text))
                    elif event.message.text=='@車號登入':
                       line_bot_api.reply_message(event.reply_token, TextSendMessage(text = res_text))
                    else:
                       line_bot_api.reply_message(event.reply_token, TextSendMessage(text = res_text))
        return HttpResponse()
    else:
        return HttpResponseBadRequest()


def sendMsg(requests, uid,msg):
    line_bot_api.push_message(uid, TextSendMessage(text = msg))
    return HttpResponse()