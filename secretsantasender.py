from matcher import Secret_Santa_Matcher
from twilio.rest import Client
import os

if 'TWILIO_SID' not in os.environ or 'TWILIO_AUTH' not in os.environ:
    print( "Must set TWILIO_SID and TWILIO_AUTH environment variables first" )
    exit()

sid = os.environ[ 'TWILIO_SID' ]
auth = os.environ[ 'TWILIO_AUTH' ]

print( sid )
print( auth )
