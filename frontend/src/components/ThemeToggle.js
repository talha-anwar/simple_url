import React from "react";
import styles from "./ThemeToggle.module.css";
import { IoSunnyOutline } from "react-icons/io5";
import { IoIosMoon } from "react-icons/io";

export default function ThemeToggle({ isDark, onToggle }) {
  return (
    <div className={styles.pill}>
      <button
        className={`${styles.side} ${!isDark ? styles.activeGreen : ""}`}
        onClick={() => onToggle()}
      >
        <IoSunnyOutline />
      </button>
      <div />
      <button
        className={`${styles.side} ${isDark ? styles.activeDark : ""}`}
        onClick={() => onToggle()}
      >
        <IoIosMoon />
      </button>
    </div>
  );
}
