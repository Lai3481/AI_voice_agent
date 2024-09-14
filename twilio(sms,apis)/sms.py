from twilio.rest import Client

# Twilio 账户 SID 和身份验证令牌
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

# 发送 SMS
message = client.messages.create(
    body='Hello, this is a test message from Twilio!',
    from_='+1234567890',  # 替换为你的 Twilio 电话号码
    to='+0987654321'      # 替换为接收者的电话号码
)

print(f'Message sent with SID: {message.sid}')
