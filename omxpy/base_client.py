from typing import Optional
from cosmpy.tx.interface import TxInterface
from cosmpy.aerial.config import NetworkConfig
from cosmpy.aerial.contract import LedgerContract
from cosmpy.aerial.client import LedgerClient
from cosmpy.aerial.wallet import Wallet
from cosmpy.aerial.tx_helpers import SubmittedTx


class BaseOmxClient:
    tx: TxInterface
    gas: int = 200000
    contract: LedgerContract
    wallet: Wallet
    funds: Optional[str] = None

    def __init__(
        self,
        tx: TxInterface,
        contract_addr: str,
        net_cfg: NetworkConfig,
        wallet: Wallet,
    ):
        self.tx = tx
        ledger = LedgerClient(net_cfg)
        self.wallet = wallet
        self.contract = LedgerContract(
            path=None,
            client=ledger,
            address=contract_addr,
        )
        self.funds = None

    def execute(self, raw_msg: any) -> SubmittedTx:
        tx = self.contract.execute(
            raw_msg,
            sender=self.wallet,
            funds=self.funds,
        )

        return tx.wait_to_complete()

    def query(self, raw_msg: any) -> dict:
        return self.contract.query(raw_msg)
