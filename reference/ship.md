# Ship and run

<!-- Generated from catalog/ship.yaml. Edit the YAML, then run: python scripts/build.py -->

## Hosting

**Default**

- [Vercel](https://vercel.com) (search: Vercel hosting Hobby plan). License: free tier (Hobby), then paid; CLI is Apache-2.0. Install: `npm i -g vercel`. Hobby is $0 with hard caps (1M function invocations, 100 GB transfer, 1 seat a month) and no paid overage; see https://vercel.com/docs/limits/fair-use-guidelines and https://vercel.com/legal/terms. (16.7k stars, updated 2026-11) *(auto-checked)*

**Strong alternatives**

- [Netlify CLI](https://github.com/netlify/cli) (search: Netlify hosting netlify-cli): use when you host a static site or Jamstack app on Netlify and want to deploy from the terminal. License: MIT (CLI); Netlify hosting has a free tier, then paid. Install: `npm i -g netlify-cli`. Pricing page URL not checked yet. (1.9k stars, updated 2026-11) *(auto-checked)*
- [Cloudflare Pages](https://developers.cloudflare.com/pages/) (search: Cloudflare Pages static hosting): use when you want static or full-stack hosting on Cloudflare's network with a generous free tier. License: free tier, then paid; Wrangler CLI is MIT OR Apache-2.0. Install: `npm i -D wrangler`. Free tier limits not checked yet; Cloudflare's own pricing page needed for license_url. (4.8k stars, updated 2026-11) *(auto-checked)*
- [Cloudflare Workers](https://developers.cloudflare.com/workers/) (search: Cloudflare Workers serverless): use when you need small serverless functions or APIs that run at the edge. License: free tier, then paid; Wrangler CLI is MIT OR Apache-2.0. Install: `npm i -D wrangler`. Free tier limits not checked yet. (4.8k stars, updated 2026-11) *(auto-checked)*

## CI and automation

**Strong alternatives**

- [Renovate](https://docs.renovatebot.com/) (search: Renovate dependency update bot): use when you want automatic dependency update PRs with grouping and schedules, on GitHub, GitLab or others. License: AGPL-3.0-only. Install: `Mend Renovate GitHub app (free), or npx renovate`. Hosted app: https://docs.renovatebot.com/mend-hosted/overview/ (Community tier is free). (23.3k stars, updated 2026-11) *(auto-checked)*
- [gitlab-ci-local](https://github.com/firecow/gitlab-ci-local) (search: gitlab-ci-local run GitLab pipelines locally): use when you want to run .gitlab-ci.yml jobs on your machine before pushing. License: MIT. Install: `npm i -g gitlab-ci-local`. (4.2k stars, updated 2026-11) *(auto-checked)*
- [Changesets](https://changesets.dev) (search: Changesets versioning changelog monorepo): use when you publish npm packages (often a monorepo) and want versioning and changelogs from small change files. License: MIT. Install: `npm i -D @changesets/cli`. (12.6k stars, updated 2026-11) *(auto-checked)*
- [release-please](https://github.com/googleapis/release-please) (search: release-please conventional commits release PR): use when you use conventional commits and want a release PR that bumps versions and writes the changelog. License: Apache-2.0. Install: `googleapis/release-please-action in GitHub Actions, or npm i -g release-please`. (7.8k stars, updated 2026-11) *(auto-checked)*

**More options**

- [semantic-release](https://github.com/semantic-release/semantic-release) (search: semantic-release automated versioning): use when you want fully automatic version bumps and publishing on every merge, with no release PR. License: MIT. Install: `npm i -D semantic-release`. (24.2k stars, updated 2026-11) *(auto-checked)*
- [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci) (search: Lighthouse CI performance budgets): use when you want Lighthouse scores checked on every PR and fail the build when they drop. License: Apache-2.0. Install: `npm i -D @lhci/cli`. (7.2k stars, updated 2026-11) *(auto-checked)*

## Analytics

**Default**

- [Plausible](https://plausible.io) (search: Plausible privacy-friendly analytics). License: AGPL-3.0 (Community Edition); tracker MIT; cloud is paid. Install: `script tag, or npm i @plausible-analytics/tracker; self-host with https://github.com/plausible/community-edition/`. Cloud from $9/month with a 30-day free trial; self-hosted Community Edition is free (https://plausible.io/self-hosted-web-analytics). (30k stars, updated 2026-11) *(auto-checked)*

**Strong alternatives**

- [Vercel Web Analytics](https://vercel.com/docs/analytics) (search: Vercel Web Analytics): use when your site is already on Vercel and you want page views with no extra service. License: free tier, then paid. Install: `npm i @vercel/analytics`. Hobby plan includes 50K events a month. *(auto-checked)*

## Error tracking and monitoring

**Default**

- [Sentry](https://github.com/getsentry/sentry-javascript) (search: Sentry error tracking free tier). License: free tier, then paid; JS SDK is MIT. Install: `npm i @sentry/browser (or @sentry/nextjs, npx @sentry/wizard)`. Free tier limits and pricing page not checked yet. (8.8k stars, updated 2026-11) *(auto-checked)*

**Strong alternatives**

- [Uptime Kuma](https://github.com/louislam/uptime-kuma) (search: Uptime Kuma self-hosted uptime monitor): use when you want a self-hosted uptime monitor and status page. License: MIT. Install: `docker run -d --restart=always -p 3001:3001 -v uptime-kuma:/app/data --name uptime-kuma louislam/uptime-kuma:2`. Demo (data wiped after 10 minutes): https://demo.kuma.pet/start-demo (95k stars, updated 2026-11) *(auto-checked)*

**More options**

- [Vercel Observability](https://vercel.com/products/observability) (search: Vercel Observability logs traces): use when your app is on Vercel and you want function logs and traces without another service. License: free tier, then paid. Hobby keeps runtime logs for 1 day and traces for 3 days. *(auto-checked)*

## SEO and sharing

**Strong alternatives**

- [next-sitemap](https://github.com/iamvishnusankar/next-sitemap) (search: next-sitemap sitemap robots.txt Next.js): use when you want sitemap.xml and robots.txt generated at build time for a Next.js site. License: MIT. Install: `npm i -D next-sitemap`. Next.js App Router also has a built-in sitemap file convention. (3.8k stars, updated 2026-05) *(auto-checked)*
- [Satori](https://github.com/vercel/satori) (search: vercel satori HTML to SVG OG image): use when you want to render Open Graph images from JSX/HTML to SVG in any JS runtime. License: MPL-2.0. Install: `npm i satori`. (14.2k stars, 7951.4k npm downloads/week, updated 2026-11) *(auto-checked)*
- [next-seo](https://github.com/garmeeh/next-seo) (search: next-seo meta tags JSON-LD Next.js): use when you want meta tags and JSON-LD structured data components for Next.js. License: MIT. Install: `npm i next-seo`. (8.5k stars, updated 2026-07) *(auto-checked)*

**More options**

- [schema-dts](https://opensource.google/projects/schema-dts) (search: schema-dts TypeScript schema.org JSON-LD types): use when you write schema.org JSON-LD by hand in TypeScript and want it type-checked. License: Apache-2.0. Install: `npm i -D schema-dts`. (1.3k stars, updated 2026-11) *(auto-checked)*
