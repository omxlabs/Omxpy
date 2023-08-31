from omxpy.base_client import BaseOmxClient
from cosmpy.aerial.tx_helpers import SubmittedTx
from cosmpy.aerial.wallet import Wallet
from typing import TypedDict, Union


QueryResponse_admin = str

QueryResponse_pending_rewards = str

QueryResponse_reward_token = str

QueryResponse_token_per_interval = str

class DistributeExec(TypedDict):
	pass

SetAdminExec__admin = str

class SetAdminExec(TypedDict):
	admin: str

class SetTokensPerIntervalExec(TypedDict):
	amount: "Uint128"

Uint128 = str

class UpdateLastDistributionTimeExec(TypedDict):
	pass

class AdminQuery(TypedDict):
	pass

class PendingRewardsQuery(TypedDict):
	pass

class RewardTokenQuery(TypedDict):
	pass

class TokenPerIntervalQuery(TypedDict):
	pass

class ExecuteMsg__set_admin(TypedDict):
	set_admin: "SetAdminExec"

class ExecuteMsg__update_last_distribution_time(TypedDict):
	update_last_distribution_time: "UpdateLastDistributionTimeExec"

class ExecuteMsg__set_tokens_per_interval(TypedDict):
	set_tokens_per_interval: "SetTokensPerIntervalExec"

class ExecuteMsg__distribute(TypedDict):
	distribute: "DistributeExec"

ExecuteMsg = Union["ExecuteMsg__set_admin", "ExecuteMsg__update_last_distribution_time", "ExecuteMsg__set_tokens_per_interval", "ExecuteMsg__distribute"]

class QueryMsg__admin(TypedDict):
	admin: "AdminQuery"

class QueryMsg__reward_token(TypedDict):
	reward_token: "RewardTokenQuery"

class QueryMsg__token_per_interval(TypedDict):
	token_per_interval: "TokenPerIntervalQuery"

class QueryMsg__pending_rewards(TypedDict):
	pending_rewards: "PendingRewardsQuery"

QueryMsg = Union["QueryMsg__admin", "QueryMsg__reward_token", "QueryMsg__token_per_interval", "QueryMsg__pending_rewards"]



class OmxCwRewardDistributor(BaseOmxClient):
	def clone(self) -> "OmxCwRewardDistributor":
		instance = self.__class__.__new__(self.__class__)
		instance.tx = self.tx
		instance.gas = self.gas
		instance.contract = self.contract
		instance.wallet = self.wallet
		instance.funds = self.funds
		return instance

	def with_funds(self, funds: str) -> "OmxCwRewardDistributor":
		o = self.clone()
		o.funds = funds
		return o

	def without_funds(self) -> "OmxCwRewardDistributor":
		o = self.clone()
		o.funds = None
		return o

	def with_wallet(self, wallet: Wallet) -> "OmxCwRewardDistributor":
		o = self.clone()
		o.wallet = wallet
		return o

	def set_admin(self, admin: str) -> SubmittedTx:
		return self.execute({"set_admin": {"admin": admin}})

	def update_last_distribution_time(self) -> SubmittedTx:
		return self.execute({"update_last_distribution_time": {}})

	def set_tokens_per_interval(self, amount: "Uint128") -> SubmittedTx:
		return self.execute({"set_tokens_per_interval": {"amount": amount}})

	def distribute(self) -> SubmittedTx:
		return self.execute({"distribute": {}})

	def admin(self) -> "QueryResponse_admin":
		return self.query({"admin": {}})

	def reward_token(self) -> "QueryResponse_reward_token":
		return self.query({"reward_token": {}})

	def token_per_interval(self) -> "QueryResponse_token_per_interval":
		return self.query({"token_per_interval": {}})

	def pending_rewards(self) -> "QueryResponse_pending_rewards":
		return self.query({"pending_rewards": {}})
