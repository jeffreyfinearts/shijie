#!/usr/bin/env python3
"""Deterministic package checks for the history discussion Skill."""
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
    "LICENSE",
    "references/output-schema.md",
    "references/historical-evidence-rules.md",
    "examples/basic-session.md",
    "tests/cases.json",
    "agents/openai.yaml",
}


def main() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    assert not missing, f"missing required files: {missing}"

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    assert skill.startswith("---\n"), "SKILL.md needs YAML frontmatter"
    assert re.search(r"^name:\s+design-junior-history-role-discussions\s*$", skill, re.M)
    assert re.search(r"^description:\s+.+$", skill, re.M)
    for heading in ("输入要求", "执行流程", "输出格式", "质量检查", "异常处理与安全", "依赖与环境变量"):
        assert heading in skill, f"missing section: {heading}"
    for marker in ("事实", "解释", "争议", "待核对", "退出角色", "退出票"):
        assert marker in skill, f"missing instructional marker: {marker}"
    assert "TODO" not in skill, "template TODO remains"
    assert "OPENAI_API_KEY" in skill and "禁止索取或输出" in skill

    cases = json.loads((ROOT / "tests/cases.json").read_text(encoding="utf-8"))
    counts: dict[str, int] = {}
    for case in cases:
        counts[case["category"]] = counts.get(case["category"], 0) + 1
        assert case["id"] and case["input"] and case["expected"]
    assert counts.get("standard", 0) >= 5
    assert counts.get("boundary", 0) >= 3
    assert counts.get("error_input", 0) >= 3
    assert counts.get("age_level", 0) >= 2
    assert counts.get("security", 0) >= 1
    assert counts.get("complete_example", 0) >= 1

    package_text = "\n".join(
        path.read_text(encoding="utf-8", errors="ignore")
        for path in ROOT.rglob("*")
        if path.is_file()
    )
    for pattern in (r"sk-[A-Za-z0-9]{20,}", r"ghp_[A-Za-z0-9]{20,}", r"AKIA[0-9A-Z]{16}"):
        assert not re.search(pattern, package_text), f"possible secret pattern: {pattern}"
    assert "--fork-of" not in (ROOT / "agents/openai.yaml").read_text(encoding="utf-8")
    print(json.dumps({"status": "pass", "cases": len(cases), "categories": counts}, ensure_ascii=False))


if __name__ == "__main__":
    main()
