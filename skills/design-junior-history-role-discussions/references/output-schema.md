# 输出 Schema

## 必填块

```yaml
lesson_overview:
  grade: "七/八/九年级"
  topic: "教材主题"
  duration_minutes: 40
  central_question: "可争论、可证据化、可收束的问题"
  learning_objectives: []
fact_boundary:
  verified_facts: []
  interpretations: []
  controversies: []
  needs_verification: []
roles:
  - name: "角色或分析视角"
    historical_context: "只写可核对处境"
    concerns: []
    evidence_ids: []
    required_question: "必须回答的问题"
    forbidden_claims: []
evidence_cards:
  - id: "E1"
    content: "材料摘要或短引"
    source: "教材/史料出处；缺失时写待补"
    supports: []
    cannot_prove: []
discussion_rounds:
  - minutes: 5
    teacher_action: "教师动作"
    student_artifact: "学生可观察产物"
    stop_condition: "进入下一环节的条件"
    compression: "超时时的最小方案"
misconceptions:
  - observable_signal: "可观察表现"
    minimal_correction: "最小纠正"
    recheck_question: "再验证问题"
rubric:
  dimensions: ["史实准确", "证据使用", "解释质量", "倾听与回应"]
  scoring: "每维 0-2 分，并写可观察描述"
exit_ticket:
  prompt: "个人结论 + 最有力证据 + 一个保留或反证"
  progression_condition: "下一阶段条件"
```

## 输出约束

- 全部时间之和不得超过课时。
- 角色数量为 3-5 个；证据卡默认 4-8 张。
- 缺少原始材料时，`evidence_cards.content` 只能写模板或检索方向。
- 评价学生的证据使用和解释过程，不评价其是否选择教师偏好的立场。
- 所有 `needs_verification` 项必须显式保留，不能在后续段落中改写成确定事实。
