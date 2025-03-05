module TradingBot::StockTrading {

    struct TradeRecord has copy, drop, store {
        symbol: vector<u8>,
        action: vector<u8>,
    }

    public entry fun record_trade(
        account: &signer,
        symbol: vector<u8>, 
        action: vector<u8>
    ) {
        let record = TradeRecord { symbol, action };
        move_to(account, record);
    }
}