from omxpy.base_client import BaseOmxClient
from cosmpy.aerial.tx_helpers import SubmittedTx
from cosmpy.aerial.wallet import Wallet
from typing import TypedDict, Tuple, List, Optional, Union


QueryResponse_adjust_for_decimals = str

QueryResponse_cumulative_funding_rates = str

QueryResponse_entry_funding_rate = str

QueryResponse_fee_reserves = str

QueryResponse_funding_fee = str

Uint128 = str

QueryResponse_get_delta__has_profit = bool

class QueryResponse_get_delta(TypedDict):
	delta: "Uint128"
	has_profit: bool

QueryResponse_global_short_average_prices = str

QueryResponse_global_short_sizes = str

QueryResponse_guaranteed_usd = str

QueryResponse_is_manager = bool

QueryResponse_is_router_approved = bool

QueryResponse_max_global_short_price = str

QueryResponse_max_price = str

QueryResponse_min_price = str

QueryResponse_next_average_price = str

QueryResponse_next_funding_rate = str

QueryResponse_next_global_short_average_price = str

QueryResponse_pool_amount = str

Timestamp = Tuple["Uint64"]

Uint64 = str

QueryResponse_position__realized_pnl = int

class QueryResponse_position(TypedDict):
	average_price: "Uint128"
	collateral: "Uint128"
	entry_funding_rate: "Uint128"
	last_increased_time: "Timestamp"
	realized_pnl: int
	reserve_amount: "Uint128"
	size: "Uint128"

QueryResponse_position_delta__has_profit = bool

class QueryResponse_position_delta(TypedDict):
	delta: "Uint128"
	has_profit: bool

QueryResponse_position_fee = str

QueryResponse_position_leverage = str

QueryResponse_redemption_amount = str

QueryResponse_redemption_collateral = str

QueryResponse_redemption_collateral_usd = str

QueryResponse_reserved_amounts = str

QueryResponse_target_usdo_amount = str

QueryResponse_token_to_usd_min = str

QueryResponse_usdo_amount = str

QueryResponse_utilization = str

QueryResponse_validate_liquidation = str

Addr = str

class QueryResponse_vault_config(TypedDict):
	usdo: "Addr"

Duration__nanos = int

Duration__secs = int

class Duration(TypedDict):
	nanos: int
	secs: int

QueryResponse_vault_state__all_whitelisted_tokens = List["Addr"]

QueryResponse_vault_state__has_dynamic_fees = bool

QueryResponse_vault_state__in_manager_mode = bool

QueryResponse_vault_state__in_private_liquidation_mode = bool

QueryResponse_vault_state__include_amm_price = bool

QueryResponse_vault_state__is_leverage_enabled = bool

QueryResponse_vault_state__is_manager_mode = bool

QueryResponse_vault_state__is_swap_enabled = bool

QueryResponse_vault_state__router = Optional["Addr"]

QueryResponse_vault_state__use_swap_pricing = bool

class QueryResponse_vault_state(TypedDict):
	admin: "Addr"
	all_whitelisted_tokens: "QueryResponse_vault_state__all_whitelisted_tokens"
	funding_interval: "Duration"
	funding_rate_factor: "Uint128"
	has_dynamic_fees: bool
	in_manager_mode: bool
	in_private_liquidation_mode: bool
	include_amm_price: bool
	is_leverage_enabled: bool
	is_manager_mode: bool
	is_swap_enabled: bool
	liquidation_fee_usd: "Uint128"
	margin_fee_basis_points: "Uint128"
	max_gas_price: "Uint128"
	max_leverage: "Uint128"
	min_profit_time: "Duration"
	mint_burn_fee_basis_points: "Uint128"
	price_feed: "Addr"
	router: "QueryResponse_vault_state__router"
	stable_funding_rate_factor: "Uint128"
	stable_swap_fee_basis_points: "Uint128"
	stable_tax_basis_points: "Uint128"
	swap_fee_basis_points: "Uint128"
	tax_basis_points: "Uint128"
	total_token_weights: "Uint128"
	use_swap_pricing: bool
	whitelisted_token_count: "Uint128"

QueryResponse_whitelisted_token__decimals = int

QueryResponse_whitelisted_token__is_shortable = bool

QueryResponse_whitelisted_token__is_stable = bool

QueryResponse_whitelisted_token__max_usdo_amount = Tuple["Uint128"]

class QueryResponse_whitelisted_token(TypedDict):
	decimals: int
	is_shortable: bool
	is_stable: bool
	max_usdo_amount: "QueryResponse_whitelisted_token__max_usdo_amount"
	min_profit_basis_points: "Uint128"
	weight: "Uint128"

AddRouterMsg__router = str

class AddRouterMsg(TypedDict):
	router: str

class BuyUsdoCbMsg(TypedDict):
	fee_basis_points: "Uint128"
	mint_amount: "Uint128"
	recipient: "Addr"
	token: "Addr"
	token_amount: "Uint128"

BuyUsdoMsg__recipient = str

BuyUsdoMsg__token = str

class BuyUsdoMsg(TypedDict):
	recipient: str
	token: str

ClearTokenConfigMsg__token = str

class ClearTokenConfigMsg(TypedDict):
	token: str

DecreasePositionMsg__account = str

DecreasePositionMsg__collateral_token = str

DecreasePositionMsg__index_token = str

DecreasePositionMsg__is_long = bool

DecreasePositionMsg__recipient = str

class DecreasePositionMsg(TypedDict):
	account: str
	collateral_delta: "Uint128"
	collateral_token: str
	index_token: str
	is_long: bool
	recipient: str
	size_delta: "Uint128"

DirectPoolDepositMsg__token = str

class DirectPoolDepositMsg(TypedDict):
	token: str

IncreasePositionMsg__account = str

IncreasePositionMsg__collateral_token = str

IncreasePositionMsg__index_token = str

IncreasePositionMsg__is_long = bool

class IncreasePositionMsg(TypedDict):
	account: str
	collateral_token: str
	index_token: str
	is_long: bool
	size_delta: "Uint128"

LiquidatePositionMsg__account = str

LiquidatePositionMsg__collateral_token = str

LiquidatePositionMsg__fee_recipient = str

LiquidatePositionMsg__index_token = str

LiquidatePositionMsg__is_long = bool

class LiquidatePositionMsg(TypedDict):
	account: str
	collateral_token: str
	fee_recipient: str
	index_token: str
	is_long: bool

SellUsdoAmountMsg__amount = Tuple["Uint128"]

SellUsdoAmountMsg__token = str

class SellUsdoAmountMsg(TypedDict):
	amount: "SellUsdoAmountMsg__amount"
	token: str

class SellUsdoCbMsg(TypedDict):
	recipient: "Addr"
	redemption_amount: "Uint128"
	token: "Addr"
	usdo_amount: "Uint128"

SellUsdoMsg__recipient = str

SellUsdoMsg__token = str

class SellUsdoMsg(TypedDict):
	recipient: str
	token: str

SetAdminMsg__new_admin = str

class SetAdminMsg(TypedDict):
	new_admin: str

SetFeesMsg__has_dynamic_fees = bool

class SetFeesMsg(TypedDict):
	has_dynamic_fees: bool
	liquidation_fee_usd: "Uint128"
	margin_fee_basis_points: "Uint128"
	min_profit_time: "Duration"
	mint_burn_fee_basis_points: "Uint128"
	stable_swap_fee_basis_points: "Uint128"
	stable_tax_basis_points: "Uint128"
	swap_fee_basis_points: "Uint128"
	tax_basis_points: "Uint128"

class SetFundingRateMsg(TypedDict):
	funding_interval: "Duration"
	funding_rate_factor: "Uint128"
	stable_funding_rate_factor: "Uint128"

SetInManagerModeMsg__in_manager_mode = bool

class SetInManagerModeMsg(TypedDict):
	in_manager_mode: bool

SetInPrivateLiquidationModeMsg__value = bool

class SetInPrivateLiquidationModeMsg(TypedDict):
	value: bool

SetIsLeverageEnabledMsg__value = bool

class SetIsLeverageEnabledMsg(TypedDict):
	value: bool

SetIsLiquidatorMsg__account = str

SetIsLiquidatorMsg__value = bool

class SetIsLiquidatorMsg(TypedDict):
	account: str
	value: bool

SetIsSwapEnabledMsg__value = bool

class SetIsSwapEnabledMsg(TypedDict):
	value: bool

SetManagerMsg__addr = str

class SetManagerMsg(TypedDict):
	addr: str

class SetMaxGasPriceMsg(TypedDict):
	max_gas_price: "Uint128"

SetMaxGlobalShortPriceMsg__token = str

class SetMaxGlobalShortPriceMsg(TypedDict):
	token: str
	value: "Uint128"

SetRouterMsg__router = str

class SetRouterMsg(TypedDict):
	router: str

SetTokenConfigMsg__is_shortable = bool

SetTokenConfigMsg__is_stable = bool

SetTokenConfigMsg__token = str

SetTokenConfigMsg__token_decimals = int

class SetTokenConfigMsg(TypedDict):
	is_shortable: bool
	is_stable: bool
	max_usdo_amount: "Uint128"
	min_profit_bps: "Uint128"
	token: str
	token_decimals: int
	token_weight: "Uint128"

SetUsdoAmountMsg__token = str

class SetUsdoAmountMsg(TypedDict):
	amount: "Uint128"
	token: str

SwapMsg__recipient = Optional[str]

SwapMsg__token_in = str

SwapMsg__token_out = str

class SwapMsg(TypedDict):
	recipient: str
	token_in: str
	token_out: str

UpdateCumulativeFundingRateMsg__collateral_token = str

UpdateCumulativeFundingRateMsg__index_token = str

class UpdateCumulativeFundingRateMsg(TypedDict):
	collateral_token: str
	index_token: str

WithdrawFeesMsg__recipient = Optional[str]

WithdrawFeesMsg__token = str

class WithdrawFeesMsg(TypedDict):
	recipient: str
	token: str

AdjustForDecimalsQuery__token_div = str

AdjustForDecimalsQuery__token_mul = str

class AdjustForDecimalsQuery(TypedDict):
	amount: "Uint128"
	token_div: str
	token_mul: str

CumulativeFundingRatesQuery__token = str

class CumulativeFundingRatesQuery(TypedDict):
	token: str

EntryFundingRateQuery__collateral_token = str

EntryFundingRateQuery__index_token = str

EntryFundingRateQuery__is_long = bool

class EntryFundingRateQuery(TypedDict):
	collateral_token: str
	index_token: str
	is_long: bool

FeeReservesQuery__token = str

class FeeReservesQuery(TypedDict):
	token: str

FundingFeeQuery__collateral_token = str

class FundingFeeQuery(TypedDict):
	collateral_token: str
	entry_funding_rate: "Uint128"
	size: "Uint128"

GetDeltaQuery__index_token = str

GetDeltaQuery__is_long = bool

class GetDeltaQuery(TypedDict):
	average_price: "Uint128"
	index_token: str
	is_long: bool
	last_increased_time: "Timestamp"
	size: "Uint128"

GlobalShortAveragePricesQuery__token = str

class GlobalShortAveragePricesQuery(TypedDict):
	token: str

GlobalShortSizesQuery__token = str

class GlobalShortSizesQuery(TypedDict):
	token: str

GuaranteedUsdQuery__token = str

class GuaranteedUsdQuery(TypedDict):
	token: str

IsManagerQuery__addr = str

class IsManagerQuery(TypedDict):
	addr: str

IsRouterApprovedQuery__account = str

IsRouterApprovedQuery__router = str

class IsRouterApprovedQuery(TypedDict):
	account: str
	router: str

MaxGlobalShortPriceQuery__token = str

class MaxGlobalShortPriceQuery(TypedDict):
	token: str

MaxPriceQuery__token = str

class MaxPriceQuery(TypedDict):
	token: str

MinPriceQuery__token = str

class MinPriceQuery(TypedDict):
	token: str

NextAveragePriceQuery__index_token = str

NextAveragePriceQuery__is_long = bool

class NextAveragePriceQuery(TypedDict):
	average_price: "Uint128"
	index_token: str
	is_long: bool
	last_increased_time: "Timestamp"
	next_price: "Uint128"
	size: "Uint128"
	size_delta: "Uint128"

NextFundingRateQuery__token = str

class NextFundingRateQuery(TypedDict):
	token: str

NextGlobalShortAveragePriceQuery__index_token = str

class NextGlobalShortAveragePriceQuery(TypedDict):
	index_token: str
	next_price: "Uint128"
	size_delta: "Uint128"

PoolAmountQuery__token = str

class PoolAmountQuery(TypedDict):
	token: str

PositionDeltaQuery__account = str

PositionDeltaQuery__collateral_token = str

PositionDeltaQuery__index_token = str

PositionDeltaQuery__is_long = bool

class PositionDeltaQuery(TypedDict):
	account: str
	collateral_token: str
	index_token: str
	is_long: bool

PositionFeeQuery__account = str

PositionFeeQuery__collateral_token = str

PositionFeeQuery__index_token = str

PositionFeeQuery__is_long = bool

class PositionFeeQuery(TypedDict):
	account: str
	collateral_token: str
	index_token: str
	is_long: bool
	size_delta: "Uint128"

PositionLeverageQuery__account = str

PositionLeverageQuery__collateral_token = str

PositionLeverageQuery__index_token = str

PositionLeverageQuery__is_long = bool

class PositionLeverageQuery(TypedDict):
	account: str
	collateral_token: str
	index_token: str
	is_long: bool

PositionQuery__account = str

PositionQuery__collateral_token = str

PositionQuery__index_token = str

PositionQuery__is_long = bool

class PositionQuery(TypedDict):
	account: str
	collateral_token: str
	index_token: str
	is_long: bool

RedemptionAmountQuery__token = str

class RedemptionAmountQuery(TypedDict):
	token: str
	usdo_amount: "Uint128"

RedemptionCollateralQuery__token = str

class RedemptionCollateralQuery(TypedDict):
	token: str

RedemptionCollateralUsdQuery__token = str

class RedemptionCollateralUsdQuery(TypedDict):
	token: str

ReservedAmountsQuery__token = str

class ReservedAmountsQuery(TypedDict):
	token: str

TargetUsdoAmountQuery__token = str

class TargetUsdoAmountQuery(TypedDict):
	token: str

TokenToUsdMinQuery__token = str

class TokenToUsdMinQuery(TypedDict):
	amount: "Uint128"
	token: str

UsdoAmountQuery__token = str

class UsdoAmountQuery(TypedDict):
	token: str

UtilizationQuery__token = str

class UtilizationQuery(TypedDict):
	token: str

ValidateLiquidationQuery__account = str

ValidateLiquidationQuery__collateral_token = str

ValidateLiquidationQuery__index_token = str

ValidateLiquidationQuery__is_long = bool

ValidateLiquidationQuery__should_raise = bool

class ValidateLiquidationQuery(TypedDict):
	account: str
	collateral_token: str
	index_token: str
	is_long: bool
	should_raise: bool

WhitelistedTokenQuery__token = str

class WhitelistedTokenQuery(TypedDict):
	token: str

class ExecuteMsg__buy_usdo(TypedDict):
	buy_usdo: "BuyUsdoMsg"

class ExecuteMsg__set_is_liquidator(TypedDict):
	set_is_liquidator: "SetIsLiquidatorMsg"

class ExecuteMsg__add_router(TypedDict):
	add_router: "AddRouterMsg"

class ExecuteMsg__buy_usdo_cb(TypedDict):
	buy_usdo_cb: "BuyUsdoCbMsg"

class ExecuteMsg__clear_token_config(TypedDict):
	clear_token_config: "ClearTokenConfigMsg"

class ExecuteMsg__decrease_position(TypedDict):
	decrease_position: "DecreasePositionMsg"

class ExecuteMsg__direct_pool_deposit(TypedDict):
	direct_pool_deposit: "DirectPoolDepositMsg"

class ExecuteMsg__increase_position(TypedDict):
	increase_position: "IncreasePositionMsg"

class ExecuteMsg__liquidate_position(TypedDict):
	liquidate_position: "LiquidatePositionMsg"

class ExecuteMsg__set_router(TypedDict):
	set_router: "SetRouterMsg"

class ExecuteMsg__sell_usdo(TypedDict):
	sell_usdo: "SellUsdoMsg"

class ExecuteMsg__sell_usdo_cb(TypedDict):
	sell_usdo_cb: "SellUsdoCbMsg"

class ExecuteMsg__sell_usdo_amount(TypedDict):
	sell_usdo_amount: "SellUsdoAmountMsg"

class ExecuteMsg__set_fees(TypedDict):
	set_fees: "SetFeesMsg"

class ExecuteMsg__set_funding_rate(TypedDict):
	set_funding_rate: "SetFundingRateMsg"

class ExecuteMsg__set_token_config(TypedDict):
	set_token_config: "SetTokenConfigMsg"

class ExecuteMsg__set_usdo_amount(TypedDict):
	set_usdo_amount: "SetUsdoAmountMsg"

class ExecuteMsg__swap(TypedDict):
	swap: "SwapMsg"

class ExecuteMsg__update_cumulative_funding_rate(TypedDict):
	update_cumulative_funding_rate: "UpdateCumulativeFundingRateMsg"

class ExecuteMsg__withdraw_fees(TypedDict):
	withdraw_fees: "WithdrawFeesMsg"

class ExecuteMsg__set_in_manager_mode(TypedDict):
	set_in_manager_mode: "SetInManagerModeMsg"

class ExecuteMsg__set_in_private_liquidation_mode(TypedDict):
	set_in_private_liquidation_mode: "SetInPrivateLiquidationModeMsg"

class ExecuteMsg__set_is_swap_enabled(TypedDict):
	set_is_swap_enabled: "SetIsSwapEnabledMsg"

class ExecuteMsg__set_is_leverage_enabled(TypedDict):
	set_is_leverage_enabled: "SetIsLeverageEnabledMsg"

class ExecuteMsg__set_max_gas_price(TypedDict):
	set_max_gas_price: "SetMaxGasPriceMsg"

class ExecuteMsg__set_max_global_short_price(TypedDict):
	set_max_global_short_price: "SetMaxGlobalShortPriceMsg"

class ExecuteMsg__set_manager(TypedDict):
	set_manager: "SetManagerMsg"

class ExecuteMsg__set_admin(TypedDict):
	set_admin: "SetAdminMsg"

ExecuteMsg = Union["ExecuteMsg__buy_usdo", "ExecuteMsg__set_is_liquidator", "ExecuteMsg__add_router", "ExecuteMsg__buy_usdo_cb", "ExecuteMsg__clear_token_config", "ExecuteMsg__decrease_position", "ExecuteMsg__direct_pool_deposit", "ExecuteMsg__increase_position", "ExecuteMsg__liquidate_position", "ExecuteMsg__set_router", "ExecuteMsg__sell_usdo", "ExecuteMsg__sell_usdo_cb", "ExecuteMsg__sell_usdo_amount", "ExecuteMsg__set_fees", "ExecuteMsg__set_funding_rate", "ExecuteMsg__set_token_config", "ExecuteMsg__set_usdo_amount", "ExecuteMsg__swap", "ExecuteMsg__update_cumulative_funding_rate", "ExecuteMsg__withdraw_fees", "ExecuteMsg__set_in_manager_mode", "ExecuteMsg__set_in_private_liquidation_mode", "ExecuteMsg__set_is_swap_enabled", "ExecuteMsg__set_is_leverage_enabled", "ExecuteMsg__set_max_gas_price", "ExecuteMsg__set_max_global_short_price", "ExecuteMsg__set_manager", "ExecuteMsg__set_admin"]

class QueryMsg__vault_state__vault_state(TypedDict):
	pass

class QueryMsg__vault_state(TypedDict):
	vault_state: "QueryMsg__vault_state__vault_state"

class QueryMsg__vault_config__vault_config(TypedDict):
	pass

class QueryMsg__vault_config(TypedDict):
	vault_config: "QueryMsg__vault_config__vault_config"

class QueryMsg__utilization(TypedDict):
	utilization: "UtilizationQuery"

class QueryMsg__cumulative_funding_rates(TypedDict):
	cumulative_funding_rates: "CumulativeFundingRatesQuery"

class QueryMsg__position_leverage(TypedDict):
	position_leverage: "PositionLeverageQuery"

class QueryMsg__token_to_usd_min(TypedDict):
	token_to_usd_min: "TokenToUsdMinQuery"

class QueryMsg__global_short_average_prices(TypedDict):
	global_short_average_prices: "GlobalShortAveragePricesQuery"

class QueryMsg__global_short_sizes(TypedDict):
	global_short_sizes: "GlobalShortSizesQuery"

class QueryMsg__position_delta(TypedDict):
	position_delta: "PositionDeltaQuery"

class QueryMsg__reserved_amounts(TypedDict):
	reserved_amounts: "ReservedAmountsQuery"

class QueryMsg__guaranteed_usd(TypedDict):
	guaranteed_usd: "GuaranteedUsdQuery"

class QueryMsg__usdo_amount(TypedDict):
	usdo_amount: "UsdoAmountQuery"

class QueryMsg__entry_funding_rate(TypedDict):
	entry_funding_rate: "EntryFundingRateQuery"

class QueryMsg__next_global_short_average_price(TypedDict):
	next_global_short_average_price: "NextGlobalShortAveragePriceQuery"

class QueryMsg__next_funding_rate(TypedDict):
	next_funding_rate: "NextFundingRateQuery"

class QueryMsg__funding_fee(TypedDict):
	funding_fee: "FundingFeeQuery"

class QueryMsg__min_price(TypedDict):
	min_price: "MinPriceQuery"

class QueryMsg__max_price(TypedDict):
	max_price: "MaxPriceQuery"

class QueryMsg__redemption_amount(TypedDict):
	redemption_amount: "RedemptionAmountQuery"

class QueryMsg__target_usdo_amount(TypedDict):
	target_usdo_amount: "TargetUsdoAmountQuery"

class QueryMsg__adjust_for_decimals(TypedDict):
	adjust_for_decimals: "AdjustForDecimalsQuery"

class QueryMsg__is_router_approved(TypedDict):
	is_router_approved: "IsRouterApprovedQuery"

class QueryMsg__get_delta(TypedDict):
	get_delta: "GetDeltaQuery"

class QueryMsg__redemption_collateral(TypedDict):
	redemption_collateral: "RedemptionCollateralQuery"

class QueryMsg__redemption_collateral_usd(TypedDict):
	redemption_collateral_usd: "RedemptionCollateralUsdQuery"

class QueryMsg__position_fee(TypedDict):
	position_fee: "PositionFeeQuery"

class QueryMsg__max_global_short_price(TypedDict):
	max_global_short_price: "MaxGlobalShortPriceQuery"

class QueryMsg__next_average_price(TypedDict):
	next_average_price: "NextAveragePriceQuery"

class QueryMsg__is_manager(TypedDict):
	is_manager: "IsManagerQuery"

class QueryMsg__pool_amount(TypedDict):
	pool_amount: "PoolAmountQuery"

class QueryMsg__whitelisted_token(TypedDict):
	whitelisted_token: "WhitelistedTokenQuery"

class QueryMsg__position(TypedDict):
	position: "PositionQuery"

class QueryMsg__fee_reserves(TypedDict):
	fee_reserves: "FeeReservesQuery"

class QueryMsg__validate_liquidation(TypedDict):
	validate_liquidation: "ValidateLiquidationQuery"

QueryMsg = Union["QueryMsg__vault_state", "QueryMsg__vault_config", "QueryMsg__utilization", "QueryMsg__cumulative_funding_rates", "QueryMsg__position_leverage", "QueryMsg__token_to_usd_min", "QueryMsg__global_short_average_prices", "QueryMsg__global_short_sizes", "QueryMsg__position_delta", "QueryMsg__reserved_amounts", "QueryMsg__guaranteed_usd", "QueryMsg__usdo_amount", "QueryMsg__entry_funding_rate", "QueryMsg__next_global_short_average_price", "QueryMsg__next_funding_rate", "QueryMsg__funding_fee", "QueryMsg__min_price", "QueryMsg__max_price", "QueryMsg__redemption_amount", "QueryMsg__target_usdo_amount", "QueryMsg__adjust_for_decimals", "QueryMsg__is_router_approved", "QueryMsg__get_delta", "QueryMsg__redemption_collateral", "QueryMsg__redemption_collateral_usd", "QueryMsg__position_fee", "QueryMsg__max_global_short_price", "QueryMsg__next_average_price", "QueryMsg__is_manager", "QueryMsg__pool_amount", "QueryMsg__whitelisted_token", "QueryMsg__position", "QueryMsg__fee_reserves", "QueryMsg__validate_liquidation"]



class OmxCwVault(BaseOmxClient):
	def clone(self) -> "OmxCwVault":
		instance = self.__class__.__new__(self.__class__)
		instance.tx = self.tx
		instance.gas = self.gas
		instance.contract = self.contract
		instance.wallet = self.wallet
		instance.funds = self.funds
		return instance

	def with_funds(self, funds: str) -> "OmxCwVault":
		o = self.clone()
		o.funds = funds
		return o

	def without_funds(self) -> "OmxCwVault":
		o = self.clone()
		o.funds = None
		return o

	def with_wallet(self, wallet: Wallet) -> "OmxCwVault":
		o = self.clone()
		o.wallet = wallet
		return o

	def buy_usdo(self, recipient: str, token: str) -> SubmittedTx:
		return self.execute({"buy_usdo": {"recipient": recipient, "token": token}})

	def set_is_liquidator(self, account: str, value: bool) -> SubmittedTx:
		return self.execute({"set_is_liquidator": {"account": account, "value": value}})

	def add_router(self, router: str) -> SubmittedTx:
		return self.execute({"add_router": {"router": router}})

	def buy_usdo_cb(self, fee_basis_points: "Uint128", mint_amount: "Uint128", recipient: "Addr", token: "Addr", token_amount: "Uint128") -> SubmittedTx:
		return self.execute({"buy_usdo_cb": {"fee_basis_points": fee_basis_points, "mint_amount": mint_amount, "recipient": recipient, "token": token, "token_amount": token_amount}})

	def clear_token_config(self, token: str) -> SubmittedTx:
		return self.execute({"clear_token_config": {"token": token}})

	def decrease_position(self, account: str, collateral_delta: "Uint128", collateral_token: str, index_token: str, is_long: bool, recipient: str, size_delta: "Uint128") -> SubmittedTx:
		return self.execute({"decrease_position": {"account": account, "collateral_delta": collateral_delta, "collateral_token": collateral_token, "index_token": index_token, "is_long": is_long, "recipient": recipient, "size_delta": size_delta}})

	def direct_pool_deposit(self, token: str) -> SubmittedTx:
		return self.execute({"direct_pool_deposit": {"token": token}})

	def increase_position(self, account: str, collateral_token: str, index_token: str, is_long: bool, size_delta: "Uint128") -> SubmittedTx:
		return self.execute({"increase_position": {"account": account, "collateral_token": collateral_token, "index_token": index_token, "is_long": is_long, "size_delta": size_delta}})

	def liquidate_position(self, account: str, collateral_token: str, fee_recipient: str, index_token: str, is_long: bool) -> SubmittedTx:
		return self.execute({"liquidate_position": {"account": account, "collateral_token": collateral_token, "fee_recipient": fee_recipient, "index_token": index_token, "is_long": is_long}})

	def set_router(self, router: str) -> SubmittedTx:
		return self.execute({"set_router": {"router": router}})

	def sell_usdo(self, recipient: str, token: str) -> SubmittedTx:
		return self.execute({"sell_usdo": {"recipient": recipient, "token": token}})

	def sell_usdo_cb(self, recipient: "Addr", redemption_amount: "Uint128", token: "Addr", usdo_amount: "Uint128") -> SubmittedTx:
		return self.execute({"sell_usdo_cb": {"recipient": recipient, "redemption_amount": redemption_amount, "token": token, "usdo_amount": usdo_amount}})

	def sell_usdo_amount(self, amount: "SellUsdoAmountMsg__amount", token: str) -> SubmittedTx:
		return self.execute({"sell_usdo_amount": {"amount": amount, "token": token}})

	def set_fees(self, has_dynamic_fees: bool, liquidation_fee_usd: "Uint128", margin_fee_basis_points: "Uint128", min_profit_time: "Duration", mint_burn_fee_basis_points: "Uint128", stable_swap_fee_basis_points: "Uint128", stable_tax_basis_points: "Uint128", swap_fee_basis_points: "Uint128", tax_basis_points: "Uint128") -> SubmittedTx:
		return self.execute({"set_fees": {"has_dynamic_fees": has_dynamic_fees, "liquidation_fee_usd": liquidation_fee_usd, "margin_fee_basis_points": margin_fee_basis_points, "min_profit_time": min_profit_time, "mint_burn_fee_basis_points": mint_burn_fee_basis_points, "stable_swap_fee_basis_points": stable_swap_fee_basis_points, "stable_tax_basis_points": stable_tax_basis_points, "swap_fee_basis_points": swap_fee_basis_points, "tax_basis_points": tax_basis_points}})

	def set_funding_rate(self, funding_interval: "Duration", funding_rate_factor: "Uint128", stable_funding_rate_factor: "Uint128") -> SubmittedTx:
		return self.execute({"set_funding_rate": {"funding_interval": funding_interval, "funding_rate_factor": funding_rate_factor, "stable_funding_rate_factor": stable_funding_rate_factor}})

	def set_token_config(self, is_shortable: bool, is_stable: bool, max_usdo_amount: "Uint128", min_profit_bps: "Uint128", token: str, token_decimals: int, token_weight: "Uint128") -> SubmittedTx:
		return self.execute({"set_token_config": {"is_shortable": is_shortable, "is_stable": is_stable, "max_usdo_amount": max_usdo_amount, "min_profit_bps": min_profit_bps, "token": token, "token_decimals": token_decimals, "token_weight": token_weight}})

	def set_usdo_amount(self, amount: "Uint128", token: str) -> SubmittedTx:
		return self.execute({"set_usdo_amount": {"amount": amount, "token": token}})

	def swap(self, recipient: str, token_in: str, token_out: str) -> SubmittedTx:
		return self.execute({"swap": {"recipient": recipient, "token_in": token_in, "token_out": token_out}})

	def update_cumulative_funding_rate(self, collateral_token: str, index_token: str) -> SubmittedTx:
		return self.execute({"update_cumulative_funding_rate": {"collateral_token": collateral_token, "index_token": index_token}})

	def withdraw_fees(self, recipient: str, token: str) -> SubmittedTx:
		return self.execute({"withdraw_fees": {"recipient": recipient, "token": token}})

	def set_in_manager_mode(self, in_manager_mode: bool) -> SubmittedTx:
		return self.execute({"set_in_manager_mode": {"in_manager_mode": in_manager_mode}})

	def set_in_private_liquidation_mode(self, value: bool) -> SubmittedTx:
		return self.execute({"set_in_private_liquidation_mode": {"value": value}})

	def set_is_swap_enabled(self, value: bool) -> SubmittedTx:
		return self.execute({"set_is_swap_enabled": {"value": value}})

	def set_is_leverage_enabled(self, value: bool) -> SubmittedTx:
		return self.execute({"set_is_leverage_enabled": {"value": value}})

	def set_max_gas_price(self, max_gas_price: "Uint128") -> SubmittedTx:
		return self.execute({"set_max_gas_price": {"max_gas_price": max_gas_price}})

	def set_max_global_short_price(self, token: str, value: "Uint128") -> SubmittedTx:
		return self.execute({"set_max_global_short_price": {"token": token, "value": value}})

	def set_manager(self, addr: str) -> SubmittedTx:
		return self.execute({"set_manager": {"addr": addr}})

	def set_admin(self, new_admin: str) -> SubmittedTx:
		return self.execute({"set_admin": {"new_admin": new_admin}})

	def vault_state(self) -> "QueryResponse_vault_state":
		return self.query({"vault_state": {}})

	def vault_config(self) -> "QueryResponse_vault_config":
		return self.query({"vault_config": {}})

	def utilization(self, token: str) -> "QueryResponse_utilization":
		return self.query({"utilization": {"token": token}})

	def cumulative_funding_rates(self, token: str) -> "QueryResponse_cumulative_funding_rates":
		return self.query({"cumulative_funding_rates": {"token": token}})

	def position_leverage(self, account: str, collateral_token: str, index_token: str, is_long: bool) -> "QueryResponse_position_leverage":
		return self.query({"position_leverage": {"account": account, "collateral_token": collateral_token, "index_token": index_token, "is_long": is_long}})

	def token_to_usd_min(self, amount: "Uint128", token: str) -> "QueryResponse_token_to_usd_min":
		return self.query({"token_to_usd_min": {"amount": amount, "token": token}})

	def global_short_average_prices(self, token: str) -> "QueryResponse_global_short_average_prices":
		return self.query({"global_short_average_prices": {"token": token}})

	def global_short_sizes(self, token: str) -> "QueryResponse_global_short_sizes":
		return self.query({"global_short_sizes": {"token": token}})

	def position_delta(self, account: str, collateral_token: str, index_token: str, is_long: bool) -> "QueryResponse_position_delta":
		return self.query({"position_delta": {"account": account, "collateral_token": collateral_token, "index_token": index_token, "is_long": is_long}})

	def reserved_amounts(self, token: str) -> "QueryResponse_reserved_amounts":
		return self.query({"reserved_amounts": {"token": token}})

	def guaranteed_usd(self, token: str) -> "QueryResponse_guaranteed_usd":
		return self.query({"guaranteed_usd": {"token": token}})

	def usdo_amount(self, token: str) -> "QueryResponse_usdo_amount":
		return self.query({"usdo_amount": {"token": token}})

	def entry_funding_rate(self, collateral_token: str, index_token: str, is_long: bool) -> "QueryResponse_entry_funding_rate":
		return self.query({"entry_funding_rate": {"collateral_token": collateral_token, "index_token": index_token, "is_long": is_long}})

	def next_global_short_average_price(self, index_token: str, next_price: "Uint128", size_delta: "Uint128") -> "QueryResponse_next_global_short_average_price":
		return self.query({"next_global_short_average_price": {"index_token": index_token, "next_price": next_price, "size_delta": size_delta}})

	def next_funding_rate(self, token: str) -> "QueryResponse_next_funding_rate":
		return self.query({"next_funding_rate": {"token": token}})

	def funding_fee(self, collateral_token: str, entry_funding_rate: "Uint128", size: "Uint128") -> "QueryResponse_funding_fee":
		return self.query({"funding_fee": {"collateral_token": collateral_token, "entry_funding_rate": entry_funding_rate, "size": size}})

	def min_price(self, token: str) -> "QueryResponse_min_price":
		return self.query({"min_price": {"token": token}})

	def max_price(self, token: str) -> "QueryResponse_max_price":
		return self.query({"max_price": {"token": token}})

	def redemption_amount(self, token: str, usdo_amount: "Uint128") -> "QueryResponse_redemption_amount":
		return self.query({"redemption_amount": {"token": token, "usdo_amount": usdo_amount}})

	def target_usdo_amount(self, token: str) -> "QueryResponse_target_usdo_amount":
		return self.query({"target_usdo_amount": {"token": token}})

	def adjust_for_decimals(self, amount: "Uint128", token_div: str, token_mul: str) -> "QueryResponse_adjust_for_decimals":
		return self.query({"adjust_for_decimals": {"amount": amount, "token_div": token_div, "token_mul": token_mul}})

	def is_router_approved(self, account: str, router: str) -> "QueryResponse_is_router_approved":
		return self.query({"is_router_approved": {"account": account, "router": router}})

	def get_delta(self, average_price: "Uint128", index_token: str, is_long: bool, last_increased_time: "Timestamp", size: "Uint128") -> "QueryResponse_get_delta":
		return self.query({"get_delta": {"average_price": average_price, "index_token": index_token, "is_long": is_long, "last_increased_time": last_increased_time, "size": size}})

	def redemption_collateral(self, token: str) -> "QueryResponse_redemption_collateral":
		return self.query({"redemption_collateral": {"token": token}})

	def redemption_collateral_usd(self, token: str) -> "QueryResponse_redemption_collateral_usd":
		return self.query({"redemption_collateral_usd": {"token": token}})

	def position_fee(self, account: str, collateral_token: str, index_token: str, is_long: bool, size_delta: "Uint128") -> "QueryResponse_position_fee":
		return self.query({"position_fee": {"account": account, "collateral_token": collateral_token, "index_token": index_token, "is_long": is_long, "size_delta": size_delta}})

	def max_global_short_price(self, token: str) -> "QueryResponse_max_global_short_price":
		return self.query({"max_global_short_price": {"token": token}})

	def next_average_price(self, average_price: "Uint128", index_token: str, is_long: bool, last_increased_time: "Timestamp", next_price: "Uint128", size: "Uint128", size_delta: "Uint128") -> "QueryResponse_next_average_price":
		return self.query({"next_average_price": {"average_price": average_price, "index_token": index_token, "is_long": is_long, "last_increased_time": last_increased_time, "next_price": next_price, "size": size, "size_delta": size_delta}})

	def is_manager(self, addr: str) -> "QueryResponse_is_manager":
		return self.query({"is_manager": {"addr": addr}})

	def pool_amount(self, token: str) -> "QueryResponse_pool_amount":
		return self.query({"pool_amount": {"token": token}})

	def whitelisted_token(self, token: str) -> "QueryResponse_whitelisted_token":
		return self.query({"whitelisted_token": {"token": token}})

	def position(self, account: str, collateral_token: str, index_token: str, is_long: bool) -> "QueryResponse_position":
		return self.query({"position": {"account": account, "collateral_token": collateral_token, "index_token": index_token, "is_long": is_long}})

	def fee_reserves(self, token: str) -> "QueryResponse_fee_reserves":
		return self.query({"fee_reserves": {"token": token}})

	def validate_liquidation(self, account: str, collateral_token: str, index_token: str, is_long: bool, should_raise: bool) -> "QueryResponse_validate_liquidation":
		return self.query({"validate_liquidation": {"account": account, "collateral_token": collateral_token, "index_token": index_token, "is_long": is_long, "should_raise": should_raise}})
