# EthereumPrivateBlockchain

Using GETH to create custom private blockchain

## Create Accounts

* Creating three accounts with password in a file

    `geth --datadir node01 account new --password ./pwd.txt`

    `geth --datadir node02 account new --password ./pwd.txt`

    `geth --datadir node03 account new --password ./pwd.txt`

* Init genesis in each node

    `geth init --datadir node01 genesis.json`

    `geth init --datadir node02 genesis.json`

    `geth init --datadir node03 genesis.json`