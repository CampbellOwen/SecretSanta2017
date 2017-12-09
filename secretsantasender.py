from matcher import Secret_Santa_Matcher
from twilio.rest import Client
import os
import json

if 'TWILIO_SID' not in os.environ or 'TWILIO_AUTH' not in os.environ or 'TWILIO_NUMBER' not in os.environ:
    print( "Must set TWILIO_SID, TWILIO_AUTH, and TWILIO_NUMBER environment variables first" )
    exit()

sid = os.environ[ 'TWILIO_SID' ]
auth = os.environ[ 'TWILIO_AUTH' ]
number = os.environ[ 'TWILIO_NUMBER' ]

client = Client( sid, auth )

participants = {}
with open( 'participants.json', 'r' ) as p_file:
    participants = json.loads( p_file.read() )[ 'participants']

matcher = Secret_Santa_Matcher( participants, None )

matches = matcher.match()

message = "Hello {0}, your Secret Santa 2017 match is: {1}. Reminder: Keep the gift under $30!"

for giver in matches:
    client.api.account.messages.create( to=participants[ giver ]['number'], from_=number, body=message.format( giver, matches[ giver ] ) )

