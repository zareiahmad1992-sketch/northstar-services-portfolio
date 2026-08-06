# Northstar Services — Jinja + Tailwind template demo

A small, responsive service catalogue built to demonstrate structured frontend templating with **Flask, Jinja, Tailwind CSS, and JSON-driven content**.

![Northstar Services homepage](docs/homepage.png)

## What the project demonstrates

- Responsive HTML/CSS layout for desktop and mobile screens
- Tailwind CSS utility classes with a small custom CSS layer
- Jinja template inheritance using `base.html` and `index.html`
- Reusable Jinja loops, conditionals, and a service-card macro
- JSON-based content loaded from `data/services.json`
- Server-side search and category filtering with Flask
- Semantic HTML, accessible labels, and visible keyboard focus states
- Clear empty-state handling when a filter returns no results
- Simple, maintainable project structure with no duplicated card markup

## Tech stack

- **Python / Flask** — routing and server-side rendering
- **Jinja** — reusable templates and dynamic content
- **Tailwind CSS** — responsive styling and layout
- **JSON** — lightweight content/data source
- **HTML/CSS** — semantic and responsive UI

## Project structure

```text
pome-template-demo/
├── app.py
├── data/
│   └── services.json
├── docs/
│   └── homepage.png
├── static/
│   └── css/
│       └── styles.css
├── templates/
│   ├── base.html
│   └── index.html
├── requirements.txt
└── README.md
```

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 app.py
```

Then open:

```text
http://127.0.0.1:5000/
```

## Design decisions

The service cards are intentionally loaded from JSON rather than hard-coded in the HTML. This makes the template easier to maintain and allows the same layout to support new services without changing the markup. The search and category filters are handled on the server through query parameters, keeping the example simple and easy to extend.

The interface uses semantic sections, form labels, clear focus states, responsive grids, and an explicit empty state to keep the experience understandable for different users and screen sizes.

## Deployment

The project includes a `Procfile` for platforms such as Render or Railway:

```text
web: gunicorn app:app
```

The Flask app reads the `PORT` environment variable when it is available and binds to `0.0.0.0`, so it can run locally or on a cloud platform.

## Possible next improvements

- Add a service details page using a dynamic slug
- Add a contact form with validation
- Move Tailwind from the browser CDN to a local production build
- Add automated tests for routes, filtering, and template rendering
- Add a CMS or API as the content source
