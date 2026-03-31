import React from "react";

export default function ThemeToggle({ isDark, onToggle }) {
    return (
        <button onClick={onToggle}>
            {isDark ? "Light" : "Dark"}
        </button>
    );
}