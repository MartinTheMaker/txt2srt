from pathlib import Path
import argparse

def ms_to_srt_time(ms: int) -> str:
    # ms -> HH:MM:SS,mmm
    if ms < 0:
        ms = 0
    h = ms // 3_600_000
    ms %= 3_600_000
    m = ms // 60_000
    ms %= 60_000
    s = ms // 1000
    ms %= 1000
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

def read_blocks_line_mode(text: str) -> list[str]:
    # Jede NICHT-leere Zeile wird ein Block
    return [line.strip() for line in text.splitlines() if line.strip()]

def read_blocks_paragraph_mode(text: str) -> list[str]:
    # Absätze (durch Leerzeilen getrennt) werden je ein Block
    blocks = []
    cur = []
    for line in text.splitlines():
        if line.strip():
            cur.append(line.rstrip())
        else:
            if cur:
                blocks.append("\n".join(cur).strip())
                cur = []
    if cur:
        blocks.append("\n".join(cur).strip())
    return blocks

def make_srt(blocks: list[str], duration_ms: int, gap_ms: int = 0, start_offset_ms: int = 0) -> str:
    out_lines = []
    t = start_offset_ms
    idx = 1
    for b in blocks:
        start = t
        end = t + duration_ms
        out_lines.append(str(idx))
        out_lines.append(f"{ms_to_srt_time(start)} --> {ms_to_srt_time(end)}")
        out_lines.append(b)
        out_lines.append("")  # Leerzeile
        idx += 1
        t = end + gap_ms
    return "\n".join(out_lines)

def main():
    ap = argparse.ArgumentParser(description="Convert lyrics TXT to SRT with constant block duration.")
    ap.add_argument("input_txt", help="Input .txt file with lyrics")
    ap.add_argument("output_srt", help="Output .srt file")
    ap.add_argument("--seconds", type=float, default=3.0, help="Duration per subtitle block in seconds (default: 3.0)")
    ap.add_argument("--gap", type=float, default=0.0, help="Gap between blocks in seconds (default: 0.0)")
    ap.add_argument("--offset", type=float, default=0.0, help="Start offset in seconds (default: 0.0)")
    ap.add_argument("--mode", choices=["line", "paragraph"], default="line",
                    help="line: each non-empty line is a block; paragraph: each paragraph is a block")
    args = ap.parse_args()

    text = Path(args.input_txt).read_text(encoding="utf-8")
    if args.mode == "line":
        blocks = read_blocks_line_mode(text)
    else:
        blocks = read_blocks_paragraph_mode(text)

    duration_ms = int(round(args.seconds * 1000))
    gap_ms = int(round(args.gap * 1000))
    offset_ms = int(round(args.offset * 1000))

    srt = make_srt(blocks, duration_ms, gap_ms=gap_ms, start_offset_ms=offset_ms)
    Path(args.output_srt).write_text(srt, encoding="utf-8")

    print(f"OK: {len(blocks)} blocks -> {args.output_srt}")

if __name__ == "__main__":
    main()
