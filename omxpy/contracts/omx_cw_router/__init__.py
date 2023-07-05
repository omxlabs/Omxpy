from omxpy.base_client import BaseOmxClient
from cosmpy.aerial.tx_helpers import SubmittedTx
from cosmpy.aerial.wallet import Wallet
from typing import TypedDict, Tuple, Union


QueryResponse_admin = str

QueryResponse_approved_plugin = bool

QueryResponse_has_plugin = bool

AddPluginExec__plugin = str

class AddPluginExec(TypedDict):
	plugin: str

Addr = str

ApprovePluginExec__plugin = str

class ApprovePluginExec(TypedDict):
	plugin: str

DecreasePositionExec__collateral_token = str

DecreasePositionExec__index_token = str

DecreasePositionExec__is_long = bool

DecreasePositionExec__recipient = str

class DecreasePositionExec(TypedDict):
	collateral_delta: "Uint128"
	collateral_token: str
	index_token: str
	is_long: bool
	price: "Uint128"
	recipient: str
	size_delta: "Uint128"

DecreasePositionInternalExec__is_long = bool

class DecreasePositionInternalExec(TypedDict):
	collateral_delta: "Uint128"
	collateral_token: "Addr"
	index_token: "Addr"
	is_long: bool
	owner: "Addr"
	price: "Uint128"
	recipient: "Addr"
	size_delta: "Uint128"

class DecreasePositionOsmoCbExec(TypedDict):
	balance_before: "Uint128"
	collateral_token: "Addr"
	recipient: "Addr"

DecreasePositionOsmoExec__collateral_token = str

DecreasePositionOsmoExec__index_token = str

DecreasePositionOsmoExec__is_long = bool

DecreasePositionOsmoExec__recipient = str

class DecreasePositionOsmoExec(TypedDict):
	collateral_delta: "Uint128"
	collateral_token: str
	index_token: str
	is_long: bool
	price: "Uint128"
	recipient: str
	size_delta: "Uint128"

DenyPluginExec__plugin = str

class DenyPluginExec(TypedDict):
	plugin: str

DirectPoolDepositExec__amount = Tuple["Uint128"]

DirectPoolDepositExec__token = str

class DirectPoolDepositExec(TypedDict):
	amount: "DirectPoolDepositExec__amount"
	token: str

IncreasePositionExec__index_token = str

IncreasePositionExec__is_long = bool

class IncreasePositionExec(TypedDict):
	amount_in: "Uint128"
	collateral: "PositionCollateral"
	index_token: str
	is_long: bool
	min_out: "Uint128"
	price: "Uint128"
	size_delta: "Uint128"

IncreasePositionIndirectCbExec__balance_before = Tuple["Uint128"]

IncreasePositionIndirectCbExec__is_long = bool

class IncreasePositionIndirectCbExec(TypedDict):
	balance_before: "IncreasePositionIndirectCbExec__balance_before"
	index_token: "Addr"
	is_long: bool
	price: "Uint128"
	size_delta: "Uint128"
	token_out: "Addr"

IncreasePositionInternalExec__is_long = bool

class IncreasePositionInternalExec(TypedDict):
	account: "Addr"
	collateral_token: "Addr"
	index_token: "Addr"
	is_long: bool
	price: "Uint128"
	size_delta: "Uint128"

IncreasePositionOsmoExec__index_token = str

IncreasePositionOsmoExec__is_long = bool

class IncreasePositionOsmoExec(TypedDict):
	collateral: "PositionCollateral"
	index_token: str
	is_long: bool
	min_out: "Uint128"
	price: "Uint128"
	size_delta: "Uint128"

PluginDecreasePositionExec__account = str

PluginDecreasePositionExec__collateral_token = str

PluginDecreasePositionExec__index_token = str

PluginDecreasePositionExec__is_long = bool

PluginDecreasePositionExec__recipient = str

class PluginDecreasePositionExec(TypedDict):
	account: str
	collateral_delta: "Uint128"
	collateral_token: str
	index_token: str
	is_long: bool
	recipient: str
	size_delta: "Uint128"

PluginIncreasePositionExec__account = str

PluginIncreasePositionExec__collateral_token = str

PluginIncreasePositionExec__index_token = str

PluginIncreasePositionExec__is_long = bool

class PluginIncreasePositionExec(TypedDict):
	account: str
	collateral_token: str
	index_token: str
	is_long: bool
	size_delta: "Uint128"

PluginTransferExec__amount = Tuple["Uint128"]

PluginTransferExec__owner = str

PluginTransferExec__recipient = str

PluginTransferExec__token = str

class PluginTransferExec(TypedDict):
	amount: "PluginTransferExec__amount"
	owner: str
	recipient: str
	token: str

PositionCollateral__token__token = str

class PositionCollateral__token(TypedDict):
	token: str

class PositionCollateral__path(TypedDict):
	path: "SwapPath"

PositionCollateral = Union["PositionCollateral__token", "PositionCollateral__path"]

RemovePluginExec__plugin = str

class RemovePluginExec(TypedDict):
	plugin: str

SetAdminExec__new_admin = str

class SetAdminExec(TypedDict):
	new_admin: str

SwapExec__recipient = str

class SwapExec(TypedDict):
	amount_in: "Uint128"
	min_out: "Uint128"
	path: "SwapPath"
	recipient: str

SwapInternalCbExec__intermediate_balance_before = Tuple["Uint128"]

class SwapInternalCbExec(TypedDict):
	intermediate: "Addr"
	intermediate_balance_before: "SwapInternalCbExec__intermediate_balance_before"
	min_out: "Uint128"
	recipient: "Addr"
	token_out: "Addr"

class SwapInternalExec(TypedDict):
	min_out: "Uint128"
	path: "SwapPath"
	recipient: "Addr"

class SwapOsmoToTokensCbExec(TypedDict):
	amount_in: "Uint128"
	balance_before: "Uint128"
	recipient: "Addr"
	token_in: "Addr"
	token_out: "Addr"

SwapOsmoToTokensExec__recipient = str

class SwapOsmoToTokensExec(TypedDict):
	min_out: "Uint128"
	path: "SwapPath"
	recipient: str

SwapPath__direct__direct__token_in = str

SwapPath__direct__direct__token_out = str

class SwapPath__direct__direct(TypedDict):
	token_in: str
	token_out: str

class SwapPath__direct(TypedDict):
	direct: "SwapPath__direct__direct"

SwapPath__indirect__indirect__intermediate = str

SwapPath__indirect__indirect__token_in = str

SwapPath__indirect__indirect__token_out = str

class SwapPath__indirect__indirect(TypedDict):
	intermediate: str
	token_in: str
	token_out: str

class SwapPath__indirect(TypedDict):
	indirect: "SwapPath__indirect__indirect"

SwapPath = Union["SwapPath__direct", "SwapPath__indirect"]

class SwapTokensToOsmoCbExec(TypedDict):
	amount_in: "Uint128"
	balance_before: "Uint128"
	recipient: "Addr"
	token_in: "Addr"
	token_out: "Addr"

SwapTokensToOsmoExec__recipient = str

class SwapTokensToOsmoExec(TypedDict):
	amount_in: "Uint128"
	min_out: "Uint128"
	path: "SwapPath"
	recipient: str

class TransferOsmoToVaultExec(TypedDict):
	pass

class TransferOutOsmoExec(TypedDict):
	amount_out: "Uint128"
	recipient: "Addr"

Uint128 = str

class VaultSwapCbExec(TypedDict):
	balance_before: "Uint128"
	min_out: "Uint128"
	recipient: "Addr"
	token_out: "Addr"

class VaultSwapExec(TypedDict):
	min_out: "Uint128"
	recipient: "Addr"
	token_in: "Addr"
	token_out: "Addr"

AdminQuery = None

ApprovedPluginQuery__account = str

ApprovedPluginQuery__plugin = str

class ApprovedPluginQuery(TypedDict):
	account: str
	plugin: str

HasPluginQuery__plugin = str

class HasPluginQuery(TypedDict):
	plugin: str

class ExecuteMsg__set_admin(TypedDict):
	set_admin: "SetAdminExec"

class ExecuteMsg__decrease_position_osmo_cb(TypedDict):
	decrease_position_osmo_cb: "DecreasePositionOsmoCbExec"

class ExecuteMsg__decrease_position_osmo(TypedDict):
	decrease_position_osmo: "DecreasePositionOsmoExec"

class ExecuteMsg__increase_position_osmo(TypedDict):
	increase_position_osmo: "IncreasePositionOsmoExec"

class ExecuteMsg__increase_position(TypedDict):
	increase_position: "IncreasePositionExec"

class ExecuteMsg__increase_position_indirect_cb(TypedDict):
	increase_position_indirect_cb: "IncreasePositionIndirectCbExec"

class ExecuteMsg__decrease_position(TypedDict):
	decrease_position: "DecreasePositionExec"

class ExecuteMsg__increase_position_internal(TypedDict):
	increase_position_internal: "IncreasePositionInternalExec"

class ExecuteMsg__decrease_position_internal(TypedDict):
	decrease_position_internal: "DecreasePositionInternalExec"

class ExecuteMsg__swap_internal_cb(TypedDict):
	swap_internal_cb: "SwapInternalCbExec"

class ExecuteMsg__swap_tokens_to_osmo(TypedDict):
	swap_tokens_to_osmo: "SwapTokensToOsmoExec"

class ExecuteMsg__swap_tokens_to_osmo_cb(TypedDict):
	swap_tokens_to_osmo_cb: "SwapTokensToOsmoCbExec"

class ExecuteMsg__swap_osmo_to_tokens_cb(TypedDict):
	swap_osmo_to_tokens_cb: "SwapOsmoToTokensCbExec"

class ExecuteMsg__swap_osmo_to_tokens(TypedDict):
	swap_osmo_to_tokens: "SwapOsmoToTokensExec"

class ExecuteMsg__transfer_out_osmo(TypedDict):
	transfer_out_osmo: "TransferOutOsmoExec"

class ExecuteMsg__transfer_osmo_to_vault(TypedDict):
	transfer_osmo_to_vault: "TransferOsmoToVaultExec"

class ExecuteMsg__add_plugin(TypedDict):
	add_plugin: "AddPluginExec"

class ExecuteMsg__swap_internal(TypedDict):
	swap_internal: "SwapInternalExec"

class ExecuteMsg__remove_plugin(TypedDict):
	remove_plugin: "RemovePluginExec"

class ExecuteMsg__approve_plugin(TypedDict):
	approve_plugin: "ApprovePluginExec"

class ExecuteMsg__deny_plugin(TypedDict):
	deny_plugin: "DenyPluginExec"

class ExecuteMsg__plugin_transfer(TypedDict):
	plugin_transfer: "PluginTransferExec"

class ExecuteMsg__plugin_increase_position(TypedDict):
	plugin_increase_position: "PluginIncreasePositionExec"

class ExecuteMsg__plugin_decrease_position(TypedDict):
	plugin_decrease_position: "PluginDecreasePositionExec"

class ExecuteMsg__direct_pool_deposit(TypedDict):
	direct_pool_deposit: "DirectPoolDepositExec"

class ExecuteMsg__vault_swap(TypedDict):
	vault_swap: "VaultSwapExec"

class ExecuteMsg__vault_swap_cb(TypedDict):
	vault_swap_cb: "VaultSwapCbExec"

class ExecuteMsg__swap(TypedDict):
	swap: "SwapExec"

ExecuteMsg = Union["ExecuteMsg__set_admin", "ExecuteMsg__decrease_position_osmo_cb", "ExecuteMsg__decrease_position_osmo", "ExecuteMsg__increase_position_osmo", "ExecuteMsg__increase_position", "ExecuteMsg__increase_position_indirect_cb", "ExecuteMsg__decrease_position", "ExecuteMsg__increase_position_internal", "ExecuteMsg__decrease_position_internal", "ExecuteMsg__swap_internal_cb", "ExecuteMsg__swap_tokens_to_osmo", "ExecuteMsg__swap_tokens_to_osmo_cb", "ExecuteMsg__swap_osmo_to_tokens_cb", "ExecuteMsg__swap_osmo_to_tokens", "ExecuteMsg__transfer_out_osmo", "ExecuteMsg__transfer_osmo_to_vault", "ExecuteMsg__add_plugin", "ExecuteMsg__swap_internal", "ExecuteMsg__remove_plugin", "ExecuteMsg__approve_plugin", "ExecuteMsg__deny_plugin", "ExecuteMsg__plugin_transfer", "ExecuteMsg__plugin_increase_position", "ExecuteMsg__plugin_decrease_position", "ExecuteMsg__direct_pool_deposit", "ExecuteMsg__vault_swap", "ExecuteMsg__vault_swap_cb", "ExecuteMsg__swap"]

class QueryMsg__approved_plugin(TypedDict):
	approved_plugin: "ApprovedPluginQuery"

class QueryMsg__has_plugin(TypedDict):
	has_plugin: "HasPluginQuery"

class QueryMsg__admin(TypedDict):
	admin: "AdminQuery"

QueryMsg = Union["QueryMsg__approved_plugin", "QueryMsg__has_plugin", "QueryMsg__admin"]



class OmxCwRouter(BaseOmxClient):
	def clone(self) -> "OmxCwRouter":
		instance = self.__class__.__new__(self.__class__)
		instance.tx = self.tx
		instance.gas = self.gas
		instance.contract = self.contract
		instance.wallet = self.wallet
		instance.funds = self.funds
		return instance

	def with_funds(self, funds: str) -> "OmxCwRouter":
		o = self.clone()
		o.funds = funds
		return o

	def without_funds(self) -> "OmxCwRouter":
		o = self.clone()
		o.funds = None
		return o

	def with_wallet(self, wallet: Wallet) -> "OmxCwRouter":
		o = self.clone()
		o.wallet = wallet
		return o

	def set_admin(self, new_admin: str) -> SubmittedTx:
		return self.execute({"set_admin": {"new_admin": new_admin}})

	def decrease_position_osmo_cb(self, balance_before: "Uint128", collateral_token: "Addr", recipient: "Addr") -> SubmittedTx:
		return self.execute({"decrease_position_osmo_cb": {"balance_before": balance_before, "collateral_token": collateral_token, "recipient": recipient}})

	def decrease_position_osmo(self, collateral_delta: "Uint128", collateral_token: str, index_token: str, is_long: bool, price: "Uint128", recipient: str, size_delta: "Uint128") -> SubmittedTx:
		return self.execute({"decrease_position_osmo": {"collateral_delta": collateral_delta, "collateral_token": collateral_token, "index_token": index_token, "is_long": is_long, "price": price, "recipient": recipient, "size_delta": size_delta}})

	def increase_position_osmo(self, collateral: "PositionCollateral", index_token: str, is_long: bool, min_out: "Uint128", price: "Uint128", size_delta: "Uint128") -> SubmittedTx:
		return self.execute({"increase_position_osmo": {"collateral": collateral, "index_token": index_token, "is_long": is_long, "min_out": min_out, "price": price, "size_delta": size_delta}})

	def increase_position(self, amount_in: "Uint128", collateral: "PositionCollateral", index_token: str, is_long: bool, min_out: "Uint128", price: "Uint128", size_delta: "Uint128") -> SubmittedTx:
		return self.execute({"increase_position": {"amount_in": amount_in, "collateral": collateral, "index_token": index_token, "is_long": is_long, "min_out": min_out, "price": price, "size_delta": size_delta}})

	def increase_position_indirect_cb(self, balance_before: "IncreasePositionIndirectCbExec__balance_before", index_token: "Addr", is_long: bool, price: "Uint128", size_delta: "Uint128", token_out: "Addr") -> SubmittedTx:
		return self.execute({"increase_position_indirect_cb": {"balance_before": balance_before, "index_token": index_token, "is_long": is_long, "price": price, "size_delta": size_delta, "token_out": token_out}})

	def decrease_position(self, collateral_delta: "Uint128", collateral_token: str, index_token: str, is_long: bool, price: "Uint128", recipient: str, size_delta: "Uint128") -> SubmittedTx:
		return self.execute({"decrease_position": {"collateral_delta": collateral_delta, "collateral_token": collateral_token, "index_token": index_token, "is_long": is_long, "price": price, "recipient": recipient, "size_delta": size_delta}})

	def increase_position_internal(self, account: "Addr", collateral_token: "Addr", index_token: "Addr", is_long: bool, price: "Uint128", size_delta: "Uint128") -> SubmittedTx:
		return self.execute({"increase_position_internal": {"account": account, "collateral_token": collateral_token, "index_token": index_token, "is_long": is_long, "price": price, "size_delta": size_delta}})

	def decrease_position_internal(self, collateral_delta: "Uint128", collateral_token: "Addr", index_token: "Addr", is_long: bool, owner: "Addr", price: "Uint128", recipient: "Addr", size_delta: "Uint128") -> SubmittedTx:
		return self.execute({"decrease_position_internal": {"collateral_delta": collateral_delta, "collateral_token": collateral_token, "index_token": index_token, "is_long": is_long, "owner": owner, "price": price, "recipient": recipient, "size_delta": size_delta}})

	def swap_internal_cb(self, intermediate: "Addr", intermediate_balance_before: "SwapInternalCbExec__intermediate_balance_before", min_out: "Uint128", recipient: "Addr", token_out: "Addr") -> SubmittedTx:
		return self.execute({"swap_internal_cb": {"intermediate": intermediate, "intermediate_balance_before": intermediate_balance_before, "min_out": min_out, "recipient": recipient, "token_out": token_out}})

	def swap_tokens_to_osmo(self, amount_in: "Uint128", min_out: "Uint128", path: "SwapPath", recipient: str) -> SubmittedTx:
		return self.execute({"swap_tokens_to_osmo": {"amount_in": amount_in, "min_out": min_out, "path": path, "recipient": recipient}})

	def swap_tokens_to_osmo_cb(self, amount_in: "Uint128", balance_before: "Uint128", recipient: "Addr", token_in: "Addr", token_out: "Addr") -> SubmittedTx:
		return self.execute({"swap_tokens_to_osmo_cb": {"amount_in": amount_in, "balance_before": balance_before, "recipient": recipient, "token_in": token_in, "token_out": token_out}})

	def swap_osmo_to_tokens_cb(self, amount_in: "Uint128", balance_before: "Uint128", recipient: "Addr", token_in: "Addr", token_out: "Addr") -> SubmittedTx:
		return self.execute({"swap_osmo_to_tokens_cb": {"amount_in": amount_in, "balance_before": balance_before, "recipient": recipient, "token_in": token_in, "token_out": token_out}})

	def swap_osmo_to_tokens(self, min_out: "Uint128", path: "SwapPath", recipient: str) -> SubmittedTx:
		return self.execute({"swap_osmo_to_tokens": {"min_out": min_out, "path": path, "recipient": recipient}})

	def transfer_out_osmo(self, amount_out: "Uint128", recipient: "Addr") -> SubmittedTx:
		return self.execute({"transfer_out_osmo": {"amount_out": amount_out, "recipient": recipient}})

	def transfer_osmo_to_vault(self) -> SubmittedTx:
		return self.execute({"transfer_osmo_to_vault": {}})

	def add_plugin(self, plugin: str) -> SubmittedTx:
		return self.execute({"add_plugin": {"plugin": plugin}})

	def swap_internal(self, min_out: "Uint128", path: "SwapPath", recipient: "Addr") -> SubmittedTx:
		return self.execute({"swap_internal": {"min_out": min_out, "path": path, "recipient": recipient}})

	def remove_plugin(self, plugin: str) -> SubmittedTx:
		return self.execute({"remove_plugin": {"plugin": plugin}})

	def approve_plugin(self, plugin: str) -> SubmittedTx:
		return self.execute({"approve_plugin": {"plugin": plugin}})

	def deny_plugin(self, plugin: str) -> SubmittedTx:
		return self.execute({"deny_plugin": {"plugin": plugin}})

	def plugin_transfer(self, amount: "PluginTransferExec__amount", owner: str, recipient: str, token: str) -> SubmittedTx:
		return self.execute({"plugin_transfer": {"amount": amount, "owner": owner, "recipient": recipient, "token": token}})

	def plugin_increase_position(self, account: str, collateral_token: str, index_token: str, is_long: bool, size_delta: "Uint128") -> SubmittedTx:
		return self.execute({"plugin_increase_position": {"account": account, "collateral_token": collateral_token, "index_token": index_token, "is_long": is_long, "size_delta": size_delta}})

	def plugin_decrease_position(self, account: str, collateral_delta: "Uint128", collateral_token: str, index_token: str, is_long: bool, recipient: str, size_delta: "Uint128") -> SubmittedTx:
		return self.execute({"plugin_decrease_position": {"account": account, "collateral_delta": collateral_delta, "collateral_token": collateral_token, "index_token": index_token, "is_long": is_long, "recipient": recipient, "size_delta": size_delta}})

	def direct_pool_deposit(self, amount: "DirectPoolDepositExec__amount", token: str) -> SubmittedTx:
		return self.execute({"direct_pool_deposit": {"amount": amount, "token": token}})

	def vault_swap(self, min_out: "Uint128", recipient: "Addr", token_in: "Addr", token_out: "Addr") -> SubmittedTx:
		return self.execute({"vault_swap": {"min_out": min_out, "recipient": recipient, "token_in": token_in, "token_out": token_out}})

	def vault_swap_cb(self, balance_before: "Uint128", min_out: "Uint128", recipient: "Addr", token_out: "Addr") -> SubmittedTx:
		return self.execute({"vault_swap_cb": {"balance_before": balance_before, "min_out": min_out, "recipient": recipient, "token_out": token_out}})

	def swap(self, amount_in: "Uint128", min_out: "Uint128", path: "SwapPath", recipient: str) -> SubmittedTx:
		return self.execute({"swap": {"amount_in": amount_in, "min_out": min_out, "path": path, "recipient": recipient}})

	def approved_plugin(self, account: str, plugin: str) -> "QueryResponse_approved_plugin":
		return self.query({"approved_plugin": {"account": account, "plugin": plugin}})

	def has_plugin(self, plugin: str) -> "QueryResponse_has_plugin":
		return self.query({"has_plugin": {"plugin": plugin}})

	def admin(self) -> "QueryResponse_admin":
		return self.query({"admin": {}})
