# txt2srt – Opinionated Lyrics → SRT Converter

A minimal Python converter to quickly turn **lyrics from a `.txt` file** into a **`.srt` subtitle file**.

**Design goal:**  
Simple, reproducible, and perfect for **lyric videos** (e.g. DaVinci Resolve), where **timing and pauses are fine-tuned manually later**.

---

## ✨ Features

- ✅ TXT → SRT conversion  
- ✅ **One line = one subtitle block**  
- ✅ Optional: **paragraphs = blocks**  
- ✅ **Constant duration per block** (e.g. 3 or 5 seconds)  
- ✅ Optional start offset & gaps between blocks  
- ✅ UTF-8 compatible (umlauts, special characters)  
- ✅ No external dependencies  

---

## 📄 Input Format

### Standard (recommended)
**One line = one subtitle block**

```txt
I get up without a goal for the day,
do what you do because that’s how it’s done.
I know my paths, they carry me far,
but none of them feel like they’re really mine.
````

Empty lines are ignored.

---

### Paragraph Mode (optional)

**Multiple lines = one block, empty line = block separator**

```txt
I get up without a goal for the day,
do what you do because that’s how it’s done.

I know my paths, they carry me far,
but none of them feel like they’re really mine.
```

---

## ▶️ Usage / CLI Commands

General usage:

```bash
python txt2srt.py <input.txt> <output.srt> [options]
```

---

### 🔹 Simplest Use Case (Standard)

* one line = one subtitle block
* 3 seconds duration per block

```bash
python txt2srt.py lyrics.txt lyrics.srt
```

---

### 🔹 Change Block Duration (e.g. 5 seconds)

```bash
python txt2srt.py lyrics.txt lyrics.srt --seconds 5
```

---

### 🔹 Use Paragraph Mode

```bash
python txt2srt.py lyrics.txt lyrics.srt --mode paragraph
```

---

### 🔹 Set a Start Offset (e.g. intro without text)

```bash
python txt2srt.py lyrics.txt lyrics.srt --offset 1.5
```

---

### 🔹 Insert a Fixed Gap Between Blocks

```bash
python txt2srt.py lyrics.txt lyrics.srt --gap 0.3
```

---

## ⚙️ Options Overview

| Option      | Description                           | Default |
| ----------- | ------------------------------------- | ------- |
| `--seconds` | Duration per subtitle block (seconds) | `3.0`   |
| `--mode`    | `line` or `paragraph`                 | `line`  |
| `--offset`  | Start offset before the first block   | `0.0`   |
| `--gap`     | Pause between blocks                  | `0.0`   |

---

## 📝 License

MIT License
