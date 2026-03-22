import streamlit as st
import random
import string
import math
from datetime import datetime

st.set_page_config(
    page_title="CryptForge — Password Suite",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ══════════════════════════════════════════════════════════════════════════════
# GLOBAL CSS  —  Green × Lime palette only
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@400;600;700;900&family=Outfit:wght@200;300;400;600;700;900&display=swap');

:root {
    --pink:       #00e5ff;
    --pink-light: #40eeff;
    --pink-dim:   rgba(0,229,255,0.15);
    --pink-glow:  rgba(0,229,255,0.35);
    --green:      #39ff14;
    --cyan:       #00e5ff;
    --g1:         #39ff14;
    --g2:         #7fff00;
    --g3:         #00ff88;
    --g-dim:      rgba(57,255,20,0.12);
    --g-glow:     rgba(57,255,20,0.35);
    --g-border:   rgba(0,229,255,0.22);
    --g-border2:  rgba(0,229,255,0.10);
    --bg:         #06010a;
    --surface:    #0d040f;
    --surface2:   #130818;
}

*, *::before, *::after { box-sizing: border-box; }

html, body,
[data-testid="stAppViewContainer"],
[data-testid="stApp"] {
    background: var(--bg) !important;
    font-family: 'Outfit', sans-serif !important;
    color: rgba(57,255,20,0.82) !important;
}

/* Pink+green diagonal grid */
[data-testid="stAppViewContainer"] {
    background-image:
        linear-gradient(135deg, rgba(0,229,255,0.035) 1px, transparent 1px),
        linear-gradient(225deg, rgba(57,255,20,0.03) 1px, transparent 1px);
    background-size: 52px 52px;
}

[data-testid="stHeader"]     { display: none !important; }
[data-testid="stDecoration"] { display: none !important; }
[data-testid="stMainBlockContainer"] { padding-top: 1.5rem !important; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: #080010 !important;
    border-right: 1px solid rgba(57,255,20,0.22) !important;
}
[data-testid="stSidebarNav"] { display: none; }
section[data-testid="stSidebar"] > div { padding-top: 0 !important; }

/* ── Nav radio ── */
[data-testid="stRadio"] > div { flex-direction: column !important; gap: 3px !important; }
[data-testid="stRadio"] label {
    background: transparent !important;
    border: 1px solid transparent !important;
    color: rgba(57,255,20,0.38) !important;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 0.73rem !important;
    letter-spacing: 0.14em !important;
    padding: 11px 18px !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
    border-radius: 0 !important;
    width: 100% !important;
}
[data-testid="stRadio"] label:hover {
    background: rgba(57,255,20,0.08) !important;
    border-color: rgba(57,255,20,0.35) !important;
    color: #39ff14 !important;
}

/* ── Slider ── */
[data-baseweb="slider"] [role="slider"] {
    background: var(--g1) !important;
    box-shadow: 0 0 14px var(--g-glow) !important;
    border-radius: 0 !important;
}

/* ── Checkboxes ── */
[data-testid="stCheckbox"] span {
    color: rgba(57,255,20,0.75) !important;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 0.78rem !important;
    letter-spacing: 0.05em !important;
}
input[type="checkbox"] { accent-color: #39ff14 !important; }

/* ── Buttons ── */
.stButton > button {
    background: transparent !important;
    border: 1px solid rgba(57,255,20,0.4) !important;
    color: #39ff14 !important;
    font-family: 'Share Tech Mono', monospace !important;
    letter-spacing: 0.18em !important;
    font-size: 0.7rem !important;
    border-radius: 0 !important;
    padding: 0.6rem 1rem !important;
    transition: all 0.2s !important;
}
.stButton > button:hover {
    background: rgba(57,255,20,0.08) !important;
    border-color: #39ff14 !important;
    box-shadow: 0 0 22px rgba(57,255,20,0.3) !important;
    color: #7fff00 !important;
}
.stButton > button:active { transform: scale(0.98) !important; }

/* ── Text inputs ── */
input, textarea {
    background: rgba(0,0,0,0.75) !important;
    border: 1px solid rgba(57,255,20,0.22) !important;
    color: var(--g1) !important;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 0.85rem !important;
    border-radius: 0 !important;
    caret-color: #39ff14 !important;
}
input:focus, textarea:focus {
    border-color: #39ff14 !important;
    box-shadow: 0 0 16px rgba(57,255,20,0.3) !important;
    outline: none !important;
}

/* ── Metrics ── */
[data-testid="stMetric"] {
    background: linear-gradient(135deg, rgba(57,255,20,0.05), rgba(0,229,255,0.03)) !important;
    border: 1px solid rgba(57,255,20,0.25) !important;
    padding: 18px 16px !important;
    border-radius: 0 !important;
    position: relative !important;
}
[data-testid="stMetric"]::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; height: 2px;
    background: linear-gradient(90deg, var(--g1), var(--g3));
}
[data-testid="stMetricValue"] {
    font-family: 'Orbitron', monospace !important;
    color: var(--g1) !important;
    font-size: 1.5rem !important;
    font-weight: 700 !important;
    text-shadow: 0 0 12px var(--g-glow) !important;
}
[data-testid="stMetricLabel"] {
    color: rgba(0,229,255,0.6) !important;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 0.58rem !important;
    letter-spacing: 0.22em !important;
    text-transform: uppercase !important;
}

/* ── Container borders ── */
[data-testid="stVerticalBlockBorderWrapper"] > div {
    border: 1px solid rgba(57,255,20,0.2) !important;
    background: rgba(57,255,20,0.02) !important;
    border-radius: 0 !important;
}

/* ── Progress ── */
[data-testid="stProgress"] > div {
    background: rgba(57,255,20,0.07) !important;
    border-radius: 0 !important;
}
[data-testid="stProgress"] > div > div {
    background: linear-gradient(90deg, var(--g1), var(--g3)) !important;
    border-radius: 0 !important;
}

/* ── Alerts ── */
[data-testid="stAlert"] {
    background: rgba(57,255,20,0.06) !important;
    border: 1px solid rgba(57,255,20,0.35) !important;
    border-radius: 0 !important;
    color: var(--g1) !important;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 0.8rem !important;
}

/* ── Expander ── */
[data-testid="stExpander"] {
    border: 1px solid rgba(57,255,20,0.2) !important;
    background: rgba(57,255,20,0.02) !important;
    border-radius: 0 !important;
}
[data-testid="stExpander"] summary {
    color: rgba(57,255,20,0.6) !important;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 0.75rem !important;
    letter-spacing: 0.12em !important;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 3px; height: 3px; }
::-webkit-scrollbar-track { background: #000; }
::-webkit-scrollbar-thumb { background: linear-gradient(var(--g1), var(--g3)); }

/* ── Selectbox ── */
[data-testid="stSelectbox"] > div > div {
    background: #000 !important;
    border: 1px solid var(--g-border) !important;
    border-radius: 0 !important;
    color: var(--g1) !important;
    font-family: 'Share Tech Mono', monospace !important;
}

/* ── hr ── */
hr { border-color: var(--g-border2) !important; }

/* ── Tabs ── */
[data-baseweb="tab-list"] {
    background: transparent !important;
    border-bottom: 1px solid var(--g-border) !important;
}
[data-baseweb="tab"] {
    background: transparent !important;
    color: rgba(57,255,20,0.35) !important;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 0.68rem !important;
    letter-spacing: 0.15em !important;
    border-radius: 0 !important;
    border: none !important;
}
[aria-selected="true"][data-baseweb="tab"] {
    background: var(--g-dim) !important;
    color: var(--g1) !important;
    border-bottom: 2px solid var(--g1) !important;
}

/* ── Labels ── */
label, p {
    font-family: 'Outfit', sans-serif !important;
    color: rgba(57,255,20,0.65) !important;
}

/* ── Code ── */
code, pre {
    font-family: 'Share Tech Mono', monospace !important;
    background: rgba(0,0,0,0.6) !important;
    color: var(--g1) !important;
    border: 1px solid var(--g-border2) !important;
    border-radius: 0 !important;
    font-size: 0.85rem !important;
}

@keyframes glow-pulse {
    0%,100% { opacity:1; box-shadow:0 0 8px rgba(57,255,20,0.8); }
    50%      { opacity:0.5; box-shadow:0 0 20px rgba(57,255,20,0.4); }
}
@keyframes scan {
    0%   { transform: translateY(-100%); }
    100% { transform: translateY(100vh); }
}
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# HELPERS
# ══════════════════════════════════════════════════════════════════════════════
def build_pool(upper, lower, digits, symbols, exclude=""):
    pool = ""
    if upper:   pool += string.ascii_uppercase
    if lower:   pool += string.ascii_lowercase
    if digits:  pool += string.digits
    if symbols: pool += string.punctuation
    if exclude: pool = "".join(c for c in pool if c not in exclude)
    return pool

def generate_password(length, upper, lower, digits, symbols, exclude=""):
    pool = build_pool(upper, lower, digits, symbols, exclude)
    if not pool: return None, "No characters available."
    required = []
    for flag, chars in [(upper, string.ascii_uppercase), (lower, string.ascii_lowercase),
                        (digits, string.digits), (symbols, string.punctuation)]:
        if flag:
            c = [x for x in chars if x not in exclude]
            if c: required.append(random.choice(c))
    if len(required) > length: return None, "Length too short for selected charsets."
    filler   = [random.choice(pool) for _ in range(length - len(required))]
    combined = required + filler
    random.shuffle(combined)
    return "".join(combined), None

def entropy_bits(pwd, pool_size):
    if not pwd or pool_size == 0: return 0
    return round(len(pwd) * math.log2(pool_size))

def crack_time(bits):
    s = (2 ** bits) / 1e12
    if s < 1:        return "Instant"
    if s < 60:       return f"{int(s)}s"
    if s < 3600:     return f"{int(s/60)} min"
    if s < 86400:    return f"{int(s/3600)} hrs"
    if s < 31536000: return f"{int(s/86400)} days"
    y = s / 31536000
    if y < 1000:  return f"{int(y)} yrs"
    if y < 1e6:   return f"{y/1000:.1f}K yrs"
    if y < 1e9:   return f"{y/1e6:.1f}M yrs"
    return f"{y/1e9:.1f}B yrs"

def analyze_password(pwd):
    r = {}
    r["length"]       = len(pwd)
    r["has_upper"]    = any(c.isupper() for c in pwd)
    r["has_lower"]    = any(c.islower() for c in pwd)
    r["has_digit"]    = any(c.isdigit() for c in pwd)
    r["has_symbol"]   = any(c in string.punctuation for c in pwd)
    r["has_repeat"]   = len(set(pwd)) < len(pwd)
    r["has_sequence"] = any(
        ord(pwd[i+1])-ord(pwd[i])==1 and ord(pwd[i+2])-ord(pwd[i+1])==1
        for i in range(len(pwd)-2)
    ) if len(pwd) > 2 else False
    score = 0
    if r["length"] >= 8:  score += 1
    if r["length"] >= 12: score += 1
    if r["length"] >= 16: score += 1
    if r["has_upper"]:    score += 1
    if r["has_lower"]:    score += 1
    if r["has_digit"]:    score += 1
    if r["has_symbol"]:   score += 1
    if not r["has_repeat"]:   score += 0.5
    if not r["has_sequence"]: score += 0.5
    r["score"] = score
    # All strength tiers in green shades only
    if score <= 2:   r["label"] = "CRITICAL"; r["color"] = "#00bcd4"
    elif score <= 4: r["label"] = "WEAK";     r["color"] = "#ff6b00"
    elif score <= 5: r["label"] = "FAIR";     r["color"] = "#ffaa00"
    elif score <= 6: r["label"] = "GOOD";     r["color"] = "#00e5ff"
    else:            r["label"] = "STRONG";   r["color"] = "#39ff14"
    pool = sum([26 if r["has_upper"] else 0, 26 if r["has_lower"] else 0,
                10 if r["has_digit"] else 0, 32 if r["has_symbol"] else 0])
    r["entropy"]    = entropy_bits(pwd, max(pool, 1))
    r["crack_time"] = crack_time(r["entropy"])
    return r

# ── Session state ─────────────────────────────────────────────────────────────
for k, v in [("password",""), ("history",[]), ("vault",[]), ("bulk_passwords",[])]:
    if k not in st.session_state: st.session_state[k] = v


# ══════════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("""
    <div style="padding:28px 20px 24px;border-bottom:1px solid rgba(57,255,20,0.12);margin-bottom:14px;">
        <div style="font-family:'Share Tech Mono',monospace;font-size:0.47rem;
                    color:rgba(57,255,20,0.3);letter-spacing:0.4em;margin-bottom:8px;">
            SYSTEM v3.0 // SECURE
        </div>
        <div style="font-family:'Orbitron',monospace;font-size:1.35rem;font-weight:900;letter-spacing:0.08em;line-height:1;">
            <span style="color:#39ff14;text-shadow:0 0 20px rgba(57,255,20,0.6);">CRYPT</span><span style="color:#7fff00;text-shadow:0 0 20px rgba(127,255,0,0.5);">FORGE</span>
        </div>
        <div style="font-family:'Outfit',sans-serif;font-size:0.65rem;font-weight:300;
                    color:rgba(0,229,255,0.35);letter-spacing:0.15em;margin-top:6px;">
            Password Security Suite
        </div>
        <div style="display:flex;gap:8px;margin-top:14px;align-items:center;">
            <div style="width:7px;height:7px;border-radius:50%;background:#00e5ff;
                        animation:glow-pulse 2s infinite;"></div>
            <div style="width:7px;height:7px;border-radius:50%;background:#ffaa00;opacity:0.5;"></div>
            <div style="width:7px;height:7px;border-radius:50%;background:#39ff14;opacity:0.5;"></div>
            <span style="font-family:'Share Tech Mono',monospace;font-size:0.44rem;
                         color:rgba(57,255,20,0.5);letter-spacing:0.2em;margin-left:4px;">ONLINE</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio("NAV",
        ["🏠  DASHBOARD","⚡  GENERATOR","🔍  ANALYZER","🗄️  VAULT","📊  STATS"],
        label_visibility="collapsed", key="nav_radio")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="font-family:'Share Tech Mono',monospace;font-size:0.47rem;
                color:rgba(57,255,20,0.3);letter-spacing:0.3em;padding:0 4px;margin-bottom:10px;">
        SESSION STATUS
    </div>
    """, unsafe_allow_html=True)
    st.metric("GENERATED", len(st.session_state.history))
    st.metric("VAULTED",   len(st.session_state.vault))

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="padding:14px 16px;border:1px solid rgba(57,255,20,0.1);background:rgba(57,255,20,0.02);">
        <div style="font-family:'Share Tech Mono',monospace;font-size:0.47rem;
                    color:rgba(57,255,20,0.25);letter-spacing:0.15em;line-height:2.4;">
            <span style="color:rgba(57,255,20,0.5);">●</span> LOCAL ONLY<br>
            <span style="color:rgba(57,255,20,0.5);">●</span> NO SERVER CALLS<br>
            <span style="color:rgba(57,255,20,0.5);">●</span> SESSION MEMORY<br>
            <span style="color:rgba(57,255,20,0.5);">●</span> CRYPTO RANDOM
        </div>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# HELPERS: shared UI snippets
# ══════════════════════════════════════════════════════════════════════════════
def page_header(module, title):
    g1, g2 = "#00e5ff", "#39ff14"
    st.markdown(f"""
    <div style="border-bottom:1px solid rgba(57,255,20,0.1);padding-bottom:20px;margin-bottom:32px;">
        <div style="font-family:'Share Tech Mono',monospace;font-size:0.49rem;
                    color:rgba(0,229,255,0.45);letter-spacing:0.45em;margin-bottom:8px;">{module}</div>
        <h2 style="font-family:'Orbitron',monospace;font-size:2rem;font-weight:900;
                   background:linear-gradient(90deg,{g1},{g2});
                   -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                   margin:0;letter-spacing:0.06em;line-height:1.1;">{title}</h2>
    </div>
    """, unsafe_allow_html=True)

def slabel(text, color="rgba(0,229,255,0.55)"):
    st.markdown(f"""
    <div style="font-family:'Share Tech Mono',monospace;font-size:0.57rem;
                color:{color};letter-spacing:0.3em;margin-bottom:8px;margin-top:4px;">{text}</div>
    """, unsafe_allow_html=True)

def tag(txt, border="rgba(57,255,20,0.25)", color="rgba(57,255,20,0.5)"):
    return f'<span style="font-family:\'Share Tech Mono\',monospace;font-size:0.49rem;color:{color};border:1px solid {border};padding:3px 10px;letter-spacing:0.2em;">{txt}</span>'

def empty_state(icon, headline, sub):
    st.markdown(f"""
    <div style="border:1px dashed rgba(57,255,20,0.1);padding:70px 20px;text-align:center;
                background:linear-gradient(135deg,rgba(57,255,20,0.015),rgba(0,255,136,0.01));">
        <div style="font-size:2.6rem;margin-bottom:14px;">{icon}</div>
        <div style="font-family:'Orbitron',monospace;font-size:0.85rem;
                    color:rgba(57,255,20,0.18);letter-spacing:0.22em;">{headline}</div>
        <div style="font-family:'Outfit',sans-serif;font-size:0.92rem;font-weight:300;
                    color:rgba(255,255,255,0.1);margin-top:8px;">{sub}</div>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE ➊  DASHBOARD
# ══════════════════════════════════════════════════════════════════════════════
if page == "🏠  DASHBOARD":
    st.markdown(f"""
    <div style="text-align:center;padding:38px 0 30px;
                border-bottom:1px solid rgba(57,255,20,0.1);margin-bottom:36px;">
        <div style="font-family:'Share Tech Mono',monospace;font-size:0.5rem;
                    color:rgba(57,255,20,0.28);letter-spacing:0.5em;margin-bottom:12px;">
            WELCOME TO
        </div>
        <div style="font-family:'Orbitron',monospace;font-size:3.4rem;font-weight:900;
                    letter-spacing:0.06em;line-height:1;margin-bottom:10px;">
            <span style="color:#39ff14;text-shadow:0 0 32px rgba(57,255,20,0.5);">CRYPT</span><span style="color:#7fff00;text-shadow:0 0 32px rgba(127,255,0,0.4);">FORGE</span>
        </div>
        <div style="font-family:'Outfit',sans-serif;font-size:1.05rem;font-weight:300;
                    color:rgba(57,255,20,0.35);letter-spacing:0.18em;">Advanced Password Security Suite</div>
        <div style="margin-top:20px;display:flex;justify-content:center;gap:10px;flex-wrap:wrap;">
            {tag("SECURE","rgba(0,229,255,0.3)","rgba(0,229,255,0.6)")} {tag("LOCAL","rgba(57,255,20,0.25)","rgba(57,255,20,0.55)")} {tag("FAST","rgba(0,229,255,0.3)","rgba(0,229,255,0.6)")} {tag("OFFLINE","rgba(57,255,20,0.25)","rgba(57,255,20,0.55)")}
        </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("PASSWORDS GENERATED", len(st.session_state.history))
    c2.metric("VAULT ENTRIES",        len(st.session_state.vault))
    avg_bits = (
        round(sum(analyze_password(p["pwd"])["entropy"]
                  for p in st.session_state.history[:10])
              / min(len(st.session_state.history), 10))
        if st.session_state.history else 0
    )
    c3.metric("AVG ENTROPY", f"{avg_bits} bits")
    strong = sum(1 for p in st.session_state.history
                 if analyze_password(p["pwd"])["label"] == "STRONG")
    c4.metric("STRONG PASSWORDS", strong)

    st.markdown("<br>", unsafe_allow_html=True)

    # Feature cards — 3 shades of green
    k1, k2, k3 = st.columns(3)
    cards = [
        (k1, "⚡", "#39ff14", "7fff00", "GENERATOR",
         "Create cryptographically strong passwords — charset control, bulk generation & exclusions."),
        (k2, "🔍", "#7fff00", "00ff88", "ANALYZER",
         "Deep-scan any password: entropy, crack-time, 11-point security checklist & vulnerability report."),
        (k3, "🗄️", "#00e5ff", "39ff14", "VAULT",
         "Save labelled passwords with per-entry copy & delete. Session-based secure storage."),
    ]
    for col, icon, c1c, c2c, title, desc in cards:
        col.markdown(f"""
        <div style="border:1px solid #{c1c}28;
                    background:linear-gradient(145deg,rgba(0,0,0,0.75),rgba(57,255,20,0.03));
                    padding:28px 22px;height:215px;position:relative;overflow:hidden;">
            <div style="position:absolute;top:0;left:0;right:0;height:2px;
                        background:linear-gradient(90deg,#{c1c},#{c2c});"></div>
            <div style="font-size:1.9rem;margin-bottom:14px;">{icon}</div>
            <div style="font-family:'Orbitron',monospace;font-size:0.88rem;font-weight:700;
                        color:#{c1c};letter-spacing:0.12em;margin-bottom:10px;
                        text-shadow:0 0 10px #{c1c}55;">{title}</div>
            <div style="font-family:'Outfit',sans-serif;font-size:0.92rem;font-weight:300;
                        color:rgba(255,255,255,0.45);line-height:1.65;">{desc}</div>
            <div style="position:absolute;bottom:12px;right:16px;font-family:'Orbitron',monospace;
                        font-size:2rem;font-weight:900;color:#{c1c}08;">{title[0]}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    slabel("RECENT ACTIVITY //")

    if st.session_state.history:
        st.markdown("""
        <div style="display:grid;grid-template-columns:1fr 90px 100px 80px;
                    border:1px solid rgba(57,255,20,0.12);background:rgba(57,255,20,0.04);
                    padding:7px 16px;margin-bottom:2px;">
            <span style="font-family:'Share Tech Mono',monospace;font-size:0.51rem;color:rgba(0,229,255,0.5);letter-spacing:0.2em;">PASSWORD</span>
            <span style="font-family:'Share Tech Mono',monospace;font-size:0.51rem;color:rgba(0,229,255,0.5);letter-spacing:0.2em;">STRENGTH</span>
            <span style="font-family:'Share Tech Mono',monospace;font-size:0.51rem;color:rgba(0,229,255,0.5);letter-spacing:0.2em;">ENTROPY</span>
            <span style="font-family:'Share Tech Mono',monospace;font-size:0.51rem;color:rgba(0,229,255,0.5);letter-spacing:0.2em;">TIME</span>
        </div>
        """, unsafe_allow_html=True)
        for item in st.session_state.history[:7]:
            a = analyze_password(item["pwd"])
            st.markdown(f"""
            <div style="display:grid;grid-template-columns:1fr 90px 100px 80px;
                        padding:9px 16px;border:1px solid rgba(57,255,20,0.05);
                        border-top:none;background:rgba(0,0,0,0.38);">
                <span style="font-family:'Share Tech Mono',monospace;font-size:0.72rem;
                             color:rgba(57,255,20,0.62);overflow:hidden;text-overflow:ellipsis;white-space:nowrap;">
                    {item["pwd"][:44]}{"…" if len(item["pwd"])>44 else ""}
                </span>
                <span style="font-family:'Orbitron',monospace;font-size:0.65rem;font-weight:700;color:{a['color']};">{a['label']}</span>
                <span style="font-family:'Share Tech Mono',monospace;font-size:0.68rem;color:rgba(57,255,20,0.3);">{a['entropy']} bits</span>
                <span style="font-family:'Share Tech Mono',monospace;font-size:0.62rem;color:rgba(255,255,255,0.18);">{item['time']}</span>
            </div>
            """, unsafe_allow_html=True)
    else:
        empty_state("⚡", "NO ACTIVITY YET", "Head to the Generator to get started")


# ══════════════════════════════════════════════════════════════════════════════
# PAGE ➋  GENERATOR
# ══════════════════════════════════════════════════════════════════════════════
elif page == "⚡  GENERATOR":
    page_header("MODULE 01", "PASSWORD GENERATOR")

    left, right = st.columns([1, 1], gap="large")

    with left:
        with st.container(border=True):
            slabel("LENGTH://")
            length = st.slider("len", 4, 128, 20, label_visibility="collapsed")

            slabel("CHARSET://")
            g1, g2 = st.columns(2)
            with g1:
                use_upper  = st.checkbox("UPPERCASE  A–Z", value=True)
                use_digits = st.checkbox("NUMBERS    0–9", value=True)
            with g2:
                use_lower   = st.checkbox("LOWERCASE  a–z", value=True)
                use_symbols = st.checkbox("SYMBOLS  !@#$",  value=False)

            slabel("QUANTITY://")
            qty = st.slider("qty", 1, 10, 1, label_visibility="collapsed")

            slabel("EXCLUDE CHARS://")
            exclude = st.text_input("excl", placeholder="e.g. 0Ol1 (ambiguous chars)",
                                    label_visibility="collapsed").replace(" ","")

            b1, b2 = st.columns(2)
            with b1: generate = st.button("⟳  GENERATE", use_container_width=True)
            with b2:
                if st.button("✕  CLEAR", use_container_width=True):
                    st.session_state.password = ""
                    st.session_state.bulk_passwords = []

    with right:
        if generate:
            passwords = []
            for _ in range(qty):
                pwd, err = generate_password(length, use_upper, use_lower,
                                              use_digits, use_symbols, exclude)
                if pwd:
                    passwords.append(pwd)
                    st.session_state.history.insert(0, {
                        "pwd": pwd, "time": datetime.now().strftime("%H:%M:%S")
                    })
                else:
                    st.error(err)
            st.session_state.history = st.session_state.history[:50]
            if passwords:
                st.session_state.password      = passwords[0]
                st.session_state.bulk_passwords = passwords

        pwd  = st.session_state.password
        bulk = st.session_state.bulk_passwords or ([pwd] if pwd else [])

        if pwd:
            a   = analyze_password(pwd)
            pct = min(int(a['score']/8*100), 100)
            fsz = "0.9rem" if len(pwd) > 28 else "1.22rem"
            st.markdown(f"""
            <div style="background:rgba(0,0,0,0.78);border:1px solid rgba(57,255,20,0.3);
                        padding:22px;margin-bottom:16px;position:relative;overflow:hidden;">
                <div style="position:absolute;top:0;left:0;right:0;height:2px;
                            background:linear-gradient(90deg,#39ff14,#00ff88);"></div>
                <div style="font-family:'Share Tech Mono',monospace;font-size:0.49rem;
                            color:rgba(57,255,20,0.32);letter-spacing:0.35em;margin-bottom:12px;">
                    OUTPUT://
                </div>
                <div style="font-family:'Share Tech Mono',monospace;font-size:{fsz};
                            color:#39ff14;word-break:break-all;line-height:1.6;
                            text-shadow:0 0 14px rgba(57,255,20,0.55);">{pwd}</div>
                <div style="margin-top:18px;">
                    <div style="display:flex;justify-content:space-between;margin-bottom:6px;">
                        <span style="font-family:'Share Tech Mono',monospace;font-size:0.51rem;
                                     color:rgba(57,255,20,0.35);letter-spacing:0.2em;">STRENGTH</span>
                        <span style="font-family:'Orbitron',monospace;font-size:0.65rem;font-weight:700;
                                     color:{a['color']};text-shadow:0 0 8px {a['color']}80;">{a['label']}</span>
                    </div>
                    <div style="height:4px;background:rgba(57,255,20,0.07);">
                        <div style="height:100%;width:{pct}%;
                                    background:linear-gradient(90deg,rgba(57,255,20,0.5),{a['color']});
                                    box-shadow:0 0 10px {a['color']}70;transition:width 0.5s;"></div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            m1, m2, m3 = st.columns(3)
            m1.metric("LENGTH",     f"{len(pwd)}")
            m2.metric("ENTROPY",    f"{a['entropy']} bits")
            m3.metric("CRACK TIME", a["crack_time"])

            cc1, cc2 = st.columns(2)
            with cc1:
                if st.button("⧉  COPY PASSWORD", use_container_width=True):
                    try:
                        import pyperclip; pyperclip.copy(pwd)
                        st.success("✓ COPIED TO CLIPBOARD")
                    except: st.code(pwd)
            with cc2:
                if st.button("🗄  SAVE TO VAULT", use_container_width=True):
                    st.session_state.vault.append({
                        "label": f"Password #{len(st.session_state.vault)+1}",
                        "pwd": pwd, "entropy": a["entropy"],
                        "strength": a["label"],
                        "time": datetime.now().strftime("%Y-%m-%d %H:%M")
                    })
                    st.success("✓ SAVED TO VAULT")

            if len(bulk) > 1:
                slabel("ALL GENERATED://", "rgba(57,255,20,0.38)")
                for p in bulk:
                    ab = analyze_password(p)
                    st.markdown(f"""
                    <div style="display:flex;justify-content:space-between;align-items:center;
                                padding:9px 14px;border:1px solid rgba(57,255,20,0.07);
                                border-top:none;background:rgba(0,0,0,0.42);">
                        <span style="font-family:'Share Tech Mono',monospace;font-size:0.7rem;
                                     color:rgba(57,255,20,0.58);flex:1;word-break:break-all;">{p}</span>
                        <span style="font-family:'Orbitron',monospace;font-size:0.6rem;font-weight:700;
                                     color:{ab['color']};margin-left:16px;white-space:nowrap;">{ab['label']}</span>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            empty_state("⚡", "CONFIGURE &amp; PRESS GENERATE", "Your password will appear here")


# ══════════════════════════════════════════════════════════════════════════════
# PAGE ➌  ANALYZER
# ══════════════════════════════════════════════════════════════════════════════
elif page == "🔍  ANALYZER":
    page_header("MODULE 02", "PASSWORD ANALYZER")

    st.markdown("""
    <div style="font-family:'Outfit',sans-serif;font-size:1rem;font-weight:300;
                color:rgba(57,255,20,0.3);margin-bottom:20px;letter-spacing:0.04em;">
        Paste any password for a full deep-security audit.
    </div>
    """, unsafe_allow_html=True)

    analyze_input = st.text_input("", placeholder="Enter password to analyze...",
                                  label_visibility="collapsed", type="password")
    show_pwd = st.checkbox("REVEAL PASSWORD", value=False)

    if show_pwd and analyze_input:
        st.markdown(f"""
        <div style="font-family:'Share Tech Mono',monospace;font-size:1.1rem;
                    color:#39ff14;background:rgba(0,0,0,0.7);padding:14px 18px;
                    border:1px solid rgba(57,255,20,0.25);margin-bottom:16px;
                    word-break:break-all;text-shadow:0 0 10px rgba(57,255,20,0.45);">
            {analyze_input}
        </div>
        """, unsafe_allow_html=True)

    if analyze_input:
        a   = analyze_password(analyze_input)
        pct = min(int(a['score']/8*100), 100)

        # Score banner
        st.markdown(f"""
        <div style="border:1px solid {a['color']}38;
                    background:linear-gradient(135deg,rgba(0,0,0,0.82),{a['color']}06);
                    padding:24px 28px;margin:18px 0;position:relative;overflow:hidden;">
            <div style="position:absolute;top:0;left:0;right:0;height:3px;
                        background:linear-gradient(90deg,#39ff14,{a['color']});"></div>
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;">
                <div>
                    <div style="font-family:'Share Tech Mono',monospace;font-size:0.5rem;
                                color:rgba(57,255,20,0.22);letter-spacing:0.3em;margin-bottom:6px;">SECURITY RATING</div>
                    <div style="font-family:'Orbitron',monospace;font-size:2.3rem;font-weight:900;
                                color:{a['color']};text-shadow:0 0 22px {a['color']}55;letter-spacing:0.08em;">
                        {a['label']}
                    </div>
                </div>
                <div style="font-family:'Orbitron',monospace;font-size:2.8rem;font-weight:900;
                            color:rgba(57,255,20,0.07);">{a['score']:.0f}<span style="font-size:1.2rem;">/8</span></div>
            </div>
            <div style="height:5px;background:rgba(57,255,20,0.05);">
                <div style="height:100%;width:{pct}%;background:linear-gradient(90deg,#39ff14,{a['color']});
                            box-shadow:0 0 12px {a['color']}55;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("LENGTH",     f"{a['length']} chars")
        m2.metric("ENTROPY",    f"{a['entropy']} bits")
        m3.metric("CRACK TIME", a["crack_time"])
        m4.metric("SCORE",      f"{a['score']:.1f}/8")

        st.markdown("<br>", unsafe_allow_html=True)
        slabel("SECURITY CHECKLIST://")
        checks = [
            ("Length ≥ 8",        a["length"] >= 8),
            ("Length ≥ 12",       a["length"] >= 12),
            ("Length ≥ 16",       a["length"] >= 16),
            ("Has uppercase",     a["has_upper"]),
            ("Has lowercase",     a["has_lower"]),
            ("Has digits",        a["has_digit"]),
            ("Has symbols",       a["has_symbol"]),
            ("No repeated chars", not a["has_repeat"]),
            ("No sequences",      not a["has_sequence"]),
            ("Entropy > 60 bits", a["entropy"] > 60),
            ("Entropy > 80 bits", a["entropy"] > 80),
        ]
        cl, cr = st.columns(2)
        for i, (label, passed) in enumerate(checks):
            icon = "✓" if passed else "✗"
            clr  = "#39ff14" if passed else "#00e5ff"
            col  = cl if i % 2 == 0 else cr
            col.markdown(f"""
            <div style="display:flex;align-items:center;gap:12px;padding:9px 14px;
                        border:1px solid {clr}20;background:rgba(0,0,0,0.32);margin-bottom:5px;">
                <span style="font-family:'Orbitron',monospace;color:{clr};font-size:0.8rem;
                             font-weight:700;text-shadow:0 0 8px {clr}55;">{icon}</span>
                <span style="font-family:'Outfit',sans-serif;font-size:0.9rem;font-weight:400;
                             color:rgba(255,255,255,0.45);">{label}</span>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        slabel("CHARACTER BREAKDOWN://")
        uppers  = sum(1 for c in analyze_input if c.isupper())
        lowers  = sum(1 for c in analyze_input if c.islower())
        digits  = sum(1 for c in analyze_input if c.isdigit())
        symbols = sum(1 for c in analyze_input if c in string.punctuation)
        total   = len(analyze_input) or 1
        for lbl, cnt, clr in [("UPPERCASE", uppers, "#39ff14"),
                               ("LOWERCASE", lowers, "#00e5ff"),
                               ("DIGITS",    digits, "#00e5ff"),
                               ("SYMBOLS",   symbols,"#7fff00")]:
            p2 = cnt / total * 100
            st.markdown(f"""
            <div style="display:flex;align-items:center;gap:16px;margin-bottom:10px;">
                <span style="font-family:'Share Tech Mono',monospace;font-size:0.6rem;
                             color:{clr};width:82px;letter-spacing:0.07em;">{lbl}</span>
                <div style="flex:1;height:8px;background:rgba(57,255,20,0.05);">
                    <div style="height:100%;width:{p2:.0f}%;background:{clr};
                                box-shadow:0 0 8px {clr}55;"></div>
                </div>
                <span style="font-family:'Share Tech Mono',monospace;font-size:0.62rem;
                             color:{clr};width:72px;text-align:right;">{cnt} ({p2:.0f}%)</span>
            </div>
            """, unsafe_allow_html=True)

        recs = []
        if a["length"] < 12:    recs.append("Increase length to at least 12 characters")
        if not a["has_upper"]:  recs.append("Add uppercase letters (A–Z)")
        if not a["has_lower"]:  recs.append("Add lowercase letters (a–z)")
        if not a["has_digit"]:  recs.append("Include numbers (0–9)")
        if not a["has_symbol"]: recs.append("Add special symbols (!@#$%)")
        if a["has_sequence"]:   recs.append("Avoid sequential characters (abc, 123)")
        if a["entropy"] < 60:   recs.append("Aim for entropy > 60 bits")

        if recs:
            st.markdown("<br>", unsafe_allow_html=True)
            slabel("RECOMMENDATIONS://", "rgba(127,255,0,0.5)")
            for r in recs:
                st.markdown(f"""
                <div style="padding:9px 16px;border-left:3px solid #ffaa00;
                            background:rgba(255,170,0,0.04);margin-bottom:5px;">
                    <span style="font-family:'Outfit',sans-serif;font-size:0.95rem;font-weight:400;
                                 color:rgba(255,170,0,0.65);">→ {r}</span>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.success("✓ PASSWORD MEETS ALL SECURITY REQUIREMENTS")
    else:
        empty_state("🔍", "TYPE OR PASTE A PASSWORD ABOVE", "Your analysis will appear instantly")


# ══════════════════════════════════════════════════════════════════════════════
# PAGE ➍  VAULT
# ══════════════════════════════════════════════════════════════════════════════
elif page == "🗄️  VAULT":
    page_header("MODULE 03", "SECURE VAULT")

    if not st.session_state.vault:
        empty_state("🗄️", "VAULT IS EMPTY", "Generate passwords and save them here")
    else:
        st.markdown(f"""
        <div style="font-family:'Outfit',sans-serif;font-size:0.95rem;font-weight:300;
                    color:rgba(57,255,20,0.38);margin-bottom:22px;letter-spacing:0.06em;">
            {len(st.session_state.vault)} entries stored &nbsp;·&nbsp;
            <span style="color:rgba(0,229,255,0.4);">Session only — not persisted to disk</span>
        </div>
        """, unsafe_allow_html=True)

        for i, item in enumerate(st.session_state.vault):
            with st.expander(f"  {item['label']}   ·   {item['strength']}   ·   {item['time']}"):
                st.markdown(f"""
                <div style="background:rgba(0,0,0,0.82);border:1px solid rgba(57,255,20,0.2);
                            padding:18px 20px;margin-bottom:14px;position:relative;">
                    <div style="position:absolute;top:0;left:0;right:0;height:2px;
                                background:linear-gradient(90deg,#39ff14,#00ff88);"></div>
                    <div style="font-family:'Share Tech Mono',monospace;font-size:0.49rem;
                                color:rgba(57,255,20,0.28);letter-spacing:0.35em;margin-bottom:10px;">PASSWORD://</div>
                    <div style="font-family:'Share Tech Mono',monospace;font-size:1.05rem;
                                color:#39ff14;word-break:break-all;line-height:1.6;
                                text-shadow:0 0 10px rgba(57,255,20,0.45);">{item['pwd']}</div>
                </div>
                """, unsafe_allow_html=True)
                vc1, vc2, vc3 = st.columns(3)
                vc1.metric("LENGTH",   len(item["pwd"]))
                vc2.metric("ENTROPY",  f"{item['entropy']} bits")
                vc3.metric("STRENGTH", item["strength"])
                d_col, c_col = st.columns(2)
                with c_col:
                    if st.button("⧉ COPY", key=f"cv_{i}", use_container_width=True):
                        try:
                            import pyperclip; pyperclip.copy(item["pwd"])
                            st.success("✓ COPIED")
                        except: st.code(item["pwd"])
                with d_col:
                    if st.button("✕ REMOVE", key=f"dv_{i}", use_container_width=True):
                        st.session_state.vault.pop(i); st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("✕  CLEAR ENTIRE VAULT", use_container_width=True):
            st.session_state.vault = []; st.rerun()


# ══════════════════════════════════════════════════════════════════════════════
# PAGE ➎  STATS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "📊  STATS":
    page_header("MODULE 04", "STATISTICS")

    if not st.session_state.history:
        empty_state("📊", "NO DATA YET", "Generate some passwords first to see statistics")
    else:
        history  = st.session_state.history
        analyses = [analyze_password(h["pwd"]) for h in history]

        avg_len     = round(sum(a["length"]  for a in analyses)/len(analyses), 1)
        avg_entropy = round(sum(a["entropy"] for a in analyses)/len(analyses), 1)
        strong_pct  = round(sum(1 for a in analyses if a["label"]=="STRONG")/len(analyses)*100)

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("TOTAL GENERATED", len(history))
        c2.metric("AVG LENGTH",      f"{avg_len} chars")
        c3.metric("AVG ENTROPY",     f"{avg_entropy} bits")
        c4.metric("STRONG %",        f"{strong_pct}%")

        st.markdown("<br>", unsafe_allow_html=True)
        sl, sr = st.columns(2)

        with sl:
            slabel("STRENGTH DISTRIBUTION://")
            dist  = {}
            for a in analyses: dist[a["label"]] = dist.get(a["label"],0)+1
            order = ["CRITICAL","WEAK","FAIR","GOOD","STRONG"]
            clrs  = {"CRITICAL":"#00bcd4","WEAK":"#00e5ff",
                     "FAIR":"#ffaa00","GOOD":"#00e5ff","STRONG":"#39ff14"}
            for lbl in order:
                cnt  = dist.get(lbl, 0)
                pct  = (cnt/len(history)*100) if history else 0
                clr  = clrs[lbl]
                st.markdown(f"""
                <div style="display:flex;align-items:center;gap:14px;margin-bottom:10px;">
                    <span style="font-family:'Share Tech Mono',monospace;font-size:0.64rem;
                                 color:{clr};width:72px;letter-spacing:0.05em;">{lbl}</span>
                    <div style="flex:1;height:22px;background:rgba(57,255,20,0.04);position:relative;">
                        <div style="height:100%;width:{pct:.0f}%;background:{clr}22;
                                    border-right:3px solid {clr};
                                    box-shadow:inset 0 0 10px {clr}12;"></div>
                        <span style="position:absolute;left:8px;top:50%;transform:translateY(-50%);
                                     font-family:'Share Tech Mono',monospace;font-size:0.54rem;
                                     color:{clr}80;">{cnt} ({pct:.0f}%)</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)

        with sr:
            slabel("ENTROPY OVER TIME://")
            recent = analyses[:20][::-1]
            max_e  = max((a["entropy"] for a in recent), default=1)
            for i, a in enumerate(recent):
                p2  = (a["entropy"]/max_e*100) if max_e else 0
                clr = a["color"]
                st.markdown(f"""
                <div style="display:flex;align-items:center;gap:10px;margin-bottom:6px;">
                    <span style="font-family:'Share Tech Mono',monospace;font-size:0.49rem;
                                 color:rgba(57,255,20,0.18);width:22px;">#{i+1}</span>
                    <div style="flex:1;height:14px;background:rgba(57,255,20,0.04);">
                        <div style="height:100%;width:{p2:.0f}%;
                                    background:linear-gradient(90deg,rgba(57,255,20,0.4),{clr});
                                    opacity:0.75;"></div>
                    </div>
                    <span style="font-family:'Share Tech Mono',monospace;font-size:0.57rem;
                                 color:{clr};width:65px;text-align:right;">{a['entropy']}b</span>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        slabel("FULL HISTORY://")
        st.markdown("""
        <div style="display:grid;grid-template-columns:1fr 60px 90px 100px 80px;
                    border:1px solid rgba(0,229,255,0.15);
                    background:rgba(0,229,255,0.04);padding:8px 16px;margin-bottom:2px;">
            <span style="font-family:'Share Tech Mono',monospace;font-size:0.51rem;color:rgba(57,255,20,0.4);letter-spacing:0.18em;">PASSWORD</span>
            <span style="font-family:'Share Tech Mono',monospace;font-size:0.51rem;color:rgba(57,255,20,0.4);letter-spacing:0.18em;">LEN</span>
            <span style="font-family:'Share Tech Mono',monospace;font-size:0.51rem;color:rgba(57,255,20,0.4);letter-spacing:0.18em;">ENTROPY</span>
            <span style="font-family:'Share Tech Mono',monospace;font-size:0.51rem;color:rgba(57,255,20,0.4);letter-spacing:0.18em;">STRENGTH</span>
            <span style="font-family:'Share Tech Mono',monospace;font-size:0.51rem;color:rgba(57,255,20,0.4);letter-spacing:0.18em;">TIME</span>
        </div>
        """, unsafe_allow_html=True)
        for h, a in zip(history[:25], analyses[:25]):
            st.markdown(f"""
            <div style="display:grid;grid-template-columns:1fr 60px 90px 100px 80px;
                        border:1px solid rgba(57,255,20,0.04);border-top:none;
                        background:rgba(0,0,0,0.42);padding:8px 16px;">
                <span style="font-family:'Share Tech Mono',monospace;font-size:0.7rem;
                             color:rgba(57,255,20,0.55);overflow:hidden;text-overflow:ellipsis;white-space:nowrap;">
                    {h['pwd'][:36]}{"…" if len(h['pwd'])>36 else ""}
                </span>
                <span style="font-family:'Outfit',sans-serif;font-size:0.82rem;font-weight:600;
                             color:rgba(57,255,20,0.32);">{a['length']}</span>
                <span style="font-family:'Outfit',sans-serif;font-size:0.82rem;font-weight:400;
                             color:rgba(57,255,20,0.28);">{a['entropy']} bits</span>
                <span style="font-family:'Orbitron',monospace;font-size:0.64rem;font-weight:700;
                             color:{a['color']};text-shadow:0 0 6px {a['color']}45;">{a['label']}</span>
                <span style="font-family:'Share Tech Mono',monospace;font-size:0.6rem;
                             color:rgba(255,255,255,0.15);">{h['time']}</span>
            </div>
            """, unsafe_allow_html=True)