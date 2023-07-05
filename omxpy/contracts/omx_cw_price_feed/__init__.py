from omxpy.base_client import BaseOmxClient
from cosmpy.aerial.tx_helpers import SubmittedTx
from cosmpy.aerial.wallet import Wallet
from typing import TypedDict, Tuple, Optional, Union


Uint128 = str

QueryResponse_latest_answer__positive = bool

class QueryResponse_latest_answer(TypedDict):
	positive: bool
	value: "Uint128"

QueryResponse_latest_round = str

Answer__positive = bool

class Answer(TypedDict):
	positive: bool
	value: "Uint128"

Timestamp = Tuple["Uint64"]

Uint64 = str

class QueryResponse_round_data(TypedDict):
	answer: "Answer"
	answered_in_round: "Uint128"
	round_id: "Uint128"
	started_at: "Timestamp"
	updated_at: "Timestamp"

SetAdminArgs__admin = Optional[str]

SetAdminArgs__value = bool

class SetAdminArgs(TypedDict):
	admin: str
	value: bool

class SetLatestAnswerArgs(TypedDict):
	answer: "Answer"

LatestAnswerMsg = None

LatestRoundMsg = None

class RoundDataMsg(TypedDict):
	round_id: "Uint128"

class ExecuteMsg__set_admin(TypedDict):
	set_admin: "SetAdminArgs"

class ExecuteMsg__set_latest_answer(TypedDict):
	set_latest_answer: "SetLatestAnswerArgs"

ExecuteMsg = Union["ExecuteMsg__set_admin", "ExecuteMsg__set_latest_answer"]

class QueryMsg__latest_round(TypedDict):
	latest_round: "LatestRoundMsg"

class QueryMsg__latest_answer(TypedDict):
	latest_answer: "LatestAnswerMsg"

class QueryMsg__round_data(TypedDict):
	round_data: "RoundDataMsg"

QueryMsg = Union["QueryMsg__latest_round", "QueryMsg__latest_answer", "QueryMsg__round_data"]



class OmxCwPriceFeed(BaseOmxClient):
	def clone(self) -> "OmxCwPriceFeed":
		instance = self.__class__.__new__(self.__class__)
		instance.tx = self.tx
		instance.gas = self.gas
		instance.contract = self.contract
		instance.wallet = self.wallet
		instance.funds = self.funds
		return instance

	def with_funds(self, funds: str) -> "OmxCwPriceFeed":
		o = self.clone()
		o.funds = funds
		return o

	def without_funds(self) -> "OmxCwPriceFeed":
		o = self.clone()
		o.funds = None
		return o

	def with_wallet(self, wallet: Wallet) -> "OmxCwPriceFeed":
		o = self.clone()
		o.wallet = wallet
		return o

	def set_admin(self, admin: str, value: bool) -> SubmittedTx:
		return self.execute({"set_admin": {"admin": admin, "value": value}})

	def set_latest_answer(self, answer: "Answer") -> SubmittedTx:
		return self.execute({"set_latest_answer": {"answer": answer}})

	def latest_round(self) -> "QueryResponse_latest_round":
		return self.query({"latest_round": {}})

	def latest_answer(self) -> "QueryResponse_latest_answer":
		return self.query({"latest_answer": {}})

	def round_data(self, round_id: "Uint128") -> "QueryResponse_round_data":
		return self.query({"round_data": {"round_id": round_id}})
