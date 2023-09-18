import re
from pprint import pprint

import requests as req
from bs4 import BeautifulSoup

from utils.helpers import list_flatter, save_json, read_json

firms = [

    {"symbol": "coinmetrics", "name": "CoinMetrics", "jobs": "https://coinmetrics.io/careers/#open-positions",
     "source": "native",
     "image": ""},

    {"symbol": "santiment", "name": "Santiment",
     "jobs": "https://santiment.notion.site/Work-with-Santiment-f1880de7557b468a80b1465013f311cd", "source": "notion"},

    {"symbol": "parseq", "name": "Parseq Finance", "jobs": "https://wellfound.com/company/parsec-finance/jobs",
     "source": "wellfound"},

    {"symbol": "tally", "name": "Tally", "jobs": "https://hirevise.com/tally", "source": "hiverise"},

    {"symbol": "manifold", "name": "Manifold", "jobs": "https://manifold.recruitee.com/", "source": "recruitee"},

    {"symbol": "dfns", "name": "Dfns", "jobs": "https://www.welcometothejungle.com/fr/companies/dfns/jobs",
     "source": "welcometothejungle"},

    {"symbol": "starkware", "name": "Starkware", "jobs": "https://starkware.co/careers/", "source": "comeet"}, # comeet integrate in native page
    ###############################################################################################################################################

    {"symbol": "dune", "name": "Dune", "jobs": "https://jobs.ashbyhq.com/dune", "source": "ashby"},
    {"symbol": "opensea", "name": "OpenSea", "jobs": "https://jobs.ashbyhq.com/OpenSea", "source": "ashby"},
    {"symbol": "safe", "name": "Safe", "jobs": "https://jobs.ashbyhq.com/safe.global", "source": "ashby"},

    ###############################################################################################################################################
    ###############################################################################################################################################
    ###############################################################################################################################################
    {"symbol": "tokenmetrics", "name": "TokenMetrics", "jobs": "https://jobs.lever.co/tokenmetrics?&",
     "source": "jobs_lever",
     "logo": "https://global-uploads.webflow.com/634054bf0f60201ce9b30604/634503713190a76b2bdd040b_TM%20Logo.svg"},
    {"symbol": "polygon", "name": "Polygon", "jobs": "https://jobs.lever.co/Polygon", "source": "jobs_lever",
     "logo": "https://assets-global.website-files.com/6364e65656ab107e465325d2/637adca2e1a09547acd85968_Y_44LwHNRnOEvnRExgnO1UujtZwn7zq7BCb4oxxHgpI.jpeg"},
    {"symbol": "kraken", "name": "Kraken", "jobs": "https://jobs.lever.co/kraken", "source": "jobs_lever",
     "logo": "https://assets-global.website-files.com/6364e65656ab107e465325d2/637aee1ef72214496f12a341__60qR_QlkLmCec1XXmNJptaSGIgNjEKqh2NIFTp3-AI.png"},
    {"symbol": "atomic", "name": "Atomic", "jobs": "https://jobs.lever.co/atomic", "source": "jobs_lever",
     "logo": ""},
    {"symbol": "offchainlabs", "name": "OffChain Labs", "jobs": "https://jobs.lever.co/offchainlabs",
     "source": "jobs_lever",
     "logo": "https://offchainlabs.com/wp-content/themes/offchain/images/home/hero/navi_logoo.svg"},


    {"symbol": "utopia_labs", "name": "Utopia Labs", "jobs": "https://boards.greenhouse.io/utopialabs",
     "source": "greenhouse",
     "logo": "https://global-uploads.webflow.com/63d9506ce2c2a2c301338d9b/63d950a50c18d87b498d6947_Utopia%20Labs%20Logo.svg"},
    {"symbol": "messari", "name": "Messari", "jobs": "https://boards.greenhouse.io/messari", "source": "greenhouse",
     "logo": "https://images.crunchbase.com/image/upload/c_lpad,f_auto,q_auto:eco,dpr_1/yltdya90noo6ptm2ohks"},
    {"symbol": "nansen", "name": "Nansen", "jobs": "https://boards.greenhouse.io/nansen", "source": "greenhouse",
     "logo": "https://assets-global.website-files.com/60118ca18674407b85935203/64f6f41dcae1161d9e6a7b43_White.svg"},
    {"symbol": "ox", "name": "0x", "jobs": "https://boards.greenhouse.io/0x", "source": "greenhouse",
     "logo": "https://assets.website-files.com/640bf70a17d12b42d97a052b/640bfd7d8441821c4cd20210_logo.svg"},
    {"symbol": "magiceden", "name": "MagicEden", "jobs": "https://boards.greenhouse.io/magiceden",
     "source": "greenhouse",
     "logo": "https://pbs.twimg.com/card_img/1701691186321469440/jzjaPs2J?format=jpg&name=medium"},
    {"symbol": "edgeandnode", "name": "Edge & Node", "jobs": "https://boards.greenhouse.io/edgeandnode",
     "source": "greenhouse",
     "logo": "https://edgeandnode.com/images/logo-big.png"},
    {"symbol": "uniswaplabs", "name": "Uniswap", "jobs": "https://boards.greenhouse.io/uniswaplabs",
     "source": "greenhouse",
     "logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTFOIW5iK418FeYIZZf4aTxP8lWg_AzyZbrU0aviNaYhg&s"},
    {"symbol": "layerzerolabs", "name": "LayerZero Labs", "jobs": "https://boards.greenhouse.io/layerzerolabs",
     "source": "greenhouse",
     "logo": "https://cdn-images-1.medium.com/v2/resize:fit:1200/format:png/1*Iz7ZjBiBzQXhqWF8o1X9vw.png"},
    {"symbol": "alchemy", "name": "Alchemy", "jobs": "https://boards.greenhouse.io/alchemy", "source": "greenhouse",
     "logo": "https://www.solodev.com/file/b2360ebd-dd29-11ec-b9ad-0eaef3759f5f/Alchemy-Logo-Icon.png"},
    {"symbol": "okx", "name": "OKX", "jobs": "https://boards.greenhouse.io/okx", "source": "greenhouse",
     "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Logo-OKX.png/800px-Logo-OKX.png"},

    {"symbol": "zero_hash", "name": "Zero Hash", "jobs": "https://zero-hash.breezy.hr/", "source": "breezy",
     "logo": "https://cdn-images-1.medium.com/max/1200/1*yhA5ylNNLZAGxGZ3rT3WwA.jpeg"},
    {"symbol": "bitwave", "name": "Bitwave", "jobs": "https://bitwave.breezy.hr/", "source": "breezy",
     "logo": "https://images.crunchbase.com/image/upload/c_lpad,f_auto,q_auto:eco,dpr_1/beyw4cr4ul2fcdey1kdk"},
    # {"symbol": "", "name": "", "jobs": ""},
]


class Parser(object):
    @staticmethod
    def greenhouse_parser(content):
        soup = BeautifulSoup(content, 'html.parser')
        jobs = []
        job_section = soup.find('section', class_='level-0')
        if job_section:
            openings = job_section.find_all('div', class_='opening')
            for opening in openings:
                job_url = "https://boards.greenhouse.io/" + opening.find('a')['href']
                job_title = opening.find('a').text
                location = opening.find('span', class_='location').text
                job_info = {'title': job_title, 'location': location, 'url': job_url}
                jobs.append(job_info)
        return jobs

    @staticmethod
    def breezy_parser(content):
        soup = BeautifulSoup(content, 'html.parser')
        job_listings = soup.find_all('li', class_='position transition')
        jobs = []
        for job_listing in job_listings:
            pprint(job_listing)
            job_title = job_listing.find('h2').text.strip()
            location = job_listing.find('li', class_='location').text.strip()
            if re.search(' - %LABEL_POSITION_TYPE_REMOTE%', location):
                location = re.sub('%LABEL_POSITION_TYPE_REMOTE%', '', location) + 'remote'

            job_type_code = job_listing.find('li', class_='type').text.strip()
            if job_type_code == "%LABEL_POSITION_TYPE_FULL_TIME%":
                job_type = "full time"
            elif job_type_code == "%LABEL_POSITION_TYPE_PART_TIME%":
                job_type = "part time"
            elif job_type_code == "%LABEL_POSITION_TYPE_OTHER%":
                job_type = "other"
            else:
                job_type = job_type_code
            try:
                department = job_listing.find('li', class_='department').text.strip()
            except:
                department = ""
            try:
                job_url = "https://zero-hash.breezy.hr" + job_listing.find('a')['href']
            except:
                job_url = ""
            job_info = {'title': job_title, 'location': location, 'url': job_url, 'department': department,
                        'job_type': job_type}
            jobs.append(job_info)
            pprint(job_info)
        return jobs

    @staticmethod
    def jobslever_parser(content):
        soup = BeautifulSoup(content, 'html.parser')
        postings = soup.find_all('div', class_='posting')
        jobs = []
        for posting in postings:
            job_title = posting.find('h5', {'data-qa': 'posting-name'}).text.strip()
            location = posting.find('span', class_='location').text.strip()
            department = posting.find('span', class_='department').text.strip()
            try:
                commitment = posting.find('span', class_='commitment').text.strip()
            except:
                commitment = ""
            job_url = posting.find('a', class_='posting-btn-submit')['href']
            job_code = posting['data-qa-posting-id']
            job_info = {'title': job_title, 'location': location, 'url': job_url, 'department': department,
                        'job_type': commitment, 'code': job_code}
            jobs.append(job_info)
        return jobs

    @staticmethod
    def ashby_parser(content):
        data = {}
        return data

    @staticmethod
    def wellfound_parser(content):
        data = {}
        return data

    @staticmethod
    def notion_parser(content):
        data = {}
        return data

    def parser(self, content, hr_provider):
        if hr_provider == 'greenhouse':
            jobs = self.greenhouse_parser(content)
        elif hr_provider == 'breezy':
            jobs = self.breezy_parser(content)
        elif hr_provider == 'jobslever':
            jobs = self.jobslever_parser(content)
        elif hr_provider == 'ashby':
            jobs = self.ashby_parser(content)
        elif hr_provider == 'wellfound':
            jobs = self.wellfound_parser(content)
        elif hr_provider == 'notion':
            jobs = self.notion_parser(content)
        else:
            jobs = []
        return jobs


class Fetcher(object):
    def __init__(self):
        self.Parser = Parser()

    def fetcher(self, fims_list):
        all_jobz = []
        for f in fims_list:
            # if f['symbol'] == 'utopia_labs':
            # if f['source'] == 'ashby':
            if f['source'] in ['jobs_lever', 'greenhouse', 'breezy']:
                print(f['name'], f['jobs'])
                resp = req.get(f['jobs'])
                if resp.status_code == 200:
                    print(f['name'], resp.status_code)
                    content = resp.text
                    # pprint(content)
                    jobz = self.Parser.parser(content, f['source'])
                    for j in jobz:
                        j['company'] = f['name']
                        j['company_symbol'] = f['symbol']
                        j['company_logo'] = f['logo']
                    all_jobz.append(jobz)
                else:
                    print(f"ERROR {resp.status_code}, for {f['name']}")
                print(
                    "////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        all_jobz = list_flatter(all_jobz)
        all_jobz = list_flatter(all_jobz)
        return all_jobz


ft = Fetcher()
all_jobz = ft.fetcher(firms)
save_json(all_jobz, "all_jobz", local=True)
all_jobz =  read_json("all_jobz", local=True)
print("len(all_jobz): ",len(all_jobz))
for j in all_jobz:
    pprint(j)
    print("**************************************************************************************************************************")