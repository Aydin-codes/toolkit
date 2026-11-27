# Docs, print and PDF

<!-- Generated from catalog/print-pdf.yaml. Edit the YAML, then run: python scripts/build.py -->

## Make PDFs

**Default**

- [Typst](https://typst.app) (search: Typst typesetting system). License: Apache-2.0. Install: `cargo install --locked typst-cli, brew install typst, or download a release binary; typst compile doc.typ`. (57.5k stars, updated 2026-11) *(auto-checked)*

**Strong alternatives**

- [WeasyPrint](https://weasyprint.org/) (search: WeasyPrint HTML CSS to PDF Python): use when you already have HTML and CSS and want print-quality PDFs from Python without a browser. License: BSD-3-Clause. Install: `pip install weasyprint`. (9.8k stars, updated 2026-11) *(auto-checked)*
- [React-PDF](https://github.com/diegomura/react-pdf) (search: react-pdf renderer diegomura): use when you build PDFs from React components in the browser or on Node, with its own flexbox layout. License: MIT. Install: `npm i @react-pdf/renderer`. (16.9k stars, updated 2026-11) *(auto-checked)*
- [Playwright page.pdf()](https://playwright.dev/python/docs/api/class-page) (search: Playwright page.pdf): use when you want a PDF of a real web page exactly as headless Chromium prints it. License: Apache-2.0. Install: `npm i playwright (or pip install playwright), then page.pdf()`. page.pdf() works in Chromium only. (101.2k stars, updated 2026-11) *(auto-checked)*
- [Pandoc](https://pandoc.org/) (search: Pandoc universal document converter): use when you convert Markdown, DOCX or HTML into PDF, DOCX, EPUB and other formats. License: GPL-2.0-or-later. Install: `see https://pandoc.org/installing.html (apt install pandoc, brew install pandoc); needs a PDF engine such as Typst, WeasyPrint or LaTeX`. (47.1k stars, updated 2026-11) *(auto-checked)*

**More options**

- [Puppeteer](https://github.com/puppeteer/puppeteer) (search: Puppeteer page.pdf): use when you are already on Puppeteer and want headless Chrome to print pages to PDF. License: Apache-2.0. Install: `npm i puppeteer`. (95.9k stars, updated 2026-11) *(auto-checked)*
- [pdfme](https://pdfme.com/) (search: pdfme PDF template designer generator): use when you want a drag-and-drop template designer plus JSON data to generate forms, invoices and labels. License: MIT. Install: `npm i @pdfme/generator @pdfme/common (add @pdfme/ui for the WYSIWYG designer)`. (5.1k stars, updated 2026-11) *(auto-checked)*
- [TeX Live](https://tug.org/texlive/) (search: TeX Live distribution): use when you need the complete LaTeX distribution with every package and engine (pdfLaTeX, XeLaTeX, LuaLaTeX). License: free software, mixed licenses (LPPL, GPL and others per package). Install: `see https://www.tug.org/texlive/acquire.html (or apt install texlive-latex-recommended)`. *(auto-checked)*
- [Gotenberg](https://github.com/gotenberg/gotenberg) (search: Gotenberg Docker API PDF): use when you want an HTTP service that turns HTML, URLs, Markdown and Office files into PDF (Chromium and LibreOffice inside). License: MIT. Install: `docker run --rm -p 3000:3000 gotenberg/gotenberg:8`. (13.7k stars, updated 2026-11) *(auto-checked)*
- [Vivliostyle CLI](https://github.com/vivliostyle/vivliostyle-cli) (search: Vivliostyle CLI CSS typesetting): use when you typeset books from Markdown or HTML with CSS Paged Media, including vertical Japanese text. License: AGPL-3.0. Install: `npm i -D @vivliostyle/cli; npx vivliostyle build`. AGPL; fine as a build tool, check terms before bundling into a served product. (247 stars, updated 2026-11) *(auto-checked)*

**Paid** (only when asked, or when no free option fits)

- [Prince](https://princexml.com/) (search: Prince XML HTML to PDF). License: paid; free non-commercial license adds a logo to page one. Strongest CSS Paged Media support. Free option: WeasyPrint or Vivliostyle. *(auto-checked)*

## Edit and merge

**Default**

- [qpdf](https://qpdf.sourceforge.io) (search: qpdf PDF transformation command line). License: Apache-2.0. Install: `apt install qpdf or brew install qpdf`. (5.6k stars, updated 2026-11) *(auto-checked)*

**Strong alternatives**

- [pikepdf](https://pikepdf.readthedocs.io/) (search: pikepdf Python qpdf): use when you want qpdf's robustness from Python, including low-level object edits and repairing damaged files. License: MPL-2.0. Install: `pip install pikepdf`. (2.8k stars, updated 2026-11) *(auto-checked)*
- [PyMuPDF](https://pymupdf.readthedocs.io/) (search: PyMuPDF fitz Python MuPDF): use when you need fast rendering, text extraction, redaction and page edits in one Python library and can accept AGPL. License: AGPL-3.0 or Artifex commercial license. Install: `pip install pymupdf`. AGPL; a closed-source product or service needs the paid Artifex license. Same engine as MuPDF / mutool. (11.2k stars, updated 2026-11) *(auto-checked)*
- [PDFtk Server (pdftk-java)](https://www.pdflabs.com/tools/pdftk-server) (search: pdftk-java PDF toolkit): use when you want the classic one-line commands for merging, splitting, stamping and filling forms. License: GPL-2.0-or-later; redistribution in non-GPL commercial products needs a paid license. Install: `apt install pdftk-java or brew install pdftk-java`. The original C++ PDFtk is unmaintained; pdftk-java is the maintained port that distros ship. *(auto-checked)*

**More options**

- [Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF) (search: Stirling-PDF self-hosted PDF tools): use when you want a self-hosted web app and API with dozens of PDF operations (merge, convert, OCR, sign). License: MIT core; Pro and Enterprise features under a proprietary license. Install: `docker run -p 8080:8080 stirlingtools/stirling-pdf`. Some features are not open source; check which build you run. (97.6k stars, updated 2026-11) *(auto-checked)*

## Read and extract

**Default**

- [Docling](https://docling-project.github.io/docling) (search: Docling IBM document conversion). License: MIT. Install: `pip install docling`. (71.1k stars, updated 2026-11) *(auto-checked)*

**Strong alternatives**

- [pdfplumber](https://github.com/jsvine/pdfplumber) (search: pdfplumber Python table extraction): use when you need exact text positions, lines and tables from digital (not scanned) PDFs. License: MIT. Install: `pip install pdfplumber`. (10.9k stars, updated 2026-11) *(auto-checked)*
- [PDF.js](https://mozilla.github.io/pdf.js/) (search: Mozilla PDF.js): use when you render or read text from PDFs in the browser or Node with JavaScript. License: Apache-2.0. Install: `npm i pdfjs-dist`. (54.2k stars, updated 2026-11) *(auto-checked)*
- [Marker](https://github.com/datalab-to/marker) (search: Marker PDF to markdown datalab): use when you want PDFs (including equations and tables) converted to Markdown with deep-learning layout models. License: Apache-2.0 code; model weights under modified AI Pubs Open Rail-M (free for research, personal use and startups under $5M). Install: `pip install marker-pdf`. Larger companies need a paid license for the weights. (41.1k stars, updated 2026-11) *(auto-checked)*
- [Unstructured](https://github.com/Unstructured-IO/unstructured) (search: Unstructured document partitioning Python): use when you split many file types into typed elements (titles, tables, text) for RAG pipelines. License: Apache-2.0. Install: `pip install unstructured (add extras like "unstructured[pdf]")`. (15.8k stars, updated 2026-11) *(auto-checked)*
- [Apache Tika](https://tika.apache.org) (search: Apache Tika content analysis toolkit): use when you need text and metadata out of more than a thousand file types through one Java server. License: Apache-2.0. Install: `run the tika-server jar or Docker image; Python client via pip install tika`. (4.2k stars, updated 2026-11) *(auto-checked)*

**More options**

- [MinerU](https://mineru.net/) (search: MinerU PDF to markdown opendatalab): use when you convert complex PDFs (papers, formulas, Chinese text) to Markdown or JSON. License: MinerU Open Source License (custom; read before commercial use). Install: `pip install mineru`. (84.4k stars, updated 2026-11) *(auto-checked)*
- [unpdf](https://github.com/unjs/unpdf) (search: unjs unpdf): use when you extract text or images from PDFs in serverless or edge JavaScript runtimes (PDF.js build without the DOM). License: MIT. Install: `npm i unpdf`. (1.3k stars, updated 2026-11) *(auto-checked)*
- [Camelot](https://camelot-py.readthedocs.io/) (search: Camelot PDF table extraction Python): use when you only need tables out of digital PDFs, straight into pandas DataFrames. License: MIT. Install: `pip install camelot-py`. (3.9k stars, updated 2026-11) *(auto-checked)*

## OCR

**Default**

- [OCRmyPDF](https://ocrmypdf.readthedocs.io/) (search: OCRmyPDF searchable PDF). License: MPL-2.0. Install: `pip install ocrmypdf (needs Tesseract and Ghostscript), or apt install ocrmypdf`. (35.4k stars, updated 2026-11) *(auto-checked)*

**Strong alternatives**

- [Tesseract](https://github.com/tesseract-ocr/tesseract) (search: Tesseract OCR engine): use when you need the standard open OCR engine for images, with 100+ languages. License: Apache-2.0. Install: `apt install tesseract-ocr or brew install tesseract`. (77.7k stars, updated 2026-11) *(auto-checked)*
- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) (search: PaddleOCR): use when you need higher accuracy on hard scans, photos, Chinese and mixed layouts than Tesseract gives. License: Apache-2.0. Install: `pip install paddleocr (plus paddlepaddle)`. (93.4k stars, updated 2026-09) *(auto-checked)*
- [docTR](https://mindee.github.io/doctr) (search: docTR Mindee OCR): use when you want a deep-learning OCR pipeline (detection plus recognition) on PyTorch. License: Apache-2.0. Install: `pip install python-doctr`. (6.4k stars, updated 2026-11) *(auto-checked)*
- [Tesseract.js](https://github.com/naptha/tesseract.js) (search: tesseract.js OCR JavaScript): use when you need OCR in the browser or Node without a native install. License: Apache-2.0. Install: `npm i tesseract.js`. (38.9k stars, updated 2026-05) *(auto-checked)*

**More options**

- [pytesseract](https://github.com/madmaze/pytesseract) (search: pytesseract Python wrapper): use when you call Tesseract from Python on images you already have in memory. License: Apache-2.0. Install: `pip install pytesseract (needs Tesseract installed)`. (6.4k stars, updated 2026-11) *(auto-checked)*

## Templates

**Strong alternatives**

- [LaTeXTemplates.com](https://www.latextemplates.com) (search: LaTeXTemplates.com): use when you want curated, well-kept LaTeX templates for books, theses, CVs and reports. License: per template (mostly LPPL, MIT, CC BY); some have no license. Get it: download the .zip from each template page. Treat templates with no listed license as all rights reserved. *(auto-checked)*
- [Overleaf template gallery](https://overleaf.com/latex/templates) (search: Overleaf LaTeX templates gallery): use when you need a journal, conference or university template, often the official one. License: per template (Overleaf recommends LPPL for templates). Install: `open in Overleaf or download the source zip`. *(auto-checked)*
- [pdfme templates](https://pdfme.com/docs/template-contribution-guide) (search: pdfme templates playground): use when you want starting JSON templates (invoices, certificates, labels) for pdfme. License: MIT. Install: `copy a template JSON from the pdfme playground; use with @pdfme/generator`. (5.1k stars, updated 2026-11) *(auto-checked)*

## Print and layout tools

**Default**

- [Scribus](https://www.scribus.net) (search: Scribus desktop publishing). License: GPL-2.0-or-later. Install: `apt install scribus, or download from scribus.net; scriptable with Python`. *(auto-checked)*

**Strong alternatives**

- [MDN @page reference](https://developer.mozilla.org/docs/Web/CSS/@page) (search: MDN CSS @page): use when you need page size, margins and page selectors for print CSS. License: CC-BY-SA-2.5 (MDN content). *(auto-checked)*
- [CSS Paged Media Module Level 3 (W3C)](https://www.w3.org/TR/css-page/) (search: W3C CSS Paged Media Module Level 3): use when you need the spec for margin boxes, page counters and named pages used by Paged.js, WeasyPrint and Prince. License: W3C Document License. *(auto-checked)*
- [Can I use CSS Paged Media](https://caniuse.com/css-paged-media) (search: caniuse CSS paged media): use when you check which @page features a browser supports before relying on browser print-to-PDF. License: free reference, link only. *(auto-checked)*

**More options**

- [Scribus color management guide](https://raw.githubusercontent.com/scribusproject/scribus/master/doc/en/cms.html) (search: Scribus color management CMYK ICC): use when you need a plain explanation of ICC profiles, CMYK and soft-proofing before sending files to print. License: GPL-2.0-or-later (Scribus docs). *(auto-checked)*
