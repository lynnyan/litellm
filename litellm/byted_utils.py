import json
import os

import requests


class TccApiV2:
    def __init__(self, base_url=None, token=None):
        self.base_url = base_url if base_url else os.getenv(
            "TCC_API_BASE_URL", 'https://tcc-i18n.byted.org')
        self.token = token if token else os.getenv(
            "TCC_API_TOKEN", '4f441f0fa766ca6425bf89772f404f88')

    def get_tcc_conf(self, service_name, key, confspace="default", region="MVAALI"):
        url = "{}/api/v2/open/config/detail?service_name={}&region={}&confspace={}&key={}&token={}".format(
            self.base_url,
            service_name,
            region,
            confspace,
            key,
            self.token
        )
        resp = requests.get(url)
        resp.raise_for_status()
        return resp.json()['data']


if __name__ == '__main__':
    tcc_psm = "tiktok.aiic.nexstone"
    tcc_key = "litellm"
    api = TccApiV2()
    tcc_conf = api.get_tcc_conf(tcc_psm, tcc_key)['online_value']
    print(tcc_conf)
