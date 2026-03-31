import React, { useState} from "react";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import "./index.css";

function App() {
  const [isDark, setIsDark] = useState(false);
  function Toggle() {
    setIsDark(!isDark)
    document.documentElement.classList.toggle("dark")
  }
  return (
    <>
      <Navbar isDark={isDark} onToggle={Toggle}/>
      <Home />
    </>
  );
}

export default App;
