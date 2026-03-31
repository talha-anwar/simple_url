import React, { useState, useEffect } from "react";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import "./index.css";

function App() {
  const [isDark, setIsDark] = useState(localStorage.getItem("theme") === "true");
  function Toggle() {
    setIsDark(!isDark)
    document.documentElement.classList.toggle("dark")
    localStorage.setItem("theme", !isDark)
  }

  useEffect(() => {
    if (isDark) {
      document.documentElement.classList.add("dark");
    }
  }, []);

  return (
    <>
      <Navbar isDark={isDark} onToggle={Toggle}/>
      <Home />
    </>
  );
}

export default App;
