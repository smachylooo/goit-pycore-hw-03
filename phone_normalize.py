ALLOWED_CH = '+0123456789'

def normalize_phone(phone: str | int) -> str:
    res = ''
    for symbol in str(phone).strip():
        if symbol in ALLOWED_CH:
            res+=symbol

    if len(res) < 10: # Після міжнародного коду завжди повинно бути 10 чисел
        return 'Please write correct number'

    if len(res) > 10 and res[0] != '+' or res.startswith('380'):  # OR Для того, якщо хтось ввів іноземний номкр без + щоб просто добавлявся +
        res = '+' + res

    if len(res) <= 10 and not res.startswith('380'):
        res = '+38' + res
    
    return res

