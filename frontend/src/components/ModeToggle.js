import React from "react";
import styles from "./ModeToggle.module.css";

export default function ModeToggle({ mode, onSwitch }) {
  return (
    <div className={styles.pill}>
      <button
        className={`${styles.side} ${mode === "quick" ? styles.activeGreen : ""}`}
        onClick={() => onSwitch("quick")}
      >
        Simple
      </button>
      <div className={styles.divider} />
      <button
        className={`${styles.side} ${mode === "persistent" ? styles.activeDark : ""}`}
        onClick={() => onSwitch("persistent")}
      >
        Persistent
      </button>
    </div>
  );
}
