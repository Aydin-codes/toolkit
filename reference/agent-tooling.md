# Agent tooling

<!-- Generated from catalog/agent-tooling.yaml. Edit the YAML, then run: python scripts/build.py -->

## MCP servers and connectors

**Strong alternatives**

- [GitHub MCP Server](https://github.com/github/github-mcp-server) (search: github-mcp-server official GitHub MCP): use when the agent needs to read and act on GitHub issues, pull requests, code and Actions. License: MIT. Install: `remote https://api.githubcopilot.com/mcp/ or local Docker image with GITHUB_PERSONAL_ACCESS_TOKEN`. (34.8k stars, updated 2026-11) *(auto-checked)*
- [Playwright MCP](https://github.com/microsoft/playwright-mcp) (search: microsoft playwright-mcp browser automation MCP): use when the agent needs to open, click through and check a real browser page through the accessibility tree. License: Apache-2.0. Install: `claude mcp add playwright npx @playwright/mcp@latest`. (40.2k stars, 9696.3k npm downloads/week, updated 2026-11) *(auto-checked)*
- [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) (search: ChromeDevTools chrome-devtools-mcp): use when you want the agent to read console, network and performance traces from Chrome while debugging. License: Apache-2.0. Install: `npx chrome-devtools-mcp@latest`. (59.6k stars, 2886.4k npm downloads/week, updated 2026-11) *(auto-checked)*
- [shadcn MCP server](https://ui.shadcn.com/docs/mcp) (search: shadcn MCP server registry): use when you want the agent to browse, search and install components from shadcn and other registries set in components.json. License: MIT. Install: `npx shadcn@latest mcp init --client claude`. (129.3k stars, 17931.4k npm downloads/week, updated 2026-11) *(auto-checked)*
- [Supabase MCP Server](https://github.com/supabase/mcp) (search: Supabase MCP server mcp.supabase.com): use when the agent needs to manage tables, read config and query data in a Supabase project. License: Apache-2.0. Install: `remote https://mcp.supabase.com/mcp (OAuth login)`. older links point to supabase-community/supabase-mcp (3k stars, 225.5k npm downloads/week, updated 2026-11) *(auto-checked)*

**More options**

- [Sentry MCP](https://github.com/getsentry/sentry-mcp) (search: getsentry sentry-mcp): use when the agent should read production errors and issues from Sentry while fixing bugs. License: FSL-1.1-ALv2 (source-available, becomes Apache-2.0 later). Install: `remote https://mcp.sentry.dev/mcp, or npx @sentry/mcp-server@latest --access-token=<token>`. npm package metadata points to getsentry/toolkit; GitHub page is getsentry/sentry-mcp (976 stars, 231.3k npm downloads/week, updated 2026-11) *(auto-checked)*
- [Next.js DevTools MCP](https://github.com/vercel/next-devtools-mcp) (search: vercel next-devtools-mcp): use when you build with Next.js and want the agent to read the dev server's errors and Next.js docs. License: MIT. Install: `npx next-devtools-mcp@latest`. (835 stars, 175.5k npm downloads/week, updated 2026-09) *(auto-checked)*

**Big lists**

- [awesome-mcp-servers (punkpeye)](https://github.com/punkpeye/awesome-mcp-servers) (search: punkpeye awesome-mcp-servers). License: MIT. web directory at https://glama.ai/mcp/servers (98.6k stars, updated 2026-11) *(auto-checked)*

**Paid** (only when asked, or when no free option fits)

- [Figma MCP server](https://github.com/figma/mcp-server-guide) (search: Figma MCP server Dev Mode guide). License: Figma Developer Terms (not open source); free Starter use limited to 6 tool calls a month. Install: `claude mcp add --transport http figma https://mcp.figma.com/mcp`. Full use needs a Dev or Full seat on a paid plan. Free option: export design tokens and screenshots by hand. (2.2k stars, updated 2026-11) *(auto-checked)*

## Skills

**Strong alternatives**

- [Agent Skills specification](https://agentskills.io) (search: Agent Skills open standard SKILL.md specification): use when you write a SKILL.md and need the exact format rules, best practices and the list of clients that load skills. License: Apache-2.0 (code), CC-BY-4.0 (docs). Install: `read https://agentskills.io/specification.md`. (27.7k stars, updated 2026-11) *(auto-checked)*
- [skills-ref](https://github.com/agentskills/agentskills) (search: agentskills skills-ref validator): use when you want to check a skill folder against the spec before publishing it. License: Apache-2.0. Install: `from the skills-ref/ folder of agentskills/agentskills`. an npm package named skills-ref (MIT) exists but its metadata has no repository link; not confirmed to be the same tool (27.7k stars, updated 2026-11) *(auto-checked)*

## Docs for agents

**Default**

- [Context7](https://github.com/upstash/context7) (search: Context7 MCP up-to-date code docs). License: MIT (MCP server); the API backend and crawler are closed. Install: `npx ctx7 setup, or remote https://mcp.context7.com/mcp (API key recommended for higher limits)`. (65.6k stars, 964.2k npm downloads/week, updated 2026-11) *(auto-checked)*
