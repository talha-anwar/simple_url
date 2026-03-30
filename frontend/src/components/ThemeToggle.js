import React from "react";
import styles from "./ThemeToggle.module.css";

export default function ModeToggle({ mode, onSwitch }) {
  return (
    <div className={styles.pill}>
      <button
        className={`${styles.side} ${mode === "light" ? styles.activeGreen : ""}`}
        onClick={() => onSwitch("light")}
      >
        Simple
      </button>
      <div className={styles.divider} />
      <button
        className={`${styles.side} ${mode === "dark" ? styles.activeDark : ""}`}
        onClick={() => onSwitch("dark")}
      >
        Persistent
      </button>
    </div>
  );
}
