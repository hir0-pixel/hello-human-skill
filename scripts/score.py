#!/usr/bin/env python3
"""Score text for AI-likeness using lmscan. Pass threshold: ai_probability <= 0.40"""

import argparse
import json
import sys

PASS_THRESHOLD = 0.40
MIN_WORDS_RELIABLE = 300
MIN_CHARS = 20


def score(text: str) -> dict:
    try:
        from lmscan import scan
    except ImportError:
        print(
            "lmscan not installed. Run: pip install lmscan",
            file=sys.stderr,
        )
        sys.exit(2)

    r = scan(text)
    word_count = len(text.split())
    passed = r.ai_probability <= PASS_THRESHOLD and r.verdict != "AI-generated"
    reliable = word_count >= MIN_WORDS_RELIABLE
    return {
        "ai_probability": round(r.ai_probability, 4),
        "verdict": r.verdict,
        "confidence": r.confidence,
        "burstiness": round(r.features.burstiness, 4),
        "slop_word_score": round(r.features.slop_word_score, 4),
        "word_count": word_count,
        "reliable": reliable,
        "pass": passed,
        "threshold": PASS_THRESHOLD,
        "flags": r.flags,
    }


def main():
    p = argparse.ArgumentParser(description="Hello Human AI detector scorer")
    p.add_argument("text", nargs="?", help="Text to score")
    p.add_argument("--file", "-f", help="Read text from file")
    p.add_argument("--json", action="store_true", help="JSON output")
    args = p.parse_args()

    if args.file:
        with open(args.file, encoding="utf-8") as f:
            text = f.read()
    elif args.text:
        text = args.text
    else:
        p.print_help()
        sys.exit(1)

    if len(text.strip()) < MIN_CHARS:
        print(f"Text too short for scoring (min {MIN_CHARS} chars)", file=sys.stderr)
        sys.exit(1)

    result = score(text)
    word_count = result["word_count"]

    if word_count < MIN_WORDS_RELIABLE:
        print(
            f"Warning: {word_count} words — scores below {MIN_WORDS_RELIABLE} are directional only",
            file=sys.stderr,
        )

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        status = "PASS" if result["pass"] else "FAIL"
        print(f"{status}  ai_probability={result['ai_probability']}  threshold={PASS_THRESHOLD}")
        print(f"verdict={result['verdict']}  burstiness={result['burstiness']}  words={word_count}")
        if not result["reliable"]:
            print(f"  (directional only — aim for ≥{MIN_WORDS_RELIABLE} words)")
        if result["flags"]:
            print("\nFlags:")
            for flag in result["flags"][:8]:
                print(f"  - {flag}")

    sys.exit(0 if result["pass"] else 1)


if __name__ == "__main__":
    main()
