from omxpy.base_client import BaseOmxClient
from cosmpy.aerial.tx_helpers import SubmittedTx
from cosmpy.aerial.wallet import Wallet
from typing import TypedDict, Union


QueryResponse_price = str

Identifier = str

SetAdminExec__admin = str

class SetAdminExec(TypedDict):
	admin: str

SetMaxPriceAgeExec__value = int

class SetMaxPriceAgeExec(TypedDict):
	value: int

SetPriceFeedExec__address = str

class SetPriceFeedExec(TypedDict):
	address: str

SetTokenConfigExec__is_strict_stable = bool

SetTokenConfigExec__token = str

class SetTokenConfigExec(TypedDict):
	is_strict_stable: bool
	price_feed: "Identifier"
	token: str

PriceQuery__include_amm_price = bool

PriceQuery__maximize = bool

PriceQuery__token = str

class PriceQuery(TypedDict):
	include_amm_price: bool
	maximize: bool
	token: str

class ExecuteMsg__set_admin(TypedDict):
	set_admin: "SetAdminExec"

class ExecuteMsg__set_token_config(TypedDict):
	set_token_config: "SetTokenConfigExec"

class ExecuteMsg__set_price_feed(TypedDict):
	set_price_feed: "SetPriceFeedExec"

class ExecuteMsg__set_max_price_age(TypedDict):
	set_max_price_age: "SetMaxPriceAgeExec"

ExecuteMsg = Union["ExecuteMsg__set_admin", "ExecuteMsg__set_token_config", "ExecuteMsg__set_price_feed", "ExecuteMsg__set_max_price_age"]

class QueryMsg__price(TypedDict):
	price: "PriceQuery"

QueryMsg = "QueryMsg__price"



class OmxCwVaultPriceFeed(BaseOmxClient):
	def clone(self) -> "OmxCwVaultPriceFeed":
		instance = self.__class__.__new__(self.__class__)
		instance.tx = self.tx
		instance.gas = self.gas
		instance.contract = self.contract
		instance.wallet = self.wallet
		instance.funds = self.funds
		return instance

	def with_funds(self, funds: str) -> "OmxCwVaultPriceFeed":
		o = self.clone()
		o.funds = funds
		return o

	def without_funds(self) -> "OmxCwVaultPriceFeed":
		o = self.clone()
		o.funds = None
		return o

	def with_wallet(self, wallet: Wallet) -> "OmxCwVaultPriceFeed":
		o = self.clone()
		o.wallet = wallet
		return o

	def set_admin(self, admin: str) -> SubmittedTx:
		return self.execute({"set_admin": {"admin": admin}})

	def set_token_config(self, is_strict_stable: bool, price_feed: "Identifier", token: str) -> SubmittedTx:
		return self.execute({"set_token_config": {"is_strict_stable": is_strict_stable, "price_feed": price_feed, "token": token}})

	def set_price_feed(self, address: str) -> SubmittedTx:
		return self.execute({"set_price_feed": {"address": address}})

	def set_max_price_age(self, value: int) -> SubmittedTx:
		return self.execute({"set_max_price_age": {"value": value}})

	def price(self, include_amm_price: bool, maximize: bool, token: str) -> "QueryResponse_price":
		return self.query({"price": {"include_amm_price": include_amm_price, "maximize": maximize, "token": token}})
