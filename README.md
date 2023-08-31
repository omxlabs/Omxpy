# OMX python api

Python client for interacting with [OMX](https://www.omxapp.com/) contracts.

[![ReadTheDocs](https://readthedocs.org/projects/switcheo-python/badge/?version=latest)](https://docs.omxapp.com)
[![PyPi](https://img.shields.io/pypi/v/omxpy.svg)](https://github.com/omxlabs/omxpy/blob/master/LICENSE.md)
[![PyPi](https://img.shields.io/pypi/pyversions/omxpy.svg)](https://pypi.org/project/omxpy)
[![PyPi](https://img.shields.io/pypi/l/omxpy.svg)](https://img.shields.io/pypi/l/omxpy.svg)

# Installation

## Requirements

- [Python 3.10](https://www.python.org/downloads/) or higher
- Highly recommended to use [Poetry](https://python-poetry.org/docs/#installation) for dependency management
- [Osmosis localnet](https://github.com/osmosis-labs/osmosis/tree/main/tests/localosmosis) for testing

```bash
pip install omxpy
# or with poetry
poetry add omxpy
```

# Example

```python
from cosmpy.aerial.config import NetworkConfig
from cosmpy.tx.rest_client import RestClient
from omxpy.contracts.omx_cw_router import OmxCwRouter
from omxpy.contracts.omx_cw_vault import OmxCwVault
from cosmpy.aerial.wallet import LocalWallet

wallet = LocalWallet.from_mnemonic("...", prefix="osmo")

net_cfg = NetworkConfig(
    chain_id="localosmosis",
    fee_denomination="uosmo",
    staking_denomination="stake",
    fee_minimum_gas_price=0.025,
    url="rest+http://127.0.0.1:1317",
)
rest_client = LedgerClient(net_cfg)
tx_client = TxRestClient(rest_client)

# replace with your contract addresses
vault_addr = "osmo1w..."
osmo_addr = "osmo1j..."
router_addr = "osmo16..."

# create contract clients
router = OmxCwRouter(
    tx=rest_client,
    contract_addr=router_addr,
    net_cfg=net_cfg
    wallet=wallet
)
vault = OmxCwVault(
    tx=rest_client,
    contract_addr=router_addr,
    net_cfg=net_cfg
    wallet=wallet
)

amount_in = "100000000uosmo"
# in real life you would want to use a price oracle
price_in_usd = "1000000000000000000";
# 3x leverage
size_delta = "3000000000000000000";

# add router to the vault
vault.add_router(router=router_addr)

# open long position
router.with_funds(amount_in).increase_position_osmo(
    collateral={"token": osmo_addr},
    index_token=osmo_addr,
    is_long=True,
    min_out="0",
    price=price_in_usd,
    size_delta=size_delta,
)
```
