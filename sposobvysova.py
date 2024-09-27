def send_email(message, recipient, sender="university.help@gmail.com"):
    def valid_email(email):
        return ("@" in email and (email.endswith(".com") or email.endswith(".ru") or email.endswith(".net")))
    if not valid_email(sender) or not valid_email(recipient):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')
        return
    if sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')

send_email('hello', 'stepan@d.r')
send_email('hello', 'university.help@gmail.com','university.help@gmail.com')
send_email('hello', 'stepan@r.ru', 'university.help@gmail.com')
send_email('hello', 'stepan@r.ru', 'university.help@gmail.ru')
