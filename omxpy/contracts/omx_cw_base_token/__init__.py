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

class QueryResponse_balance(TypedDict):
	balance: "Uint128"

Binary = str

QueryResponse_download_logo__mime_type = str

class QueryResponse_download_logo(TypedDict):
	data: "Binary"
	mime_type: str

QueryResponse_id = str

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

class QueryResponse_staked_balance(TypedDict):
	balance: "Uint128"

QueryResponse_token_info__decimals = int

QueryResponse_token_info__name = str

QueryResponse_token_info__symbol = str

class QueryResponse_token_info(TypedDict):
	decimals: int
	name: str
	symbol: str
	total_supply: "Uint128"

QueryResponse_total_staked = str

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

ExecuteMsg__set_in_private_transfer_mode__set_in_private_transfer_mode__value = bool

class ExecuteMsg__set_in_private_transfer_mode__set_in_private_transfer_mode(TypedDict):
	value: bool

class ExecuteMsg__set_in_private_transfer_mode(TypedDict):
	set_in_private_transfer_mode: "ExecuteMsg__set_in_private_transfer_mode__set_in_private_transfer_mode"

ExecuteMsg = Union["ExecuteMsg__transfer", "ExecuteMsg__burn", "ExecuteMsg__send", "ExecuteMsg__increase_allowance", "ExecuteMsg__decrease_allowance", "ExecuteMsg__transfer_from", "ExecuteMsg__send_from", "ExecuteMsg__burn_from", "ExecuteMsg__mint", "ExecuteMsg__update_minter", "ExecuteMsg__update_marketing", "ExecuteMsg__upload_logo", "ExecuteMsg__add_admin", "ExecuteMsg__remove_admin", "ExecuteMsg__set_in_private_transfer_mode"]

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

class QueryMsg__total_staked__total_staked(TypedDict):
	pass

class QueryMsg__total_staked(TypedDict):
	total_staked: "QueryMsg__total_staked__total_staked"

QueryMsg__staked_balance__staked_balance__account = str

class QueryMsg__staked_balance__staked_balance(TypedDict):
	account: str

class QueryMsg__staked_balance(TypedDict):
	staked_balance: "QueryMsg__staked_balance__staked_balance"

class QueryMsg__id__id(TypedDict):
	pass

class QueryMsg__id(TypedDict):
	id: "QueryMsg__id__id"

QueryMsg = Union["QueryMsg__balance", "QueryMsg__token_info", "QueryMsg__minter", "QueryMsg__allowance", "QueryMsg__all_allowances", "QueryMsg__all_spender_allowances", "QueryMsg__all_accounts", "QueryMsg__marketing_info", "QueryMsg__download_logo", "QueryMsg__total_staked", "QueryMsg__staked_balance", "QueryMsg__id"]



class OmxCwBaseToken(BaseOmxClient):
	def clone(self) -> "OmxCwBaseToken":
		instance = self.__class__.__new__(self.__class__)
		instance.tx = self.tx
		instance.gas = self.gas
		instance.contract = self.contract
		instance.wallet = self.wallet
		instance.funds = self.funds
		return instance

	def with_funds(self, funds: str) -> "OmxCwBaseToken":
		o = self.clone()
		o.funds = funds
		return o

	def without_funds(self) -> "OmxCwBaseToken":
		o = self.clone()
		o.funds = None
		return o

	def with_wallet(self, wallet: Wallet) -> "OmxCwBaseToken":
		o = self.clone()
		o.wallet = wallet
		return o

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

	def add_admin(self, account: str) -> SubmittedTx:
		return self.execute({"add_admin": {"account": account}})

	def remove_admin(self, account: str) -> SubmittedTx:
		return self.execute({"remove_admin": {"account": account}})

	def set_in_private_transfer_mode(self, value: bool) -> SubmittedTx:
		return self.execute({"set_in_private_transfer_mode": {"value": value}})

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

	def total_staked(self) -> "QueryResponse_total_staked":
		return self.query({"total_staked": {}})

	def staked_balance(self, account: str) -> "QueryResponse_staked_balance":
		return self.query({"staked_balance": {"account": account}})

	def id(self) -> "QueryResponse_id":
		return self.query({"id": {}})
