import { useEffect, useState } from "react";

function App() {
  const [loading, setLoading] = useState(true);
  const [coins, setCoins] = useState([]);
  const [count, setCount] = useState(0);
  const [money, setMoney] = useState(0);
  useEffect(() => {
    fetch("https://api.coinpaprika.com/v1/tickers").then((response) =>
      response.json().then((json) => {
        setCoins(json);
        setLoading(false);
      })
    );
  }, []);
  const setCoin = (event) => {
    setCount(event.target.value);
  };
  const setInput = (event) => {
    setMoney(event.target.value);
  };
  return (
    <div>
      <input
        onChange={setInput}
        type="number"
        placeholder="Please enter a value"
      ></input>
      $<h1>The Coins! {loading ? "" : `(${coins.length})`}</h1>
      {loading ? (
        <strong>Loading...</strong>
      ) : (
        <select onChange={setCoin}>
          <option>Select Coin</option>
          {coins.map((coin) => (
            <option value={coin.quotes.USD.price}>
              {coin.name} ({coin.symbol}) : {coin.quotes.USD.price} USD
            </option>
          ))}
        </select>
      )}
      <h3>You can buy : {count > 0 ? money / count : 0}</h3>
    </div>
  );
}

export default App;
