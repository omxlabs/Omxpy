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

# Examples

## Setup environment

Before running tests, make sure you have a local node running contracts deployed:

- Run local osmosis node
  ```bash
  git clone https://github.com/osmosis-labs/osmosis.git
  cd osmosis
  make localnet-init
  make localnet-startd
  make localnet-keys
  cd ..
  ```
- Optional: change block timeouts too 0.2 seconds  
  Open `$HOME/.osmosisd-local/config/config.toml` and update the following values:
  ```toml
  ...
  timeout_commit = "200ms"
  timeout_precommit = "200ms"
  timeout_precommit_delta = "200ms"
  timeout_prevote = "200ms"
  timeout_prevote_delta = "500ms"
  timeout_propose = "200ms"
  timeout_propose_delta = "200ms"
  ...
  ```
- Setup and configure [osmosisd](https://docs.osmosis.zone/cosmwasm/local/localosmosis) to use localnode
- Open `~/.osmosisd/config/client.toml` and change `keyring-backend` to `"test"`
  ```bash
  chain-id = "localosmosis"
  keyring-backend = "test" # <--- make sure this is set to "test"
  output = "text"
  node = "tcp://127.0.0.1:26657"
  ```
  Now you can check balance of main account:
  ```bash
  osmosisd query bank balance osmo12smx2wdlyttvyzvzg54y2vnqwq2qjateuf7thj
  ```
  Output:
  ```
  balances:
  - amount: "100000000000"
    denom: stake
  - amount: "100000000000"
    denom: uion
  - amount: "99500000000" <-- this is the amount of UOSMO tokens, some of them was spent on fees
    denom: uosmo
  pagination:
    next_key: null
    total: "0"
  ```
- Deploy contracts (it will take 3-5 minutes if you didn't change timeouts)
  ```bash
  CONTRACTS=$(node scripts/deploy-localnet.js)
  # check that contracts are deployed
  echo $CONTRACTS
  ```
  Output:
  ```json
  {"osmo":"osmo1w...","usdc":"osmo16...", ...}
  ```

## Run examples

Run one of the examples:

**WARNING**: you need to set the `CONTRACTS` environment variable (see section [Setup environment](#setup-environment)

```bash
poetry install
poetry run python -m examples.long_win
```
