import random
import requests
import time
from bs4 import BeautifulSoup


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.58'
}

url = "https://evemaps.dotlan.net/system/"
url_ali = "https://evemaps.dotlan.net/alliance/"


def adm_compare(alliance):
    sys_lst = get_ali_sys(alliance)
    old_adm = []

    for sys in sys_lst:
        old_adm.append([sys, 0])

    while True:
        curr_amd = get_sys_adm(sys_lst)
        for x in range(len(curr_amd)):
            if old_adm[x][1] == curr_amd[x][1]:
                pass
            if old_adm[x][1] > curr_amd[x][1]:
                print(f'AMD in system {old_adm[x][0]} DOWN')
            if old_adm[x][1] < curr_amd[x][1]:
                print(f'AMD in system {old_adm[x][0]} UP')
        old_adm = curr_amd


def get_ali_sys(alliance):
    print('Scanning alliance')
    sys_lst = []
    s = requests.Session()

    response = s.get(url=url_ali+alliance, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    sov_sys = soup.find_all('table')[2].find_all('tr')

    for row in range(1, len(sov_sys)):
        sys_lst.append(sov_sys[row].find_all('td')[2].find_all('a')[1].text)

    return sys_lst


def get_sys_adm(sys_lst):
    print('Scanning systems')
    curr_adm = []
    s = requests.Session()
    for sys in sys_lst:
        response = s.get(url=url+sys, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        if soup.find_all('table')[3].find_all('tr')[0].find_all('th')[2].text == 'ADM / Time':
            adm = float(soup.find_all('table')[3].find_all('tr')[1].find_all('td')[3].text.split('x')[0])
        else:
            adm = float(soup.find_all('table')[2].find_all('tr')[1].find_all('td')[3].text.split('x')[0])
        curr_adm.append([sys, adm])
        r_time = random.randint(1, 5)
        time.sleep(r_time)

    return curr_adm


def main():
    alliance = 'Red_Alliance'

    adm_compare(alliance)


if __name__ == "__main__":
    main()
