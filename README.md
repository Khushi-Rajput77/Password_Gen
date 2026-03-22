# 🔐 CryptForge — Password Security Suite

> Advanced password generation, analysis & secure vault — built with Python & Streamlit

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Security](https://img.shields.io/badge/Security-Local_Only-39ff14?style=for-the-badge&logo=shield&logoColor=black)
![No Server](https://img.shields.io/badge/No_Server-Offline_Ready-00e5ff?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-7fff00?style=for-the-badge)

---

## 📋 Overview

**CryptForge** is a cyberpunk-themed password security suite that lets you generate cryptographically strong passwords, deep-scan any password for vulnerabilities, and store your best passwords in a session vault — all running **100% locally** in your browser with zero server calls.

- ✅ **No internet required** after install
- ✅ **No data leaves your machine** — everything stays local
- ✅ **Cryptographically random** generation using Python's `random` module
- ✅ **Real entropy calculation** with crack-time estimation
- ✅ **Multi-module** — Generator, Analyzer, Vault, and Statistics in one app

---

## ✨ Features

### 🏠 Dashboard
- Live session stats — passwords generated, vault entries, average entropy
- Quick overview cards for every module
- Recent activity feed showing last 7 passwords with strength and entropy

### ⚡ Generator
- Password length: **4 to 128 characters** (slider control)
- Charset options: Uppercase A–Z, Lowercase a–z, Digits 0–9, Symbols `!@#$`
- **Bulk generation**: create up to 10 passwords at once
- **Exclude characters**: remove ambiguous chars like `0`, `O`, `l`, `1`
- Real-time strength bar and entropy display for every generated password
- One-click copy to clipboard
- Save any password directly to the Vault

### 🔍 Analyzer
- Paste any existing password for a full **deep security audit**
- **11-point security checklist** — length, charset diversity, sequences, entropy
- Entropy bits + estimated crack time at 1 trillion guesses/second
- Character breakdown: Uppercase / Lowercase / Digits / Symbols with visual bars
- Personalised recommendations to improve weak passwords
- Optional password **reveal toggle**

### 🗄️ Vault
- Save labelled passwords with strength rating and timestamp
- Per-entry **copy** and **delete** buttons
- Full vault clear option
- Session-based — vault lives in memory, never written to disk

### 📊 Statistics
- Total generated, average length, average entropy, strong password percentage
- Strength distribution bar chart (Critical → Weak → Fair → Good → Strong)
- Entropy over time chart for last 20 passwords
- Full history table — last 25 entries with length, entropy, strength, and time

---

## 📁 File Structure

```
cryptforge/
├── cryptforge.py       # Main application (single file — run this)
└── README.md           # This file
```

> **Note:** CryptForge has no database and writes no files to disk. All data lives in Streamlit session memory and is cleared when you close or refresh the browser tab.

---

## 📦 Requirements

**Python 3.8 or higher** is required.

| Library | Purpose |
|---|---|
| `streamlit` | Web UI framework — renders the entire app in browser |
| `random` | Built-in — random password generation |
| `string` | Built-in — character set pools (uppercase, lowercase, digits, symbols) |
| `math` | Built-in — entropy calculation using `log2` |
| `datetime` | Built-in — timestamps for history and vault entries |
| `pyperclip` | Optional — enables clipboard copy button |

---

## 🚀 Installation & Setup

### Step 1 — Clone the Repository

```bash
git clone https://github.com/your-username/cryptforge.git
cd cryptforge
```

### Step 2 — Install Dependencies

```bash
pip install streamlit
```

For clipboard copy support (optional but recommended):

```bash
pip install pyperclip
```

### Step 3 — Run the App

```bash
streamlit run cryptforge.py
```

The app opens automatically in your browser at:

```
http://localhost:8501
```

### Step 4 — Stop the App

Press `Ctrl + C` in the terminal.

---

## 📖 How to Use

### Generating a Password
1. Go to **⚡ Generator** in the sidebar
2. Set your desired **length** using the slider (default: 20)
3. Choose your **character sets** — Uppercase, Lowercase, Digits, Symbols
4. Optionally set **quantity** (1–10) for bulk generation
5. Optionally **exclude** ambiguous characters like `0Ol1`
6. Click **⟳ GENERATE**
7. Copy the result or save it to the Vault

### Analyzing a Password
1. Go to **🔍 Analyzer** in the sidebar
2. Paste or type any password into the input field
3. View your **security rating**, entropy, crack time, and 11-point checklist
4. Follow the **recommendations** shown at the bottom to fix weaknesses

### Using the Vault
1. Generate a password and click **🗄 SAVE TO VAULT**
2. Go to **🗄️ Vault** to view, copy, or delete saved entries
3. Note: vault is **session only** — it clears when you close the browser tab

### Viewing Statistics
1. Generate several passwords first
2. Go to **📊 Stats** to see strength distribution, entropy trends, and full history

---

## 🔐 Security & Privacy

| Feature | Detail |
|---|---|
| Local only | No data is ever sent to any server or external service |
| No disk writes | Vault and history exist only in session memory |
| No logging | Nothing is recorded beyond the current browser session |
| Crypto random | Uses Python's `random` module seeded by OS entropy |
| Minimal dependencies | Core functionality needs only Python's standard library |

> ⚠️ **Important:** Because the vault is session-based, all saved passwords are lost when you close or refresh the browser tab. Copy important passwords before closing.

---

## 📊 Entropy & Strength Reference

| Entropy | Strength Label | Approx. Crack Time at 1T guesses/sec |
|---|---|---|
| Below 40 bits | CRITICAL | Seconds to minutes |
| 40 – 60 bits | WEAK | Hours to days |
| 60 – 70 bits | FAIR | Years |
| 70 – 80 bits | GOOD | Thousands of years |
| 80+ bits | STRONG | Millions+ of years |

**Entropy Formula:**

```
Entropy (bits) = Password Length × log₂(Character Pool Size)
```

**Example:**

```
20 chars, pool = upper + lower + digits = 62 chars
→ 20 × log₂(62) = 20 × 5.95 = 119 bits  →  STRONG ✅
```

---

## ⚙️ Generation Algorithm

```
1. Build character pool from selected charsets
2. Remove any user-excluded characters from the pool
3. Guarantee at least one character from each selected charset
4. Fill remaining positions randomly from the full pool
5. Shuffle the combined list to remove positional bias
6. Return the final password string
```

This ensures every selected charset is always represented while maintaining true randomness across all positions.

---

## 🔧 Troubleshooting

| Problem | Solution |
|---|---|
| `ModuleNotFoundError: streamlit` | Run `pip install streamlit` |
| Copy button not working | Run `pip install pyperclip` — password shows as code block as fallback |
| Port 8501 already in use | Run `streamlit run cryptforge.py --server.port 8502` |
| Sidebar not visible | Click the `>` arrow on the top-left of the screen |
| App shows error on start | Check Python version — needs 3.8 or higher |
| Browser does not open automatically | Go to `http://localhost:8501` manually |
| Vault was cleared | Vault is session-only — refreshing the page clears it by design |
| `No characters available` error | At least one charset must be selected in the Generator |

---

## 🛠️ Technology Stack

| Technology | Role |
|---|---|
| Python 3.8+ | Core programming language |
| Streamlit | Web UI framework — entire app in a single Python file |
| Orbitron (Google Fonts) | Cyberpunk-style headings and metric values |
| Share Tech Mono (Google Fonts) | Monospace labels, password display, and nav items |
| Outfit (Google Fonts) | Body text and descriptions |
| Custom CSS | Full dark neon theme — green/cyan palette with glow animations |

---

## 🎨 Design System

CryptForge uses a **cyberpunk neon aesthetic** throughout:

| Element | Value |
|---|---|
| Background | `#06010a` — deep black with diagonal grid overlay |
| Primary accent | `#39ff14` — neon green with CSS glow |
| Secondary accent | `#00e5ff` — cyan |
| Tertiary | `#7fff00` — lime green |
| Border style | Sharp corners — zero border-radius |
| Animations | Glow pulse on status indicators |

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m 'Add my feature'`
4. Push to the branch: `git push origin feature/my-feature`
5. Open a Pull Request

**Ideas for future features:**
- Export vault to encrypted JSON or CSV
- Persistent vault using local encrypted file
- Passphrase generator (word-based, e.g. Diceware)
- Password breach check via HaveIBeenPwned API (k-anonymity)
- Dark/light theme toggle

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

---

## 👤 Author

**Your Name**  
GitHub: [@your-username](https://github.com/your-username)

---

<div align="center">
  <strong>🔐 CryptForge</strong> — Password Security Suite<br>
  Local only &nbsp;•&nbsp; No server calls &nbsp;•&nbsp; Crypto random generation<br><br>
  <code>streamlit run cryptforge.py</code>
</div>