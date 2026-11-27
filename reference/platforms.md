# Platforms

<!-- Generated from catalog/platforms.yaml. Edit the YAML, then run: python scripts/build.py -->

## Mobile apps

**Default**

- [Expo](https://github.com/expo/expo) (search: Expo React Native framework). License: MIT. Install: `npx create-expo-app@latest`. (53.8k stars, updated 2026-11) *(auto-checked)*

**Strong alternatives**

- [React Native](https://reactnative.dev/) (search: React Native framework): use when you need the bare React Native runtime without the Expo toolchain. License: MIT. Install: `npm i react-native (usually through Expo)`. (127k stars, updated 2026-11) *(auto-checked)*
- [Flutter](https://flutter.dev/) (search: Flutter SDK Dart cross-platform): use when you are fine writing Dart and want one UI toolkit for mobile, web and desktop. License: BSD-3-Clause. Get it: download the Flutter SDK. (181.5k stars, updated 2026-11) *(auto-checked)*
- [Capacitor](https://capacitorjs.com) (search: Capacitor native runtime web apps): use when you already have a web app and want to ship it as a native app with access to device APIs. License: MIT. Install: `npm i @capacitor/core @capacitor/cli`. (17.2k stars, updated 2026-11) *(auto-checked)*
- [Ionic Framework](https://ionicframework.com/) (search: Ionic Framework mobile UI components): use when you want mobile-styled UI components on top of Capacitor. License: MIT. Install: `npm i @ionic/core (or @ionic/react, @ionic/vue, @ionic/angular)`. (52.8k stars, updated 2026-11) *(auto-checked)*

**More options**

- [vite-plugin-pwa](https://github.com/vite-pwa/vite-plugin-pwa) (search: vite-plugin-pwa service worker manifest): use when you build with Vite and want the manifest and service worker generated for a PWA. License: MIT. Install: `npm i -D vite-plugin-pwa`. (4.3k stars, updated 2026-10) *(auto-checked)*

**Paid** (only when asked, or when no free option fits)

- [RevenueCat](https://www.revenuecat.com/pricing/) (search: RevenueCat in-app purchases subscriptions). License: SDK MIT; service free up to $2,500 monthly tracked revenue, then 1%. Install: `npm i react-native-purchases`. Free option: use StoreKit and Google Play Billing directly. (1.2k stars, updated 2026-11) *(auto-checked)*

## Desktop apps

**Default**

- [Tauri](https://github.com/tauri-apps/tauri) (search: Tauri desktop apps Rust web frontend). License: Apache-2.0 OR MIT. Install: `npm create tauri-app@latest`. (113.3k stars, updated 2026-11) *(auto-checked)*

**Strong alternatives**

- [Electron](https://github.com/electron/electron) (search: Electron desktop apps JavaScript): use when you want a Node.js backend and the same Chromium engine on every OS, and app size matters less. License: MIT. Install: `npm i -D electron`. (124.2k stars, updated 2026-11) *(auto-checked)*
- [Wails](https://wails.io) (search: Wails Go desktop apps): use when your backend is in Go and you want a web frontend in a native window. License: MIT. Install: `go install github.com/wailsapp/wails/v2/cmd/wails@latest`. (37.2k stars, updated 2026-11) *(auto-checked)*
- [Neutralinojs](https://neutralino.js.org/docs/cli/neu-cli) (search: Neutralinojs lightweight desktop apps): use when you want a very light desktop wrapper for a plain web app with no Rust or Go. License: MIT. Install: `npm i -g @neutralinojs/neu`. repo listed is the CLI; the framework repo was not checked (118 stars, updated 2026-11) *(auto-checked)*
- [electron-builder](https://www.electron.build/) (search: electron-builder package Electron app): use when you need installers, code signing and auto-update for an Electron app. License: MIT. Install: `npm i -D electron-builder`. (14.7k stars, updated 2026-11) *(auto-checked)*

**More options**

- [Electron Forge](https://github.com/electron/forge) (search: Electron Forge build package publish): use when you want the Electron team's own tool to scaffold, package and publish. License: MIT. Install: `npx create-electron-app@latest`. (7.2k stars, updated 2026-11) *(auto-checked)*

**Big lists**

- [awesome-tauri](https://github.com/tauri-apps/awesome-tauri) (search: awesome-tauri list). License: MIT. (8.2k stars, updated 2026-11) *(auto-checked)*

## Browser extensions

**Default**

- [WXT](https://wxt.dev) (search: WXT web extension framework). License: MIT. Install: `npx wxt@latest init`. (10.8k stars, updated 2026-11) *(auto-checked)*

**Strong alternatives**

- [Plasmo](https://docs.plasmo.com/) (search: Plasmo browser extension framework): use when you want a React-first extension framework with file-based entry points. License: MIT. Install: `npm create plasmo`. (13.3k stars, updated 2026-11) *(auto-checked)*

## Games

**Strong alternatives**

- [Godot](https://godotengine.org) (search: Godot game engine): use when you want a full 2D/3D engine with an editor, and can export to web, desktop and mobile. License: MIT. Get it: download the editor. (121k stars, updated 2026-11) *(auto-checked)*
- [PixiJS](https://pixijs.com/) (search: PixiJS 2D WebGL renderer): use when you only need a fast 2D renderer and will write your own game logic. License: MIT. Install: `npm i pixi.js`. (48.9k stars, updated 2026-11) *(auto-checked)*
- [KAPLAY](https://kaplayjs.com/) (search: KAPLAY game library (Kaboom successor)): use when you want a small, beginner-friendly API for quick 2D games and jams. License: MIT. Install: `npm i kaplay`. community fork that continues Kaboom.js (1.9k stars, updated 2026-11) *(auto-checked)*
- [Excalibur.js](https://github.com/excaliburjs/Excalibur) (search: Excalibur.js TypeScript game engine): use when you want a 2D engine written in TypeScript with types throughout. License: BSD-2-Clause. Install: `npm i excalibur`. (2.4k stars, updated 2026-11) *(auto-checked)*

**More options**

- [Colyseus](https://colyseus.io/) (search: Colyseus multiplayer game server Node.js): use when you need an authoritative multiplayer server with room and state sync. License: MIT. Install: `npm create colyseus-app@latest`. (7.6k stars, updated 2026-11) *(auto-checked)*

## MCP servers

**Default**

- [MCP TypeScript SDK](https://modelcontextprotocol.io) (search: Model Context Protocol TypeScript SDK). License: MIT. Install: `npm i @modelcontextprotocol/sdk`. (13.8k stars, updated 2026-11) *(auto-checked)*

**Strong alternatives**

- [MCP Python SDK](https://py.sdk.modelcontextprotocol.io/) (search: Model Context Protocol Python SDK): use when your server is in Python and you want the official SDK. License: MIT. Install: `pip install mcp`. (25k stars, updated 2026-11) *(auto-checked)*
- [FastMCP](https://gofastmcp.com) (search: FastMCP Python MCP framework): use when you want a higher-level Python framework with less boilerplate than the official SDK. License: Apache-2.0. Install: `uv add fastmcp`. (28.8k stars, updated 2026-11) *(auto-checked)*
- [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector) (search: MCP Inspector debug MCP servers): use when you need to test and debug an MCP server in a browser, CLI or terminal UI. License: see LICENSE in repo (npm says "SEE LICENSE IN LICENSE"). Install: `npx @modelcontextprotocol/inspector`. (11.4k stars, updated 2026-11) *(auto-checked)*
- [MCP reference servers](https://github.com/modelcontextprotocol/servers) (search: modelcontextprotocol servers reference implementations): use when you want working example servers to copy patterns from or run as-is. License: see LICENSE in repo (npm says "SEE LICENSE IN LICENSE"). Install: `npx -y @modelcontextprotocol/server-filesystem <dir>`. (92.3k stars, updated 2026-11) *(auto-checked)*
