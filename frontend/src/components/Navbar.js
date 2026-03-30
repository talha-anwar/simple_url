import React from "react";
import styles from "./Navbar.module.css";

function Navbar() {
    return (
        <nav className={styles.navbar}>
            <span className={styles.logo}>Simple Url</span>
            <div className={styles.actions}>
                {/* stuff */}
            </div>
        </nav>
    );
}

export default Navbar;