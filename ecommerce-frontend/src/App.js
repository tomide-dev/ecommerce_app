import { useState, useEffect } from "react";
import Login from "./pages/Login";
import Products from "./pages/Products";

function App() {
  const [token, setToken] = useState(null);

  // Load token from localStorage
  useEffect(() => {
    const savedToken = localStorage.getItem("token");
    if (savedToken) {
      setToken(savedToken);
    }
  }, []);

  // Save token when it changes
  useEffect(() => {
    if (token) {
      localStorage.setItem("token", token);
    }
  }, [token]);

  return (
    <div>
      {!token ? (
        <Login setToken={setToken} />
      ) : (
        <Products token={token} setToken={setToken} />
      )}
    </div>
  );
}

export default App;