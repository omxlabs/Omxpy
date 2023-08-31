from omxpy.base_client import BaseOmxClient
from cosmpy.aerial.tx_helpers import SubmittedTx
from cosmpy.aerial.wallet import Wallet
from typing import List, TypedDict, Tuple, Union, Optional


QueryResponse_all_accounts__accounts__item = str

QueryResponse_all_accounts__accounts = List[str]

class QueryResponse_all_accounts(TypedDict):
	accounts: "QueryResponse_all_accounts__accounts"

Uint128 = str

class QueryResponse_balance(TypedDict):
	balance: "Uint128"

QueryResponse_bonus_reward = str

QueryResponse_claimable = str

QueryResponse_claimed_amount = str

QueryResponse_combined_average_staked_amount = str

QueryResponse_cumulative_claim_amount = str

QueryResponse_cumulative_reward_deduction = str

Binary = str

QueryResponse_download_logo__mime_type = str

class QueryResponse_download_logo(TypedDict):
	data: "Binary"
	mime_type: str

Uint64 = str

QueryResponse_last_vesting_time = Tuple["Uint64"]

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

QueryResponse_max_vestable_amount = str

QueryResponse_pair_amount = str

QueryResponse_raw_pair_amount = str

QueryResponse_reward_tracker = Optional["Addr"]

QueryResponse_token_info__decimals = int

QueryResponse_token_info__name = str

QueryResponse_token_info__symbol = str

class QueryResponse_token_info(TypedDict):
	decimals: int
	name: str
	symbol: str
	total_supply: "Uint128"

QueryResponse_total_vested = str

QueryResponse_transferred_average_staked_amount = str

QueryResponse_transferred_cumulative_reward = str

QueryResponse_vested_amount = str

QueryResponse_vester_state__has_max_vestable_amount = bool

QueryResponse_vester_state__pair_token = Optional["Addr"]

QueryResponse_vester_state__reward_tracker = Optional["Addr"]

QueryResponse_vester_state__vesting_duration_sec = int

class QueryResponse_vester_state(TypedDict):
	claimable_token: "Addr"
	es_token: "Addr"
	has_max_vestable_amount: bool
	pair_supply: "Uint128"
	pair_token: "QueryResponse_vester_state__pair_token"
	reward_tracker: "QueryResponse_vester_state__reward_tracker"
	vesting_duration_sec: int

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

class ExecuteMsg__burn__burn(TypedDict):
	amount: "Uint128"

class ExecuteMsg__burn(TypedDict):
	burn: "ExecuteMsg__burn__burn"

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

ExecuteMsg__add_admin__add_admin__account = str

class ExecuteMsg__add_admin__add_admin(TypedDict):
	account: str

class ExecuteMsg__add_admin(TypedDict):
	add_admin: "ExecuteMsg__add_admin__add_admin"

ExecuteMsg__remove_admin__remove_admin__account = str

class ExecuteMsg__remove_admin__remove_admin(TypedDict):
	account: str

class ExecuteMsg__remove_admin(TypedDict):
	remove_admin: "ExecuteMsg__remove_admin__remove_admin"

ExecuteMsg__set_has_max_vestable_amount__set_has_max_vestable_amount__value = bool

class ExecuteMsg__set_has_max_vestable_amount__set_has_max_vestable_amount(TypedDict):
	value: bool

class ExecuteMsg__set_has_max_vestable_amount(TypedDict):
	set_has_max_vestable_amount: "ExecuteMsg__set_has_max_vestable_amount__set_has_max_vestable_amount"

ExecuteMsg__set_handler__set_handler__account = str

ExecuteMsg__set_handler__set_handler__is_handler = bool

class ExecuteMsg__set_handler__set_handler(TypedDict):
	account: str
	is_handler: bool

class ExecuteMsg__set_handler(TypedDict):
	set_handler: "ExecuteMsg__set_handler__set_handler"

class ExecuteMsg__deposit__deposit(TypedDict):
	amount: "Uint128"

class ExecuteMsg__deposit(TypedDict):
	deposit: "ExecuteMsg__deposit__deposit"

class ExecuteMsg__deposit_cb__deposit_cb(TypedDict):
	account: "Addr"
	amount: "Uint128"

class ExecuteMsg__deposit_cb(TypedDict):
	deposit_cb: "ExecuteMsg__deposit_cb__deposit_cb"

ExecuteMsg__deposit_for_account__deposit_for_account__account = str

class ExecuteMsg__deposit_for_account__deposit_for_account(TypedDict):
	account: str
	amount: "Uint128"

class ExecuteMsg__deposit_for_account(TypedDict):
	deposit_for_account: "ExecuteMsg__deposit_for_account__deposit_for_account"

class ExecuteMsg__claim__claim(TypedDict):
	pass

class ExecuteMsg__claim(TypedDict):
	claim: "ExecuteMsg__claim__claim"

ExecuteMsg__claim_for_account__claim_for_account__account = str

ExecuteMsg__claim_for_account__claim_for_account__recipient = str

class ExecuteMsg__claim_for_account__claim_for_account(TypedDict):
	account: str
	recipient: str

class ExecuteMsg__claim_for_account(TypedDict):
	claim_for_account: "ExecuteMsg__claim_for_account__claim_for_account"

class ExecuteMsg__withdraw__withdraw(TypedDict):
	pass

class ExecuteMsg__withdraw(TypedDict):
	withdraw: "ExecuteMsg__withdraw__withdraw"

ExecuteMsg__transfer_stake_values__transfer_stake_values__recipient = str

ExecuteMsg__transfer_stake_values__transfer_stake_values__sender = str

class ExecuteMsg__transfer_stake_values__transfer_stake_values(TypedDict):
	recipient: str
	sender: str

class ExecuteMsg__transfer_stake_values(TypedDict):
	transfer_stake_values: "ExecuteMsg__transfer_stake_values__transfer_stake_values"

ExecuteMsg__set_transferred_average_staked_amounts__set_transferred_average_staked_amounts__account = str

class ExecuteMsg__set_transferred_average_staked_amounts__set_transferred_average_staked_amounts(TypedDict):
	account: str
	amount: "Uint128"

class ExecuteMsg__set_transferred_average_staked_amounts(TypedDict):
	set_transferred_average_staked_amounts: "ExecuteMsg__set_transferred_average_staked_amounts__set_transferred_average_staked_amounts"

ExecuteMsg__set_transferred_cumulative_rewards__set_transferred_cumulative_rewards__account = str

class ExecuteMsg__set_transferred_cumulative_rewards__set_transferred_cumulative_rewards(TypedDict):
	account: str
	amount: "Uint128"

class ExecuteMsg__set_transferred_cumulative_rewards(TypedDict):
	set_transferred_cumulative_rewards: "ExecuteMsg__set_transferred_cumulative_rewards__set_transferred_cumulative_rewards"

ExecuteMsg__set_cumulative_reward_deductions__set_cumulative_reward_deductions__account = str

class ExecuteMsg__set_cumulative_reward_deductions__set_cumulative_reward_deductions(TypedDict):
	account: str
	amount: "Uint128"

class ExecuteMsg__set_cumulative_reward_deductions(TypedDict):
	set_cumulative_reward_deductions: "ExecuteMsg__set_cumulative_reward_deductions__set_cumulative_reward_deductions"

ExecuteMsg__set_bonus_rewards__set_bonus_rewards__account = str

class ExecuteMsg__set_bonus_rewards__set_bonus_rewards(TypedDict):
	account: str
	amount: "Uint128"

class ExecuteMsg__set_bonus_rewards(TypedDict):
	set_bonus_rewards: "ExecuteMsg__set_bonus_rewards__set_bonus_rewards"

ExecuteMsg = Union["ExecuteMsg__burn", "ExecuteMsg__send_from", "ExecuteMsg__burn_from", "ExecuteMsg__update_marketing", "ExecuteMsg__upload_logo", "ExecuteMsg__add_admin", "ExecuteMsg__remove_admin", "ExecuteMsg__set_has_max_vestable_amount", "ExecuteMsg__set_handler", "ExecuteMsg__deposit", "ExecuteMsg__deposit_cb", "ExecuteMsg__deposit_for_account", "ExecuteMsg__claim", "ExecuteMsg__claim_for_account", "ExecuteMsg__withdraw", "ExecuteMsg__transfer_stake_values", "ExecuteMsg__set_transferred_average_staked_amounts", "ExecuteMsg__set_transferred_cumulative_rewards", "ExecuteMsg__set_cumulative_reward_deductions", "ExecuteMsg__set_bonus_rewards"]

QueryMsg__balance__balance__address = str

class QueryMsg__balance__balance(TypedDict):
	address: str

class QueryMsg__balance(TypedDict):
	balance: "QueryMsg__balance__balance"

class QueryMsg__token_info__token_info(TypedDict):
	pass

class QueryMsg__token_info(TypedDict):
	token_info: "QueryMsg__token_info__token_info"

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

QueryMsg__max_vestable_amount__max_vestable_amount__account = str

class QueryMsg__max_vestable_amount__max_vestable_amount(TypedDict):
	account: str

class QueryMsg__max_vestable_amount(TypedDict):
	max_vestable_amount: "QueryMsg__max_vestable_amount__max_vestable_amount"

QueryMsg__combined_average_staked_amount__combined_average_staked_amount__account = str

class QueryMsg__combined_average_staked_amount__combined_average_staked_amount(TypedDict):
	account: str

class QueryMsg__combined_average_staked_amount(TypedDict):
	combined_average_staked_amount: "QueryMsg__combined_average_staked_amount__combined_average_staked_amount"

QueryMsg__cumulative_claim_amount__cumulative_claim_amount__account = str

class QueryMsg__cumulative_claim_amount__cumulative_claim_amount(TypedDict):
	account: str

class QueryMsg__cumulative_claim_amount(TypedDict):
	cumulative_claim_amount: "QueryMsg__cumulative_claim_amount__cumulative_claim_amount"

QueryMsg__claimed_amount__claimed_amount__account = str

class QueryMsg__claimed_amount__claimed_amount(TypedDict):
	account: str

class QueryMsg__claimed_amount(TypedDict):
	claimed_amount: "QueryMsg__claimed_amount__claimed_amount"

QueryMsg__pair_amount__pair_amount__account = str

class QueryMsg__pair_amount__pair_amount(TypedDict):
	account: str
	es_amount: "Uint128"

class QueryMsg__pair_amount(TypedDict):
	pair_amount: "QueryMsg__pair_amount__pair_amount"

QueryMsg__last_vesting_time__last_vesting_time__account = str

class QueryMsg__last_vesting_time__last_vesting_time(TypedDict):
	account: str

class QueryMsg__last_vesting_time(TypedDict):
	last_vesting_time: "QueryMsg__last_vesting_time__last_vesting_time"

QueryMsg__raw_pair_amount__raw_pair_amount__account = str

class QueryMsg__raw_pair_amount__raw_pair_amount(TypedDict):
	account: str

class QueryMsg__raw_pair_amount(TypedDict):
	raw_pair_amount: "QueryMsg__raw_pair_amount__raw_pair_amount"

class QueryMsg__reward_tracker__reward_tracker(TypedDict):
	pass

class QueryMsg__reward_tracker(TypedDict):
	reward_tracker: "QueryMsg__reward_tracker__reward_tracker"

QueryMsg__total_vested__total_vested__account = str

class QueryMsg__total_vested__total_vested(TypedDict):
	account: str

class QueryMsg__total_vested(TypedDict):
	total_vested: "QueryMsg__total_vested__total_vested"

QueryMsg__vested_amount__vested_amount__account = str

class QueryMsg__vested_amount__vested_amount(TypedDict):
	account: str

class QueryMsg__vested_amount(TypedDict):
	vested_amount: "QueryMsg__vested_amount__vested_amount"

class QueryMsg__vester_state__vester_state(TypedDict):
	pass

class QueryMsg__vester_state(TypedDict):
	vester_state: "QueryMsg__vester_state__vester_state"

QueryMsg__transferred_average_staked_amount__transferred_average_staked_amount__account = str

class QueryMsg__transferred_average_staked_amount__transferred_average_staked_amount(TypedDict):
	account: str

class QueryMsg__transferred_average_staked_amount(TypedDict):
	transferred_average_staked_amount: "QueryMsg__transferred_average_staked_amount__transferred_average_staked_amount"

QueryMsg__transferred_cumulative_reward__transferred_cumulative_reward__account = str

class QueryMsg__transferred_cumulative_reward__transferred_cumulative_reward(TypedDict):
	account: str

class QueryMsg__transferred_cumulative_reward(TypedDict):
	transferred_cumulative_reward: "QueryMsg__transferred_cumulative_reward__transferred_cumulative_reward"

QueryMsg__cumulative_reward_deduction__cumulative_reward_deduction__account = str

class QueryMsg__cumulative_reward_deduction__cumulative_reward_deduction(TypedDict):
	account: str

class QueryMsg__cumulative_reward_deduction(TypedDict):
	cumulative_reward_deduction: "QueryMsg__cumulative_reward_deduction__cumulative_reward_deduction"

QueryMsg__bonus_reward__bonus_reward__account = str

class QueryMsg__bonus_reward__bonus_reward(TypedDict):
	account: str

class QueryMsg__bonus_reward(TypedDict):
	bonus_reward: "QueryMsg__bonus_reward__bonus_reward"

QueryMsg = Union["QueryMsg__balance", "QueryMsg__token_info", "QueryMsg__all_accounts", "QueryMsg__marketing_info", "QueryMsg__download_logo", "QueryMsg__claimable", "QueryMsg__max_vestable_amount", "QueryMsg__combined_average_staked_amount", "QueryMsg__cumulative_claim_amount", "QueryMsg__claimed_amount", "QueryMsg__pair_amount", "QueryMsg__last_vesting_time", "QueryMsg__raw_pair_amount", "QueryMsg__reward_tracker", "QueryMsg__total_vested", "QueryMsg__vested_amount", "QueryMsg__vester_state", "QueryMsg__transferred_average_staked_amount", "QueryMsg__transferred_cumulative_reward", "QueryMsg__cumulative_reward_deduction", "QueryMsg__bonus_reward"]



class OmxCwVester(BaseOmxClient):
	def clone(self) -> "OmxCwVester":
		instance = self.__class__.__new__(self.__class__)
		instance.tx = self.tx
		instance.gas = self.gas
		instance.contract = self.contract
		instance.wallet = self.wallet
		instance.funds = self.funds
		return instance

	def with_funds(self, funds: str) -> "OmxCwVester":
		o = self.clone()
		o.funds = funds
		return o

	def without_funds(self) -> "OmxCwVester":
		o = self.clone()
		o.funds = None
		return o

	def with_wallet(self, wallet: Wallet) -> "OmxCwVester":
		o = self.clone()
		o.wallet = wallet
		return o

	def burn(self, amount: "Uint128") -> SubmittedTx:
		return self.execute({"burn": {"amount": amount}})

	def send_from(self, amount: "Uint128", contract: str, msg: "Binary", owner: str) -> SubmittedTx:
		return self.execute({"send_from": {"amount": amount, "contract": contract, "msg": msg, "owner": owner}})

	def burn_from(self, amount: "Uint128", owner: str) -> SubmittedTx:
		return self.execute({"burn_from": {"amount": amount, "owner": owner}})

	def update_marketing(self, description: str, marketing: str, project: str) -> SubmittedTx:
		return self.execute({"update_marketing": {"description": description, "marketing": marketing, "project": project}})

	def upload_logo(self, value: Union["Logo__url", "Logo__embedded"]) -> SubmittedTx:
		return self.execute({"upload_logo": value})

	def add_admin(self, account: str) -> SubmittedTx:
		return self.execute({"add_admin": {"account": account}})

	def remove_admin(self, account: str) -> SubmittedTx:
		return self.execute({"remove_admin": {"account": account}})

	def set_has_max_vestable_amount(self, value: bool) -> SubmittedTx:
		return self.execute({"set_has_max_vestable_amount": {"value": value}})

	def set_handler(self, account: str, is_handler: bool) -> SubmittedTx:
		return self.execute({"set_handler": {"account": account, "is_handler": is_handler}})

	def deposit(self, amount: "Uint128") -> SubmittedTx:
		return self.execute({"deposit": {"amount": amount}})

	def deposit_cb(self, account: "Addr", amount: "Uint128") -> SubmittedTx:
		return self.execute({"deposit_cb": {"account": account, "amount": amount}})

	def deposit_for_account(self, account: str, amount: "Uint128") -> SubmittedTx:
		return self.execute({"deposit_for_account": {"account": account, "amount": amount}})

	def claim(self) -> SubmittedTx:
		return self.execute({"claim": {}})

	def claim_for_account(self, account: str, recipient: str) -> SubmittedTx:
		return self.execute({"claim_for_account": {"account": account, "recipient": recipient}})

	def withdraw(self) -> SubmittedTx:
		return self.execute({"withdraw": {}})

	def transfer_stake_values(self, recipient: str, sender: str) -> SubmittedTx:
		return self.execute({"transfer_stake_values": {"recipient": recipient, "sender": sender}})

	def set_transferred_average_staked_amounts(self, account: str, amount: "Uint128") -> SubmittedTx:
		return self.execute({"set_transferred_average_staked_amounts": {"account": account, "amount": amount}})

	def set_transferred_cumulative_rewards(self, account: str, amount: "Uint128") -> SubmittedTx:
		return self.execute({"set_transferred_cumulative_rewards": {"account": account, "amount": amount}})

	def set_cumulative_reward_deductions(self, account: str, amount: "Uint128") -> SubmittedTx:
		return self.execute({"set_cumulative_reward_deductions": {"account": account, "amount": amount}})

	def set_bonus_rewards(self, account: str, amount: "Uint128") -> SubmittedTx:
		return self.execute({"set_bonus_rewards": {"account": account, "amount": amount}})

	def balance(self, address: str) -> "QueryResponse_balance":
		return self.query({"balance": {"address": address}})

	def token_info(self) -> "QueryResponse_token_info":
		return self.query({"token_info": {}})

	def all_accounts(self, limit: int, start_after: str) -> "QueryResponse_all_accounts":
		return self.query({"all_accounts": {"limit": limit, "start_after": start_after}})

	def marketing_info(self) -> "QueryResponse_marketing_info":
		return self.query({"marketing_info": {}})

	def download_logo(self) -> "QueryResponse_download_logo":
		return self.query({"download_logo": {}})

	def claimable(self, account: str) -> "QueryResponse_claimable":
		return self.query({"claimable": {"account": account}})

	def max_vestable_amount(self, account: str) -> "QueryResponse_max_vestable_amount":
		return self.query({"max_vestable_amount": {"account": account}})

	def combined_average_staked_amount(self, account: str) -> "QueryResponse_combined_average_staked_amount":
		return self.query({"combined_average_staked_amount": {"account": account}})

	def cumulative_claim_amount(self, account: str) -> "QueryResponse_cumulative_claim_amount":
		return self.query({"cumulative_claim_amount": {"account": account}})

	def claimed_amount(self, account: str) -> "QueryResponse_claimed_amount":
		return self.query({"claimed_amount": {"account": account}})

	def pair_amount(self, account: str, es_amount: "Uint128") -> "QueryResponse_pair_amount":
		return self.query({"pair_amount": {"account": account, "es_amount": es_amount}})

	def last_vesting_time(self, account: str) -> "QueryResponse_last_vesting_time":
		return self.query({"last_vesting_time": {"account": account}})

	def raw_pair_amount(self, account: str) -> "QueryResponse_raw_pair_amount":
		return self.query({"raw_pair_amount": {"account": account}})

	def reward_tracker(self) -> "QueryResponse_reward_tracker":
		return self.query({"reward_tracker": {}})

	def total_vested(self, account: str) -> "QueryResponse_total_vested":
		return self.query({"total_vested": {"account": account}})

	def vested_amount(self, account: str) -> "QueryResponse_vested_amount":
		return self.query({"vested_amount": {"account": account}})

	def vester_state(self) -> "QueryResponse_vester_state":
		return self.query({"vester_state": {}})

	def transferred_average_staked_amount(self, account: str) -> "QueryResponse_transferred_average_staked_amount":
		return self.query({"transferred_average_staked_amount": {"account": account}})

	def transferred_cumulative_reward(self, account: str) -> "QueryResponse_transferred_cumulative_reward":
		return self.query({"transferred_cumulative_reward": {"account": account}})

	def cumulative_reward_deduction(self, account: str) -> "QueryResponse_cumulative_reward_deduction":
		return self.query({"cumulative_reward_deduction": {"account": account}})

	def bonus_reward(self, account: str) -> "QueryResponse_bonus_reward":
		return self.query({"bonus_reward": {"account": account}})
