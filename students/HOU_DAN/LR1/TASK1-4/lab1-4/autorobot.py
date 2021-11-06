import requests


# 18edce3ce905a4c1dbb965e6b35c3834d
# 2eb720a8970964f3f855d863d24406576
# 31107d5601866433dba9599fac1bc0083
# 471f28bf79c820df10d39b4074345ef8c
def reply_msg(receive_msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': '2eb720a8970964f3f855d863d24406576',
        'info': receive_msg,
        'userid': 'wechat-robot',
    }
    r = requests.post(apiUrl, data=data).json()
    return r['text']
