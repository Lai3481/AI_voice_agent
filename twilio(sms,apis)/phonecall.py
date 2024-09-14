from twilio.rest import Client

# Twilio 账户 SID 和身份验证令牌
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

# 发起语音通话
call = client.calls.create(
    to='+0987654321',  # 替换为接收者的电话号码
    from_='+1234567890',  # 替换为你的 Twilio 电话号码
    url='http://demo.twilio.com/docs/voice.xml'  # 替换为你自己的 TwiML URL
)

print(f'Call initiated with SID: {call.sid}')
