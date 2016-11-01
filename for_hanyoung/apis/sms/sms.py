import os
import json
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException
from for_hanyoung import settings

config_file = open(os.path.join(settings.CONF_DIR, 'apis_debug.json'))
config = json.loads(config_file.read())
config_file.close()

##  @brief This sample code demonstrate how to send sms through CoolSMS Rest API PHP
__all__ = ['send_sms']


def send_sms(number, message):

    # set api key, api secret
    api_key = config['sms']['API_KEY']
    api_secret = config['sms']['API_SECRET']

    params = dict()
    params['type'] = 'sms' # Message type ( sms, lms, mms, ata )
    params['from'] = config['sms']['SENDER_NUMBER'] # Sender number
    params['text'] = str(message) # Message


    # 1. 여러 명한테 보낼 때를 대비. 2. 번호 안에 '-'가 있으면 '-'를 없앰.
    if isinstance(number, (list, tuple)):
        map(lambda x: x.replace('-', ''), number)
        number = ','.join(number)
    else:
        number = number.replace('-', '')

    params['to'] = str(number)  # Recipients Number '01000000000,01000000001'
    cool = Message(api_key, api_secret)
    try:
        response = cool.send(params)
        print("Success Count : %s" % response['success_count'])
        print("Error Count : %s" % response['error_count'])
        print("Group ID : %s" % response['group_id'])

        if "error_list" in response:
            print("Error List : %s" % response['error_list'])

    except CoolsmsException as e:
        print("Error Code : %s" % e.code)
        print("Error Message : %s" % e.msg)