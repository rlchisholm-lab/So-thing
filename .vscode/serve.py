import os
import socket
import sys
from urllib.error import URLError
from urllib.request import urlopen


HOST = "127.0.0.1"
PORT = 8000


def is_cork7_server():
    try:
        with urlopen(f"http://{HOST}:{PORT}/", timeout=2) as response:
            page = response.read(100_000)
        return b"Cork7" in page and b"js/index-CYJEV1ir.js" in page
    except (OSError, URLError):
        return False


print("Starting Cork7 server", flush=True)

if is_cork7_server():
    print(f"Serving HTTP on 0.0.0.0 port {PORT} (existing Cork7 server)", flush=True)
    sys.exit(0)

with socket.socket() as sock:
    try:
        sock.bind(("0.0.0.0", PORT))
    except OSError as error:
        raise SystemExit(
            f"Port {PORT} is already in use by a server that is not this Cork7 project."
        ) from error

print(f"Starting static server on port {PORT}", flush=True)
sys.stdout.flush()
sys.stderr.flush()

os.execv(
    sys.executable,
    [sys.executable, "-m", "http.server", str(PORT), "--bind", "0.0.0.0"],
)
