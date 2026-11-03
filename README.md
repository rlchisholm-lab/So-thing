# So-thing

A static web game project for Cork7.

## Run locally

In desktop VS Code, press **F5** and choose **Launch Cork7**. This starts the static server and opens the site in the integrated browser.

To run it manually from the project folder:

```bash
cd /workspaces/So-thing
python3 -m http.server 8000 --bind 0.0.0.0
```

On the same computer, open:

```text
http://localhost:8000
```

On a phone using Codespaces, open the **Ports** tab, find port **8000**, and open or copy its forwarded address. Do not use `localhost` on the phone; that points to the phone itself. Keep the server running while using the forwarded address.

If port 8000 is already in use, try:

```bash
cd /workspaces/So-thing
python3 -m http.server 8001 --bind 0.0.0.0
```

Use port **8001** in the Ports tab (or on the same computer):

```text
http://localhost:8001
```

## Notes

This project is served as a static site and does not require a package install or build step.
