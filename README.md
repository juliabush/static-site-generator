![Tests](https://github.com/juliabush/static-site-generator/actions/workflows/tests.yml/badge.svg)
![Coverage](https://codecov.io/gh/juliabush/static-site-generator/branch/main/graph/badge.svg)

# Static Site Generator in Python - Backend

A lightweight static site generator written entirely in Python.
It converts Markdown (.md) files into full HTML pages using a custom-built Markdown parser, HTML node tree, and recursive file generation system — no external libraries required.

## Features & How They Work

- **Custom Markdown Parses**

* Supports:
* Headings (`# syntax`)
  - Paragraphs
  - Code blocks (```)
  - Blockquotes (`>`)
  - Ordered and unordered lists
  - Inline formatting (`**bold**`, `_italic_`, `` `code` ``)
  - Links (`[text](url)`)
  - Images (`![alt](url)`)
  - 🧩 **HTML Node Tree System**
  - Uses `HTMLNode`, `ParentNode`, and `LeafNode` classes to represent and render HTML elements programmatically.

- **Recursive Site Builder**
  - Walks through your `/content` directory, converts every Markdown file to HTML, and applies a shared HTML template.

- **Template Rendering**
  - Injects Markdown-generated HTML and page titles into an HTML template (`template.html`) using placeholders:
    ```
    {{ Title }}
    {{ Content }}
    ```

- **No Dependencies**
  - Built entirely with the Python 3 standard library — no external packages required.

- **Fully Unit Tested**
  - Comprehensive tests for Markdown parsing and HTML generation ensure reliability.

  ### ⚙️ How It Works (Behind the Scenes)

1. **Parse Markdown → Blocks**  
   Splits Markdown into blocks (paragraphs, code, lists, etc.) and detects their type.

2. **Convert Blocks → HTML Nodes**  
   Builds a tree of `ParentNode` and `LeafNode` objects representing the HTML structure.

3. **Render HTML**  
   Recursively renders all nodes into HTML strings.

4. **Inject into Template**  
   Inserts the rendered HTML and page title into `template.html`.

5. **Generate Output**  
   Writes final pages into the `/docs` directory, preserving the folder structure.

### Example

```Markdown
# Hello World

Welcome to **my site**!

> A simple quote.

- Item 1
- Item 2

![Logo](logo.png)
```

This is what the output would look like:

```HTML
<h1>Hello World</h1>
<p>Welcome to <b>my site</b>!</p>
<blockquote>A simple quote.</blockquote>
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
</ul>
<img src="logo.png" alt="Logo" />
```
