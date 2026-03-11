---
title: "Oracle Integration Lab"
description: "Hands-on: Chainlink price feed, Pyth dual-feed fallback, monitoring script."
tags:
  - oracle
  - solidity
  - lab
updated: 2026-03-11
---

# 🧪 Oracle Integration Lab

Goal: Build smart contract đọc Chainlink feed, fallback sang Pyth/Uniswap TWAP và thiết lập monitoring script.

## Lab Setup

1. `forge init oracle-lab`
2. Thêm dependency:
   ```bash
   forge install smartcontractkit/chainlink-brownie-contracts --no-commit
   forge install pyth-network/pyth-sdk-solidity --no-commit
   ```
3. Set env: `.env` chứa RPC, PRIVATE_KEY, ETHERSCAN_API.

## Step 1: Chainlink Feed Reader

`src/PriceFeed.sol`

```solidity
contract PriceFeed {
    AggregatorV3Interface public immutable chainlinkFeed;
    uint256 public immutable heartbeat;

    constructor(address feed, uint256 _heartbeat) {
        chainlinkFeed = AggregatorV3Interface(feed);
        heartbeat = _heartbeat;
    }

    function getPrice() public view returns (int256 price) {
        (, price,, uint256 updatedAt,) = chainlinkFeed.latestRoundData();
        require(price > 0, "Invalid");
        require(block.timestamp - updatedAt < heartbeat, "Stale");
    }
}
```

**Task:** Viết test sử dụng mock aggregator (`MockV3Aggregator`) để kiểm tra stale guard.

## Step 2: Dual Feed Fallback (Pyth)

```solidity
function getReliablePrice(bytes[] calldata priceUpdateData) external returns (int256) {
    try this.getPrice() returns (int256 chainlinkPrice) {
        lastPrice = chainlinkPrice;
        return chainlinkPrice;
    } catch {
        pyth.updatePriceFeeds(priceUpdateData);
        PythStructs.Price memory price = pyth.getPriceUnsafe(feedId);
        require(block.timestamp - price.publishTime < pythHeartbeat, "stale pyth");
        lastPrice = price.price;
        return price.price;
    }
}
```

**Exercise:** Implement requirement so that Pyth price phải gần với Chainlink price trước đó (`abs(price - lastPrice) < maxDeviation`).

## Step 3: On-chain TWAP Backup

- Sử dụng Uniswap v3 `OracleLibrary.consult(pool, secondsAgo)` để lấy TWAP.
- So sánh TWAP vs oracle → nếu sai lệch lớn → trigger circuit breaker event.

## Step 4: Monitoring Script

Python script `monitor.py`:

```python
import asyncio
from web3 import Web3

w3 = Web3(Web3.HTTPProvider(os.environ["RPC"]))
contract = w3.eth.contract(address=..., abi=json.load(open('abi.json')))

async def loop():
    while True:
        price, updated_at = contract.functions.latest().call()
        if time.time() - updated_at > HEARTBEAT:
            alert_slack("Feed stale")
        await asyncio.sleep(30)

asyncio.run(loop())
```

**Exercise:** Thêm logic gửi alert khi Chainlink vs Pyth price lệch > 1%.

## Deliverables

- [ ] Contract + tests.
- [ ] Script monitor.
- [ ] README lab ghi lại command deploy + test result.