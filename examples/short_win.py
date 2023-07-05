import json
import os
from cosmpy.aerial.config import NetworkConfig
from cosmpy.aerial.client import LedgerClient
from cosmpy.tx.rest_client import TxRestClient
from cosmpy.aerial.wallet import LocalWallet
from .helpers import (
    CHAIN_ID,
    NODE_URL,
    MIN_GAS_FEE,
    ETH_SCALE,
    USDC_SCALE,
    OSMO_SCALE,
    PRICE_PRECISION,
    ORACLE_PRICE_PRECISION,
)
from omxpy import (
    OmxCwVault,
    OmxCwRouter,
    OmxCwBaseToken,
    OmxCwPriceFeed,
    OmxCwVaultPriceFeed,
)
from .helpers.wallets import Wallets


def set_env():
    raw_contracts = os.environ["CONTRACTS"]
    if raw_contracts is None:
        raise Exception("CONTRACTS env variable is not set")
    contracts = json.loads(raw_contracts)

    wallets = Wallets()

    net_cfg = NetworkConfig(
        chain_id=CHAIN_ID,
        fee_denomination="uosmo",
        staking_denomination="stake",
        fee_minimum_gas_price=MIN_GAS_FEE,
        url=NODE_URL,
    )
    rest_client = LedgerClient(net_cfg)
    tx_client = TxRestClient(rest_client)

    rest_client.send_tokens(
        amount=str(OSMO_SCALE),
        denom="uosmo",
        destination=wallets.user0.address(),
        sender=wallets.deployer,
    ).wait_to_complete()

    base_args = {
        "tx": tx_client,
        "net_cfg": net_cfg,
        "wallet": wallets.deployer,
    }

    vault = OmxCwVault(contract_addr=contracts["vault"], **base_args)
    router = OmxCwRouter(contract_addr=contracts["router"], **base_args)
    eth = OmxCwBaseToken(contract_addr=contracts["eth"], **base_args)
    usdc = OmxCwBaseToken(contract_addr=contracts["usdc"], **base_args)
    eth_price_feed = OmxCwPriceFeed(
        contract_addr=contracts["eth_price_feed"], **base_args
    )
    vault_price_feed = OmxCwVaultPriceFeed(
        contract_addr=contracts["vault_price_feed"], **base_args
    )

    def get_pool_amounts():
        return {
            "eth": float(vault.pool_amount(contracts["eth"])) / ETH_SCALE,
            "usdc": float(vault.pool_amount(contracts["usdc"])) / USDC_SCALE,
        }

    def get_balances(wallet: LocalWallet = wallets.deployer):
        return {
            "eth": float(eth.balance(wallet.address())["balance"]) / ETH_SCALE,
            "usdc": float(usdc.balance(wallet.address())["balance"]) / USDC_SCALE,
        }

    pool_initial = get_pool_amounts()

    # mint some additional eth to open position
    amount_in = 1000 * USDC_SCALE
    usdc.mint(str(amount_in), wallets.user0.address())

    # add some tokens to the pool
    pool_initial_eth = 10
    eth.mint(str(pool_initial_eth * ETH_SCALE), contracts["vault"])
    vault.direct_pool_deposit(contracts["eth"])

    pool_initial_usdc = 10_000
    usdc.mint(str(pool_initial_usdc * USDC_SCALE), contracts["vault"])
    vault.direct_pool_deposit(contracts["usdc"])

    # configure price feeds to use only one sample
    vault_price_feed.set_price_sample_space(1)

    return (
        pool_initial,
        amount_in,
        contracts,
        wallets,
        vault,
        router,
        usdc,
        eth_price_feed,
        get_pool_amounts,
        get_balances,
    )


def example_short_win():
    (
        pool_initial,
        amount_in,
        contracts,
        wallets,
        vault,
        router,
        usdc,
        eth_price_feed,
        get_pool_amounts,
        get_balances,
    ) = set_env()

    # query initial state
    pool_before_open = get_pool_amounts()
    balances_before_open = get_balances(wallets.user0)

    print(
        "Pool amounts before opening position:",
        {
            "eth": pool_before_open["eth"] - pool_initial["eth"],
            "usdc": pool_before_open["usdc"] - pool_initial["usdc"],
        },
    )
    print("Balances before opening position:", balances_before_open)

    start_eth_price = 1000
    eth_price_feed.set_latest_answer(
        {"positive": True, "value": str(start_eth_price * ORACLE_PRICE_PRECISION)}
    )

    # add router and allow it to spend user0's eth
    vault.with_wallet(wallets.user0).add_router(contracts["router"])
    usdc.with_wallet(wallets.user0).increase_allowance(
        amount=str(amount_in), spender=contracts["router"]
    )

    # open position with 10x leverage
    size_delta = 10 * start_eth_price * PRICE_PRECISION
    router.with_wallet(wallets.user0).increase_position(
        amount_in=str(amount_in),
        collateral={
            "token": contracts["usdc"],
        },
        index_token=contracts["eth"],
        is_long=False,
        min_out="0",
        price=str(start_eth_price * PRICE_PRECISION),
        size_delta=str(size_delta),
    )

    # check position after opening
    position = vault.position(
        account=wallets.user0.address(),
        collateral_token=contracts["usdc"],
        index_token=contracts["eth"],
        is_long=False,
    )
    print("Position opened:", position)

    # check balances after opening
    pool_after_open = get_pool_amounts()
    balances_after_open = get_balances(wallets.user0)

    print(
        "Pool amounts after opening position:",
        {
            "eth": pool_after_open["eth"] - pool_initial["eth"],
            "usdc": pool_after_open["usdc"] - pool_initial["usdc"],
        },
    )
    print("Balances after opening position:", balances_after_open)

    # simulate price change (0.5x by default)
    price_multiplier = float(os.getenv("PRICE_INCREASE", 0.5))
    eth_price_feed.set_latest_answer(
        {
            "positive": True,
            "value": str(
                start_eth_price * int(ORACLE_PRICE_PRECISION * price_multiplier)
            ),
        }
    )

    # close position
    router.with_wallet(wallets.user0).decrease_position(
        collateral_token=contracts["usdc"],
        index_token=contracts["eth"],
        is_long=False,
        collateral_delta=str(amount_in),
        size_delta=str(size_delta),
        price=str(
            start_eth_price * int(PRICE_PRECISION * price_multiplier)
        ),  # new price is lower
        recipient=wallets.user0.address(),
    )

    # check balances after closing
    pool_after_close = get_pool_amounts()
    balances_after_close = get_balances(wallets.user0)

    print(
        "Pool amounts after closing position:",
        {
            "eth": pool_after_close["eth"] - pool_initial["eth"],
            "usdc": pool_after_close["usdc"] - pool_initial["usdc"],
        },
    )
    print("Balances after closing position:", balances_after_close)


if __name__ == "__main__":
    example_short_win()
