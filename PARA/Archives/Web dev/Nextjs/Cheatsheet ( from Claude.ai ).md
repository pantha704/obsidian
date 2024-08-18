
# Next.js Cheatsheet

## Project Structure

```
my-next-app/
├── pages/
│   ├── api/
│   │   └── hello.js
│   ├── _app.js
│   ├── index.js
│   └── about.js
├── public/
│   └── favicon.ico
├── styles/
│   └── globals.css
├── components/
│   └── Layout.js
├── lib/
├── next.config.js
└── package.json
```

- `pages/`: Routes are based on the file structure in this directory
- `pages/api/`: API routes
- `public/`: Static assets
- `styles/`: Global styles
- `components/`: Reusable React components
- `lib/`: Utility functions and modules

## Key Concepts and Features

### 1. Routing

- File-based routing: `pages/about.js` → `/about`
- Dynamic routes: `pages/posts/[id].js` → `/posts/1`, `/posts/2`, etc.
- Catch-all routes: `pages/posts/[...slug].js`

### 2. Link Component

```jsx
import Link from 'next/link'

<Link href="/about">
  <a>About</a>
</Link>
```

### 3. Image Component

```jsx
import Image from 'next/image'

<Image src="/profile.jpg" alt="Profile" width={500} height={500} />
```

### 4. Data Fetching

- `getStaticProps`: Fetch data at build time
- `getServerSideProps`: Fetch data on each request
- `getStaticPaths`: Specify dynamic routes to pre-render

### 5. API Routes

Create in `pages/api/` directory:

```javascript
// pages/api/hello.js
export default function handler(req, res) {
  res.status(200).json({ name: 'John Doe' })
}
```

### 6. CSS Support

- CSS Modules: `styles/Home.module.css`
- Sass: Built-in support
- CSS-in-JS: Styled-components, Emotion

### 7. Environment Variables

- `.env.local` for local variables
- `process.env.NEXT_PUBLIC_` prefix for client-side variables

### 8. Custom App

```jsx
// pages/_app.js
function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />
}

export default MyApp
```

### 9. Custom Document

```jsx
// pages/_document.js
import Document, { Html, Head, Main, NextScript } from 'next/document'

class MyDocument extends Document {
  render() {
    return (
      <Html>
        <Head />
        <body>
          <Main />
          <NextScript />
        </body>
      </Html>
    )
  }
}

export default MyDocument
```

### 10. Next.js Config

```javascript
// next.config.js
module.exports = {
  reactStrictMode: true,
  images: {
    domains: ['example.com'],
  },
}
```

### 11. Automatic Code Splitting

Next.js automatically code-splits your application, loading only the JavaScript needed for the current page.

### 12. TypeScript Support

Next.js has built-in TypeScript support. Just use `.ts` or `.tsx` file extensions.

### 13. Fast Refresh

Provides instantaneous feedback on edits made to React components.

### 14. Internationalization

Built-in support for internationalized routing and language detection.

### 15. Static HTML Export

```
next build && next export
```

Generates static HTML files for your entire application.



---
# Detailed


# Next.js Concepts Explained

## 1. Project Structure

Next.js has a specific project structure that enables its key features:

- `pages/`: This directory is the core of Next.js routing. Each file in this directory becomes a route in your application. For example, `pages/about.js` will be accessible at `/about`.

- `pages/api/`: This directory is used for API routes. These are serverless functions that can be used to create API endpoints.

- `public/`: This directory is used for static assets like images, fonts, etc. Files in this directory are served from the root of your application.

- `styles/`: While not required, this is commonly used for global styles.

- `components/`: This directory is for React components that are reused across multiple pages.

- `lib/`: This is commonly used for utility functions and modules.

- `next.config.js`: This file is used for custom Next.js configurations.

## 2. Routing

Next.js uses a file-system based router built on the concept of pages.

- Basic Routes: If you create a file at `pages/about.js`, it will be accessible at `/about`.

- Dynamic Routes: You can create dynamic routes by adding brackets to a page name. For example, `pages/posts/[id].js` will match `/posts/1`, `/posts/2`, etc.

- Catch-all Routes: You can create catch-all routes by adding three dots inside the brackets. For example, `pages/posts/[...slug].js` will match `/posts/a`, `/posts/a/b`, `/posts/a/b/c`, etc.

## 3. Link Component

The `Link` component is used for client-side navigation between pages. It's similar to an `<a>` tag, but it allows the navigation to happen without a full page reload.

```jsx
import Link from 'next/link'

<Link href="/about">
  <a>About</a>
</Link>
```

## 4. Image Component

Next.js provides an `Image` component that automatically optimizes images. It can automatically resize, optimize, and serve images in modern formats like WebP when the browser supports it.

```jsx
import Image from 'next/image'

<Image src="/profile.jpg" alt="Profile" width={500} height={500} />
```

## 5. Data Fetching

Next.js provides several ways to fetch data:

- `getStaticProps`: This function runs at build time in production, and fetches data to pre-render static pages.

- `getServerSideProps`: This function runs on every request, allowing you to fetch data and render pages dynamically on the server.

- `getStaticPaths`: This function specifies which paths to pre-render for dynamic routes when using static generation.

## 6. API Routes

API routes provide a solution to build your API with Next.js. Any file inside the folder `pages/api` is mapped to `/api/*` and will be treated as an API endpoint instead of a page.

```javascript
// pages/api/hello.js
export default function handler(req, res) {
  res.status(200).json({ name: 'John Doe' })
}
```

## 7. CSS Support

Next.js has built-in support for CSS and Sass. It also supports CSS Modules, which allows you to locally scope CSS by automatically creating unique class names.

## 8. Environment Variables

Next.js has built-in support for environment variables. You can create a `.env.local` file in your project root to load environment variables. To expose variables to the browser, prefix the variable with `NEXT_PUBLIC_`.

## 9. Custom App

You can override the default `App` component that initializes pages by creating a `pages/_app.js` file. This is useful for persisting layout between page changes, keeping state when navigating pages, or adding global styles.

## 10. Custom Document

A custom `Document` can update the `<html>` and `<body>` tags used to render a Page. This file is only rendered on the server, so event handlers like `onClick` cannot be used in `_document`.

## 11. Next.js Config

The `next.config.js` file allows you to customize advanced features of Next.js. You can customize the build process, add environment variables, and more.

## 12. Automatic Code Splitting

Next.js automatically splits your code into small chunks. This means that only the necessary code is loaded for each page, making your application faster.

## 13. TypeScript Support

Next.js provides an integrated TypeScript experience out of the box, including zero-config support and built-in types.

## 14. Fast Refresh

Fast Refresh is a Next.js feature that gives you instantaneous feedback on edits made to your React components.

## 15. Internationalization

Next.js has built-in support for internationalized (i18n) routing and language detection. This allows you to create multi-language websites easily.

## 16. Static HTML Export

Next.js allows you to export your application to static HTML, which can be run standalone without the need of a Node.js server.