from omxpy.base_client import BaseOmxClient
from cosmpy.aerial.tx_helpers import SubmittedTx
from cosmpy.aerial.wallet import Wallet
from typing import TypedDict, Union, Tuple


Addr = str

Uint128 = str

QueryResponse_decrease_order__is_long = bool

QueryResponse_decrease_order__trigger_above_threshold = bool

class QueryResponse_decrease_order(TypedDict):
	account: "Addr"
	collateral_delta: "Uint128"
	collateral_token: "Addr"
	execution_fee: "Uint128"
	index: "Uint128"
	index_token: "Addr"
	is_long: bool
	size_delta: "Uint128"
	trigger_above_threshold: bool
	trigger_price: "Uint128"

QueryResponse_increase_order__is_long = bool

QueryResponse_increase_order__trigger_above_threshold = bool

class QueryResponse_increase_order(TypedDict):
	account: "Addr"
	collateral_token: "Addr"
	execution_fee: "Uint128"
	index: "Uint128"
	index_token: "Addr"
	is_long: bool
	purchase_token: "Addr"
	purchase_token_amount: "Uint128"
	size_delta: "Uint128"
	trigger_above_threshold: bool
	trigger_price: "Uint128"

DecreaseOrder__is_long = bool

DecreaseOrder__trigger_above_threshold = bool

class DecreaseOrder(TypedDict):
	account: "Addr"
	collateral_delta: "Uint128"
	collateral_token: "Addr"
	execution_fee: "Uint128"
	index: "Uint128"
	index_token: "Addr"
	is_long: bool
	size_delta: "Uint128"
	trigger_above_threshold: bool
	trigger_price: "Uint128"

IncreaseOrder__is_long = bool

IncreaseOrder__trigger_above_threshold = bool

class IncreaseOrder(TypedDict):
	account: "Addr"
	collateral_token: "Addr"
	execution_fee: "Uint128"
	index: "Uint128"
	index_token: "Addr"
	is_long: bool
	purchase_token: "Addr"
	purchase_token_amount: "Uint128"
	size_delta: "Uint128"
	trigger_above_threshold: bool
	trigger_price: "Uint128"

SwapOrder__should_unwrap = bool

SwapOrder__trigger_above_threshold = bool

class SwapOrder(TypedDict):
	account: "Addr"
	amount_in: "Uint128"
	execution_fee: "Uint128"
	index: "Uint128"
	min_out: "Uint128"
	path: "ValidatedSwapPath"
	should_unwrap: bool
	trigger_above_threshold: bool
	trigger_ratio: "Uint128"

class ValidatedSwapPath__direct__direct(TypedDict):
	token_in: "Addr"
	token_out: "Addr"

class ValidatedSwapPath__direct(TypedDict):
	direct: "ValidatedSwapPath__direct__direct"

class ValidatedSwapPath__indirect__indirect(TypedDict):
	intermediate: "Addr"
	token_in: "Addr"
	token_out: "Addr"

class ValidatedSwapPath__indirect(TypedDict):
	indirect: "ValidatedSwapPath__indirect__indirect"

ValidatedSwapPath = Union["ValidatedSwapPath__direct", "ValidatedSwapPath__indirect"]

class QueryResponse_orders__swap(TypedDict):
	swap: "SwapOrder"

class QueryResponse_orders__increase(TypedDict):
	increase: "IncreaseOrder"

class QueryResponse_orders__decrease(TypedDict):
	decrease: "DecreaseOrder"

QueryResponse_orders = Union["QueryResponse_orders__swap", "QueryResponse_orders__increase", "QueryResponse_orders__decrease"]

QueryResponse_swap_order = str

QueryResponse_usdo_min_price = str

QueryResponse_validate_position_order_price__item_1 = bool

QueryResponse_validate_position_order_price = Tuple["Uint128", bool]

QueryResponse_validate_swap_order_price = bool

class CancelDecreaseOrderExec(TypedDict):
	order_index: "Uint128"

class CancelIncreaseOrderExec(TypedDict):
	order_index: "Uint128"

class CancelSwapOrderExec(TypedDict):
	order_index: "Uint128"

CreateDecreaseOrderExec__collateral_token = str

CreateDecreaseOrderExec__index_token = str

CreateDecreaseOrderExec__is_long = bool

CreateDecreaseOrderExec__trigger_above_threshold = bool

class CreateDecreaseOrderExec(TypedDict):
	collateral_delta: "Uint128"
	collateral_token: str
	index_token: str
	is_long: bool
	size_delta: "Uint128"
	trigger_above_threshold: bool
	trigger_price: "Uint128"

CreateDecreaseOrderInternalExec__is_long = bool

CreateDecreaseOrderInternalExec__trigger_above_threshold = bool

class CreateDecreaseOrderInternalExec(TypedDict):
	account: "Addr"
	collateral_delta: "Uint128"
	collateral_token: "Addr"
	execution_fee: "Uint128"
	index_token: "Addr"
	is_long: bool
	size_delta: "Uint128"
	trigger_above_threshold: bool
	trigger_price: "Uint128"

CreateIncreaseOrderCbExec__is_long = bool

CreateIncreaseOrderCbExec__should_wrap = bool

CreateIncreaseOrderCbExec__trigger_above_threshold = bool

class CreateIncreaseOrderCbExec(TypedDict):
	amount_in: "Uint128"
	collateral_token: "Addr"
	execution_fee: "Uint128"
	index_token: "Addr"
	is_long: bool
	min_out: "Uint128"
	path: "PositionCollateral"
	purchase_token: "Addr"
	purchase_token_amount: "PurchaseTokenAmount"
	sender: "Addr"
	should_wrap: bool
	size_delta: "Uint128"
	trigger_above_threshold: bool
	trigger_price: "Uint128"

CreateIncreaseOrderExec__collateral_token = str

CreateIncreaseOrderExec__index_token = str

CreateIncreaseOrderExec__is_long = bool

CreateIncreaseOrderExec__should_wrap = bool

CreateIncreaseOrderExec__trigger_above_threshold = bool

class CreateIncreaseOrderExec(TypedDict):
	amount_in: "Uint128"
	collateral_token: str
	execution_fee: "Uint128"
	index_token: str
	is_long: bool
	min_out: "Uint128"
	path: "PositionCollateral"
	should_wrap: bool
	size_delta: "Uint128"
	trigger_above_threshold: bool
	trigger_price: "Uint128"

CreateIncreaseOrderInternalExec__is_long = bool

CreateIncreaseOrderInternalExec__trigger_above_threshold = bool

class CreateIncreaseOrderInternalExec(TypedDict):
	account: "Addr"
	collateral_token: "Addr"
	execution_fee: "Uint128"
	index_token: "Addr"
	is_long: bool
	purchase_token: "Addr"
	purchase_token_amount: "Uint128"
	sender: "Addr"
	size_delta: "Uint128"
	trigger_above_threshold: bool
	trigger_price: "Uint128"

CreateIncreaseOrderSwapCbExec__is_long = bool

CreateIncreaseOrderSwapCbExec__should_wrap = bool

CreateIncreaseOrderSwapCbExec__trigger_above_threshold = bool

class CreateIncreaseOrderSwapCbExec(TypedDict):
	amount_in: "Uint128"
	collateral_token: "Addr"
	execution_fee: "Uint128"
	index_token: "Addr"
	is_long: bool
	min_out: "Uint128"
	path: "SwapPath"
	purchase_token: "Addr"
	sender: "Addr"
	should_wrap: bool
	size_delta: "Uint128"
	trigger_above_threshold: bool
	trigger_price: "Uint128"

CreateSwapOrderExec__should_unwrap = bool

CreateSwapOrderExec__should_wrap = bool

CreateSwapOrderExec__trigger_above_threshold = bool

class CreateSwapOrderExec(TypedDict):
	amount_in: "Uint128"
	execution_fee: "Uint128"
	min_out: "Uint128"
	path: "SwapPath"
	should_unwrap: bool
	should_wrap: bool
	trigger_above_threshold: bool
	trigger_ratio: "Uint128"

CreateSwapOrderInternalExec__should_unwrap = bool

CreateSwapOrderInternalExec__trigger_above_threshold = bool

class CreateSwapOrderInternalExec(TypedDict):
	account: "Addr"
	amount_in: "Uint128"
	execution_fee: "Uint128"
	min_out: "Uint128"
	native_amount_in: "Uint128"
	path: "ValidatedSwapPath"
	should_unwrap: bool
	trigger_above_threshold: bool
	trigger_ratio: "Uint128"

class ExecuteDecreaseOrderCbExec(TypedDict):
	balance_before: "Uint128"
	current_price: "Uint128"
	fee_receiver: "Addr"
	order: "DecreaseOrder"
	order_index: "Uint128"

ExecuteDecreaseOrderExec__address = str

ExecuteDecreaseOrderExec__fee_receiver = str

class ExecuteDecreaseOrderExec(TypedDict):
	address: str
	fee_receiver: str
	order_index: "Uint128"

class ExecuteIncreaseOrderCbExec(TypedDict):
	balance_before: "Uint128"
	current_price: "Uint128"
	fee_recipient: "Addr"
	order: "IncreaseOrder"
	order_index: "Uint128"

ExecuteIncreaseOrderExec__account = str

ExecuteIncreaseOrderExec__fee_recipient = str

class ExecuteIncreaseOrderExec(TypedDict):
	account: str
	fee_recipient: str
	order_index: "Uint128"

ExecuteSwapOrderCbExec__should_unwrap = bool

class ExecuteSwapOrderCbExec(TypedDict):
	balance_before: "Uint128"
	fee_recipient: "Addr"
	order: "SwapOrder"
	order_index: "Uint128"
	should_unwrap: bool

ExecuteSwapOrderExec__account = str

ExecuteSwapOrderExec__fee_recipient = str

class ExecuteSwapOrderExec(TypedDict):
	account: str
	fee_recipient: str
	order_index: "Uint128"

PositionCollateral__token__token = str

class PositionCollateral__token(TypedDict):
	token: str

class PositionCollateral__path(TypedDict):
	path: "SwapPath"

PositionCollateral = Union["PositionCollateral__token", "PositionCollateral__path"]

class PurchaseTokenAmount__amount(TypedDict):
	amount: "Uint128"

class PurchaseTokenAmount__amount_before(TypedDict):
	amount_before: "Uint128"

PurchaseTokenAmount = Union["PurchaseTokenAmount__amount", "PurchaseTokenAmount__amount_before"]

SetAdminExec__admin = str

class SetAdminExec(TypedDict):
	admin: str

class SetMinExecutionFeeExec(TypedDict):
	value: "Uint128"

class SetMinPurchaseTokenAmountUsdExec(TypedDict):
	value: "Uint128"

class SwapInternalCbExec(TypedDict):
	intermediate_balance_before: "Uint128"
	intermediate_token: "Addr"
	min_out: "Uint128"
	recipient: "Addr"
	token_out: "Addr"

class SwapInternalExec(TypedDict):
	min_out: "Uint128"
	path: "SwapPath"
	recipient: "Addr"

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

class TransferInOsmoInternalExec(TypedDict):
	pass

class TransferOutOsmoInternalExec(TypedDict):
	amount_out: "Uint128"
	recipient: "Addr"

UpdateDecreaseOrderExec__trigger_above_threshold = bool

class UpdateDecreaseOrderExec(TypedDict):
	collateral_delta: "Uint128"
	order_index: "Uint128"
	size_delta: "Uint128"
	trigger_above_threshold: bool
	trigger_price: "Uint128"

UpdateIncreaseOrderExec__trigger_above_threshold = bool

class UpdateIncreaseOrderExec(TypedDict):
	order_index: "Uint128"
	size_delta: "Uint128"
	trigger_above_threshold: bool
	trigger_price: "Uint128"

UpdateSwapOrderExec__trigger_above_threshold = bool

class UpdateSwapOrderExec(TypedDict):
	min_out: "Uint128"
	order_index: "Uint128"
	trigger_above_threshold: bool
	trigger_ratio: "Uint128"

class VaultSwapInternalExec__swap__swap(TypedDict):
	min_out: "Uint128"
	recipient: "Addr"
	token_in: "Addr"
	token_out: "Addr"

class VaultSwapInternalExec__swap(TypedDict):
	swap: "VaultSwapInternalExec__swap__swap"

class VaultSwapInternalExec__post_swap__post_swap(TypedDict):
	amount_out_before: "Uint128"
	min_out: "Uint128"
	recipient: "Addr"
	token_out: "Addr"

class VaultSwapInternalExec__post_swap(TypedDict):
	post_swap: "VaultSwapInternalExec__post_swap__post_swap"

VaultSwapInternalExec = Union["VaultSwapInternalExec__swap", "VaultSwapInternalExec__post_swap"]

DecreaseOrderQuery__account = str

class DecreaseOrderQuery(TypedDict):
	account: str
	order_index: "Uint128"

IncreaseOrderQuery__account = str

class IncreaseOrderQuery(TypedDict):
	account: str
	order_index: "Uint128"

OrdersQuery__ready = bool

class OrdersQuery(TypedDict):
	ready: bool

SwapOrderQuery__account = str

class SwapOrderQuery(TypedDict):
	account: str
	order_index: "Uint128"

UsdoMinPriceQuery__other_token = str

class UsdoMinPriceQuery(TypedDict):
	other_token: str

ValidatePositionOrderPriceQuery__index_token = str

ValidatePositionOrderPriceQuery__maximize_price = bool

ValidatePositionOrderPriceQuery__should_raise = bool

ValidatePositionOrderPriceQuery__trigger_above_threshold = bool

class ValidatePositionOrderPriceQuery(TypedDict):
	index_token: str
	maximize_price: bool
	should_raise: bool
	trigger_above_threshold: bool
	trigger_price: "Uint128"

class ValidateSwapOrderPriceQuery(TypedDict):
	path: "SwapPath"
	trigger_ratio: "Uint128"

class ExecuteMsg__set_admin(TypedDict):
	set_admin: "SetAdminExec"

class ExecuteMsg__set_min_execution_fee(TypedDict):
	set_min_execution_fee: "SetMinExecutionFeeExec"

class ExecuteMsg__set_min_purchase_token_amount_usd(TypedDict):
	set_min_purchase_token_amount_usd: "SetMinPurchaseTokenAmountUsdExec"

class ExecuteMsg__cancel_decrease_order(TypedDict):
	cancel_decrease_order: "CancelDecreaseOrderExec"

class ExecuteMsg__cancel_increase_order(TypedDict):
	cancel_increase_order: "CancelIncreaseOrderExec"

class ExecuteMsg__cancel_swap_order(TypedDict):
	cancel_swap_order: "CancelSwapOrderExec"

class ExecuteMsg__create_decrease_order_internal(TypedDict):
	create_decrease_order_internal: "CreateDecreaseOrderInternalExec"

class ExecuteMsg__create_decrease_order(TypedDict):
	create_decrease_order: "CreateDecreaseOrderExec"

class ExecuteMsg__create_increase_order_internal(TypedDict):
	create_increase_order_internal: "CreateIncreaseOrderInternalExec"

class ExecuteMsg__create_increase_order(TypedDict):
	create_increase_order: "CreateIncreaseOrderExec"

class ExecuteMsg__create_swap_order(TypedDict):
	create_swap_order: "CreateSwapOrderExec"

class ExecuteMsg__create_swap_order_internal(TypedDict):
	create_swap_order_internal: "CreateSwapOrderInternalExec"

class ExecuteMsg__execute_decrease_order(TypedDict):
	execute_decrease_order: "ExecuteDecreaseOrderExec"

class ExecuteMsg__execute_decrease_order_cb(TypedDict):
	execute_decrease_order_cb: "ExecuteDecreaseOrderCbExec"

class ExecuteMsg__execute_increase_order(TypedDict):
	execute_increase_order: "ExecuteIncreaseOrderExec"

class ExecuteMsg__execute_increase_order_cb(TypedDict):
	execute_increase_order_cb: "ExecuteIncreaseOrderCbExec"

class ExecuteMsg__execute_swap_order(TypedDict):
	execute_swap_order: "ExecuteSwapOrderExec"

class ExecuteMsg__execute_swap_order_cb(TypedDict):
	execute_swap_order_cb: "ExecuteSwapOrderCbExec"

class ExecuteMsg__swap_internal(TypedDict):
	swap_internal: "SwapInternalExec"

class ExecuteMsg__transfer_in_osmo_internal(TypedDict):
	transfer_in_osmo_internal: "TransferInOsmoInternalExec"

class ExecuteMsg__transfer_out_osmo_internal(TypedDict):
	transfer_out_osmo_internal: "TransferOutOsmoInternalExec"

class ExecuteMsg__update_decrease_order(TypedDict):
	update_decrease_order: "UpdateDecreaseOrderExec"

class ExecuteMsg__update_increase_order(TypedDict):
	update_increase_order: "UpdateIncreaseOrderExec"

class ExecuteMsg__update_swap_order(TypedDict):
	update_swap_order: "UpdateSwapOrderExec"

class ExecuteMsg__vault_swap_internal(TypedDict):
	vault_swap_internal: "VaultSwapInternalExec"

class ExecuteMsg__swap_internal_cb(TypedDict):
	swap_internal_cb: "SwapInternalCbExec"

class ExecuteMsg__create_increase_order_swap_cb(TypedDict):
	create_increase_order_swap_cb: "CreateIncreaseOrderSwapCbExec"

class ExecuteMsg__create_increase_order_cb(TypedDict):
	create_increase_order_cb: "CreateIncreaseOrderCbExec"

ExecuteMsg = Union["ExecuteMsg__set_admin", "ExecuteMsg__set_min_execution_fee", "ExecuteMsg__set_min_purchase_token_amount_usd", "ExecuteMsg__cancel_decrease_order", "ExecuteMsg__cancel_increase_order", "ExecuteMsg__cancel_swap_order", "ExecuteMsg__create_decrease_order_internal", "ExecuteMsg__create_decrease_order", "ExecuteMsg__create_increase_order_internal", "ExecuteMsg__create_increase_order", "ExecuteMsg__create_swap_order", "ExecuteMsg__create_swap_order_internal", "ExecuteMsg__execute_decrease_order", "ExecuteMsg__execute_decrease_order_cb", "ExecuteMsg__execute_increase_order", "ExecuteMsg__execute_increase_order_cb", "ExecuteMsg__execute_swap_order", "ExecuteMsg__execute_swap_order_cb", "ExecuteMsg__swap_internal", "ExecuteMsg__transfer_in_osmo_internal", "ExecuteMsg__transfer_out_osmo_internal", "ExecuteMsg__update_decrease_order", "ExecuteMsg__update_increase_order", "ExecuteMsg__update_swap_order", "ExecuteMsg__vault_swap_internal", "ExecuteMsg__swap_internal_cb", "ExecuteMsg__create_increase_order_swap_cb", "ExecuteMsg__create_increase_order_cb"]

class QueryMsg__swap_order(TypedDict):
	swap_order: "SwapOrderQuery"

class QueryMsg__decrease_order(TypedDict):
	decrease_order: "DecreaseOrderQuery"

class QueryMsg__orders(TypedDict):
	orders: "OrdersQuery"

class QueryMsg__increase_order(TypedDict):
	increase_order: "IncreaseOrderQuery"

class QueryMsg__usdo_min_price(TypedDict):
	usdo_min_price: "UsdoMinPriceQuery"

class QueryMsg__validate_position_order_price(TypedDict):
	validate_position_order_price: "ValidatePositionOrderPriceQuery"

class QueryMsg__validate_swap_order_price(TypedDict):
	validate_swap_order_price: "ValidateSwapOrderPriceQuery"

QueryMsg = Union["QueryMsg__swap_order", "QueryMsg__decrease_order", "QueryMsg__orders", "QueryMsg__increase_order", "QueryMsg__usdo_min_price", "QueryMsg__validate_position_order_price", "QueryMsg__validate_swap_order_price"]



class OmxCwOrderbook(BaseOmxClient):
	def clone(self) -> "OmxCwOrderbook":
		instance = self.__class__.__new__(self.__class__)
		instance.tx = self.tx
		instance.gas = self.gas
		instance.contract = self.contract
		instance.wallet = self.wallet
		instance.funds = self.funds
		return instance

	def with_funds(self, funds: str) -> "OmxCwOrderbook":
		o = self.clone()
		o.funds = funds
		return o

	def without_funds(self) -> "OmxCwOrderbook":
		o = self.clone()
		o.funds = None
		return o

	def with_wallet(self, wallet: Wallet) -> "OmxCwOrderbook":
		o = self.clone()
		o.wallet = wallet
		return o

	def set_admin(self, admin: str) -> SubmittedTx:
		return self.execute({"set_admin": {"admin": admin}})

	def set_min_execution_fee(self, value: "Uint128") -> SubmittedTx:
		return self.execute({"set_min_execution_fee": {"value": value}})

	def set_min_purchase_token_amount_usd(self, value: "Uint128") -> SubmittedTx:
		return self.execute({"set_min_purchase_token_amount_usd": {"value": value}})

	def cancel_decrease_order(self, order_index: "Uint128") -> SubmittedTx:
		return self.execute({"cancel_decrease_order": {"order_index": order_index}})

	def cancel_increase_order(self, order_index: "Uint128") -> SubmittedTx:
		return self.execute({"cancel_increase_order": {"order_index": order_index}})

	def cancel_swap_order(self, order_index: "Uint128") -> SubmittedTx:
		return self.execute({"cancel_swap_order": {"order_index": order_index}})

	def create_decrease_order_internal(self, account: "Addr", collateral_delta: "Uint128", collateral_token: "Addr", execution_fee: "Uint128", index_token: "Addr", is_long: bool, size_delta: "Uint128", trigger_above_threshold: bool, trigger_price: "Uint128") -> SubmittedTx:
		return self.execute({"create_decrease_order_internal": {"account": account, "collateral_delta": collateral_delta, "collateral_token": collateral_token, "execution_fee": execution_fee, "index_token": index_token, "is_long": is_long, "size_delta": size_delta, "trigger_above_threshold": trigger_above_threshold, "trigger_price": trigger_price}})

	def create_decrease_order(self, collateral_delta: "Uint128", collateral_token: str, index_token: str, is_long: bool, size_delta: "Uint128", trigger_above_threshold: bool, trigger_price: "Uint128") -> SubmittedTx:
		return self.execute({"create_decrease_order": {"collateral_delta": collateral_delta, "collateral_token": collateral_token, "index_token": index_token, "is_long": is_long, "size_delta": size_delta, "trigger_above_threshold": trigger_above_threshold, "trigger_price": trigger_price}})

	def create_increase_order_internal(self, account: "Addr", collateral_token: "Addr", execution_fee: "Uint128", index_token: "Addr", is_long: bool, purchase_token: "Addr", purchase_token_amount: "Uint128", sender: "Addr", size_delta: "Uint128", trigger_above_threshold: bool, trigger_price: "Uint128") -> SubmittedTx:
		return self.execute({"create_increase_order_internal": {"account": account, "collateral_token": collateral_token, "execution_fee": execution_fee, "index_token": index_token, "is_long": is_long, "purchase_token": purchase_token, "purchase_token_amount": purchase_token_amount, "sender": sender, "size_delta": size_delta, "trigger_above_threshold": trigger_above_threshold, "trigger_price": trigger_price}})

	def create_increase_order(self, amount_in: "Uint128", collateral_token: str, execution_fee: "Uint128", index_token: str, is_long: bool, min_out: "Uint128", path: "PositionCollateral", should_wrap: bool, size_delta: "Uint128", trigger_above_threshold: bool, trigger_price: "Uint128") -> SubmittedTx:
		return self.execute({"create_increase_order": {"amount_in": amount_in, "collateral_token": collateral_token, "execution_fee": execution_fee, "index_token": index_token, "is_long": is_long, "min_out": min_out, "path": path, "should_wrap": should_wrap, "size_delta": size_delta, "trigger_above_threshold": trigger_above_threshold, "trigger_price": trigger_price}})

	def create_swap_order(self, amount_in: "Uint128", execution_fee: "Uint128", min_out: "Uint128", path: "SwapPath", should_unwrap: bool, should_wrap: bool, trigger_above_threshold: bool, trigger_ratio: "Uint128") -> SubmittedTx:
		return self.execute({"create_swap_order": {"amount_in": amount_in, "execution_fee": execution_fee, "min_out": min_out, "path": path, "should_unwrap": should_unwrap, "should_wrap": should_wrap, "trigger_above_threshold": trigger_above_threshold, "trigger_ratio": trigger_ratio}})

	def create_swap_order_internal(self, account: "Addr", amount_in: "Uint128", execution_fee: "Uint128", min_out: "Uint128", native_amount_in: "Uint128", path: "ValidatedSwapPath", should_unwrap: bool, trigger_above_threshold: bool, trigger_ratio: "Uint128") -> SubmittedTx:
		return self.execute({"create_swap_order_internal": {"account": account, "amount_in": amount_in, "execution_fee": execution_fee, "min_out": min_out, "native_amount_in": native_amount_in, "path": path, "should_unwrap": should_unwrap, "trigger_above_threshold": trigger_above_threshold, "trigger_ratio": trigger_ratio}})

	def execute_decrease_order(self, address: str, fee_receiver: str, order_index: "Uint128") -> SubmittedTx:
		return self.execute({"execute_decrease_order": {"address": address, "fee_receiver": fee_receiver, "order_index": order_index}})

	def execute_decrease_order_cb(self, balance_before: "Uint128", current_price: "Uint128", fee_receiver: "Addr", order: "DecreaseOrder", order_index: "Uint128") -> SubmittedTx:
		return self.execute({"execute_decrease_order_cb": {"balance_before": balance_before, "current_price": current_price, "fee_receiver": fee_receiver, "order": order, "order_index": order_index}})

	def execute_increase_order(self, account: str, fee_recipient: str, order_index: "Uint128") -> SubmittedTx:
		return self.execute({"execute_increase_order": {"account": account, "fee_recipient": fee_recipient, "order_index": order_index}})

	def execute_increase_order_cb(self, balance_before: "Uint128", current_price: "Uint128", fee_recipient: "Addr", order: "IncreaseOrder", order_index: "Uint128") -> SubmittedTx:
		return self.execute({"execute_increase_order_cb": {"balance_before": balance_before, "current_price": current_price, "fee_recipient": fee_recipient, "order": order, "order_index": order_index}})

	def execute_swap_order(self, account: str, fee_recipient: str, order_index: "Uint128") -> SubmittedTx:
		return self.execute({"execute_swap_order": {"account": account, "fee_recipient": fee_recipient, "order_index": order_index}})

	def execute_swap_order_cb(self, balance_before: "Uint128", fee_recipient: "Addr", order: "SwapOrder", order_index: "Uint128", should_unwrap: bool) -> SubmittedTx:
		return self.execute({"execute_swap_order_cb": {"balance_before": balance_before, "fee_recipient": fee_recipient, "order": order, "order_index": order_index, "should_unwrap": should_unwrap}})

	def swap_internal(self, min_out: "Uint128", path: "SwapPath", recipient: "Addr") -> SubmittedTx:
		return self.execute({"swap_internal": {"min_out": min_out, "path": path, "recipient": recipient}})

	def transfer_in_osmo_internal(self) -> SubmittedTx:
		return self.execute({"transfer_in_osmo_internal": {}})

	def transfer_out_osmo_internal(self, amount_out: "Uint128", recipient: "Addr") -> SubmittedTx:
		return self.execute({"transfer_out_osmo_internal": {"amount_out": amount_out, "recipient": recipient}})

	def update_decrease_order(self, collateral_delta: "Uint128", order_index: "Uint128", size_delta: "Uint128", trigger_above_threshold: bool, trigger_price: "Uint128") -> SubmittedTx:
		return self.execute({"update_decrease_order": {"collateral_delta": collateral_delta, "order_index": order_index, "size_delta": size_delta, "trigger_above_threshold": trigger_above_threshold, "trigger_price": trigger_price}})

	def update_increase_order(self, order_index: "Uint128", size_delta: "Uint128", trigger_above_threshold: bool, trigger_price: "Uint128") -> SubmittedTx:
		return self.execute({"update_increase_order": {"order_index": order_index, "size_delta": size_delta, "trigger_above_threshold": trigger_above_threshold, "trigger_price": trigger_price}})

	def update_swap_order(self, min_out: "Uint128", order_index: "Uint128", trigger_above_threshold: bool, trigger_ratio: "Uint128") -> SubmittedTx:
		return self.execute({"update_swap_order": {"min_out": min_out, "order_index": order_index, "trigger_above_threshold": trigger_above_threshold, "trigger_ratio": trigger_ratio}})

	def vault_swap_internal(self, value: Union["VaultSwapInternalExec__swap", "VaultSwapInternalExec__post_swap"]) -> SubmittedTx:
		return self.execute({"vault_swap_internal": value})

	def swap_internal_cb(self, intermediate_balance_before: "Uint128", intermediate_token: "Addr", min_out: "Uint128", recipient: "Addr", token_out: "Addr") -> SubmittedTx:
		return self.execute({"swap_internal_cb": {"intermediate_balance_before": intermediate_balance_before, "intermediate_token": intermediate_token, "min_out": min_out, "recipient": recipient, "token_out": token_out}})

	def create_increase_order_swap_cb(self, amount_in: "Uint128", collateral_token: "Addr", execution_fee: "Uint128", index_token: "Addr", is_long: bool, min_out: "Uint128", path: "SwapPath", purchase_token: "Addr", sender: "Addr", should_wrap: bool, size_delta: "Uint128", trigger_above_threshold: bool, trigger_price: "Uint128") -> SubmittedTx:
		return self.execute({"create_increase_order_swap_cb": {"amount_in": amount_in, "collateral_token": collateral_token, "execution_fee": execution_fee, "index_token": index_token, "is_long": is_long, "min_out": min_out, "path": path, "purchase_token": purchase_token, "sender": sender, "should_wrap": should_wrap, "size_delta": size_delta, "trigger_above_threshold": trigger_above_threshold, "trigger_price": trigger_price}})

	def create_increase_order_cb(self, amount_in: "Uint128", collateral_token: "Addr", execution_fee: "Uint128", index_token: "Addr", is_long: bool, min_out: "Uint128", path: "PositionCollateral", purchase_token: "Addr", purchase_token_amount: "PurchaseTokenAmount", sender: "Addr", should_wrap: bool, size_delta: "Uint128", trigger_above_threshold: bool, trigger_price: "Uint128") -> SubmittedTx:
		return self.execute({"create_increase_order_cb": {"amount_in": amount_in, "collateral_token": collateral_token, "execution_fee": execution_fee, "index_token": index_token, "is_long": is_long, "min_out": min_out, "path": path, "purchase_token": purchase_token, "purchase_token_amount": purchase_token_amount, "sender": sender, "should_wrap": should_wrap, "size_delta": size_delta, "trigger_above_threshold": trigger_above_threshold, "trigger_price": trigger_price}})

	def swap_order(self, account: str, order_index: "Uint128") -> "QueryResponse_swap_order":
		return self.query({"swap_order": {"account": account, "order_index": order_index}})

	def decrease_order(self, account: str, order_index: "Uint128") -> "QueryResponse_decrease_order":
		return self.query({"decrease_order": {"account": account, "order_index": order_index}})

	def orders(self, ready: bool) -> "QueryResponse_orders":
		return self.query({"orders": {"ready": ready}})

	def increase_order(self, account: str, order_index: "Uint128") -> "QueryResponse_increase_order":
		return self.query({"increase_order": {"account": account, "order_index": order_index}})

	def usdo_min_price(self, other_token: str) -> "QueryResponse_usdo_min_price":
		return self.query({"usdo_min_price": {"other_token": other_token}})

	def validate_position_order_price(self, index_token: str, maximize_price: bool, should_raise: bool, trigger_above_threshold: bool, trigger_price: "Uint128") -> "QueryResponse_validate_position_order_price":
		return self.query({"validate_position_order_price": {"index_token": index_token, "maximize_price": maximize_price, "should_raise": should_raise, "trigger_above_threshold": trigger_above_threshold, "trigger_price": trigger_price}})

	def validate_swap_order_price(self, path: "SwapPath", trigger_ratio: "Uint128") -> "QueryResponse_validate_swap_order_price":
		return self.query({"validate_swap_order_price": {"path": path, "trigger_ratio": trigger_ratio}})
