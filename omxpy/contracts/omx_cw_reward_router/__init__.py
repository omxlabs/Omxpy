from omxpy.base_client import BaseOmxClient
from cosmpy.aerial.tx_helpers import SubmittedTx
from cosmpy.aerial.wallet import Wallet
from typing import TypedDict, Union


QueryResponse_admin = str

Addr = str

class ClaimEsOmxExec(TypedDict):
	pass

class ClaimExec(TypedDict):
	pass

class ClaimFeesExec(TypedDict):
	pass

class CompoundCb(TypedDict):
	account: "Addr"
	balance_before: "Uint128"
	reward_token: "Addr"
	stake_token: "Addr"

class CompoundExec(TypedDict):
	pass

CompoundForAccountExec__account = str

class CompoundForAccountExec(TypedDict):
	account: str

class CompoundOmxCb(TypedDict):
	account: "Addr"
	balance_before: "Uint128"
	bn_omx: "Addr"
	fee_omx_tracker: "Addr"

class MintAndStakeOlpCb(TypedDict):
	account: "Addr"
	olp_balance_before: "Uint128"
	token: "Addr"

MintAndStakeOlpExec__token = str

class MintAndStakeOlpExec(TypedDict):
	amount: "Uint128"
	min_olp: "Uint128"
	min_usdo: "Uint128"
	token: str

SetAdminExec__admin = str

class SetAdminExec(TypedDict):
	admin: str

class StakeEsOmxExec(TypedDict):
	amount: "Uint128"

class StakeOmxExec(TypedDict):
	amount: "Uint128"

StakeOmxForAccountExec__account = str

class StakeOmxForAccountExec(TypedDict):
	account: str
	amount: "Uint128"

Uint128 = str

UnstakeAndRedeemOlpExec__recipient = str

UnstakeAndRedeemOlpExec__token_out = str

class UnstakeAndRedeemOlpExec(TypedDict):
	min_out: "Uint128"
	olp_amount: "Uint128"
	recipient: str
	token_out: str

UnstakeAndRedeemOlpOsmoCb__remove_liquidity__remove_liquidity__recipient = str

class UnstakeAndRedeemOlpOsmoCb__remove_liquidity__remove_liquidity(TypedDict):
	account: "Addr"
	min_out: "Uint128"
	olp_amount: "Uint128"
	recipient: str

class UnstakeAndRedeemOlpOsmoCb__remove_liquidity(TypedDict):
	remove_liquidity: "UnstakeAndRedeemOlpOsmoCb__remove_liquidity__remove_liquidity"

UnstakeAndRedeemOlpOsmoCb__withdraw__withdraw__recipient = str

class UnstakeAndRedeemOlpOsmoCb__withdraw__withdraw(TypedDict):
	olp_amount: "Uint128"
	osmo_balance_before: "Uint128"
	recipient: str

class UnstakeAndRedeemOlpOsmoCb__withdraw(TypedDict):
	withdraw: "UnstakeAndRedeemOlpOsmoCb__withdraw__withdraw"

UnstakeAndRedeemOlpOsmoCb = Union["UnstakeAndRedeemOlpOsmoCb__remove_liquidity", "UnstakeAndRedeemOlpOsmoCb__withdraw"]

UnstakeAndRedeemOlpOsmoExec__recipient = str

class UnstakeAndRedeemOlpOsmoExec(TypedDict):
	min_out: "Uint128"
	olp_amount: "Uint128"
	recipient: str

class UnstakeCb__stake_fee_omx_tracker__stake_fee_omx_tracker(TypedDict):
	account: "Addr"
	amount: "Uint128"
	balance: "Uint128"
	balance_before: "Uint128"
	reward_token: "Addr"

class UnstakeCb__stake_fee_omx_tracker(TypedDict):
	stake_fee_omx_tracker: "UnstakeCb__stake_fee_omx_tracker__stake_fee_omx_tracker"

class UnstakeCb__unstake_fee_omx_tracker__unstake_fee_omx_tracker(TypedDict):
	account: "Addr"
	amount: "Uint128"
	balance: "Uint128"

class UnstakeCb__unstake_fee_omx_tracker(TypedDict):
	unstake_fee_omx_tracker: "UnstakeCb__unstake_fee_omx_tracker__unstake_fee_omx_tracker"

UnstakeCb = Union["UnstakeCb__stake_fee_omx_tracker", "UnstakeCb__unstake_fee_omx_tracker"]

class UnstakeEsOmxExec(TypedDict):
	amount: "Uint128"

class UnstakeOmxExec(TypedDict):
	amount: "Uint128"

class AdminQuery(TypedDict):
	pass

class ExecuteMsg__set_admin(TypedDict):
	set_admin: "SetAdminExec"

class ExecuteMsg__unstake_cb(TypedDict):
	unstake_cb: "UnstakeCb"

class ExecuteMsg__compound_cb(TypedDict):
	compound_cb: "CompoundCb"

class ExecuteMsg__compound_omx_cb(TypedDict):
	compound_omx_cb: "CompoundOmxCb"

class ExecuteMsg__stake_omx_for_account(TypedDict):
	stake_omx_for_account: "StakeOmxForAccountExec"

class ExecuteMsg__stake_omx(TypedDict):
	stake_omx: "StakeOmxExec"

class ExecuteMsg__stake_es_omx(TypedDict):
	stake_es_omx: "StakeEsOmxExec"

class ExecuteMsg__unstake_omx(TypedDict):
	unstake_omx: "UnstakeOmxExec"

class ExecuteMsg__unstake_es_omx(TypedDict):
	unstake_es_omx: "UnstakeEsOmxExec"

class ExecuteMsg__claim(TypedDict):
	claim: "ClaimExec"

class ExecuteMsg__claim_es_omx(TypedDict):
	claim_es_omx: "ClaimEsOmxExec"

class ExecuteMsg__claim_fees(TypedDict):
	claim_fees: "ClaimFeesExec"

class ExecuteMsg__compound(TypedDict):
	compound: "CompoundExec"

class ExecuteMsg__compound_for_account(TypedDict):
	compound_for_account: "CompoundForAccountExec"

class ExecuteMsg__mint_and_stake_olp(TypedDict):
	mint_and_stake_olp: "MintAndStakeOlpExec"

class ExecuteMsg__mint_and_stake_olp_cb(TypedDict):
	mint_and_stake_olp_cb: "MintAndStakeOlpCb"

class ExecuteMsg__unstake_and_redeem_olp(TypedDict):
	unstake_and_redeem_olp: "UnstakeAndRedeemOlpExec"

class ExecuteMsg__unstake_and_redeem_olp_osmo(TypedDict):
	unstake_and_redeem_olp_osmo: "UnstakeAndRedeemOlpOsmoExec"

class ExecuteMsg__unstake_and_redeem_olp_osmo_cb(TypedDict):
	unstake_and_redeem_olp_osmo_cb: "UnstakeAndRedeemOlpOsmoCb"

ExecuteMsg = Union["ExecuteMsg__set_admin", "ExecuteMsg__unstake_cb", "ExecuteMsg__compound_cb", "ExecuteMsg__compound_omx_cb", "ExecuteMsg__stake_omx_for_account", "ExecuteMsg__stake_omx", "ExecuteMsg__stake_es_omx", "ExecuteMsg__unstake_omx", "ExecuteMsg__unstake_es_omx", "ExecuteMsg__claim", "ExecuteMsg__claim_es_omx", "ExecuteMsg__claim_fees", "ExecuteMsg__compound", "ExecuteMsg__compound_for_account", "ExecuteMsg__mint_and_stake_olp", "ExecuteMsg__mint_and_stake_olp_cb", "ExecuteMsg__unstake_and_redeem_olp", "ExecuteMsg__unstake_and_redeem_olp_osmo", "ExecuteMsg__unstake_and_redeem_olp_osmo_cb"]

class QueryMsg__admin(TypedDict):
	admin: "AdminQuery"

QueryMsg = "QueryMsg__admin"



class OmxCwRewardRouter(BaseOmxClient):
	def clone(self) -> "OmxCwRewardRouter":
		instance = self.__class__.__new__(self.__class__)
		instance.tx = self.tx
		instance.gas = self.gas
		instance.contract = self.contract
		instance.wallet = self.wallet
		instance.funds = self.funds
		return instance

	def with_funds(self, funds: str) -> "OmxCwRewardRouter":
		o = self.clone()
		o.funds = funds
		return o

	def without_funds(self) -> "OmxCwRewardRouter":
		o = self.clone()
		o.funds = None
		return o

	def with_wallet(self, wallet: Wallet) -> "OmxCwRewardRouter":
		o = self.clone()
		o.wallet = wallet
		return o

	def set_admin(self, admin: str) -> SubmittedTx:
		return self.execute({"set_admin": {"admin": admin}})

	def unstake_cb(self, value: Union["UnstakeCb__stake_fee_omx_tracker", "UnstakeCb__unstake_fee_omx_tracker"]) -> SubmittedTx:
		return self.execute({"unstake_cb": value})

	def compound_cb(self, account: "Addr", balance_before: "Uint128", reward_token: "Addr", stake_token: "Addr") -> SubmittedTx:
		return self.execute({"compound_cb": {"account": account, "balance_before": balance_before, "reward_token": reward_token, "stake_token": stake_token}})

	def compound_omx_cb(self, account: "Addr", balance_before: "Uint128", bn_omx: "Addr", fee_omx_tracker: "Addr") -> SubmittedTx:
		return self.execute({"compound_omx_cb": {"account": account, "balance_before": balance_before, "bn_omx": bn_omx, "fee_omx_tracker": fee_omx_tracker}})

	def stake_omx_for_account(self, account: str, amount: "Uint128") -> SubmittedTx:
		return self.execute({"stake_omx_for_account": {"account": account, "amount": amount}})

	def stake_omx(self, amount: "Uint128") -> SubmittedTx:
		return self.execute({"stake_omx": {"amount": amount}})

	def stake_es_omx(self, amount: "Uint128") -> SubmittedTx:
		return self.execute({"stake_es_omx": {"amount": amount}})

	def unstake_omx(self, amount: "Uint128") -> SubmittedTx:
		return self.execute({"unstake_omx": {"amount": amount}})

	def unstake_es_omx(self, amount: "Uint128") -> SubmittedTx:
		return self.execute({"unstake_es_omx": {"amount": amount}})

	def claim(self) -> SubmittedTx:
		return self.execute({"claim": {}})

	def claim_es_omx(self) -> SubmittedTx:
		return self.execute({"claim_es_omx": {}})

	def claim_fees(self) -> SubmittedTx:
		return self.execute({"claim_fees": {}})

	def compound(self) -> SubmittedTx:
		return self.execute({"compound": {}})

	def compound_for_account(self, account: str) -> SubmittedTx:
		return self.execute({"compound_for_account": {"account": account}})

	def mint_and_stake_olp(self, amount: "Uint128", min_olp: "Uint128", min_usdo: "Uint128", token: str) -> SubmittedTx:
		return self.execute({"mint_and_stake_olp": {"amount": amount, "min_olp": min_olp, "min_usdo": min_usdo, "token": token}})

	def mint_and_stake_olp_cb(self, account: "Addr", olp_balance_before: "Uint128", token: "Addr") -> SubmittedTx:
		return self.execute({"mint_and_stake_olp_cb": {"account": account, "olp_balance_before": olp_balance_before, "token": token}})

	def unstake_and_redeem_olp(self, min_out: "Uint128", olp_amount: "Uint128", recipient: str, token_out: str) -> SubmittedTx:
		return self.execute({"unstake_and_redeem_olp": {"min_out": min_out, "olp_amount": olp_amount, "recipient": recipient, "token_out": token_out}})

	def unstake_and_redeem_olp_osmo(self, min_out: "Uint128", olp_amount: "Uint128", recipient: str) -> SubmittedTx:
		return self.execute({"unstake_and_redeem_olp_osmo": {"min_out": min_out, "olp_amount": olp_amount, "recipient": recipient}})

	def unstake_and_redeem_olp_osmo_cb(self, value: Union["UnstakeAndRedeemOlpOsmoCb__remove_liquidity", "UnstakeAndRedeemOlpOsmoCb__withdraw"]) -> SubmittedTx:
		return self.execute({"unstake_and_redeem_olp_osmo_cb": value})

	def admin(self) -> "QueryResponse_admin":
		return self.query({"admin": {}})
