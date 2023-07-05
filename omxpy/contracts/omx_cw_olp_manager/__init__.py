from omxpy.base_client import BaseOmxClient
from cosmpy.aerial.tx_helpers import SubmittedTx
from cosmpy.aerial.wallet import Wallet
from typing import TypedDict


QueryResponse_price = str

Addr = str

class SetAdminExec(TypedDict):
	admin: "Addr"

class PriceQuery(TypedDict):
	pass

class ExecuteMsg__set_admin(TypedDict):
	set_admin: "SetAdminExec"

ExecuteMsg = "ExecuteMsg__set_admin"

class QueryMsg__price(TypedDict):
	price: "PriceQuery"

QueryMsg = "QueryMsg__price"



class OmxCwOlpManager(BaseOmxClient):
	def clone(self) -> "OmxCwOlpManager":
		instance = self.__class__.__new__(self.__class__)
		instance.tx = self.tx
		instance.gas = self.gas
		instance.contract = self.contract
		instance.wallet = self.wallet
		instance.funds = self.funds
		return instance

	def with_funds(self, funds: str) -> "OmxCwOlpManager":
		o = self.clone()
		o.funds = funds
		return o

	def without_funds(self) -> "OmxCwOlpManager":
		o = self.clone()
		o.funds = None
		return o

	def with_wallet(self, wallet: Wallet) -> "OmxCwOlpManager":
		o = self.clone()
		o.wallet = wallet
		return o

	def set_admin(self, admin: "Addr") -> SubmittedTx:
		return self.execute({"set_admin": {"admin": admin}})

	def price(self) -> "QueryResponse_price":
		return self.query({"price": {}})
