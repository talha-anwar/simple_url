import React, { useState } from "react";
import styles from "./ResultCard.module.css";

export default function ResultCard({ result, mode, onResult }) {
  const [copied, setCopied] = useState(false);
  const [shuffling, setShuffling] = useState(false);

  const shortUrl = `http://localhost:8000/${result.short_code}`;

  const handleCopy = () => {
    navigator.clipboard.writeText(shortUrl);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const handleShuffle = async () => {
    setShuffling(true);
    try {
      const res = await fetch("http://localhost:8000/shuffle", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          original_url: result.original_url,
          old_short_code: result.short_code,
          expiry_days: result.expiry_days ?? null,
        }),
      });
      if (!res.ok) throw new Error("Shuffle failed.");
      const data = await res.json();
      onResult(data);
    } catch (err) {
      console.error(err);
    } finally {
      setShuffling(false);
    }
  };

  return (
    <div className={styles.card}>
      <p className={styles.label}>YOUR LINK</p>
      <div className={styles.row}>
        <a
          href={shortUrl}
          target="_blank"
          rel="noopener noreferrer"
          className={styles.link}
        >
          {shortUrl}
        </a>
        <div className={styles.actions}>
          <button className={styles.shuffleBtn} onClick={handleShuffle} disabled={shuffling}>
            {shuffling ? "..." : "↺"}
          </button>
          <button className={styles.copyBtn} onClick={handleCopy}>
            {copied ? "Copied!" : "Copy"}
          </button>
        </div>
      </div>
      <p className={styles.original} title={result.original_url}>
        ↳ {result.original_url}
      </p>
    </div>
  );
}