# learn-claude-code

A comprehensive tutorial repository for learning **harness engineering** -- building the environment that surrounds an AI agent model.

## Overview

This project teaches you how to build effective agent harnesses by reverse-engineering Claude Code's architecture through 12 progressive sessions.

## What You'll Learn

- How agent loops work (model decides, harness executes)
- Tool implementation and dispatch patterns
- Planning, subagents, and context management
- Task systems with dependency graphs
- Multi-agent team coordination
- Worktree isolation for parallel execution

## Quick Start

```bash
git clone https://github.com/shareAI-lab/learn-claude-code
cd learn-claude-code
pip install -r requirements.txt
cp .env.example .env   # Add your ANTHROPIC_API_KEY
```

## Sessions

| Session | Topic |
|---------|-------|
| s01 | The Agent Loop |
| s02 | Tool Use |
| s03 | TodoWrite |
| s04 | Subagents |
| s05 | Skills |
| s06 | Context Compact |
| s07 | Tasks |
| s08 | Background Tasks |
| s09 | Agent Teams |
| s10 | Team Protocols |
| s11 | Autonomous Agents |
| s12 | Worktree + Task Isolation |

## The Core Pattern

The agent is the model. The harness is the code surrounding it.

```
User --> messages[] --> LLM --> response
                                 |
                    stop_reason == "tool_use"?
                   /                          \
                 yes                           no
                  |                             |
            execute tools                   return text
            append results
            loop back
```

## License

MIT
