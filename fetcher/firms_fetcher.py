import requests as req
from pprint import pprint


class FirmsFetcher(object):
    @staticmethod
    def get_firms_list_from_alchemy():  # source alchemy dapp store
        url = "https://www.alchemy.com/dapps"
        resp = req.get(url)
        pprint(resp.content)


ff = FirmsFetcher()
ff.get_firms_list_from_alchemy()
