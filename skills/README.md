# 可调用课程 Skills

本目录收录由课程逐集资料提炼而成的 4 个 Codex Skill。它们用于按对应课程体系讲题、诊断错因、规划复习和定位回看分集；不是老师本人，也不代表老师或课程方的官方产品。

## Skill 清单

| Skill | 适用范围 | 入口 |
| --- | --- | --- |
| `laolv-laoluo-guanzong-math` | 老吕、老罗管综数学：44 个考点、88 个母题模型 | [SKILL.md](laolv-laoluo-guanzong-math/SKILL.md) |
| `xuerui-guanzong-logic` | 薛睿形式逻辑、分析推理与论证推理 | [SKILL.md](xuerui-guanzong-logic/SKILL.md) |
| `laolv-guanzong-writing` | 老吕管综论证有效性分析与论说文 | [SKILL.md](laolv-guanzong-writing/SKILL.md) |
| `chenzhengkang-english-two` | 陈正康英语二完型、阅读、新题型、翻译与写作 | [SKILL.md](chenzhengkang-english-two/SKILL.md) |

每个 Skill 均保留：

- `SKILL.md`：触发范围、解题流程、心智模型、输出规范与边界。
- `agents/openai.yaml`：Codex 中的显示名称与默认调用提示。
- `references/`：课程路径、逐集索引、章节细则、来源边界、验证和精炼记录。

## 历年真题解析（2026-10-25 增补）

四个 Skill 新增按卷种、年份、题号或阅读 Text 定位 B 站真题课的入口，以及题面核验、整卷统计、逐题错因和跨卷复做流程。

| Skill | 公开目录范围 | 真题入口 |
| --- | --- | --- |
| 数学 | 老罗/老吕课程2015—2026年度目录，27P；题内分钟尚未索引 | [索引](laolv-laoluo-guanzong-math/references/past-papers/index.md) |
| 逻辑 | 薛睿2007—2024年度主线及2007—2014十月联考，另有单题课，共79P；缺题逐条注明 | [索引](xuerui-guanzong-logic/references/past-papers/index.md) |
| 写作 | 基础课真题23P（含396）及旧年度候选6P；199论效2021—2025、论说文2021—2026 | [索引](laolv-guanzong-writing/references/past-papers/index.md) |
| 英语二 | 2012阅读、2019成套入口、2024/2025阅读，共13P | [索引](chenzhengkang-english-two/references/past-papers/index.md) |

合计148个公开分P记录，另有149条受限课程目录。它们不是297道独立真题，也不表示所有课程已完成内容提炼。新增内容证据仅包括薛睿2020年第28题样例，以及老吕三个既有写作片段的重新核验；其余新视频保持目录证据级别。

每科 `references/past-papers/` 内含分集索引、可查询目录、工作流、来源与内容证据卡。检索脚本仅依赖Python标准库，可在对应Skill目录执行：

```bash
python3 scripts/find_past_paper.py --year 2023 --question 51
```

英语可用 `--text 2`，写作可用 `--type 论说文`；受限目录默认不返回，需加 `--include-restricted`。没有题内定位证据时只返回年度候选，不能编造分钟或老师具体讲法。研究音视频、原始转写和本机路径不包含在本次增补中。

## 安装

将需要的完整 Skill 子文件夹复制到本机 `~/.codex/skills/`。例如，在本仓库根目录执行：

```bash
mkdir -p ~/.codex/skills
cp -R skills/xuerui-guanzong-logic ~/.codex/skills/
```

如需全部安装，可分别复制本目录下的四个 Skill 文件夹。重新打开 Codex 任务后，即可通过 `$skill-name` 显式调用，也可在题目与描述匹配时自动触发。

## 调用示例

```text
$laolv-laoluo-guanzong-math 用母题模型讲解这道条件充分性题，并诊断我的第一处错误。

$xuerui-guanzong-logic 把这道分析推理题画成表格，区分必然与可能，并指出该回看哪些分集。

$laolv-guanzong-writing 按论证有效性分析的评分任务批改这篇文章，先找最值得展开的四个漏洞。

$chenzhengkang-english-two 分析这道阅读题的定位句、同义改写和三个错误选项。
```

## 使用边界

- 课程方法、基于课程方法的新题推断以及最新官方口径必须分开说明。
- 原题、答案或当年考试规则需要可靠来源核验，不能凭课程记忆重构。
- `xuerui-guanzong-logic/references/learner-profile-2022-errors.md` 是当前学习者的个人错题档案；其他使用者应删除或替换该文件，不得把其中结论推广为普遍规律。
- 课程名称、教师姓名和原始内容的权利归相应权利人所有；本目录提供的是学习方法提炼与索引，不是课程逐字稿。

这些 Skill 按 [女娲 · Skill 造人术](https://github.com/alchaincyf/nuwa-skill) 的提炼方法构建，并分别通过结构验证、行为用例检查和女娲质量检查。
