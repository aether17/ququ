Browse the uncommitted code in the current workspace, generate a concise git commit message, and execute the git commit. Follow these rules:
1. Commit messages should be concise and clear, summarizing the main changes.
2. Use the imperative mood, for example, "Fix bug" instead of "Fixed bug".
3. Avoid using the first person, such as "I" or "we".
4. If a change involves multiple aspects, prioritize highlighting the most significant one.
5. Keep the commit message under 50 characters, adding a more detailed description in the body if necessary.
6. Commit messages should only be a summary of the changes; it is strictly forbidden to include content such as "Generated with [Claude Code]", "Co-Authored-By: Claude Opus 4.5", etc.
7. Ensure commit messages are clean and concise; do not use emojis, ensure correct grammar, and avoid spelling errors.
8. Use conventional commit prefixes based on the type of change:
   - `feat:` for new features or functionality
   - `fix:` for bug fixes
   - `docs:` for documentation-only changes
   - `perf:` for performance improvements
   - `refactor:` for code refactoring without adding features or fixing bugs
   - `chore:` for maintenance tasks, dependency updates, or build changes
