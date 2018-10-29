# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

def create_code():
    import random
    checkcode = ''
    for i in range(4):
        current = random.randrange(0, 4)  # 生成随机数与循环次数比对
        current1 = random.randrange(0, 4)
        if current == i:
            tmp = chr(random.randint(65, 90))  # 65~90为ASCii码表A~Z
        elif current1 == i:
            tmp = chr(random.randint(97, 122))  # 97~122为ASCii码表a~z
        else:
            tmp = random.randint(0, 9)
        checkcode += str(tmp)
    return checkcode


def send_code(ema):
    '''
    暂时只支持qq邮箱，
    后期需要支持更多种类型的邮箱
    '''
    import smtplib
    from email.mime.text import MIMEText

    msg_from = '117465@qq.com'  # 发送方邮箱
    passwd = 'qrmzvmamfloctfhicz'  # 填入发送方邮箱的授权码
    msg_to = ema  # 收件人邮箱

    subject = "chou-ti验证码"  # 主题
    code = create_code()
    content = "你的验证码为%s"%code  # 正文
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465) # 邮件服务器及端口号
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print("发送成功")
        return code

    # except s.SMTPException as e:
    except:
        print("发送失败")
    finally:
        s.quit()

