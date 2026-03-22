import React, { useState } from "react";
import UrlForm from "../components/UrlForm";
import ResultCard from "../components/ResultCard";
import ModeToggle from "../components/ModeToggle";
import styles from "./Home.module.css";

export default function Home() {
  const [mode, setMode] = useState("quick");
  const [result, setResult] = useState(null);

  const handleModeSwitch = (newMode) => {
    setMode(newMode);
    setResult(null);
  };

  return (
    <main className={styles.wrapper}>
      <div className={styles.stack}>
        <div className={styles.card}>
          <div className={styles.header}>
            {mode === "quick" ? (
              <>
                <h1 className={styles.title}>
                  Simple <em className={styles.accentGreen}>URL</em>
                </h1>
                <p className={styles.tagline}>Disappears in 24 hours.</p>
              </>
            ) : (
              <>
                <h1 className={styles.title}>
                  Persistent <em className={styles.accentDark}>URL</em>
                </h1>
                <p className={styles.tagline}>Pick how long it sticks around.</p>
              </>
            )}
          </div>

          <UrlForm mode={mode} onResult={setResult} />
          {result && <ResultCard result={result} mode={mode} onResult={setResult} />}
        </div>

        <ModeToggle mode={mode} onSwitch={handleModeSwitch} />
      </div>
    </main>
  );
}
