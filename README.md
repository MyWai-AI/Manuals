# MYW.AI User Manual (Mintlify)

Documentazione utente della piattaforma MYW.AI, migrata da GitBook a [Mintlify](https://mintlify.com).

## Requisiti

- [Node.js](https://nodejs.org/) (LTS consigliato)
- npm (incluso con Node.js)

## Anteprima in locale

Dalla root del repository:

```bash
npm i -g mint
mint dev
```

Apri nel browser l’URL indicato dal terminale (di solito `http://localhost:3000`).

Le modifiche ai file `.mdx` e a `docs.json` si aggiornano in anteprima automaticamente.

### Comandi utili

```bash
mint validate       # verifica che il progetto sia valido
mint broken-links   # controlla i link interni
```

Ferma il server di anteprima con `Ctrl+C`.

## Versioni

Il sito ha due versioni nello stesso branch, selezionabili dal menu Mintlify:

| Cartella | Versione | Ruolo |
|----------|----------|--------|
| `3.1/` | 3.1 | Manuale pubblicato. È la versione di default. |
| `3.2/` | 3.2 | Manuale in lavorazione. Le modifiche della prossima release vanno qui. |

Le immagini restano in `images/` e `assets/`, condivise dalle due versioni. Un link interno a una pagina usa il prefisso della versione, per esempio `/3.2/configuration/offline-maps`.

## Struttura del progetto

| Path | Descrizione |
|------|-------------|
| `docs.json` | Configurazione Mintlify (versioni, navigazione, tema, colori) |
| `3.1/`, `3.2/` | Pagine del manuale per ciascuna versione |
| `images/` | Immagini e asset |
| `.mintignore` | Esclude dal build il backup GitBook e gli script |
| `user-manual/` | Export originale GitBook (backup) |
| `scripts/` | Script di conversione / fix |

## Riconversione da GitBook (opzionale)

Se aggiorni il contenuto in `user-manual/` e vuoi rigenerare i file Mintlify:

```bash
python scripts/gitbook_to_mintlify.py
```

Dopo aver verificato l’anteprima Mintlify, puoi rimuovere `user-manual/` e `gitbook-docs.yaml`.
