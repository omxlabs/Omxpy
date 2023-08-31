from omxpy.base_client import BaseOmxClient
from cosmpy.aerial.tx_helpers import SubmittedTx
from cosmpy.aerial.wallet import Wallet
from typing import Tuple, TypedDict, Union


QueryResponse_global_short_average_prices = str

Uint128 = str

QueryResponse_global_short_delta__item_0 = bool

QueryResponse_global_short_delta = Tuple[bool, "Uint128"]

QueryResponse_is_global_short_data_ready = bool

QueryResponse_next_global_short_data = Tuple["Uint128", "Uint128"]

QueryResponse_realised_pnl = int

Addr = str

class SetAdminExec(TypedDict):
	admin: "Addr"

SetHandlerExec__is_handler = bool

class SetHandlerExec(TypedDict):
	account: "Addr"
	is_handler: bool

SetIsGlobalShortDataReadyExec__value = bool

class SetIsGlobalShortDataReadyExec(TypedDict):
	value: bool

UpdateGlobalShortDataExec__account = str

UpdateGlobalShortDataExec__collateral_token = str

UpdateGlobalShortDataExec__index_token = str

UpdateGlobalShortDataExec__is_increase = bool

UpdateGlobalShortDataExec__is_long = bool

class UpdateGlobalShortDataExec(TypedDict):
	account: str
	collateral_token: str
	index_token: str
	is_increase: bool
	is_long: bool
	mark_price: "Uint128"
	size_delta: "Uint128"

GlobalShortAveragePricesQuery__token = str

class GlobalShortAveragePricesQuery(TypedDict):
	token: str

GlobalShortDeltaQuery__token = str

class GlobalShortDeltaQuery(TypedDict):
	token: str

class IsGlobalShortDataReadyQuery(TypedDict):
	pass

NextGlobalShortDataQuery__account = str

NextGlobalShortDataQuery__collateral_token = str

NextGlobalShortDataQuery__index_token = str

NextGlobalShortDataQuery__is_increase = bool

class NextGlobalShortDataQuery(TypedDict):
	account: str
	collateral_token: str
	index_token: str
	is_increase: bool
	next_price: "Uint128"
	size_delta: "Uint128"

RealisedPnlQuery__account = str

RealisedPnlQuery__collateral_token = str

RealisedPnlQuery__index_token = str

RealisedPnlQuery__is_increase = bool

class RealisedPnlQuery(TypedDict):
	account: str
	collateral_token: str
	index_token: str
	is_increase: bool
	next_price: "Uint128"
	size_delta: "Uint128"

class ExecuteMsg__set_admin(TypedDict):
	set_admin: "SetAdminExec"

class ExecuteMsg__set_handler(TypedDict):
	set_handler: "SetHandlerExec"

class ExecuteMsg__set_is_global_short_data_ready(TypedDict):
	set_is_global_short_data_ready: "SetIsGlobalShortDataReadyExec"

class ExecuteMsg__update_global_short_data(TypedDict):
	update_global_short_data: "UpdateGlobalShortDataExec"

ExecuteMsg = Union["ExecuteMsg__set_admin", "ExecuteMsg__set_handler", "ExecuteMsg__set_is_global_short_data_ready", "ExecuteMsg__update_global_short_data"]

class QueryMsg__next_global_short_data(TypedDict):
	next_global_short_data: "NextGlobalShortDataQuery"

class QueryMsg__global_short_average_prices(TypedDict):
	global_short_average_prices: "GlobalShortAveragePricesQuery"

class QueryMsg__global_short_delta(TypedDict):
	global_short_delta: "GlobalShortDeltaQuery"

class QueryMsg__is_global_short_data_ready(TypedDict):
	is_global_short_data_ready: "IsGlobalShortDataReadyQuery"

class QueryMsg__realised_pnl(TypedDict):
	realised_pnl: "RealisedPnlQuery"

QueryMsg = Union["QueryMsg__next_global_short_data", "QueryMsg__global_short_average_prices", "QueryMsg__global_short_delta", "QueryMsg__is_global_short_data_ready", "QueryMsg__realised_pnl"]



class OmxCwShortsTracker(BaseOmxClient):
	def clone(self) -> "OmxCwShortsTracker":
		instance = self.__class__.__new__(self.__class__)
		instance.tx = self.tx
		instance.gas = self.gas
		instance.contract = self.contract
		instance.wallet = self.wallet
		instance.funds = self.funds
		return instance

	def with_funds(self, funds: str) -> "OmxCwShortsTracker":
		o = self.clone()
		o.funds = funds
		return o

	def without_funds(self) -> "OmxCwShortsTracker":
		o = self.clone()
		o.funds = None
		return o

	def with_wallet(self, wallet: Wallet) -> "OmxCwShortsTracker":
		o = self.clone()
		o.wallet = wallet
		return o

	def set_admin(self, admin: "Addr") -> SubmittedTx:
		return self.execute({"set_admin": {"admin": admin}})

	def set_handler(self, account: "Addr", is_handler: bool) -> SubmittedTx:
		return self.execute({"set_handler": {"account": account, "is_handler": is_handler}})

	def set_is_global_short_data_ready(self, value: bool) -> SubmittedTx:
		return self.execute({"set_is_global_short_data_ready": {"value": value}})

	def update_global_short_data(self, account: str, collateral_token: str, index_token: str, is_increase: bool, is_long: bool, mark_price: "Uint128", size_delta: "Uint128") -> SubmittedTx:
		return self.execute({"update_global_short_data": {"account": account, "collateral_token": collateral_token, "index_token": index_token, "is_increase": is_increase, "is_long": is_long, "mark_price": mark_price, "size_delta": size_delta}})

	def next_global_short_data(self, account: str, collateral_token: str, index_token: str, is_increase: bool, next_price: "Uint128", size_delta: "Uint128") -> "QueryResponse_next_global_short_data":
		return self.query({"next_global_short_data": {"account": account, "collateral_token": collateral_token, "index_token": index_token, "is_increase": is_increase, "next_price": next_price, "size_delta": size_delta}})

	def global_short_average_prices(self, token: str) -> "QueryResponse_global_short_average_prices":
		return self.query({"global_short_average_prices": {"token": token}})

	def global_short_delta(self, token: str) -> "QueryResponse_global_short_delta":
		return self.query({"global_short_delta": {"token": token}})

	def is_global_short_data_ready(self) -> "QueryResponse_is_global_short_data_ready":
		return self.query({"is_global_short_data_ready": {}})

	def realised_pnl(self, account: str, collateral_token: str, index_token: str, is_increase: bool, next_price: "Uint128", size_delta: "Uint128") -> "QueryResponse_realised_pnl":
		return self.query({"realised_pnl": {"account": account, "collateral_token": collateral_token, "index_token": index_token, "is_increase": is_increase, "next_price": next_price, "size_delta": size_delta}})
