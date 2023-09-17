import re
from pprint import pprint

import requests as req
from bs4 import BeautifulSoup

from utils.helpers import list_flatter, save_json, read_json

firms = [

    {"symbol": "coinmetrics", "name": "CoinMetrics", "jobs": "https://coinmetrics.io/careers/#open-positions",
     "source": "native"},

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
     "source": "jobs_lever"},
    {"symbol": "polygon", "name": "Polygon", "jobs": "https://jobs.lever.co/Polygon", "source": "jobs_lever"},
    {"symbol": "kraken", "name": "Kraken", "jobs": "https://jobs.lever.co/kraken", "source": "jobs_lever"},
    {"symbol": "atomic", "name": "Atomic", "jobs": "https://jobs.lever.co/atomic", "source": "jobs_lever"},
    {"symbol": "offchainlabs", "name": "OffChain Labs", "jobs": "https://jobs.lever.co/offchainlabs",
     "source": "jobs_lever"},


    {"symbol": "utopia_labs", "name": "Utopia Labs", "jobs": "https://boards.greenhouse.io/utopialabs",
     "source": "greenhouse"},
    {"symbol": "messari", "name": "Messari", "jobs": "https://boards.greenhouse.io/messari", "source": "greenhouse"},
    {"symbol": "nansen", "name": "Nansen", "jobs": "https://boards.greenhouse.io/nansen", "source": "greenhouse"},
    {"symbol": "ox", "name": "0x", "jobs": "https://boards.greenhouse.io/0x", "source": "greenhouse"},
    {"symbol": "magiceden", "name": "MagicEden", "jobs": "https://boards.greenhouse.io/magiceden",
     "source": "greenhouse"},
    {"symbol": "edgeandnode", "name": "Edge & Node", "jobs": "https://boards.greenhouse.io/edgeandnode",
     "source": "greenhouse"},
    {"symbol": "uniswaplabs", "name": "Uniswap", "jobs": "https://boards.greenhouse.io/uniswaplabs",
     "source": "greenhouse"},
    {"symbol": "layerzerolabs", "name": "LayerZero Labs", "jobs": "https://boards.greenhouse.io/layerzerolabs",
     "source": "greenhouse"},
    {"symbol": "alchemy", "name": "Alchemy", "jobs": "https://boards.greenhouse.io/alchemy", "source": "greenhouse"},
    {"symbol": "okx", "name": "OKX", "jobs": "https://boards.greenhouse.io/okx", "source": "greenhouse"},

    {"symbol": "zero_hash", "name": "Zero Hash", "jobs": "https://zero-hash.breezy.hr/", "source": "breezy"},
    {"symbol": "bitwave", "name": "Bitwave", "jobs": "https://bitwave.breezy.hr/", "source": "breezy"},
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
                    all_jobz.append(jobz)
                else:
                    print(f"ERROR {resp.status_code}, for {f['name']}")
                print(
                    "////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        all_jobz = list_flatter(all_jobz)
        all_jobz = list_flatter(all_jobz)
        return all_jobz


# ft = Fetcher()
# all_jobz = ft.fetcher(firms)
# save_json(all_jobz, "all_jobz", local=True)
all_jobz =  read_json("all_jobz", local=True)
print("len(all_jobz): ",len(all_jobz))
for j in all_jobz:
    pprint(j)
    print("******************************************************************************************************************************")