import random

import requests
import time
from random import randrange
from bs4 import BeautifulSoup
import json

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
          'application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.58'
}

url = "https://evemaps.dotlan.net/system/"


def get_sys_adm(sys_lst):


    # sys_lst = ["A1-AUH"]
    curr_adm = []
    s = requests.Session()
    for sys in sys_lst:
        # print(f'Scanning {sys}')
        response = s.get(url=url+sys, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        if soup.find_all('table')[3].find_all('tr')[0].find_all('th')[2].text == 'ADM / Time':
            adm = float(soup.find_all('table')[3].find_all('tr')[1].find_all('td')[3].text.split('x')[0])
        else:
            adm = float(soup.find_all('table')[2].find_all('tr')[1].find_all('td')[3].text.split('x')[0])

        print(f'ADM in {sys} - {adm}')
        # curr_sys = [sys, adm]
        curr_adm.append([sys, adm])
        # print(curr_adm)
        r_time = random.randint(1, 5)
        time.sleep(r_time)

    return curr_adm

def adm_compare(new_adm, old_adm):



    for x in range(len(old_adm)):
        print(new_adm[x])
        print(old_adm[x])



    old_adm = new_adm
    return old_adm




def main():
    sys_lst = ["A1-AUH",
               "A5MT-B",
               "JD-TYH",
               "SN9S-N",
               "02V-BK",
               "R-ARKN",
               "MS2-V8",
               "DL-CDY",
               "X-HISR",
               "QS-530",
               "VR-YRV",
               "IPX-H5",
               "29YH-V",
               "LG-RO2"]
    sys_lst = ["A1-AUH",
               "A5MT-B"]
    old_adm = []
    for sys in sys_lst:
        old_adm.append([sys, 0])


    while True:

        curr_adm = get_sys_adm(sys_lst)
        old_adm = adm_compare(curr_adm, old_adm)





if __name__ == "__main__":
    main()
