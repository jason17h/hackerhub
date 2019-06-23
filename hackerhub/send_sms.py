import os
from twilio.rest import Client 
from django.shortcuts import render
from hackerhub.models import Hackathon


def sendSMS(request):
 
    account_sid = 'AC14fde0e29bed1ea85511c5d6190f2029' 
    auth_token = 'a97b39e3f8e6199743c9d16944527dc3' 
    client = Client(account_sid, auth_token) 
    
    message = client.messages.create( 
                                from_='+18678880333',  
                                body='Hello from WeHack! The deadline to apply to EngHack 2020 is due in a week.',      
                                to='+16479653904' 
                            ) 
    
    print(message.sid)

    hackathons = Hackathon.objects.order_by('startDate').reverse()
    template_name = 'index.html'
    context = {
        'hackathons':hackathons,
    }

    return render(request, template_name, context)