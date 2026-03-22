import React, { useState } from "react";
import styles from "./UrlForm.module.css";

const EXPIRY_OPTIONS = [
  { label: "1 month", value: 30 },
  { label: "3 months", value: 90 },
  { label: "6 months", value: 180 },
];

export default function UrlForm({ mode, onResult }) {
  const [url, setUrl] = useState("");
  const [expiry, setExpiry] = useState(30);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async () => {
    setError("");
    if (!url.trim()) {
      setError("Please enter a URL.");
      return;
    }

    setLoading(true);
    try {
      const body = mode === "quick"
        ? { original_url: url }
        : { original_url: url, expiry_days: expiry };
      console.log("Sending body:", body);

      const res = await fetch("http://localhost:8000/shorten", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body),
      });

      if (!res.ok) throw new Error("Failed to shorten URL.");
      const data = await res.json();
      onResult(data);
      setUrl("");
    } catch (err) {
      setError(err.message || "Something went wrong.");
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") handleSubmit();
  };

  const isPersist = mode === "persistent";

  return (
    <div className={styles.wrapper}>
      <div className={`${styles.inputRow} ${isPersist ? styles.persistBorder : ""}`}>
        <input
          className={styles.input}
          type="url"
          placeholder="https://your-long-url.com"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          onKeyDown={handleKeyDown}
          spellCheck={false}
        />
        <button
          className={`${styles.button} ${isPersist ? styles.buttonDark : ""}`}
          onClick={handleSubmit}
          disabled={loading}
        >
          {loading ? <span className={styles.spinner} /> : "Shorten"}
        </button>
      </div>

      <div className={styles.expiryRow} style={{ visibility: isPersist ? "visible" : "hidden" }}>
        {EXPIRY_OPTIONS.map((opt) => (
          <button
            key={opt.value}
            className={`${styles.expiryOpt} ${expiry === opt.value ? styles.expiryActive : ""}`}
            onClick={() => setExpiry(opt.value)}
          >
            {opt.label}
          </button>
        ))}
      </div>
      
      {error && <p className={styles.error}>{error}</p>}
    </div>
  );
}
