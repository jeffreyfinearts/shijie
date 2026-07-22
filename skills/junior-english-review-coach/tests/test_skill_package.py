#!/usr/bin/env python3
"""Deterministic package checks for the first educational Skill."""
from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = {
    "SKILL.md",
    "README.md",
    "CHANGELOG.md",
    "SOURCE_ANALYSIS.md",
    "ORIGINALITY_REPORT.md",
    "ENHANCEMENT_REPORT.md",
    "MONETIZATION.md",
    "references/output_schema.md",
    "examples/basic_session.md",
    "tests/cases.json",
}


def main() -> None:
    missing = [p for p in REQUIRED_FILES if not (ROOT / p).is_file()]
    assert not missing, f"missing required files: {missing}"

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    assert skill.startswith("---\n"), "SKILL.md needs YAML frontmatter"
    assert re.search(r"^name:\s+junior-english-review-coach\s*$", skill, re.M)
    assert re.search(r"^description:\s+.+$", skill, re.M)
    for heading in ("输入要求", "执行流程", "输出格式", "质量检查", "异常处理与安全", "依赖与环境变量"):
        assert heading in skill, f"missing section: {heading}"
    assert "OPENAI_API_KEY" in skill and "禁止索取或输出" in skill

    cases = json.loads((ROOT / "tests/cases.json").read_text(encoding="utf-8"))
    counts = {}
    for case in cases:
        counts[case["category"]] = counts.get(case["category"], 0) + 1
        assert case["id"] and case["input"] and case["expected"]
    assert counts.get("standard", 0) >= 5
    assert counts.get("boundary", 0) >= 3
    assert counts.get("error_input", 0) >= 3
    assert counts.get("age_level", 0) >= 2
    assert counts.get("security", 0) >= 1
    assert counts.get("complete_example", 0) >= 1

    package_text = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in ROOT.rglob("*") if p.is_file())
    for pattern in (r"sk-[A-Za-z0-9]{20,}", r"ghp_[A-Za-z0-9]{20,}", r"AKIA[0-9A-Z]{16}"):
        assert not re.search(pattern, package_text), f"possible secret pattern: {pattern}"
    assert "--fork-of" not in (ROOT / "agents/openai.yaml").read_text(encoding="utf-8"), "source fork metadata must not be present"
    print(json.dumps({"status": "pass", "cases": len(cases), "categories": counts}, ensure_ascii=False))


if __name__ == "__main__":
    main()
