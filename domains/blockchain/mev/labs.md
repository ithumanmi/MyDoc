---
title: "MEV Searcher Lab"
description: "Hands-on: build arbitrage bundle, send via Flashbots, monitor inclusion."
tags:
  - mev
  - lab
  - flashbots
updated: 2026-03-11
---

# 🧪 MEV Searcher Lab

Goal: Xây dựng bot đơn giản phát hiện arbitrage Uniswap v2, simulate và submit bundle qua Flashbots.

## Prerequisites

- `python` 3.10 + `web3`, `flashbots`, `dotenv`.
- Access archive node (Alchemy, QuickNode) + signer key.

## Step 1: Setup Repo

```bash
git clone https://github.com/flashbots/searcher-min-bot
cp .env.example .env
```

`.env`

```
ETH_RPC=https://eth-mainnet.alchemyapi.io/v2/KEY
PRIVATE_KEY=0xabc
BUNDLE_SIGNER=0x...
``` 

## Step 2: Price Fetch + Simulation

```python
from web3 import Web3

w3 = Web3(Web3.HTTPProvider(os.environ["ETH_RPC"]))

def get_price(pool, token_in, token_out):
    reserve0, reserve1, _ = pool.functions.getReserves().call()
    return reserve1 / reserve0

def simulate(bundle):
    for tx in bundle:
        res = w3.eth.call(tx, block_identifier="latest")
        assert res, "tx revert"
```

**Exercise:** Implement detection logic quét nhiều pool, return best arbitrage opportunity.

## Step 3: Build Bundle

```python
from flashbots import Flashbots

flashbots = Flashbots(w3, signer)
bundle = [tx_buy, tx_sell]
sim_result = flashbots.simulate(bundle, latest_block + 1)
assert sim_result["error"] is None
flashbots.send_bundle(bundle, target_block=latest_block + 1)
```

**Exercise:** Thêm `coinbase transfer` bribe 0.01 ETH.

## Step 4: Monitor Inclusion

```python
flashbots_response = flashbots.send_bundle(...)
receipt = flashbots_response.wait()
if receipt:
    print("Bundle included in block", receipt.blockNumber)
else:
    print("Not included, retry")
```

## Optional: Integration with `mev-share`

- Subscribe event: `wss://mev-share.flashbots.net`.
- Receive hints, run strategy on partial order flow.

## Deliverables

- [ ] Script detect arbitrage.
- [ ] Simulation + bundle submission.
- [ ] Monitor inclusion + logging.
- [ ] Postmortem nếu thất bại (gas too low, revert, conflicting bundle).