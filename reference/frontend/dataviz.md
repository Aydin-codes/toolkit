# Charts, maps and diagrams

<!-- Generated from catalog/frontend/dataviz.yaml. Edit the YAML, then run: python scripts/build.py -->

## Charts

**Default**

- [Recharts](https://github.com/recharts/recharts) (search: Recharts React chart library). License: MIT. Install: `npm i recharts`. (27.8k stars, updated 2026-11) *(auto-checked)*

**Strong alternatives**

- [Chart.js](https://www.chartjs.org) (search: Chart.js canvas charts): use when you want simple canvas charts without a framework, or in plain HTML. License: MIT. Install: `npm i chart.js (React wrapper - npm i react-chartjs-2)`. (67.8k stars, updated 2026-11) *(auto-checked)*
- [Apache ECharts](https://echarts.apache.org) (search: Apache ECharts): use when you need many chart types, large datasets, or dashboards with zoom and brushing. License: Apache-2.0. Install: `npm i echarts (React wrapper - npm i echarts-for-react)`. (67.8k stars, updated 2026-11) *(auto-checked)*
- [Observable Plot](https://github.com/observablehq/plot) (search: Observable Plot JavaScript library exploratory charts): use when you want quick, concise exploratory charts from tabular data with little code. License: ISC. Install: `npm i @observablehq/plot`. (5.4k stars, updated 2026-11) *(auto-checked)*
- [D3](https://d3js.org) (search: D3.js data-driven documents): use when you need a custom or unusual visualization and full control over SVG. License: ISC. Install: `npm i d3`. (114k stars, 34118.3k npm downloads/week, updated 2026-11) *(auto-checked)*
- [visx](https://github.com/airbnb/visx) (search: visx airbnb React visualization primitives): use when you want D3-style custom charts built from React components. License: MIT. Install: `npm i @visx/visx (or single packages like @visx/shape)`. (21.1k stars, updated 2026-06) *(auto-checked)*

**More options**

- [Nivo](https://github.com/plouc/nivo) (search: nivo React dataviz components): use when you want ready-made React charts with themes, including heatmaps, sankey and treemaps. License: MIT. Install: `npm i @nivo/core @nivo/<chart>, e.g. @nivo/bar`. (14.1k stars, updated 2026-07) *(auto-checked)*
- [uPlot](https://github.com/leeoniya/uPlot) (search: uPlot fast time series chart): use when you plot large time series and need a very small, fast library. License: MIT. Install: `npm i uplot`. (10.7k stars, updated 2026-11) *(auto-checked)*
- [Vega-Lite](https://vega.github.io/vega-lite/) (search: Vega-Lite grammar of interactive graphics JSON spec): use when you want charts described as JSON specs that can be stored, generated or shared. License: BSD-3-Clause. Install: `npm i vega vega-lite vega-embed`. (5.6k stars, updated 2026-11) *(auto-checked)*
- [Plotly.js](https://github.com/plotly/plotly.js) (search: plotly.js scientific charts 3D): use when you need scientific or 3D charts, or match charts made with Plotly in Python. License: MIT. Install: `npm i plotly.js-dist-min`. (18.4k stars, updated 2026-11) *(auto-checked)*

## Maps

**Default**

- [MapLibre GL JS](https://maplibre.org/) (search: MapLibre GL JS vector maps). License: BSD-3-Clause. Install: `npm i maplibre-gl (React - npm i react-map-gl)`. (12.2k stars, updated 2026-11) *(auto-checked)*

**Strong alternatives**

- [Leaflet](https://leafletjs.com/) (search: Leaflet JavaScript map library): use when you want a small, simple map with raster tiles and markers. License: BSD-2-Clause. Install: `npm i leaflet`. (46k stars, updated 2026-11) *(auto-checked)*
- [deck.gl](https://deck.gl) (search: deck.gl WebGL large data map layers): use when you draw very large geo datasets (points, arcs, hexbins) on top of a map. License: MIT. Install: `npm i deck.gl`. (14.8k stars, updated 2026-11) *(auto-checked)*
- [OpenFreeMap](https://openfreemap.org) (search: OpenFreeMap free vector tiles): use when you need free hosted map tiles with no API key. License: free hosted tiles; map data from OpenStreetMap (ODbL), attribution required. Install: `point MapLibre at an OpenFreeMap style URL (see openfreemap.org/quick_start)`. (6.5k stars, updated 2026-11) *(auto-checked)*
- [Protomaps](https://protomaps.com/) (search: Protomaps PMTiles basemaps self-host): use when you want to self-host a basemap as one PMTiles file on static storage. License: BSD-3-Clause (code); map data from OpenStreetMap (ODbL). Install: `npm i pmtiles @protomaps/basemaps`. (781 stars, updated 2026-09) *(auto-checked)*
- [OpenLayers](https://openlayers.org/) (search: OpenLayers web mapping library): use when you need GIS features such as projections, WMS/WFS and many data formats. License: BSD-2-Clause. Install: `npm i ol`. (12.7k stars, updated 2026-11) *(auto-checked)*

**More options**

- [react-map-gl](https://github.com/visgl/react-map-gl) (search: react-map-gl MapLibre React wrapper): use when you use MapLibre in React and want it as components. License: MIT. Install: `npm i react-map-gl maplibre-gl`. (8.5k stars, updated 2026-10) *(auto-checked)*
- [OpenStreetMap](https://www.openstreetmap.org/copyright) (search: OpenStreetMap data ODbL attribution): use when you need the underlying free map data, or must check attribution rules. License: ODbL (data); attribution required. Install: `use through a tile provider or extracts; don't use the openstreetmap.org tile servers for heavy traffic`. *(auto-checked)*
- [React Leaflet](https://react-leaflet.js.org) (search: React Leaflet components): use when you use Leaflet in React. License: Hippocratic-2.1. Install: `npm i react-leaflet leaflet`. Hippocratic License is not an OSI open-source license; read it before commercial use. (5.6k stars, updated 2026-11) *(auto-checked)*

## Diagrams

**Default**

- [Mermaid](https://github.com/mermaid-js/mermaid) (search: Mermaid diagrams from text). License: MIT. Install: `npm i mermaid (CLI - npm i @mermaid-js/mermaid-cli)`. (91.3k stars, updated 2026-11) *(auto-checked)*

**Strong alternatives**

- [React Flow (xyflow)](https://reactflow.dev) (search: React Flow xyflow node editor): use when you need interactive node graphs or editors that users drag and connect. License: MIT. Install: `npm i @xyflow/react`. (39.2k stars, updated 2026-11) *(auto-checked)*
- [D2](https://d2lang.com/) (search: D2 declarative diagramming language): use when you want text diagrams with better automatic layout and styling than Mermaid. License: MPL-2.0. Install: `CLI install from d2lang.com, or npm i @terrastruct/d2 (WASM)`. (26k stars, updated 2026-11) *(auto-checked)*
- [Viz.js (Graphviz in the browser)](https://github.com/mdaines/viz-js) (search: Graphviz DOT viz-js WebAssembly): use when you have Graphviz DOT graphs and want to render them in JavaScript. License: MIT. Install: `npm i @viz-js/viz`. Graphviz itself is the desktop/CLI tool; install it with the OS package manager. (4.4k stars, updated 2026-11) *(auto-checked)*

**More options**

- [Cytoscape.js](https://js.cytoscape.org) (search: Cytoscape.js graph network visualization): use when you visualize and analyze network graphs with many nodes. License: MIT. Install: `npm i cytoscape`. (11.3k stars, updated 2026-11) *(auto-checked)*
- [dagre](https://github.com/dagrejs/dagre) (search: dagre directed graph layout): use when you need automatic layered layout for nodes, e.g. with React Flow. License: MIT. Install: `npm i @dagrejs/dagre`. (5.9k stars, updated 2026-11) *(auto-checked)*
- [ELK.js](https://github.com/kieler/elkjs) (search: elkjs Eclipse Layout Kernel JavaScript): use when you need more layout options than dagre, such as ports and nested groups. License: EPL-2.0 OR GPL-3.0-or-later. Install: `npm i elkjs`. (2.9k stars, updated 2026-11) *(auto-checked)*

## Tables and grids

**Default**

- [TanStack Table](https://tanstack.com/table) (search: TanStack Table headless table). License: MIT. Install: `npm i @tanstack/react-table`. (28.6k stars, updated 2026-11) *(auto-checked)*

**Strong alternatives**

- [AG Grid Community](https://www.ag-grid.com/) (search: AG Grid Community free data grid): use when you need a full spreadsheet-like grid with editing and large row counts out of the box. License: MIT (Community); Enterprise features are paid. Install: `npm i ag-grid-community ag-grid-react`. (15.7k stars, updated 2026-11) *(auto-checked)*
- [Glide Data Grid](https://grid.glideapps.com) (search: Glide Data Grid canvas React): use when you show millions of rows in React and need canvas rendering for speed. License: MIT. Install: `npm i @glideapps/glide-data-grid`. (5.5k stars, updated 2026-11) *(auto-checked)*
- [react-data-grid](https://github.com/Comcast/react-data-grid) (search: react-data-grid Excel-like React grid): use when you want a lightweight, virtualized editable grid in React. License: MIT. Install: `npm i react-data-grid`. v7 is still published as beta on npm. (7.7k stars, updated 2026-11) *(auto-checked)*
- [MUI X Data Grid](https://mui.com/x/react-data-grid/) (search: MUI X Data Grid): use when the project already uses Material UI. License: MIT (free version); Pro and Premium are paid. Install: `npm i @mui/x-data-grid`. (5.9k stars, updated 2026-11) *(auto-checked)*

**More options**

- [Tabulator](https://tabulator.info/) (search: Tabulator interactive tables JavaScript): use when you need an interactive table without a framework. License: MIT. Install: `npm i tabulator-tables`. (7.8k stars, updated 2026-11) *(auto-checked)*
- [Material React Table](https://www.material-react-table.com/) (search: Material React Table TanStack MUI): use when you want TanStack Table features with ready-made Material UI styling. License: MIT. Install: `npm i material-react-table`. (1.8k stars, updated 2026-06) *(auto-checked)*
- [RevoGrid](https://rv-grid.com) (search: RevoGrid web component data grid): use when you need a fast grid as a web component that works in any framework. License: MIT. Install: `npm i @revolist/revogrid`. (3.5k stars, updated 2026-11) *(auto-checked)*
