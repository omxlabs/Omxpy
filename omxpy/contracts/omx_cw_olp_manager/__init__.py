from omxpy.base_client import BaseOmxClient
from cosmpy.aerial.tx_helpers import SubmittedTx
from cosmpy.aerial.wallet import Wallet
from typing import Tuple, TypedDict, Union


Uint64 = str

QueryResponse_add_cd_end = Tuple["Uint64"]

QueryResponse_aum = str

QueryResponse_aum_in_usdo = str

QueryResponse_cd_duration = int

QueryResponse_global_short_average_price = str

Uint128 = str

QueryResponse_global_short_delta__item_1 = bool

QueryResponse_global_short_delta = Tuple["Uint128", bool]

QueryResponse_last_added_at = Tuple["Uint64"]

AddLiquidityCb__token = str

class AddLiquidityCb(TypedDict):
	account: "Addr"
	amount: "Uint128"
	aum_in_usdo: "Uint128"
	balance_before: "Uint128"
	min_olp: "Uint128"
	min_usdo: "Uint128"
	olp_supply: "Uint128"
	token: str

AddLiquidityExec__token = str

class AddLiquidityExec(TypedDict):
	amount: "Uint128"
	min_olp: "Uint128"
	min_usdo: "Uint128"
	token: str

AddLiquidityForAccountExec__account = str

AddLiquidityForAccountExec__funding_account = str

AddLiquidityForAccountExec__token = str

class AddLiquidityForAccountExec(TypedDict):
	account: str
	amount: "Uint128"
	funding_account: str
	min_olp: "Uint128"
	min_usdo: "Uint128"
	token: str

Addr = str

RemoveLiquidityCb__account = str

RemoveLiquidityCb__receiver = str

RemoveLiquidityCb__token_out = str

class RemoveLiquidityCb(TypedDict):
	account: str
	aum_in_usdo: "Uint128"
	balance_before: "Uint128"
	min_out: "Uint128"
	olp_amount: "Uint128"
	olp_supply: "Uint128"
	receiver: str
	token_out: str

RemoveLiquidityExec__receiver = str

RemoveLiquidityExec__token_out = str

class RemoveLiquidityExec(TypedDict):
	min_out: "Uint128"
	olp_amount: "Uint128"
	receiver: str
	token_out: str

RemoveLiquidityForAccountExec__account = str

RemoveLiquidityForAccountExec__recipient = str

RemoveLiquidityForAccountExec__token_out = str

class RemoveLiquidityForAccountExec(TypedDict):
	account: str
	min_out: "Uint128"
	olp_amount: "Uint128"
	recipient: str
	token_out: str

SetAdminExec__admin = str

class SetAdminExec(TypedDict):
	admin: str

class SetAumAdjustmentExec(TypedDict):
	aum_addition: "Uint128"
	aum_deduction: "Uint128"

class SetAveragePriceWeightExec(TypedDict):
	value: "Uint128"

SetCooldownDurationExec__value = int

class SetCooldownDurationExec(TypedDict):
	value: int

SetHandlerExec__account = str

SetHandlerExec__is_handler = bool

class SetHandlerExec(TypedDict):
	account: str
	is_handler: bool

SetPrivateModeExec__in_private_mode = bool

class SetPrivateModeExec(TypedDict):
	in_private_mode: bool

SetShortsTrackerExec__shorts_tracker = str

class SetShortsTrackerExec(TypedDict):
	shorts_tracker: str

AddCdEndQuery__account = str

class AddCdEndQuery(TypedDict):
	account: str

AumInUsdoQuery__maximize = bool

class AumInUsdoQuery(TypedDict):
	maximize: bool

AumQuery__maximize = bool

class AumQuery(TypedDict):
	maximize: bool

class CdDurationQuery(TypedDict):
	pass

GlobalShortAveragePriceQuery__token = str

class GlobalShortAveragePriceQuery(TypedDict):
	token: str

GlobalShortDeltaQuery__token = str

class GlobalShortDeltaQuery(TypedDict):
	price: "Uint128"
	size: "Uint128"
	token: str

LastAddedAtQuery__account = str

class LastAddedAtQuery(TypedDict):
	account: str

class ExecuteMsg__set_admin(TypedDict):
	set_admin: "SetAdminExec"

class ExecuteMsg__set_private_mode(TypedDict):
	set_private_mode: "SetPrivateModeExec"

class ExecuteMsg__set_shorts_tracker(TypedDict):
	set_shorts_tracker: "SetShortsTrackerExec"

class ExecuteMsg__set_average_price_weight(TypedDict):
	set_average_price_weight: "SetAveragePriceWeightExec"

class ExecuteMsg__set_handler(TypedDict):
	set_handler: "SetHandlerExec"

class ExecuteMsg__set_cooldown_duration(TypedDict):
	set_cooldown_duration: "SetCooldownDurationExec"

class ExecuteMsg__set_aum_adjustment(TypedDict):
	set_aum_adjustment: "SetAumAdjustmentExec"

class ExecuteMsg__remove_liquidity_cb(TypedDict):
	remove_liquidity_cb: "RemoveLiquidityCb"

class ExecuteMsg__remove_liquidity(TypedDict):
	remove_liquidity: "RemoveLiquidityExec"

class ExecuteMsg__remove_liquidity_for_account(TypedDict):
	remove_liquidity_for_account: "RemoveLiquidityForAccountExec"

class ExecuteMsg__add_liquidity_cb(TypedDict):
	add_liquidity_cb: "AddLiquidityCb"

class ExecuteMsg__add_liquidity(TypedDict):
	add_liquidity: "AddLiquidityExec"

class ExecuteMsg__add_liquidity_for_account(TypedDict):
	add_liquidity_for_account: "AddLiquidityForAccountExec"

ExecuteMsg = Union["ExecuteMsg__set_admin", "ExecuteMsg__set_private_mode", "ExecuteMsg__set_shorts_tracker", "ExecuteMsg__set_average_price_weight", "ExecuteMsg__set_handler", "ExecuteMsg__set_cooldown_duration", "ExecuteMsg__set_aum_adjustment", "ExecuteMsg__remove_liquidity_cb", "ExecuteMsg__remove_liquidity", "ExecuteMsg__remove_liquidity_for_account", "ExecuteMsg__add_liquidity_cb", "ExecuteMsg__add_liquidity", "ExecuteMsg__add_liquidity_for_account"]

class QueryMsg__global_short_delta(TypedDict):
	global_short_delta: "GlobalShortDeltaQuery"

class QueryMsg__global_short_average_price(TypedDict):
	global_short_average_price: "GlobalShortAveragePriceQuery"

class QueryMsg__aum_in_usdo(TypedDict):
	aum_in_usdo: "AumInUsdoQuery"

class QueryMsg__aum(TypedDict):
	aum: "AumQuery"

class QueryMsg__add_cd_end(TypedDict):
	add_cd_end: "AddCdEndQuery"

class QueryMsg__last_added_at(TypedDict):
	last_added_at: "LastAddedAtQuery"

class QueryMsg__cd_duration(TypedDict):
	cd_duration: "CdDurationQuery"

QueryMsg = Union["QueryMsg__global_short_delta", "QueryMsg__global_short_average_price", "QueryMsg__aum_in_usdo", "QueryMsg__aum", "QueryMsg__add_cd_end", "QueryMsg__last_added_at", "QueryMsg__cd_duration"]



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

	def set_admin(self, admin: str) -> SubmittedTx:
		return self.execute({"set_admin": {"admin": admin}})

	def set_private_mode(self, in_private_mode: bool) -> SubmittedTx:
		return self.execute({"set_private_mode": {"in_private_mode": in_private_mode}})

	def set_shorts_tracker(self, shorts_tracker: str) -> SubmittedTx:
		return self.execute({"set_shorts_tracker": {"shorts_tracker": shorts_tracker}})

	def set_average_price_weight(self, value: "Uint128") -> SubmittedTx:
		return self.execute({"set_average_price_weight": {"value": value}})

	def set_handler(self, account: str, is_handler: bool) -> SubmittedTx:
		return self.execute({"set_handler": {"account": account, "is_handler": is_handler}})

	def set_cooldown_duration(self, value: int) -> SubmittedTx:
		return self.execute({"set_cooldown_duration": {"value": value}})

	def set_aum_adjustment(self, aum_addition: "Uint128", aum_deduction: "Uint128") -> SubmittedTx:
		return self.execute({"set_aum_adjustment": {"aum_addition": aum_addition, "aum_deduction": aum_deduction}})

	def remove_liquidity_cb(self, account: str, aum_in_usdo: "Uint128", balance_before: "Uint128", min_out: "Uint128", olp_amount: "Uint128", olp_supply: "Uint128", receiver: str, token_out: str) -> SubmittedTx:
		return self.execute({"remove_liquidity_cb": {"account": account, "aum_in_usdo": aum_in_usdo, "balance_before": balance_before, "min_out": min_out, "olp_amount": olp_amount, "olp_supply": olp_supply, "receiver": receiver, "token_out": token_out}})

	def remove_liquidity(self, min_out: "Uint128", olp_amount: "Uint128", receiver: str, token_out: str) -> SubmittedTx:
		return self.execute({"remove_liquidity": {"min_out": min_out, "olp_amount": olp_amount, "receiver": receiver, "token_out": token_out}})

	def remove_liquidity_for_account(self, account: str, min_out: "Uint128", olp_amount: "Uint128", recipient: str, token_out: str) -> SubmittedTx:
		return self.execute({"remove_liquidity_for_account": {"account": account, "min_out": min_out, "olp_amount": olp_amount, "recipient": recipient, "token_out": token_out}})

	def add_liquidity_cb(self, account: "Addr", amount: "Uint128", aum_in_usdo: "Uint128", balance_before: "Uint128", min_olp: "Uint128", min_usdo: "Uint128", olp_supply: "Uint128", token: str) -> SubmittedTx:
		return self.execute({"add_liquidity_cb": {"account": account, "amount": amount, "aum_in_usdo": aum_in_usdo, "balance_before": balance_before, "min_olp": min_olp, "min_usdo": min_usdo, "olp_supply": olp_supply, "token": token}})

	def add_liquidity(self, amount: "Uint128", min_olp: "Uint128", min_usdo: "Uint128", token: str) -> SubmittedTx:
		return self.execute({"add_liquidity": {"amount": amount, "min_olp": min_olp, "min_usdo": min_usdo, "token": token}})

	def add_liquidity_for_account(self, account: str, amount: "Uint128", funding_account: str, min_olp: "Uint128", min_usdo: "Uint128", token: str) -> SubmittedTx:
		return self.execute({"add_liquidity_for_account": {"account": account, "amount": amount, "funding_account": funding_account, "min_olp": min_olp, "min_usdo": min_usdo, "token": token}})

	def global_short_delta(self, price: "Uint128", size: "Uint128", token: str) -> "QueryResponse_global_short_delta":
		return self.query({"global_short_delta": {"price": price, "size": size, "token": token}})

	def global_short_average_price(self, token: str) -> "QueryResponse_global_short_average_price":
		return self.query({"global_short_average_price": {"token": token}})

	def aum_in_usdo(self, maximize: bool) -> "QueryResponse_aum_in_usdo":
		return self.query({"aum_in_usdo": {"maximize": maximize}})

	def aum(self, maximize: bool) -> "QueryResponse_aum":
		return self.query({"aum": {"maximize": maximize}})

	def add_cd_end(self, account: str) -> "QueryResponse_add_cd_end":
		return self.query({"add_cd_end": {"account": account}})

	def last_added_at(self, account: str) -> "QueryResponse_last_added_at":
		return self.query({"last_added_at": {"account": account}})

	def cd_duration(self) -> "QueryResponse_cd_duration":
		return self.query({"cd_duration": {}})
