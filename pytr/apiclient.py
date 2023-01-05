import asyncio
from pytr import account
from pytr.portfolio import Portfolio
from pytr.api import TradeRepublicApi

import pandas as pd


class TradeRepublicSession:
    tr: TradeRepublicApi = None

    positions = None
    info = None

    @property
    def is_logged_in(self):
        return self.tr._weblogin

    def login(self, phone_no, pin):
        self.tr = account.login(phone_no, pin, interactive=False)
        return self.tr._weblogin

    def complete_login(self, code):
        self.tr.complete_weblogin(code)

    def update_portfolio(self):
        if not self.tr.resume_websession():
            raise Exception("Login first")
        p = Portfolio(self.tr)
        asyncio.run(p.portfolio_loop())

        self.positions = p.portfolio.pop("positions")
        self.info = p.portfolio

    def get_positions(self):
        result = pd.DataFrame(self.positions)
        result["initialNetValue"] = result["netSize"] * result["unrealisedAverageCost"]
        result["currentCost"] = result["netValue"] / result["netSize"]
        result["diffCost"] = result["currentCost"] - result["unrealisedAverageCost"]
        result["diffGains"] = result["netValue"] - result["initialNetValue"]
        result = result.sort_values(["netValue"], ascending=False)
        return result

    def get_info(self):
        return self.info
