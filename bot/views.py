from django.shortcuts import render,HttpResponse
from twilio.rest import Client
from .models import Message
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
account_sid = 'ACeaf344cbda950e2aa828c052aa811fa6'
auth_token = '262d8b66b06834c5f7cfe158606026fb'
client = Client(account_sid, auth_token)

@csrf_exempt
def bot(request):
    try:
        message = request.POST['Body']
        sender_name = request.POST['ProfileName']
        sender_number = request.POST['From']
        status = request.POST['SmsStatus']
        Message.objects.create(user=sender_name,number=sender_number,message=message,status=status)
        if message not in ['1','2','3','4',]:
            client.messages.create(
                                from_='whatsapp:+14155238886',
                                body='Hello user! Please select any one of the following options\n1.Send a text\n2.Send Image\n3.Send a document\n4.Send List',
                                to=sender_number,
                            )
        elif message == '1':
            client.messages.create(
                            from_='whatsapp:+14155238886',
                            body='Hey '+sender_name+', How are you doing?',
                            to=sender_number,
                        )
        elif message == '2':
            client.messages.create(
                            from_='whatsapp:+14155238886',
                            media_url=['https://d2vrvpw63099lz.cloudfront.net/whatsapp-bots/whatsapp-bots.png'],
                            to=sender_number,
                        )
        elif message == '3':
            client.messages.create(
                            from_='whatsapp:+14155238886',
                            media_url=['http://www.africau.edu/images/default/sample.pdf'],
                            to=sender_number,
                        )
        elif message == '4':
            client.messages.create(
                                from_='whatsapp:+14155238886',
                                body='Hello user! Please select any one of the following options\n1.Send a text\n2.Send Image\n3.Send a document\n4.Send List',
                                to=sender_number,
                            )
        
    except Exception:
        pass
    return HttpResponse('The bot is working')