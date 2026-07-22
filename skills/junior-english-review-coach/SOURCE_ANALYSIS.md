# Source Analysis

## 研究对象

- 项目：`open-spaced-repetition/fsrs4anki`
- URL：https://github.com/open-spaced-repetition/fsrs4anki
- 采集日期：2026-07-21（Asia/Shanghai）
- GitHub 事实：4,020 Stars、163 Forks、4,020 Watchers、8 个开放 Issue；仓库页 `updated_at` 为 2026-07-21，`pushed_at` 为 2026-03-20；许可证字段为 MIT。
- README 事实：项目由 scheduler 和 optimizer 两部分组成，目标是按照 Free Spaced Repetition Scheduler 算法安排 Anki 卡片复习，并根据复习历史优化参数。

## 原能力解决的问题

原项目解决的是记忆卡片的复习时机安排和参数优化问题。它把“什么时候复习”从固定日期推进到基于复习历史的调度，是一种适合长期记忆任务的方法基础。

## 需求证据

- 公开热度：GitHub 4,020 Stars，且当日仓库仍有更新信号。
- 公开问题：开放 Issue 包含“Interval increases too rapidly”“Define retention rate”等复习间隔与保持率相关请求，说明用户对调度行为有持续需求。
- SkillHub 侧信号：搜索 `study` 返回 `study-habits` 3,694 downloads、`study-plan` 1,544 downloads、`study-revision-planner` 797 downloads；搜索 `tutor` 返回 `tutor` 1,805 downloads、`japanese-tutor` 3,324 downloads；这些是相关市场信号，不是本 Skill 的用户反馈。

## 原场景不足与转换机会

原仓库偏向 Anki/算法调度，不直接解决初中生的中文引导、词义/词性混淆、拼写错误、互动式作答、年龄安全边界和教材输入。直接把算法名塞进 Skill 也会增加认知负担，因此本 Skill 只提炼“根据回忆结果调整间隔”的方法，并用可解释的近似规则完成文本互动。

## 许可证判断

本 Skill 不复制 FSRS4Anki 的源码、README 文案、参数配置或文件结构，不声明为其衍生代码。研究依据和方法来源在本文件中保留，发布命令不使用 `--fork-of`。若未来引入其代码或算法实现，应重新进行许可证和署名审核；当前 Skill 仅使用独立的教育流程设计。

## 事实与推断区分

- 已验证事实：GitHub 仓库统计、MIT 字段、README 所述 scheduler/optimizer、开放 Issue 标题、SkillHub CLI 搜索结果。
- 合理推断：该方法适合转成词汇复习调度；初中英语的具体用户痛点；付费价值来自长期个性化记录。
- 待验证：SkillHub 审核通过率、企业认证状态、SkillPay 入驻/微信商户号/Pay Skill 权限、线上下载和评分。
