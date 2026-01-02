# txt2srt – Opinionated Lyrics → SRT Converter

Ein minimaler Python-Converter, um **Lyrics aus einer `.txt`-Datei** schnell in eine **`.srt`-Subtitle-Datei** zu verwandeln.

**Design-Ziel:**  
Einfach, reproduzierbar, perfekt für **Lyric-Videos** (z. B. DaVinci Resolve), bei denen **Timing und Pausen später manuell feinjustiert** werden.

---

## ✨ Features

- ✅ TXT → SRT Konvertierung
- ✅ **Eine Zeile = ein Subtitle-Block**
- ✅ Option: **Absätze = Blöcke**
- ✅ **Konstante Dauer pro Block** (z. B. 3 oder 5 Sekunden)
- ✅ Optionaler Start-Offset & Pausen zwischen Blöcken
- ✅ UTF-8 kompatibel (Umlaute, Sonderzeichen)
- ✅ Keine externen Dependencies

---

## 📄 Input-Format

### Standard (empfohlen)
**Eine Zeile = ein Subtitle-Block**

```txt
Ich steh auf, ohne Ziel für den Tag,
mach, was man macht, weil man’s so macht.
Ich kenn meine Wege, sie tragen mich weit,
aber keiner davon fühlt sich nach mir an.
```

Leerzeilen werden ignoriert.

---

### Absatz-Modus (optional)
**Mehrere Zeilen = ein Block, Leerzeile = Block-Trenner**

```txt
Ich steh auf, ohne Ziel für den Tag,
mach, was man macht, weil man’s so macht.

Ich kenn meine Wege, sie tragen mich weit,
aber keiner davon fühlt sich nach mir an.
```

---

## ▶️ Nutzung / CLI-Befehle

Allgemeiner Aufruf:

```bash
python txt2srt.py <input.txt> <output.srt> [optionen]
```

---

### 🔹 Einfachster Anwendungsfall (Standard)

- eine Zeile = ein Subtitle-Block  
- 3 Sekunden Dauer pro Block  

```bash
python txt2srt.py lyrics.txt lyrics.srt
```

---

### 🔹 Blocklänge ändern (z. B. 5 Sekunden)

```bash
python txt2srt.py lyrics.txt lyrics.srt --seconds 5
```

---

### 🔹 Absatz-Modus verwenden

```bash
python txt2srt.py lyrics.txt lyrics.srt --mode paragraph
```

---

### 🔹 Start-Offset setzen (z. B. Intro ohne Text)

```bash
python txt2srt.py lyrics.txt lyrics.srt --offset 1.5
```

---

### 🔹 Feste Pause zwischen Blöcken einfügen

```bash
python txt2srt.py lyrics.txt lyrics.srt --gap 0.3
```

---

## ⚙️ Optionen im Überblick

| Option | Beschreibung | Default |
|------|-------------|---------|
| `--seconds` | Dauer pro Subtitle-Block (Sekunden) | `3.0` |
| `--mode` | `line` oder `paragraph` | `line` |
| `--offset` | Startversatz vor dem ersten Block | `0.0` |
| `--gap` | Pause zwischen Blocks | `0.0` |


---

## 📝 Lizenz

MIT License
