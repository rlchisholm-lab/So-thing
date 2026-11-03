# So-thing

A polished static web project for Cork7, built to run directly in the browser without a package install or build pipeline.

## Overview

This repository contains the front-end assets for the Cork7 experience:

- HTML entry point: `index.html`
- Styling: `css/`
- Client logic and runtime scripts: `js/`
- Shared images and branding: `images/`
- Local onboarding art fallbacks: `onboarding/`

## Quick start

### Option 1: VS Code

Press **F5** in VS Code and choose the existing launch configuration for the project. That starts a local static server and opens the app in the integrated browser.

### Option 2: Local Python server

From the repository root:

```bash
cd /workspaces/So-thing
python3 -m http.server 8000 --bind 0.0.0.0
```

Then open:

```text
http://localhost:8000
```

### Access from a phone or another device

If you are using GitHub Codespaces or a forwarded port, open the **Ports** tab and use the forwarded URL for port `8000`.

Important:

- Do not use `localhost` on a phone, because it points to the phone itself.
- Keep the server running while using the forwarded address.

### If port 8000 is already in use

```bash
cd /workspaces/So-thing
python3 -m http.server 8001 --bind 0.0.0.0
```

Use:

```text
http://localhost:8001
```

## Project layout

```text
.
├── css/            # compiled stylesheets
├── fonts/          # bundled web fonts
├── images/         # app branding and marketing assets
├── js/             # client-side JavaScript bundles
├── onboarding/     # local fallback art used by startup/loading screens
├── index.html      # app entry point
├── README.md       # project overview and run instructions
├── site.webmanifest
└── .vscode/        # editor launch/tasks config
```

## Notes

- This project is served as a static site.
- There is no Node package install or app build step required for local development.
- If assets are missing or a browser shows an empty startup image, the bundled fallback onboarding folder ensures the page still loads correctly.

## Troubleshooting

- If the page does not load, confirm that the local HTTP server is still running.
- If port `8000` is busy, use port `8001` as shown above.
- If the browser is blank or some art is missing, refresh the page after ensuring the static server is serving the project root.
