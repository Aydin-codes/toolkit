# Frameworks and front-end libraries

<!-- Generated from catalog/frontend/frameworks.yaml. Edit the YAML, then run: python scripts/build.py -->

## Web frameworks

**Default**

- [Next.js](https://nextjs.org) (search: Next.js React framework). License: MIT. Install: `npx create-next-app@latest`. (143.8k stars, updated 2026-11) *(auto-checked)*

**Strong alternatives**

- [React Router (framework mode, formerly Remix)](https://reactrouter.com) (search: React Router framework mode Remix): use when you want a React full-stack app built on web standards (loaders, actions, forms) without Next.js. License: MIT. Install: `npx create-react-router@latest`. Remix v2 merged into React Router v7; React Router v8 is out. (56.7k stars, updated 2026-11) *(auto-checked)*
- [SvelteKit](https://svelte.dev) (search: SvelteKit Svelte app framework): use when you prefer Svelte over React and want routing, SSR and adapters in one package. License: MIT. Install: `npx sv create`. (20.9k stars, updated 2026-11) *(auto-checked)*
- [Nuxt](https://nuxt.com) (search: Nuxt Vue framework): use when the project uses Vue and needs SSR, file routing and modules. License: MIT. Install: `npm create nuxt@latest`. (61.1k stars, updated 2026-11) *(auto-checked)*
- [TanStack Start](https://tanstack.com/start) (search: TanStack Start full-stack React framework): use when you want type-safe routing from TanStack Router plus server functions, on Vite. License: MIT. Install: `npm create @tanstack/start@latest`. (15.4k stars, updated 2026-11) *(auto-checked)*

**More options**

- [Qwik](https://qwik.dev/) (search: Qwik resumable framework): use when you need very little JavaScript sent on first load (resumability instead of hydration). License: MIT. Install: `npm create qwik@latest`. (22.1k stars, updated 2026-11) *(auto-checked)*
- [Angular](https://angular.dev) (search: Angular framework angular.dev): use when the team wants a full, opinionated framework with DI, forms and router built in. License: MIT. Install: `npx @angular/cli new my-app`. (101.6k stars, updated 2026-11) *(auto-checked)*

**Big lists**

- [awesome-nextjs](https://github.com/unicodeveloper/awesome-nextjs) (search: awesome-nextjs list). License: list. (11.1k stars, updated 2026-11) *(auto-checked)*

## Static and content sites

**Default**

- [Astro](https://astro.build) (search: Astro web framework content sites). License: MIT. Install: `npm create astro@latest`. (64.3k stars, updated 2026-11) *(auto-checked)*

**Strong alternatives**

- [Starlight](https://starlight.astro.build) (search: Starlight Astro documentation theme): use when you are building a documentation site and want Astro underneath. License: MIT. Install: `npm create astro@latest -- --template starlight`. (9.7k stars, updated 2026-11) *(auto-checked)*
- [VitePress](https://vitepress.dev/) (search: VitePress static site generator): use when you want a fast Markdown docs site with Vue components. License: MIT. Install: `npm add -D vitepress`. (18.5k stars, updated 2026-11) *(auto-checked)*
- [Docusaurus](https://docusaurus.io/) (search: Docusaurus documentation site generator): use when you want a React docs site with versioning, i18n and a blog built in. License: MIT. Install: `npx create-docusaurus@latest my-website classic`. (66.8k stars, updated 2026-11) *(auto-checked)*
- [Eleventy (Build Awesome)](https://www.11ty.dev/) (search: Eleventy 11ty Build Awesome static site generator): use when you want a plain, template-based static site with no client framework. License: MIT. Install: `npm i -D @11ty/eleventy`. Eleventy is being renamed Build Awesome (v4); npm still lists @11ty/eleventy, repo field points to 11ty/buildawesome (11ty/eleventy redirects). (20.1k stars, updated 2026-11) *(auto-checked)*
- [Hugo](https://gohugo.io/) (search: Hugo static site generator Go): use when you want a single binary that builds large Markdown sites very fast, no Node needed. License: Apache-2.0. Install: `prebuilt binary or package manager (brew install hugo); not on npm`. (90.6k stars, updated 2026-11) *(auto-checked)*

## Build tools

**Default**

- [Vite](https://vite.dev) (search: Vite frontend build tool). License: MIT. Install: `npm create vite@latest`. (84.2k stars, updated 2026-11) *(auto-checked)*

**Strong alternatives**

- [Rspack](https://rspack.rs) (search: Rspack Rust webpack-compatible bundler): use when you are moving off webpack and want its config and loaders with a faster Rust core. License: MIT. Install: `npm create rsbuild@latest`. (13k stars, updated 2026-11) *(auto-checked)*
- [esbuild](https://esbuild.github.io/) (search: esbuild JavaScript bundler): use when you need a small, very fast bundler or transpiler for libraries, scripts or CLIs. License: MIT. Install: `npm i -D esbuild`. (40.2k stars, updated 2026-08) *(auto-checked)*
- [Bun](https://bun.com) (search: Bun JavaScript runtime bundler): use when you want one tool for runtime, package manager, bundler and test runner. License: MIT. Install: `curl -fsSL https://bun.sh/install | bash (or npm i -g bun)`. the npm package installs the Bun binary; the main install is the shell script. (97k stars, updated 2026-11) *(auto-checked)*
- [Turbopack](https://nextjs.org/docs/app/api-reference/turbopack) (search: Turbopack Next.js bundler): use when you are on Next.js; it is the Next.js bundler and is not used on its own. License: MIT. Install: `built into next (next dev / next build); no separate package`. repo is shared with Next.js, so its stars and activity are Next.js's. (143.8k stars, updated 2026-11) *(auto-checked)*

## Styling

**Default**

- [Tailwind CSS](https://tailwindcss.com) (search: Tailwind CSS utility-first framework). License: MIT. Install: `npm i tailwindcss @tailwindcss/vite`. (98.9k stars, updated 2026-11) *(auto-checked)*

**Strong alternatives**

- [vanilla-extract](https://vanilla-extract.style/) (search: vanilla-extract zero-runtime CSS in TypeScript): use when you want type-safe styles written in TypeScript that compile to static CSS. License: MIT. Install: `npm i @vanilla-extract/css`. (10.5k stars, updated 2026-11) *(auto-checked)*
- [Panda CSS](https://panda-css.com) (search: Panda CSS build-time CSS-in-JS): use when you want CSS-in-JS syntax and design tokens with no runtime cost. License: MIT. Install: `npm i -D @pandacss/dev`. (6.3k stars, updated 2026-11) *(auto-checked)*
- [UnoCSS](https://unocss.dev) (search: UnoCSS atomic CSS engine): use when you want a Tailwind-like utility setup that is fully configurable through presets. License: MIT. Install: `npm i -D unocss`. (19k stars, updated 2026-11) *(auto-checked)*
- [Open Props](https://open-props.style/) (search: Open Props CSS custom properties): use when you want ready design tokens as CSS variables on top of plain CSS. License: MIT. Install: `npm i open-props`. (5.6k stars, updated 2026-10) *(auto-checked)*

## State and data fetching

**Default**

- [TanStack Query](https://tanstack.com/query) (search: TanStack Query React Query server state). License: MIT. Install: `npm i @tanstack/react-query`. (50.7k stars, updated 2026-11) *(auto-checked)*

**Strong alternatives**

- [Zustand](https://zustand.docs.pmnd.rs/) (search: Zustand React state management): use when you need a small global client-state store with hooks and little boilerplate. License: MIT. Install: `npm i zustand`. (59k stars, updated 2026-11) *(auto-checked)*
- [Jotai](https://jotai.org/) (search: Jotai atomic state React): use when you want state split into small atoms that components subscribe to one by one. License: MIT. Install: `npm i jotai`. (21.4k stars, updated 2026-11) *(auto-checked)*
- [SWR](https://swr.vercel.app) (search: SWR React hooks data fetching): use when you want a lighter fetch-and-cache hook than TanStack Query. License: MIT. Install: `npm i swr`. (32.5k stars, updated 2026-10) *(auto-checked)*
- [Redux Toolkit](https://redux-toolkit.js.org) (search: Redux Toolkit RTK Query): use when the app is large, already uses Redux, or needs strict, traceable state changes. License: MIT. Install: `npm i @reduxjs/toolkit react-redux`. (11.2k stars, updated 2026-11) *(auto-checked)*
- [tRPC](https://trpc.io) (search: tRPC end-to-end typesafe APIs): use when client and server are both TypeScript and you want typed API calls without a schema file. License: MIT. Install: `npm i @trpc/server @trpc/client`. (40.9k stars, updated 2026-11) *(auto-checked)*

**Big lists**

- [awesome-react](https://github.com/enaqx/awesome-react) (search: enaqx awesome-react). License: list. (75.4k stars, updated 2026-09) *(auto-checked)*

## Forms and validation

**Default**

- [React Hook Form](https://react-hook-form.com) (search: React Hook Form). License: MIT. Install: `npm i react-hook-form`. (44.9k stars, updated 2026-11) *(auto-checked)*

**Strong alternatives**

- [Zod](https://zod.dev) (search: Zod TypeScript schema validation): use when you need a schema for validation and TypeScript types from one source (pairs with any form library). License: MIT. Install: `npm i zod`. (44.5k stars, updated 2026-11) *(auto-checked)*
- [Valibot](https://valibot.dev) (search: Valibot modular schema library): use when you want Zod-style schemas with a smaller bundle through tree-shaking. License: MIT. Install: `npm i valibot`. (9.1k stars, updated 2026-11) *(auto-checked)*
- [TanStack Form](https://tanstack.com/form) (search: TanStack Form type-safe forms): use when you want fully typed form state that also works in Vue, Solid, Svelte and Angular. License: MIT. Install: `npm i @tanstack/react-form`. (6.8k stars, updated 2026-11) *(auto-checked)*
- [Conform](https://conform.guide) (search: Conform progressive enhancement forms): use when you use server actions (React Router, Next.js) and want forms that work before JavaScript loads. License: MIT. Install: `npm i @conform-to/react @conform-to/zod`. (2.6k stars, updated 2026-11) *(auto-checked)*
