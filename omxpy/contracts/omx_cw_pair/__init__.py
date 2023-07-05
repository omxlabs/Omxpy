from omxpy.base_client import BaseOmxClient
from cosmpy.aerial.tx_helpers import SubmittedTx
from cosmpy.aerial.wallet import Wallet
from typing import Tuple, TypedDict


Uint128 = str

QueryResponse_reserves = Tuple["Uint128", "Uint128"]

class ExecuteMsg__set_reserves__set_reserves(TypedDict):
	reserves0: "Uint128"
	reserves1: "Uint128"

class ExecuteMsg__set_reserves(TypedDict):
	set_reserves: "ExecuteMsg__set_reserves__set_reserves"

ExecuteMsg = "ExecuteMsg__set_reserves"

class QueryMsg__reserves__reserves(TypedDict):
	pass

class QueryMsg__reserves(TypedDict):
	reserves: "QueryMsg__reserves__reserves"

QueryMsg = "QueryMsg__reserves"



class OmxCwPair(BaseOmxClient):
	def clone(self) -> "OmxCwPair":
		instance = self.__class__.__new__(self.__class__)
		instance.tx = self.tx
		instance.gas = self.gas
		instance.contract = self.contract
		instance.wallet = self.wallet
		instance.funds = self.funds
		return instance

	def with_funds(self, funds: str) -> "OmxCwPair":
		o = self.clone()
		o.funds = funds
		return o

	def without_funds(self) -> "OmxCwPair":
		o = self.clone()
		o.funds = None
		return o

	def with_wallet(self, wallet: Wallet) -> "OmxCwPair":
		o = self.clone()
		o.wallet = wallet
		return o

	def set_reserves(self, reserves0: "Uint128", reserves1: "Uint128") -> SubmittedTx:
		return self.execute({"set_reserves": {"reserves0": reserves0, "reserves1": reserves1}})

	def reserves(self) -> "QueryResponse_reserves":
		return self.query({"reserves": {}})
