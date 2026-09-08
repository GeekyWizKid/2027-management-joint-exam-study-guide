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
