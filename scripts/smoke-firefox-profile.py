#!/usr/bin/env python3
"""Smoke-test potatofox in a temporary Firefox profile."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path


def copy_tree(src: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("firefox", help="Path to the Firefox executable")
    parser.add_argument("--timeout", type=int, default=60)
    parser.add_argument("--startup-seconds", type=int, default=10)
    args = parser.parse_args()

    repo = Path(__file__).resolve().parents[1]
    firefox = shutil.which(args.firefox) or args.firefox
    firefox_path = Path(firefox)

    if not firefox_path.exists() and shutil.which(args.firefox) is None:
        print(f"Firefox executable not found: {args.firefox}", file=sys.stderr)
        return 2

    required = [repo / "user.js", repo / "chrome" / "userChrome.css", repo / "chrome" / "userContent.css"]
    missing = [str(path.relative_to(repo)) for path in required if not path.exists()]
    if missing:
        print(f"Missing required profile files: {', '.join(missing)}", file=sys.stderr)
        return 2

    with tempfile.TemporaryDirectory(prefix="potatofox-") as tmp:
        tmp_path = Path(tmp)
        profile = tmp_path / "profile"
        profile.mkdir()
        shutil.copy2(repo / "user.js", profile / "user.js")
        copy_tree(repo / "chrome", profile / "chrome")

        cmd = [
            str(firefox),
            "--headless",
            "--no-remote",
            "--profile",
            str(profile),
            "about:blank",
        ]

        env = os.environ.copy()
        env.setdefault("MOZ_HEADLESS", "1")
        env.setdefault("MOZ_DISABLE_CONTENT_SANDBOX", "1")

        proc = subprocess.Popen(
            cmd,
            cwd=repo,
            env=env,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        deadline = time.monotonic() + min(args.startup_seconds, args.timeout)
        while time.monotonic() < deadline:
            returncode = proc.poll()
            if returncode is not None:
                stdout, stderr = proc.communicate()
                print(stdout, file=sys.stderr)
                print(stderr, file=sys.stderr)
                print(f"Firefox exited during startup with status {returncode}", file=sys.stderr)
                return returncode or 1
            time.sleep(0.25)

        proc.terminate()
        try:
            stdout, stderr = proc.communicate(timeout=15)
        except subprocess.TimeoutExpired:
            proc.kill()
            stdout, stderr = proc.communicate(timeout=15)

        print(f"Firefox profile smoke test passed after {args.startup_seconds}s")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
