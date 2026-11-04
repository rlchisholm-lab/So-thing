# So-thing

A polished static web project for Cork7, built to run directly in the browser without a package install or build pipeline.

## Overview

This repository contains the front-end assets for the Cork7 experience:


- This project is served as a static site.
- There is no Node package install or app build step required for local development.
- Keep `_next/static/` when copying or deploying the site; the client runtime loads chunks and styles from those paths.
- Keep `models/`, `grabs/`, `images/mountain-map/`, and the Meshopt decoder in `js/`; the 3D scene, rider animations, and responsive map need them.
- If assets are missing or a browser shows an empty startup image, the bundled fallback onboarding folder ensures the page still loads correctly.
- Guest accounts save the rider name and progress on the current device only. They do not sync across devices and can be lost if the browser's site data is cleared; online account features still require signing in.
- Password recovery can stay in the app: configure the Supabase Auth **Reset Password** email template to show `{{ .Token }}` as a code instead of linking to `{{ .ConfirmationURL }}`. The user enters that code on the recovery form with their new password. Recovery still requires access to the account email; the app does not send the email itself.

## Troubleshooting

- If the page does not load, confirm that the local HTTP server is still running.
- If port `8000` is already serving another project, stop that server before launching Cork7.
- If port `8000` is busy, use port `8001` as shown above.
- If the browser is blank or some art is missing, refresh the page after ensuring the static server is serving the project root.
