"""Shared debug utilities for agent scripts."""


def print_messages(messages: list, title: str = "messages") -> None:
    """Pretty-print the full message history.

    Each message is separated by a blank line. For assistant messages whose
    content is a list of blocks, each block is printed on its own line with
    an emoji prefix indicating its type.
    """
    WIDTH = 72
    ROLE_COLOR = {"user": "\033[36m", "assistant": "\033[33m"}
    RESET = "\033[0m"
    GRAY = "\033[90m"

    print(f"{GRAY}{'─' * WIDTH}{RESET}")
    print(f"{GRAY}{title} ({len(messages)} msgs){RESET}")
    print(f"{GRAY}{'─' * WIDTH}{RESET}")

    for i, msg in enumerate(messages):
        role = msg["role"]
        color = ROLE_COLOR.get(role, "")
        content = msg["content"]

        print(f"{color}[{i}] {role.upper()}{RESET}")

        if isinstance(content, str):
            # Plain text message (user input or simple assistant reply)
            for line in content[:400].splitlines():
                print(f"    {line}")

        elif isinstance(content, list):
            for block in content:
                btype = getattr(block, "type", None) or block.get("type", "?")

                if btype == "thinking":
                    text = getattr(block, "thinking", "").replace("\n", " ")
                    print(f"    {GRAY}💭 thinking: {text}{RESET}")

                elif btype == "text":
                    text = getattr(block, "text", "")
                    print(f"    \033[97m💬 text:{RESET}")
                    for line in text[:400].splitlines():
                        print(f"       {line}")

                elif btype == "tool_use":
                    name = getattr(block, "name", "?")
                    inp = getattr(block, "input", {})
                    print(f"    \033[32m🔧 tool_use: {name}, parameters:{inp}{RESET}")

                elif btype == "tool_result":
                    tid = block.get("tool_use_id", "?")[-6:]
                    out = str(block.get("content", ""))
                    print(f"    \033[35m📤 tool_result[…{tid}]: {out}{RESET}")

                else:
                    print(f"    {GRAY}? {btype}: {str(block)[:150]}{RESET}")

        print()  # blank line between messages

    print(f"{GRAY}{'─' * WIDTH}{RESET}")
