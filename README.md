# DiggerRouter

[![Renovate](https://img.shields.io/badge/renovate-enabled-brightgreen.svg)](https://renovatebot.com)
[![Sourcery](https://img.shields.io/badge/Sourcery-Reviews-FF7A00)](https://sourcery.ai)

Ein Plugin für KiCad, das PCB-Routing direkt in KiCad anbietet: für das im
Schaltplan ausgewählte Signal, für eine Auswahl von Signalen oder für alle
Signale.

Das Plugin besteht aus einem Python-Teil, der über die IPC-API von KiCad
(`kicad-python`) mit dem PCB-Editor spricht, und einem Routing-Kern in Rust.

Das Projekt steht am Anfang. Es gibt noch keinen lauffähigen Code.

## Anforderungen

Die Anforderungen stehen als StrictDoc-Dokumente in [`req/sdoc`](req/sdoc).
[`req/README.md`](req/README.md) beschreibt den Export und das Ändern im
Browser.
