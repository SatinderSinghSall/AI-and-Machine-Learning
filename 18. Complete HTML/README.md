# 📘 HTML — Complete Guide (Beginner to Advanced)

A comprehensive guide to learning **HTML (HyperText Markup Language)** from beginner to advanced level. Includes explanations, examples, best practices, and references to official documentation.

---

# 📚 Table of Contents

1. [Introduction to HTML](#introduction-to-html)
2. [HTML Document Structure](#html-document-structure)
3. [Basic HTML Elements](#basic-html-elements)
4. [Text Formatting Tags](#text-formatting-tags)
5. [Links & Navigation (`<a>` Tag)](#links--navigation-a-tag)
6. [Images (`<img>` Tag)](#images-img-tag)
7. [Lists (ul, ol, dl)](#lists)
8. [Tables](#tables)
9. [HTML Forms](#html-forms)
10. [Semantic HTML](#semantic-html)
11. [Block vs Inline Elements](#block-vs-inline-elements)
12. [Multimedia (Audio/Video)](#multimedia)
13. [HTML Entities](#html-entities)
14. [Meta Tags](#meta-tags)
15. [File Paths](#file-paths)
16. [Responsive Images (`srcset`, `<picture>`)](#responsive-images)
17. [SVG](#svg)
18. [Canvas](#canvas)
19. [Data Attributes (`data-*`)](#data-attributes)
20. [Accessibility (a11y) Basics](#accessibility-a11y)
21. [SEO + Microdata](#seo--microdata)
22. [Web Components (Intro)](#web-components)
23. [Best Practices & Coding Standards](#best-practices)
24. [Useful Tools & Validators](#useful-tools)

---

---

# 📌 **Introduction to HTML**

HTML is the standard markup language used to create webpages.

### ✔ Example:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My HTML Page</title>
  </head>
  <body>
    <h1>Hello World</h1>
  </body>
</html>
```

### 📖 Official Docs:

- MDN: [https://developer.mozilla.org/en-US/docs/Web/HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- WHATWG HTML Spec: [https://html.spec.whatwg.org/](https://html.spec.whatwg.org/)

---

# 📌 **HTML Document Structure**

Every HTML document has a standard skeleton.

### ✔ Example:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Document</title>
  </head>
  <body>
    <p>Content goes here</p>
  </body>
</html>
```

### Key Tags:

| Tag               | Purpose         |
| ----------------- | --------------- |
| `<!DOCTYPE html>` | Defines HTML5   |
| `<html>`          | Root element    |
| `<head>`          | Metadata        |
| `<body>`          | Visible content |

📖 Docs:
[https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started)

---

# 📌 **Basic HTML Elements**

Common foundational tags:

### ✔ Example:

```html
<h1>Main Heading</h1>
<p>A paragraph of text.</p>
<br />
<hr />
```

📖 Docs:
[https://developer.mozilla.org/en-US/docs/Web/HTML/Element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element)

---

# 📌 **Text Formatting Tags**

### ✔ Common Tags:

| Tag        | Meaning          |
| ---------- | ---------------- |
| `<b>`      | Bold (stylistic) |
| `<strong>` | Important text   |
| `<i>`      | Italic           |
| `<em>`     | Emphasized text  |
| `<mark>`   | Highlight        |

### ✔ Example:

```html
<p>This is <strong>important</strong> and <em>emphasized</em> text.</p>
```

📖 Docs:
[https://developer.mozilla.org/en-US/docs/Web/HTML/Element#text_content](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#text_content)

---

# 📌 **Links & Navigation (`<a>` Tag)**

### ✔ Example:

```html
<a href="https://example.com" target="_blank">Visit Site</a>
```

### Attributes:

- `href`
- `target`
- `title`
- `download`

📖 Docs:
[https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a)

---

# 📌 **Images (`<img>` Tag)**

### ✔ Example:

```html
<img src="photo.jpg" alt="Profile Photo" width="300" />
```

📖 Docs:
[https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img)

---

# 📌 **Lists**

### ✔ Types:

- **Ordered list (`<ol>`)**
- **Unordered list (`<ul>`)**
- **Description list (`<dl>`)**

### ✔ Example:

```html
<ul>
  <li>Apple</li>
  <li>Banana</li>
</ul>
```

📖 Docs:
[https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul)

---

# 📌 **Tables**

### ✔ Example:

```html
<table>
  <tr>
    <th>Name</th>
    <th>Age</th>
  </tr>
  <tr>
    <td>Alice</td>
    <td>25</td>
  </tr>
</table>
```

📖 Docs:
[https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table)

---

# 📌 **HTML Forms**

Forms allow user input.

### ✔ Example:

```html
<form action="/submit" method="POST">
  <label>Name:</label>
  <input type="text" name="username" />

  <input type="submit" value="Send" />
</form>
```

### ✔ Input Types:

`text`, `email`, `password`, `radio`, `checkbox`, `date`, `range`, `file`, etc.

📖 Docs:
[https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form)

---

# 📌 **Semantic HTML**

Defines meaning of content rather than appearance.

### Key Tags:

`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`

### ✔ Example:

```html
<article>
  <h2>Blog Post</h2>
  <p>This is a post.</p>
</article>
```

📖 Docs:
[https://developer.mozilla.org/en-US/docs/Glossary/Semantics](https://developer.mozilla.org/en-US/docs/Glossary/Semantics)

---

# 📌 **Block vs Inline Elements**

### ✔ Block Elements:

- Take full width
- Start on a new line
- Examples: `div`, `section`, `p`, `h1`

### ✔ Inline Elements:

- Take only necessary width
- Examples: `span`, `a`, `strong`

📖 Docs:
[https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements)

---

# 📌 **Multimedia**

### Audio:

```html
<audio controls src="song.mp3"></audio>
```

### Video:

```html
<video controls width="500">
  <source src="movie.mp4" />
</video>
```

📖 Docs:
[https://developer.mozilla.org/en-US/docs/Web/Media](https://developer.mozilla.org/en-US/docs/Web/Media)

---

# 📌 **HTML Entities**

Used for reserved characters.

### ✔ Example:

```html
&lt;div&gt; renders as
<div>&copy; renders as ©</div>
```

📖 Docs:
[https://developer.mozilla.org/en-US/docs/Glossary/Entity](https://developer.mozilla.org/en-US/docs/Glossary/Entity)

---

# 📌 **Meta Tags**

### ✔ Example:

```html
<meta charset="UTF-8" />
<meta name="description" content="My website" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
```

📖 Docs:
[https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta)

---

# 📌 **File Paths**

### ✔ Types:

- Absolute path
- Relative path
- Root-relative path

### ✔ Example:

```html
<img src="images/photo.jpg" />
```

📖 Docs:
[https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Creating_hyperlinks#urls_and_paths](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Creating_hyperlinks#urls_and_paths)

---

# 📌 **Responsive Images**

### ✔ Example:

```html
<picture>
  <source srcset="large.jpg" media="(min-width: 800px)" />
  <img src="small.jpg" alt="Image" />
</picture>
```

📖 Docs:
[https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images)

---

# 📌 **SVG**

### ✔ Example:

```html
<svg width="100" height="100">
  <circle cx="50" cy="50" r="40" stroke="black" fill="red" />
</svg>
```

📖 Docs:
[https://developer.mozilla.org/en-US/docs/Web/SVG](https://developer.mozilla.org/en-US/docs/Web/SVG)

---

# 📌 **Canvas**

Used for drawing with JavaScript.

### ✔ Example:

```html
<canvas id="myCanvas" width="200" height="200"></canvas>
```

📖 Docs:
[https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API)

---

# 📌 **Data Attributes (`data-*`)**

### ✔ Example:

```html
<div data-user-id="42">User Info</div>
```

📖 Docs:
[https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes)

---

# 📌 **Accessibility (a11y)**

### ✔ Example:

```html
<img src="dog.jpg" alt="Brown dog running" />
<label for="name">Name</label>
<input id="name" type="text" />
```

📖 Docs:
[https://developer.mozilla.org/en-US/docs/Learn/Accessibility](https://developer.mozilla.org/en-US/docs/Learn/Accessibility)

---

# 📌 **SEO & Microdata**

### ✔ Example:

```html
<div itemscope itemtype="https://schema.org/Person">
  <span itemprop="name">John Doe</span>
</div>
```

📖 Docs:
[https://schema.org/](https://schema.org/)

---

# 📌 **Web Components (Intro)**

### ✔ Example:

```html
<my-button>Click</my-button>
```

📖 Docs:
[https://developer.mozilla.org/en-US/docs/Web/Web_Components](https://developer.mozilla.org/en-US/docs/Web/Web_Components)

---

# 📌 **Best Practices**

- Always use semantic tags
- Include `alt` text for images
- Use proper indentation
- Keep structure clean
- Validate your HTML

---

# 📌 **Useful Tools**

### ✔ Validators:

- W3C Validator: [https://validator.w3.org/](https://validator.w3.org/)

### ✔ Playground:

- CodePen
- JSFiddle
