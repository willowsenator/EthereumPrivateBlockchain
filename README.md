# EthereumPrivateBlockchain

Using GETH to create custom private blockchain

* Creating three accounts with password in a file

    `geth --datadir node01 account new --password ./pwd.txt`

    `geth --datadir node02 account new --password ./pwd.txt`

    `geth --datadir node03 account new --password ./pwd.txt`

* Init genesis in each node

    `geth init --datadir node01 genesis.json`

    `geth init --datadir node02 genesis.json`

    `geth init --datadir node03 genesis.json`

* Generate boot.key

    `bootnode -genkey boot.key`

* Start bind node with bootnode key

    `bootnode -nodekey boot.key -addr :30001`
    
    enode://9c52ea4e461cc3035924106eee45a1b63771e6735a61b12df4b874ef698228814ea372daf4ea0e4781d8c8369ad4481da43ff9fc72a9871635366f8501dde06b@127.0.0.1:0?discport=30001

* Start each node
* 
    `geth --datadir node01 --syncmode full --http -http.api  admin,eth,miner,net,web3,clique,txpool,personal --http.corsdomain "*" --http.addr "0.0.0.0" --http.port 8545 --allow-insecure-unlock --unlock "0x00a1866c779e7964fe58752872eb9c57ee5602b9" --password pwd.txt --port 30034 --bootnodes "enode://9c52ea4e461cc3035924106eee45a1b63771e6735a61b12df4b874ef698228814ea372daf4ea0e4781d8c8369ad4481da43ff9fc72a9871635366f8501dde06b@127.0.0.1:0?discport=30001" --ipcpath "\\. /pipe/geth.ipc"`

    `geth --authrpc.port 8552 --datadir node02 --syncmode full --http -http.api admin,eth,miner,net,web3,clique,txpool,personal --http.corsdomain "*" --http.addr "0.0.0.0" --http.port 8546 --allow-insecure-unlock --unlock "0x3812bd6e277c8bf7acfd1bca926841f7f8822af8" --password pwd.txt --port 30035 --bootnodes "enode://9c52ea4e461cc3035924106eee45a1b63771e6735a61b12df4b874ef698228814ea372daf4ea0e4781d8c8369ad4481da43ff9fc72a9871635366f8501dde06b@127.0.0.1:0?discport=30001" --ipcpath "\\. /pipe/geth.ipc"`

    `geth --authrpc.port 8553 --datadir node03 --syncmode full --http -http.api admin,eth,miner,net,web3,clique,txpool,personal --http.corsdomain "*" --http.addr "0.0.0.0" --http.port 8547 --allow-insecure-unlock --unlock "0x7fc575994a80dc2c9c4cb9f1d40f0ebddf817138" --password pwd.txt --port 30036 --bootnodes "enode://9c52ea4e461cc3035924106eee45a1b63771e6735a61b12df4b874ef698228814ea372daf4ea0e4781d8c8369ad4481da43ff9fc72a9871635366f8501dde06b@127.0.0.1:0?discport=30001" --ipcpath "\\. /pipe/geth.ipc"`

