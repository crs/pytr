from pytr.apiclient import TradeRepublicSession

tr = TradeRepublicSession()

if tr.login("+4917670284554", "1141"):
    code = input()
    tr.complete_login(code)

tr.update_portfolio()
tr.get_positions()
tr.get_info()
