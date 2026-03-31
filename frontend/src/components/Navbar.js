import React from "react";
import styles from "./Navbar.module.css";
import ThemeToggle from "./ThemeToggle";

function Navbar({ isDark, onToggle }) {
    return (
        <nav className={styles.navbar}>
            <span className={styles.logo}>Simple Url</span>
            <div className={styles.actions}>
                {<ThemeToggle isDark={isDark} onToggle={onToggle}/>}
            </div>
        </nav>
    );
}

export default Navbar;