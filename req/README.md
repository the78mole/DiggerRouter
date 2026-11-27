# Anforderungen

Die Anforderungen an DiggerRouter stehen als [StrictDoc](https://github.com/the78mole/strictdoc)-Dokumente
in `req/sdoc`.

| Datei | Inhalt | UIDs |
| --- | --- | --- |
| `01_nutzeranforderungen.sdoc` | Was der Nutzer erreichen will | `UR-` |
| `02_architektur.sdoc` | Aufbau des Plugins | `ARCH-` |
| `03_pcb_editor.sdoc` | Knöpfe im PCB-Editor | `PCB-` |
| `04_signalliste.sdoc` | Signallisten-Fenster | `SIG-` |
| `05_routing.sdoc` | Routen, Auflösen, Verbindungsstand | `RTE-` |
| `06_vorschlaege.sdoc` | Noch nicht bestätigte Vorschläge | `VOR-` |
| `grammar.sgra` | Gemeinsame Grammatik aller Dokumente | |

Jede Systemanforderung verweist mit einer `Parent`-Relation auf die
Nutzeranforderung, aus der sie folgt.

Das Feld `STATUS` zeigt den Stand einer Anforderung: `Vorschlag`, `Abgestimmt`,
`Umgesetzt` oder `Verifiziert`.

## HTML erzeugen

StrictDoc kommt aus dem Fork `the78mole/strictdoc`. `req/requirements.txt`
legt den Commit fest. Die Befehle laufen im Wurzelverzeichnis des Repos. Dort
liegt die Konfiguration `strictdoc_config.py`.

```sh
pip install -r req/requirements.txt
strictdoc export . --output-dir output
```

Der Export liegt danach in `output/html/index.html`.

## Veröffentlichung

Der Workflow `Anforderungen` veröffentlicht den Export an zwei Stellen:

- **GitHub Pages:** Jeder Push auf `main`, der die Anforderungen ändert,
  veröffentlicht den HTML-Export unter
  <https://the78mole.github.io/DiggerRouter/>.
- **Release:** Jedes veröffentlichte Release erhält die Datei
  `DiggerRouter-Anforderungen-<tag>.html`. Sie enthält den gesamten Export in
  einer Datei. Mermaid, MathJax und PlantUML lädt sie vom CDN.

Die Datei für ein Release entsteht lokal so:

```sh
strictdoc export . --output-dir output --formats html-single --html-single-libraries cdn
```

Sie liegt danach in `output/html-single/DiggerRouter.html`.

## Anforderungen im Browser ändern

Das Feature `STATIC_EDITING` ist eingeschaltet. Leser des HTML-Exports ändern
Anforderungen direkt im Browser, ohne Server:

1. Im Dokument auf den Bearbeiten-Knopf eines Knotens klicken, Felder ändern
   und speichern.
2. Unten rechts den Namen eintragen und "Export changes as JSON" wählen.
3. Die JSON-Datei auf die SDoc-Dateien anwenden:

   ```sh
   strictdoc apply-changes . strictdoc-changes-<name>-<zeit>.json --dry-run
   strictdoc apply-changes . strictdoc-changes-<name>-<zeit>.json
   ```

4. Die geänderten SDoc-Dateien als Pull Request einreichen.

Alle Knoten haben eine MID in der Quelldatei und sind damit änderbar. Neue
Knoten erhalten ihre MID mit `strictdoc format .`.

Die Dokumente nutzen kein `[DOCUMENT_FROM_FILE]`. Der statische Editor kann
Knoten aus eingebundenen Dokumenten nicht ändern.

## Neue Anforderung anlegen

1. Die Anforderung mit der nächsten freien UID in das passende Dokument
   schreiben.
2. `strictdoc format .` ausführen. Der Befehl ergänzt die MID.
3. `strictdoc export . --output-dir output` ausführen. Der Befehl bricht bei
   unbekannten UIDs in Relationen und Links ab.
