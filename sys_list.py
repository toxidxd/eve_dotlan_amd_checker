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

url_ali = "https://evemaps.dotlan.net/alliance/"


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




def main():
    alliance = 'Red_Alliance'
    sys_lst = get_ali_sys(alliance)




if __name__ == "__main__":
    main()
