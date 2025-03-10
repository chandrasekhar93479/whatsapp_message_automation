from twilio.rest import Client
from datetime import datetime, timedelta
import time

account_sid='AC95f7b91ad24e50398680a33f9882dd3b'
auth_token='a6fc7528ec062d66860e03cbac9b3752'

Client= Client(account_sid,auth_token)

def send_whatsapp_message(recipient_number,message_body):
    try:
        message=Client.messages.create(
             from_='whatsapp:+14155238886' ,
               body=message_body,
              to=f'whatsapp:{recipient_number}'
         )
           
        print(f'message sent successfully! message SID{message.sid}')
    except Exception as e:
        print('an error occured')

name=input('enter the recipient name=')
recipient_number=input('enter recipient whatsapp number with country code(e.g +123)')
message_body=input({f'enter the message you want to send to {name}:'})

date_str=input('enter the date to send message (YYYY-MM-DD):')
time_str=input('enter the time to send message(HH:MM in 24 hour format):')

schedule_datetime=datetime.strptime(f'{date_str} {time_str}',"%Y-%m-%d  %H:%M")
current_datetime=datetime.now()


time_difference=schedule_datetime-current_datetime
delay_seconds=time_difference.total_seconds()


if delay_seconds <=0:
    print('the specific time is in past.please enter future date and time :')
else:
    print(f'message scheduled to be send to {name} at {schedule_datetime}')


time.sleep(delay_seconds)

send_whatsapp_message(recipient_number,message_body)
