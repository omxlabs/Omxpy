const { exec } = require("child_process");
const { join } = require("path");
const process = require("process");

const DEPLOYER_WALLET = process.env.DEPLOYER_WALLET || "val";
const DEPLOYER_ADDR = process.env.DEPLOYER_ADDR || "osmo12smx2wdlyttvyzvzg54y2vnqwq2qjateuf7thj";
const GAS_PRICES = process.env.GAS_PRICES || "0.1uosmo";
const ARTIFACTS_PATH = process.env.ARTIFACTS_PATH || "artifacts";

const OSMO_DENOM = "uosmo";
const USDC_DENOM = "ibc/D189335C6E4A68B513C10AB227BF1C1D38C746766278BA3EEB4FB14124F1D858";
const BUSD_DENOM = "ibc/6329DD8CF31A334DD5BE3F68C846C9FE313281362B37686A62343BAC1EB1546D";
const BTC_DENOM = "ibc/D1542AA8762DB13087D8364F3EA6509FD6F009A34F00426AF9E4F9FA85CBBF1F";
const ETH_DENOM = "ibc/EA1D43981D5C9A1C4AAEA9C23BB1D4FA126BA9BC7020A25E0AE4AA841EA25DC5";
const ATOM_DENOM = "ibc/27394FB092D2ECCD56123C74F36E4C1F926001CEADA9CA97EA622B25F41E5EB2";
const USDC_DECIMALS = 6;
const BUSD_DECIMALS = 18;
const BTC_DECIMALS = 8;
const ETH_DECIMALS = 18;
const ATOM_DECIMALS = 6;
const OSMO_DECIMALS = 6;
const USDO_DECIMALS = 18;

const BTC_SCALE = 10n ** BigInt(BTC_DECIMALS);
const ETH_SCALE = 10n ** BigInt(ETH_DECIMALS);
const OSMO_SCALE = 10n ** BigInt(OSMO_DECIMALS);
const USDC_SCALE = 10n ** BigInt(USDC_DECIMALS);
const ATOM_SCALE = 10n ** BigInt(ATOM_DECIMALS);
const BUSD_SCALE = 10n ** BigInt(BUSD_DECIMALS);
const USDO_SCALE = 10n ** BigInt(USDO_DECIMALS);

const BTC_DEPOSIT_VAULT_AMOUNT = BTC_SCALE * 1000n;
const ETH_DEPOSIT_VAULT_AMOUNT = ETH_SCALE * 1000n;
const USDC_DEPOSIT_VAULT_AMOUNT = USDC_SCALE * 1000000n;
const OSMO_DEPOSIT_VAULT_AMOUNT = OSMO_SCALE * 1000n;
const ATOM_DEPOSIT_VAULT_AMOUNT = ATOM_SCALE * 1000000n;

const PRICE_PRECISION = 1_000000000000000000n; // 1e18
const ORACLE_PRICE_PRECISION = 1_00000000n; // 1e8

// orderbook constants
const MIN_EXECUTION_FEE = 500000n
const MIN_PURCHASE_TOKEN_AMOUNT_USD = PRICE_PRECISION * 5n / 10n; // 0.5 USD

// all prices is 1:1 for simplicity
const BTC_ORACLE_PRICE = 1n * ORACLE_PRICE_PRECISION;
const ETH_ORACLE_PRICE = 1n * ORACLE_PRICE_PRECISION;
const OSMO_ORACLE_PRICE = 1n * ORACLE_PRICE_PRECISION;
const USDC_ORACLE_PRICE = 1n * ORACLE_PRICE_PRECISION;
const BUSD_ORACLE_PRICE = 1n * ORACLE_PRICE_PRECISION;
const ATOM_ORACLE_PRICE = 1n * ORACLE_PRICE_PRECISION;

const CONTRACTS_NAMES = [
    "omx_cw_base_token",
    "omx_cw_pair",
    "omx_cw_price_feed",
    "omx_cw_router",
    "omx_cw_vault",
    "omx_cw_vault_price_feed",
    "omx_cw_wrapped_token",
    "omx_cw_orderbook",
];


/**
 * @param {string} command
 * @param {number|undefined} retries
 * @returns {Promise<object>}
 */
const executeWithRetries = async (command, retries = 10) => {
    return new Promise((resolve, reject) => {
        exec(
            command,
            async (error, stdout, stderr) => {
                if (error) {
                    if (retries > 0) {
                        return resolve(await executeWithRetries(command, retries - 1));
                    }
                    return reject(error);
                }

                resolve(JSON.parse(stdout));
            }
        );
    });
};


/**
 * @param {string} path
 * @returns {Promise<number>}
 */
const storeBinaries = async (path) => {
    const result = await executeWithRetries(`osmosisd tx wasm store ${path} --from ${DEPLOYER_WALLET} --gas-prices ${GAS_PRICES} --gas auto --gas-adjustment 1.3 -y --output json -b block`);

    const event = result.logs[0].events.find(({ type }) => type == "store_code");

    return parseInt(event.attributes.find(({ key }) => key == "code_id").value, 10);
};

/**
 * @returns {Promise<{[key: string]: number}>}
 */
const storeAllContracts = async () => {
    const code_ids = {};

    for (const contract of CONTRACTS_NAMES) {
        const result = await storeBinaries(join(ARTIFACTS_PATH, `${contract}.wasm`));
        code_ids[contract] = result;
    }

    return code_ids;
};

const parseInstantiateResult = (result) => {
    const event = result.logs[0].events.find(({ type }) => type == "instantiate");
    return event.attributes.find(({ key }) => key == "_contract_address").value;
};

/**
 * @param {number} code_id
 * @param {string} deployer
 * @param {string} minter
 * @param {string} denom
 * @param {number} decimals
 * @param {string} symbol
 * @returns {Promise<string>}
 */
const deployWrappedToken = async (code_id, deployer, minter, denom, decimals, symbol) => {
    const init_message = JSON.stringify({
        name: symbol,
        denom,
        symbol,
        decimals,
        mint: { minter },
    });
    const result = await executeWithRetries(`osmosisd tx wasm instantiate ${code_id} '${init_message}' --from ${deployer} --gas-prices ${GAS_PRICES} --no-admin --gas auto --gas-adjustment 1.3 -y --output json -b block --label=${symbol}`);

    const addr = parseInstantiateResult(result);

    return addr;
};


/**
 * @param {number} code_id
 * @param {string} deployer
 * @param {string} minter
 * @param {string} symbol
 * @param {number} decimals
 * @returns {Promise<string>}
 */
const deployBaseToken = async (code_id, deployer, minter, symbol, decimals) => {
    const init_message = JSON.stringify({
        name: symbol,
        symbol,
        id: symbol,
        decimals,
        mint: { minter },
    });
    const result = await executeWithRetries(`osmosisd tx wasm instantiate ${code_id} '${init_message}' --from ${deployer} --gas-prices ${GAS_PRICES} --no-admin --gas auto --gas-adjustment 1.3 -y --output json -b block --label=${symbol}`);

    const addr = parseInstantiateResult(result);

    return addr;
};


/**
 * @param {number} code_id
 * @param {string} deployer
 * @param {string} token0
 * @param {string} token1
 * @param {string} name
 * @returns {Promise<string>}
 */
const deployPair = async (code_id, deployer, token0, token1, name) => {
    const init_message = JSON.stringify({
        token0,
        token1,
    });
    const result = await executeWithRetries(`osmosisd tx wasm instantiate ${code_id} '${init_message}' --from ${deployer} --gas-prices ${GAS_PRICES} --no-admin --gas auto --gas-adjustment 1.3 -y --output json -b block --label=${name}`);

    const addr = parseInstantiateResult(result);

    return addr;
};

/**
 * Deploy price feed
 * @param {number} code_id
 * @param {string} deployer
 * @param {string} label
 */
const deployPriceFeed = async (code_id, deployer, label) => {
    const init_message = JSON.stringify({});

    const result = await executeWithRetries(`osmosisd tx wasm instantiate ${code_id} '${init_message}' --from ${deployer} --gas-prices ${GAS_PRICES} --no-admin --gas auto --gas-adjustment 1.3 -y --output json -b block --label=${label}`);
    const addr = parseInstantiateResult(result);

    return addr;
};

/**
 * Deploy Vault price feed
 * @param {number} code_id
 * @param {string} deployer
 * @param {{ btc: string, eth: string, osmo: string, eth_busd: string, btc_eth: string, osmo_eth: string }} args
 * @returns {Promise<string>}
 */
const deployVaultPriceFeed = async (code_id, deployer, args) => {
    const init_message = JSON.stringify({
        ...args,
        is_amm_enabled: false,
    });
    const result = await executeWithRetries(`osmosisd tx wasm instantiate ${code_id} '${init_message}' --from ${deployer} --gas-prices ${GAS_PRICES} --no-admin --gas auto --gas-adjustment 1.3 -y --output json -b block --label=vault_price_feed`);

    const addr = parseInstantiateResult(result);

    return addr;
};


// funding_rate_factor: Uint128::new(600),
// liquidation_fee_usd: Uint128::new(5) * PRICE_PRECISION,
// price_feed: vault_price_feed.to_string(),
// stable_funding_rate_factor: Uint128::new(600),
// usdo: usdo.to_string(),
/**
 * Deploy Vault
 * @param {number} code_id
 * @param {string} deployer
 * @param {{ funding_rate_factor: bigint, liquidation_fee_usd: bigint, vault_price_feed: string, stable_funding_rate_factor: bigint, usdo: string }} args
 * @returns {Promise<string>}
 */
const deployVault = async (code_id, deployer, args) => {
    const init_message = JSON.stringify({
        funding_rate_factor: args.funding_rate_factor.toString(),
        liquidation_fee_usd: args.liquidation_fee_usd.toString(),
        price_feed: args.vault_price_feed,
        stable_funding_rate_factor: args.stable_funding_rate_factor.toString(),
        usdo: args.usdo,
    });

    const result = await executeWithRetries(`osmosisd tx wasm instantiate ${code_id} '${init_message}' --from ${deployer} --gas-prices ${GAS_PRICES} --no-admin --gas auto --gas-adjustment 1.3 -y --output json -b block --label=vault`);
    const addr = parseInstantiateResult(result);

    return addr;
};

/**
 * Deploy router
 * @param {number} code_id
 * @param {string} deployer
 * @param {{ vault: string, usdo: string, osmo: string }} args
 * @returns {Promise<string>}
 */
const deployRouter = async (code_id, deployer, args) => {
    const init_message = JSON.stringify({
        vault: args.vault,
        usdo: args.usdo,
        wosmo: args.osmo,
    });

    const result = await executeWithRetries(`osmosisd tx wasm instantiate ${code_id} '${init_message}' --from ${deployer} --gas-prices ${GAS_PRICES} --no-admin --gas auto --gas-adjustment 1.3 -y --output json -b block --label=router`);
    const addr = parseInstantiateResult(result);

    return addr;
};

/**
 * Deploy orderbook
 * @param {number} code_id
 * @param {string} deployer
 * @param {{
 *   admin?: string,
 *   router: string,
 *   vault: string,
 *   wosmo: string,
 *   usdo: string,
 *   min_execution_fee: bigint,
 *   min_purchase_token_amount_usd: bigint,
 * }} args
 * @returns {Promise<string>}
 */
const deployOrderbook = async (code_id, deployer, args) => {
    const init_message = JSON.stringify({
        admin: args.admin || deployer,
        vault: args.vault,
        router: args.router,
        wosmo: args.wosmo,
        usdo: args.usdo,
        min_execution_fee: args.min_execution_fee.toString(),
        min_purchase_token_amount_usd: args.min_purchase_token_amount_usd.toString(),
    });

    const result = await executeWithRetries(`osmosisd tx wasm instantiate ${code_id} '${init_message}' --from ${deployer} --gas-prices ${GAS_PRICES} --no-admin --gas auto --gas-adjustment 1.3 -y --output json -b block --label=router`);
    const addr = parseInstantiateResult(result);

    return addr;
};

/**
 * Execute contract
 * @param {string} contract Contract address
 * @param {any} msg Message to execute
 * @param {{denom: string, amount: bigint}[]} funds Coins to send with the message
 * @param {string | undefined} deployer Defaults to DEPLOYER_ADDR
 * @returns {Promise<void>}
 */
const executeContractFunded = async (contract, msg, funds, deployer = DEPLOYER_ADDR) => {
    const msg_str = JSON.stringify(msg);
    const funds_str = funds.length ? `--amount ${funds.map(f => `${f.amount}${f.denom.toString()}`).join(',')}` : "";
    await executeWithRetries(`osmosisd tx wasm execute ${contract} '${msg_str}' ${funds_str} --from ${deployer} --gas-prices ${GAS_PRICES} --gas auto --gas-adjustment 1.3 -y --output json -b block`);
};

/**
 * Execute contract
 * @param {string} contract Contract address
 * @param {any} msg Message to execute
 * @param {string | undefined} deployer Defaults to DEPLOYER_ADDR
 * @returns {Promise<void>}
 */
const executeContract = async (contract, msg, deployer = DEPLOYER_ADDR) => {
    await executeContractFunded(contract, msg, [], deployer);
};

/**
 * configure vault price feed
 * @param {string} vault_price_feed
 * @param {{ token: string, price_feed: string }[]} args
 * @returns {Promise<void>}
 */
const configureVaultPriceFeed = async (vault_price_feed, args) => {
    for (const arg of args) {
        await executeContract(vault_price_feed, {
            set_token_config: {
                token: arg.token,
                price_decimals: 8,
                price_feed: arg.price_feed,
                is_strict_stable: false,
            }
        });
    }
};

/**
 * Set latest price to price feed
 * @param {string} price_feed
 * @param {bigint} price
 * @returns {Promise<void>}
 */
const updatePrice = async (price_feed, price) => {
    await executeContract(price_feed, {
        set_latest_answer: {
            answer: {
                value: price.toString(),
                positive: true,
            },
        },
    });
};

/**
 * Deposit `amount` to the `vault`
 * @param {string} deployer Wallet to execute tx
 * @param {string} vault Vault address
 * @param {string} token Token address
 * @param {bigint} amount Amount of `token` to mint and deposit
 * @returns {Promise<void>}
 */
const depositToPull = async (vault, token, amount, is_native = false) => {
    if (is_native) {
        await executeContractFunded(
            token,
            {
                deposit: {
                    recipient: vault,
                },
            },
            [{ amount: amount, denom: OSMO_DENOM }],
        );
    } else {
        await executeContract(token, {
            mint: {
                recipient: vault,
                amount: amount.toString(),
            },
        });
    }

    await executeContract(vault, {
        direct_pool_deposit: {
            token: token,
        },
    });
};

(async () => {
    const code_ids = await storeAllContracts();

    const osmo = await deployWrappedToken(code_ids["omx_cw_wrapped_token"], DEPLOYER_ADDR, DEPLOYER_ADDR, OSMO_DENOM, OSMO_DECIMALS, "osmo");
    const usdc = await deployWrappedToken(code_ids["omx_cw_wrapped_token"], DEPLOYER_ADDR, DEPLOYER_ADDR, USDC_DENOM, USDC_DECIMALS, "usdc");
    const busd = await deployWrappedToken(code_ids["omx_cw_wrapped_token"], DEPLOYER_ADDR, DEPLOYER_ADDR, BUSD_DENOM, BUSD_DECIMALS, "busd");
    const btc = await deployWrappedToken(code_ids["omx_cw_wrapped_token"], DEPLOYER_ADDR, DEPLOYER_ADDR, BTC_DENOM, BTC_DECIMALS, "btc");
    const eth = await deployWrappedToken(code_ids["omx_cw_wrapped_token"], DEPLOYER_ADDR, DEPLOYER_ADDR, ETH_DENOM, ETH_DECIMALS, "eth");
    const usdo = await deployBaseToken(code_ids["omx_cw_base_token"], DEPLOYER_ADDR, DEPLOYER_ADDR, "usdo", USDO_DECIMALS);
    const atom = await deployWrappedToken(code_ids["omx_cw_wrapped_token"], DEPLOYER_ADDR, DEPLOYER_ADDR, ATOM_DENOM, ATOM_DECIMALS, "atom");

    const osmo_price_feed = await deployPriceFeed(code_ids["omx_cw_price_feed"], DEPLOYER_ADDR, "osmo_price_feed");
    const btc_price_feed = await deployPriceFeed(code_ids["omx_cw_price_feed"], DEPLOYER_ADDR, "btc_price_feed");
    const eth_price_feed = await deployPriceFeed(code_ids["omx_cw_price_feed"], DEPLOYER_ADDR, "eth_price_feed");
    const usdc_price_feed = await deployPriceFeed(code_ids["omx_cw_price_feed"], DEPLOYER_ADDR, "usdc_price_feed");
    const busd_price_feed = await deployPriceFeed(code_ids["omx_cw_price_feed"], DEPLOYER_ADDR, "busd_price_feed");
    const atom_price_feed = await deployPriceFeed(code_ids["omx_cw_price_feed"], DEPLOYER_ADDR, "atom_price_feed");

    const eth_busd = await deployPair(code_ids["omx_cw_pair"], DEPLOYER_ADDR, eth, busd, "eth_busd");
    const osmo_eth = await deployPair(code_ids["omx_cw_pair"], DEPLOYER_ADDR, osmo, eth, "osmo_eth");
    const btc_eth = await deployPair(code_ids["omx_cw_pair"], DEPLOYER_ADDR, btc, eth, "btc_eth");

    const vault_price_feed = await deployVaultPriceFeed(code_ids["omx_cw_vault_price_feed"], DEPLOYER_ADDR, {
        btc,
        eth,
        osmo,
        eth_busd,
        btc_eth,
        osmo_eth,
    });

    const vault = await deployVault(code_ids["omx_cw_vault"], DEPLOYER_ADDR, {
        funding_rate_factor: 600n,
        liquidation_fee_usd: 5n * PRICE_PRECISION / 10n,
        vault_price_feed,
        stable_funding_rate_factor: 600n,
        usdo,
    });

    const router = await deployRouter(code_ids["omx_cw_router"], DEPLOYER_ADDR, {
        vault,
        usdo,
        osmo,
    });

    await executeContract(usdo, {
        update_minter: {
            new_minter: vault,
        }
    });

    await executeContract(vault, {
        set_router: {
            router,
        },
    });

    const orderbook = await deployOrderbook(code_ids["omx_cw_orderbook"], DEPLOYER_ADDR, {
        router,
        usdo,
        min_execution_fee: MIN_EXECUTION_FEE,
        min_purchase_token_amount_usd: MIN_PURCHASE_TOKEN_AMOUNT_USD,
        vault,
        wosmo: osmo,
    });

    await executeContract(router, {
        add_plugin: {
            plugin: orderbook,
        },
    });

    await configureVaultPriceFeed(vault_price_feed, [
        {
            price_feed: btc_price_feed,
            token: btc,
        },
        {
            price_feed: eth_price_feed,
            token: eth,
        },
        {
            price_feed: osmo_price_feed,
            token: osmo,
        },
        {
            price_feed: busd_price_feed,
            token: busd,
        },
        {
            price_feed: usdc_price_feed,
            token: usdc,
        },
        {
            price_feed: atom_price_feed,
            token: atom,
        },
    ]);

    await updatePrice(btc_price_feed, BTC_ORACLE_PRICE);
    await updatePrice(eth_price_feed, ETH_ORACLE_PRICE);
    await updatePrice(osmo_price_feed, OSMO_ORACLE_PRICE);
    await updatePrice(busd_price_feed, BUSD_ORACLE_PRICE);
    await updatePrice(usdc_price_feed, USDC_ORACLE_PRICE);
    await updatePrice(atom_price_feed, ATOM_ORACLE_PRICE);

    await executeContract(vault, {
        set_token_config: {
            is_shortable: false,
            is_stable: true,
            max_usdo_amount: "0",
            min_profit_bps: "75",
            token: usdc,
            token_decimals: USDC_DECIMALS,
            token_weight: "1000",
        },
    });
    await executeContract(vault, {
        set_token_config: {
            is_shortable: true,
            is_stable: false,
            max_usdo_amount: "0",
            min_profit_bps: "75",
            token: osmo,
            token_decimals: OSMO_DECIMALS,
            token_weight: "10000",
        },
    });
    await executeContract(vault, {
        set_token_config: {
            is_shortable: true,
            is_stable: false,
            max_usdo_amount: "0",
            min_profit_bps: "75",
            token: btc,
            token_decimals: BTC_DECIMALS,
            token_weight: "10000",
        },
    });
    await executeContract(vault, {
        set_token_config: {
            is_shortable: true,
            is_stable: false,
            max_usdo_amount: "0",
            min_profit_bps: "75",
            token: eth,
            token_decimals: ETH_DECIMALS,
            token_weight: "10000",
        },
    });
    await executeContract(vault, {
        set_token_config: {
            is_shortable: true,
            is_stable: false,
            max_usdo_amount: "0",
            min_profit_bps: "75",
            token: atom,
            token_decimals: ATOM_DECIMALS,
            token_weight: "10000",
        },
    });

    await depositToPull(vault, btc, BTC_DEPOSIT_VAULT_AMOUNT);
    await depositToPull(vault, eth, ETH_DEPOSIT_VAULT_AMOUNT);
    await depositToPull(vault, usdc, USDC_DEPOSIT_VAULT_AMOUNT);
    await depositToPull(vault, osmo, OSMO_DEPOSIT_VAULT_AMOUNT, true);
    await depositToPull(vault, atom, ATOM_DEPOSIT_VAULT_AMOUNT);

    await executeContract(usdc, {
        mint: {
            recipient: DEPLOYER_ADDR,
            amount: (USDC_SCALE * 10000n).toString(),
        },
    });

    console.log(JSON.stringify({
        osmo,
        usdc,
        btc,
        eth,
        usdo,
        busd,
        atom,

        osmo_price_feed,
        btc_price_feed,
        eth_price_feed,
        usdc_price_feed,
        busd_price_feed,
        atom_price_feed,

        eth_busd,
        btc_eth,
        osmo_eth,

        vault,
        router,
        orderbook,
        vault_price_feed,
    }, null, 2));

})().catch((e) => {
    console.error("failed to deploy contracts", e);
    process.exit(1);
});
