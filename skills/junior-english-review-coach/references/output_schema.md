# Output Schema

本文件用于保持输出字段稳定，不要求用户使用 JSON。

## Required fields

| 字段 | 说明 |
| --- | --- |
| `goal` | 可检查的本次学习目标 |
| `baseline` | 由用户记录或轻量基线得到的水平信号，不能写成诊断 |
| `batch_size` | 本次词量，范围 1-15 |
| `question` | 当前主动回忆任务；互动模式只给一题 |
| `feedback` | 作答后的结果、证据、最小纠正和下一动作 |
| `schedule` | interval 或 next_review_date，以及调整依据 |
| `stage_check` | 阶段测试、通过条件和未通过动作 |

## Error enum

`correct`, `hesitant`, `spelling_error`, `meaning_error`, `part_of_speech_error`, `confusion`, `no_attempt`

## Evidence rule

只有用户提供了作答或明确复习记录，才能写 `feedback` 和掌握变化；没有证据时使用“待测/未记录”，不要编造学生表现。
