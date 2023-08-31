from omxpy.base_client import BaseOmxClient
from cosmpy.aerial.tx_helpers import SubmittedTx
from cosmpy.aerial.wallet import Wallet
from typing import List, TypedDict, Union, Tuple, Optional


QueryResponse_all_accounts__accounts__item = str

QueryResponse_all_accounts__accounts = List[str]

class QueryResponse_all_accounts(TypedDict):
	accounts: "QueryResponse_all_accounts__accounts"

AllowanceInfo__spender = str

class AllowanceInfo(TypedDict):
	allowance: "Uint128"
	expires: "Expiration"
	spender: str

Expiration__at_height__at_height = int

class Expiration__at_height(TypedDict):
	at_height: int

class Expiration__at_time(TypedDict):
	at_time: "Timestamp"

class Expiration__never__never(TypedDict):
	pass

class Expiration__never(TypedDict):
	never: "Expiration__never__never"

Expiration = Union["Expiration__at_height", "Expiration__at_time", "Expiration__never"]

Timestamp = Tuple["Uint64"]

Uint128 = str

Uint64 = str

QueryResponse_all_allowances__allowances = List["AllowanceInfo"]

class QueryResponse_all_allowances(TypedDict):
	allowances: "QueryResponse_all_allowances__allowances"

SpenderAllowanceInfo__owner = str

class SpenderAllowanceInfo(TypedDict):
	allowance: "Uint128"
	expires: "Expiration"
	owner: str

QueryResponse_all_spender_allowances__allowances = List["SpenderAllowanceInfo"]

class QueryResponse_all_spender_allowances(TypedDict):
	allowances: "QueryResponse_all_spender_allowances__allowances"

class QueryResponse_allowance(TypedDict):
	allowance: "Uint128"
	expires: "Expiration"

QueryResponse_average_staked_amount = str

class QueryResponse_balance(TypedDict):
	balance: "Uint128"

QueryResponse_claimable = str

QueryResponse_cumulative_rewards = str

QueryResponse_deposit_balance = str

Binary = str

QueryResponse_download_logo__mime_type = str

class QueryResponse_download_logo(TypedDict):
	data: "Binary"
	mime_type: str

QueryResponse_initialized = bool

QueryResponse_is_deposit_token = bool

QueryResponse_is_handler = bool

Addr = str

LogoInfo__url__url = str

class LogoInfo__url(TypedDict):
	url: str

LogoInfo__item_1 = str

LogoInfo = Union["LogoInfo__url", str]

QueryResponse_marketing_info__description = Optional[str]

QueryResponse_marketing_info__logo = Optional["LogoInfo"]

QueryResponse_marketing_info__marketing = Optional["Addr"]

QueryResponse_marketing_info__project = Optional[str]

class QueryResponse_marketing_info(TypedDict):
	description: str
	logo: "QueryResponse_marketing_info__logo"
	marketing: "QueryResponse_marketing_info__marketing"
	project: str

QueryResponse_minter__cap = Optional["Uint128"]

QueryResponse_minter__minter = str

class QueryResponse_minter(TypedDict):
	cap: "QueryResponse_minter__cap"
	minter: str

QueryResponse_reward_token = str

QueryResponse_reward_tracker_state__in_private_claiming_mode = bool

QueryResponse_reward_tracker_state__in_private_staking_mode = bool

QueryResponse_reward_tracker_state__in_private_transfer_mode = bool

class QueryResponse_reward_tracker_state(TypedDict):
	admin: "Addr"
	cumulative_reward_per_token: "Uint128"
	distributor: "Addr"
	in_private_claiming_mode: bool
	in_private_staking_mode: bool
	in_private_transfer_mode: bool
	vault: "Addr"

QueryResponse_staked_amount = str

QueryResponse_token_info__decimals = int

QueryResponse_token_info__name = str

QueryResponse_token_info__symbol = str

class QueryResponse_token_info(TypedDict):
	decimals: int
	name: str
	symbol: str
	total_supply: "Uint128"

QueryResponse_total_deposit_supply = str

class EmbeddedLogo__svg(TypedDict):
	svg: "Binary"

class EmbeddedLogo__png(TypedDict):
	png: "Binary"

EmbeddedLogo = Union["EmbeddedLogo__svg", "EmbeddedLogo__png"]

Logo__url__url = str

class Logo__url(TypedDict):
	url: str

class Logo__embedded(TypedDict):
	embedded: "EmbeddedLogo"

Logo = Union["Logo__url", "Logo__embedded"]

ExecuteMsg__initialize__initialize__distributor = str

class ExecuteMsg__initialize__initialize(TypedDict):
	distributor: str

class ExecuteMsg__initialize(TypedDict):
	initialize: "ExecuteMsg__initialize__initialize"

ExecuteMsg__transfer__transfer__recipient = str

class ExecuteMsg__transfer__transfer(TypedDict):
	amount: "Uint128"
	recipient: str

class ExecuteMsg__transfer(TypedDict):
	transfer: "ExecuteMsg__transfer__transfer"

class ExecuteMsg__burn__burn(TypedDict):
	amount: "Uint128"

class ExecuteMsg__burn(TypedDict):
	burn: "ExecuteMsg__burn__burn"

ExecuteMsg__send__send__contract = str

class ExecuteMsg__send__send(TypedDict):
	amount: "Uint128"
	contract: str
	msg: "Binary"

class ExecuteMsg__send(TypedDict):
	send: "ExecuteMsg__send__send"

ExecuteMsg__increase_allowance__increase_allowance__expires = Optional["Expiration"]

ExecuteMsg__increase_allowance__increase_allowance__spender = str

class ExecuteMsg__increase_allowance__increase_allowance(TypedDict):
	amount: "Uint128"
	expires: "ExecuteMsg__increase_allowance__increase_allowance__expires"
	spender: str

class ExecuteMsg__increase_allowance(TypedDict):
	increase_allowance: "ExecuteMsg__increase_allowance__increase_allowance"

ExecuteMsg__decrease_allowance__decrease_allowance__expires = Optional["Expiration"]

ExecuteMsg__decrease_allowance__decrease_allowance__spender = str

class ExecuteMsg__decrease_allowance__decrease_allowance(TypedDict):
	amount: "Uint128"
	expires: "ExecuteMsg__decrease_allowance__decrease_allowance__expires"
	spender: str

class ExecuteMsg__decrease_allowance(TypedDict):
	decrease_allowance: "ExecuteMsg__decrease_allowance__decrease_allowance"

ExecuteMsg__transfer_from__transfer_from__owner = str

ExecuteMsg__transfer_from__transfer_from__recipient = str

class ExecuteMsg__transfer_from__transfer_from(TypedDict):
	amount: "Uint128"
	owner: str
	recipient: str

class ExecuteMsg__transfer_from(TypedDict):
	transfer_from: "ExecuteMsg__transfer_from__transfer_from"

ExecuteMsg__send_from__send_from__contract = str

ExecuteMsg__send_from__send_from__owner = str

class ExecuteMsg__send_from__send_from(TypedDict):
	amount: "Uint128"
	contract: str
	msg: "Binary"
	owner: str

class ExecuteMsg__send_from(TypedDict):
	send_from: "ExecuteMsg__send_from__send_from"

ExecuteMsg__burn_from__burn_from__owner = str

class ExecuteMsg__burn_from__burn_from(TypedDict):
	amount: "Uint128"
	owner: str

class ExecuteMsg__burn_from(TypedDict):
	burn_from: "ExecuteMsg__burn_from__burn_from"

ExecuteMsg__mint__mint__recipient = str

class ExecuteMsg__mint__mint(TypedDict):
	amount: "Uint128"
	recipient: str

class ExecuteMsg__mint(TypedDict):
	mint: "ExecuteMsg__mint__mint"

ExecuteMsg__update_minter__update_minter__new_minter = Optional[str]

class ExecuteMsg__update_minter__update_minter(TypedDict):
	new_minter: str

class ExecuteMsg__update_minter(TypedDict):
	update_minter: "ExecuteMsg__update_minter__update_minter"

ExecuteMsg__update_marketing__update_marketing__description = Optional[str]

ExecuteMsg__update_marketing__update_marketing__marketing = Optional[str]

ExecuteMsg__update_marketing__update_marketing__project = Optional[str]

class ExecuteMsg__update_marketing__update_marketing(TypedDict):
	description: str
	marketing: str
	project: str

class ExecuteMsg__update_marketing(TypedDict):
	update_marketing: "ExecuteMsg__update_marketing__update_marketing"

class ExecuteMsg__upload_logo(TypedDict):
	upload_logo: "Logo"

ExecuteMsg__set_admin__set_admin__account = str

class ExecuteMsg__set_admin__set_admin(TypedDict):
	account: str

class ExecuteMsg__set_admin(TypedDict):
	set_admin: "ExecuteMsg__set_admin__set_admin"

ExecuteMsg__set_in_private_transfer_mode__set_in_private_transfer_mode__value = bool

class ExecuteMsg__set_in_private_transfer_mode__set_in_private_transfer_mode(TypedDict):
	value: bool

class ExecuteMsg__set_in_private_transfer_mode(TypedDict):
	set_in_private_transfer_mode: "ExecuteMsg__set_in_private_transfer_mode__set_in_private_transfer_mode"

ExecuteMsg__set_in_private_claiming_mode__set_in_private_claiming_mode__value = bool

class ExecuteMsg__set_in_private_claiming_mode__set_in_private_claiming_mode(TypedDict):
	value: bool

class ExecuteMsg__set_in_private_claiming_mode(TypedDict):
	set_in_private_claiming_mode: "ExecuteMsg__set_in_private_claiming_mode__set_in_private_claiming_mode"

ExecuteMsg__set_in_private_staking_mode__set_in_private_staking_mode__value = bool

class ExecuteMsg__set_in_private_staking_mode__set_in_private_staking_mode(TypedDict):
	value: bool

class ExecuteMsg__set_in_private_staking_mode(TypedDict):
	set_in_private_staking_mode: "ExecuteMsg__set_in_private_staking_mode__set_in_private_staking_mode"

ExecuteMsg__set_handler__set_handler__account = str

ExecuteMsg__set_handler__set_handler__is_handler = bool

class ExecuteMsg__set_handler__set_handler(TypedDict):
	account: str
	is_handler: bool

class ExecuteMsg__set_handler(TypedDict):
	set_handler: "ExecuteMsg__set_handler__set_handler"

ExecuteMsg__set_deposit_token__set_deposit_token__is_deposit_token = bool

ExecuteMsg__set_deposit_token__set_deposit_token__token = str

class ExecuteMsg__set_deposit_token__set_deposit_token(TypedDict):
	is_deposit_token: bool
	token: str

class ExecuteMsg__set_deposit_token(TypedDict):
	set_deposit_token: "ExecuteMsg__set_deposit_token__set_deposit_token"

ExecuteMsg__stake__stake__deposit_token = str

class ExecuteMsg__stake__stake(TypedDict):
	amount: "Uint128"
	deposit_token: str

class ExecuteMsg__stake(TypedDict):
	stake: "ExecuteMsg__stake__stake"

ExecuteMsg__stake_for_account__stake_for_account__account = str

ExecuteMsg__stake_for_account__stake_for_account__deposit_token = str

ExecuteMsg__stake_for_account__stake_for_account__funding_account = str

class ExecuteMsg__stake_for_account__stake_for_account(TypedDict):
	account: str
	amount: "Uint128"
	deposit_token: str
	funding_account: str

class ExecuteMsg__stake_for_account(TypedDict):
	stake_for_account: "ExecuteMsg__stake_for_account__stake_for_account"

ExecuteMsg__unstake__unstake__deposit_token = str

class ExecuteMsg__unstake__unstake(TypedDict):
	amount: "Uint128"
	deposit_token: str

class ExecuteMsg__unstake(TypedDict):
	unstake: "ExecuteMsg__unstake__unstake"

ExecuteMsg__unstake_for_account__unstake_for_account__account = str

ExecuteMsg__unstake_for_account__unstake_for_account__deposit_token = str

ExecuteMsg__unstake_for_account__unstake_for_account__recipient = str

class ExecuteMsg__unstake_for_account__unstake_for_account(TypedDict):
	account: str
	amount: "Uint128"
	deposit_token: str
	recipient: str

class ExecuteMsg__unstake_for_account(TypedDict):
	unstake_for_account: "ExecuteMsg__unstake_for_account__unstake_for_account"

class ExecuteMsg__update_rewards__update_rewards(TypedDict):
	pass

class ExecuteMsg__update_rewards(TypedDict):
	update_rewards: "ExecuteMsg__update_rewards__update_rewards"

ExecuteMsg__claim__claim__recipient = str

class ExecuteMsg__claim__claim(TypedDict):
	recipient: str

class ExecuteMsg__claim(TypedDict):
	claim: "ExecuteMsg__claim__claim"

ExecuteMsg__claim_for_account__claim_for_account__account = str

ExecuteMsg__claim_for_account__claim_for_account__recipient = str

class ExecuteMsg__claim_for_account__claim_for_account(TypedDict):
	account: str
	recipient: str

class ExecuteMsg__claim_for_account(TypedDict):
	claim_for_account: "ExecuteMsg__claim_for_account__claim_for_account"

ExecuteMsg = Union["ExecuteMsg__initialize", "ExecuteMsg__transfer", "ExecuteMsg__burn", "ExecuteMsg__send", "ExecuteMsg__increase_allowance", "ExecuteMsg__decrease_allowance", "ExecuteMsg__transfer_from", "ExecuteMsg__send_from", "ExecuteMsg__burn_from", "ExecuteMsg__mint", "ExecuteMsg__update_minter", "ExecuteMsg__update_marketing", "ExecuteMsg__upload_logo", "ExecuteMsg__set_admin", "ExecuteMsg__set_in_private_transfer_mode", "ExecuteMsg__set_in_private_claiming_mode", "ExecuteMsg__set_in_private_staking_mode", "ExecuteMsg__set_handler", "ExecuteMsg__set_deposit_token", "ExecuteMsg__stake", "ExecuteMsg__stake_for_account", "ExecuteMsg__unstake", "ExecuteMsg__unstake_for_account", "ExecuteMsg__update_rewards", "ExecuteMsg__claim", "ExecuteMsg__claim_for_account"]

QueryMsg__balance__balance__address = str

class QueryMsg__balance__balance(TypedDict):
	address: str

class QueryMsg__balance(TypedDict):
	balance: "QueryMsg__balance__balance"

class QueryMsg__token_info__token_info(TypedDict):
	pass

class QueryMsg__token_info(TypedDict):
	token_info: "QueryMsg__token_info__token_info"

class QueryMsg__minter__minter(TypedDict):
	pass

class QueryMsg__minter(TypedDict):
	minter: "QueryMsg__minter__minter"

QueryMsg__allowance__allowance__owner = str

QueryMsg__allowance__allowance__spender = str

class QueryMsg__allowance__allowance(TypedDict):
	owner: str
	spender: str

class QueryMsg__allowance(TypedDict):
	allowance: "QueryMsg__allowance__allowance"

QueryMsg__all_allowances__all_allowances__limit = Optional[int]

QueryMsg__all_allowances__all_allowances__owner = str

QueryMsg__all_allowances__all_allowances__start_after = Optional[str]

class QueryMsg__all_allowances__all_allowances(TypedDict):
	limit: int
	owner: str
	start_after: str

class QueryMsg__all_allowances(TypedDict):
	all_allowances: "QueryMsg__all_allowances__all_allowances"

QueryMsg__all_spender_allowances__all_spender_allowances__limit = Optional[int]

QueryMsg__all_spender_allowances__all_spender_allowances__spender = str

QueryMsg__all_spender_allowances__all_spender_allowances__start_after = Optional[str]

class QueryMsg__all_spender_allowances__all_spender_allowances(TypedDict):
	limit: int
	spender: str
	start_after: str

class QueryMsg__all_spender_allowances(TypedDict):
	all_spender_allowances: "QueryMsg__all_spender_allowances__all_spender_allowances"

QueryMsg__all_accounts__all_accounts__limit = Optional[int]

QueryMsg__all_accounts__all_accounts__start_after = Optional[str]

class QueryMsg__all_accounts__all_accounts(TypedDict):
	limit: int
	start_after: str

class QueryMsg__all_accounts(TypedDict):
	all_accounts: "QueryMsg__all_accounts__all_accounts"

class QueryMsg__marketing_info__marketing_info(TypedDict):
	pass

class QueryMsg__marketing_info(TypedDict):
	marketing_info: "QueryMsg__marketing_info__marketing_info"

class QueryMsg__download_logo__download_logo(TypedDict):
	pass

class QueryMsg__download_logo(TypedDict):
	download_logo: "QueryMsg__download_logo__download_logo"

QueryMsg__claimable__claimable__account = str

class QueryMsg__claimable__claimable(TypedDict):
	account: str

class QueryMsg__claimable(TypedDict):
	claimable: "QueryMsg__claimable__claimable"

QueryMsg__deposit_balance__deposit_balance__account = str

QueryMsg__deposit_balance__deposit_balance__token = str

class QueryMsg__deposit_balance__deposit_balance(TypedDict):
	account: str
	token: str

class QueryMsg__deposit_balance(TypedDict):
	deposit_balance: "QueryMsg__deposit_balance__deposit_balance"

QueryMsg__cumulative_rewards__cumulative_rewards__account = str

class QueryMsg__cumulative_rewards__cumulative_rewards(TypedDict):
	account: str

class QueryMsg__cumulative_rewards(TypedDict):
	cumulative_rewards: "QueryMsg__cumulative_rewards__cumulative_rewards"

QueryMsg__average_staked_amount__average_staked_amount__account = str

class QueryMsg__average_staked_amount__average_staked_amount(TypedDict):
	account: str

class QueryMsg__average_staked_amount(TypedDict):
	average_staked_amount: "QueryMsg__average_staked_amount__average_staked_amount"

QueryMsg__total_deposit_supply__total_deposit_supply__token = str

class QueryMsg__total_deposit_supply__total_deposit_supply(TypedDict):
	token: str

class QueryMsg__total_deposit_supply(TypedDict):
	total_deposit_supply: "QueryMsg__total_deposit_supply__total_deposit_supply"

QueryMsg__staked_amount__staked_amount__account = str

class QueryMsg__staked_amount__staked_amount(TypedDict):
	account: str

class QueryMsg__staked_amount(TypedDict):
	staked_amount: "QueryMsg__staked_amount__staked_amount"

class QueryMsg__reward_token__reward_token(TypedDict):
	pass

class QueryMsg__reward_token(TypedDict):
	reward_token: "QueryMsg__reward_token__reward_token"

class QueryMsg__initialized__initialized(TypedDict):
	pass

class QueryMsg__initialized(TypedDict):
	initialized: "QueryMsg__initialized__initialized"

QueryMsg__is_handler__is_handler__account = str

class QueryMsg__is_handler__is_handler(TypedDict):
	account: str

class QueryMsg__is_handler(TypedDict):
	is_handler: "QueryMsg__is_handler__is_handler"

QueryMsg__is_deposit_token__is_deposit_token__token = str

class QueryMsg__is_deposit_token__is_deposit_token(TypedDict):
	token: str

class QueryMsg__is_deposit_token(TypedDict):
	is_deposit_token: "QueryMsg__is_deposit_token__is_deposit_token"

class QueryMsg__reward_tracker_state__reward_tracker_state(TypedDict):
	pass

class QueryMsg__reward_tracker_state(TypedDict):
	reward_tracker_state: "QueryMsg__reward_tracker_state__reward_tracker_state"

QueryMsg = Union["QueryMsg__balance", "QueryMsg__token_info", "QueryMsg__minter", "QueryMsg__allowance", "QueryMsg__all_allowances", "QueryMsg__all_spender_allowances", "QueryMsg__all_accounts", "QueryMsg__marketing_info", "QueryMsg__download_logo", "QueryMsg__claimable", "QueryMsg__deposit_balance", "QueryMsg__cumulative_rewards", "QueryMsg__average_staked_amount", "QueryMsg__total_deposit_supply", "QueryMsg__staked_amount", "QueryMsg__reward_token", "QueryMsg__initialized", "QueryMsg__is_handler", "QueryMsg__is_deposit_token", "QueryMsg__reward_tracker_state"]



class OmxCwRewardTracker(BaseOmxClient):
	def clone(self) -> "OmxCwRewardTracker":
		instance = self.__class__.__new__(self.__class__)
		instance.tx = self.tx
		instance.gas = self.gas
		instance.contract = self.contract
		instance.wallet = self.wallet
		instance.funds = self.funds
		return instance

	def with_funds(self, funds: str) -> "OmxCwRewardTracker":
		o = self.clone()
		o.funds = funds
		return o

	def without_funds(self) -> "OmxCwRewardTracker":
		o = self.clone()
		o.funds = None
		return o

	def with_wallet(self, wallet: Wallet) -> "OmxCwRewardTracker":
		o = self.clone()
		o.wallet = wallet
		return o

	def initialize(self, distributor: str) -> SubmittedTx:
		return self.execute({"initialize": {"distributor": distributor}})

	def transfer(self, amount: "Uint128", recipient: str) -> SubmittedTx:
		return self.execute({"transfer": {"amount": amount, "recipient": recipient}})

	def burn(self, amount: "Uint128") -> SubmittedTx:
		return self.execute({"burn": {"amount": amount}})

	def send(self, amount: "Uint128", contract: str, msg: "Binary") -> SubmittedTx:
		return self.execute({"send": {"amount": amount, "contract": contract, "msg": msg}})

	def increase_allowance(self, amount: "Uint128", spender: str, expires: "ExecuteMsg__increase_allowance__increase_allowance__expires" = None) -> SubmittedTx:
		return self.execute({"increase_allowance": {"amount": amount, "spender": spender, "expires": expires}})

	def decrease_allowance(self, amount: "Uint128", spender: str, expires: "ExecuteMsg__decrease_allowance__decrease_allowance__expires" = None) -> SubmittedTx:
		return self.execute({"decrease_allowance": {"amount": amount, "spender": spender, "expires": expires}})

	def transfer_from(self, amount: "Uint128", owner: str, recipient: str) -> SubmittedTx:
		return self.execute({"transfer_from": {"amount": amount, "owner": owner, "recipient": recipient}})

	def send_from(self, amount: "Uint128", contract: str, msg: "Binary", owner: str) -> SubmittedTx:
		return self.execute({"send_from": {"amount": amount, "contract": contract, "msg": msg, "owner": owner}})

	def burn_from(self, amount: "Uint128", owner: str) -> SubmittedTx:
		return self.execute({"burn_from": {"amount": amount, "owner": owner}})

	def mint(self, amount: "Uint128", recipient: str) -> SubmittedTx:
		return self.execute({"mint": {"amount": amount, "recipient": recipient}})

	def update_minter(self, new_minter: str) -> SubmittedTx:
		return self.execute({"update_minter": {"new_minter": new_minter}})

	def update_marketing(self, description: str, marketing: str, project: str) -> SubmittedTx:
		return self.execute({"update_marketing": {"description": description, "marketing": marketing, "project": project}})

	def upload_logo(self, value: Union["Logo__url", "Logo__embedded"]) -> SubmittedTx:
		return self.execute({"upload_logo": value})

	def set_admin(self, account: str) -> SubmittedTx:
		return self.execute({"set_admin": {"account": account}})

	def set_in_private_transfer_mode(self, value: bool) -> SubmittedTx:
		return self.execute({"set_in_private_transfer_mode": {"value": value}})

	def set_in_private_claiming_mode(self, value: bool) -> SubmittedTx:
		return self.execute({"set_in_private_claiming_mode": {"value": value}})

	def set_in_private_staking_mode(self, value: bool) -> SubmittedTx:
		return self.execute({"set_in_private_staking_mode": {"value": value}})

	def set_handler(self, account: str, is_handler: bool) -> SubmittedTx:
		return self.execute({"set_handler": {"account": account, "is_handler": is_handler}})

	def set_deposit_token(self, is_deposit_token: bool, token: str) -> SubmittedTx:
		return self.execute({"set_deposit_token": {"is_deposit_token": is_deposit_token, "token": token}})

	def stake(self, amount: "Uint128", deposit_token: str) -> SubmittedTx:
		return self.execute({"stake": {"amount": amount, "deposit_token": deposit_token}})

	def stake_for_account(self, account: str, amount: "Uint128", deposit_token: str, funding_account: str) -> SubmittedTx:
		return self.execute({"stake_for_account": {"account": account, "amount": amount, "deposit_token": deposit_token, "funding_account": funding_account}})

	def unstake(self, amount: "Uint128", deposit_token: str) -> SubmittedTx:
		return self.execute({"unstake": {"amount": amount, "deposit_token": deposit_token}})

	def unstake_for_account(self, account: str, amount: "Uint128", deposit_token: str, recipient: str) -> SubmittedTx:
		return self.execute({"unstake_for_account": {"account": account, "amount": amount, "deposit_token": deposit_token, "recipient": recipient}})

	def update_rewards(self) -> SubmittedTx:
		return self.execute({"update_rewards": {}})

	def claim(self, recipient: str) -> SubmittedTx:
		return self.execute({"claim": {"recipient": recipient}})

	def claim_for_account(self, account: str, recipient: str) -> SubmittedTx:
		return self.execute({"claim_for_account": {"account": account, "recipient": recipient}})

	def balance(self, address: str) -> "QueryResponse_balance":
		return self.query({"balance": {"address": address}})

	def token_info(self) -> "QueryResponse_token_info":
		return self.query({"token_info": {}})

	def minter(self) -> "QueryResponse_minter":
		return self.query({"minter": {}})

	def allowance(self, owner: str, spender: str) -> "QueryResponse_allowance":
		return self.query({"allowance": {"owner": owner, "spender": spender}})

	def all_allowances(self, limit: int, owner: str, start_after: str) -> "QueryResponse_all_allowances":
		return self.query({"all_allowances": {"limit": limit, "owner": owner, "start_after": start_after}})

	def all_spender_allowances(self, limit: int, spender: str, start_after: str) -> "QueryResponse_all_spender_allowances":
		return self.query({"all_spender_allowances": {"limit": limit, "spender": spender, "start_after": start_after}})

	def all_accounts(self, limit: int, start_after: str) -> "QueryResponse_all_accounts":
		return self.query({"all_accounts": {"limit": limit, "start_after": start_after}})

	def marketing_info(self) -> "QueryResponse_marketing_info":
		return self.query({"marketing_info": {}})

	def download_logo(self) -> "QueryResponse_download_logo":
		return self.query({"download_logo": {}})

	def claimable(self, account: str) -> "QueryResponse_claimable":
		return self.query({"claimable": {"account": account}})

	def deposit_balance(self, account: str, token: str) -> "QueryResponse_deposit_balance":
		return self.query({"deposit_balance": {"account": account, "token": token}})

	def cumulative_rewards(self, account: str) -> "QueryResponse_cumulative_rewards":
		return self.query({"cumulative_rewards": {"account": account}})

	def average_staked_amount(self, account: str) -> "QueryResponse_average_staked_amount":
		return self.query({"average_staked_amount": {"account": account}})

	def total_deposit_supply(self, token: str) -> "QueryResponse_total_deposit_supply":
		return self.query({"total_deposit_supply": {"token": token}})

	def staked_amount(self, account: str) -> "QueryResponse_staked_amount":
		return self.query({"staked_amount": {"account": account}})

	def reward_token(self) -> "QueryResponse_reward_token":
		return self.query({"reward_token": {}})

	def initialized(self) -> "QueryResponse_initialized":
		return self.query({"initialized": {}})

	def is_handler(self, account: str) -> "QueryResponse_is_handler":
		return self.query({"is_handler": {"account": account}})

	def is_deposit_token(self, token: str) -> "QueryResponse_is_deposit_token":
		return self.query({"is_deposit_token": {"token": token}})

	def reward_tracker_state(self) -> "QueryResponse_reward_tracker_state":
		return self.query({"reward_tracker_state": {}})
