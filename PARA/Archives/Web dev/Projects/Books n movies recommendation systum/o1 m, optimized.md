
# Optimized Structure for Building a Books and Movie Recommendation System with Next.js 14+

Your initial approach is solid, but we can optimize the structure and provide more detailed guidance to ensure maintainability, scalability, and adherence to best practices. Below is an enhanced structure with optimizations and additional explanations.

## Table of Contents

1. [Project Structure](#project-structure)
2. [Initial Setup](#initial-setup)
3. [Database Schema with Prisma](#database-schema-with-prisma)
4. [Authentication with Clerk](#authentication-with-clerk)
5. [API Integration](#api-integration)
6. [Web Scraper Development](#web-scraper-development)
7. [Frontend Development](#frontend-development)
8. [Animations](#animations)
9. [Deployment](#deployment)
10. [Testing and Optimization](#testing-and-optimization)
11. [Conclusion](#conclusion)

---

## Project Structure

A well-organized project structure enhances maintainability and scalability. Here's the optimized folder structure:

```
my-recommendation-app/
├── prisma/
│   └── schema.prisma
├── src/
│   ├── components/
│   │   ├── auth-wizard/
│   │   ├── books/
│   │   ├── movies/
│   │   └── common/
│   ├── lib/
│   │   ├── api/
│   │   ├── db/
│   │   ├── scraper/
│   │   └── validation/
│   ├── app/
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   └── globals.css
│   ├── hooks/
│   ├── pages/
│   ├── styles/
│   └── types/
├── scripts/
│   └── scraper.ts
├── public/
├── tests/
│   ├── components/
│   └── lib/
├── .env
├── .gitignore
├── package.json
├── tsconfig.json
└── next.config.js
```

### Enhancements:

- **Hooks Directory:** Centralize custom React hooks.
- **Validation Directory:** Manage schema validations using Zod.
- **Tests Directory:** Organize unit and integration tests.
- **Globals.css:** Centralized styling.
- **Next.config.js:** Configuration for Next.js, including image optimization settings.

---

## Initial Setup

1. **Initialize the Next.js Project**

   ```bash
   npx create-next-app@latest my-recommendation-app --typescript
   cd my-recommendation-app
   ```

2. **Install Dependencies**

   ```bash
   npm install prisma @prisma/client react-query zustand framer-motion react-spring @clerk/nextjs axios cheerio puppeteer zod
   npm install --save-dev jest @testing-library/react @testing-library/jest-dom @types/jest ts-node
   ```

3. **Configure Environment Variables**

   Create a `.env` file at the root:

   ```env
   DATABASE_URL=postgresql://USER:PASSWORD@HOST:PORT/DATABASE
   CLERK_API_KEY=your-clerk-api-key
   CLERK_FRONTEND_API=your-clerk-frontend-api
   ```

4. **Initialize Prisma**

   ```bash
   npx prisma init
   ```

   Update `prisma/schema.prisma` as shown in the next section.

---

## Database Schema with Prisma

Define a comprehensive schema to manage users, books, movies, and their relationships.

```markdown
### prisma/schema.prisma
```

```prisma:path/to/prisma/schema.prisma
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model User {
  id        String   @id @default(cuid())
  email     String   @unique
  name      String?
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
  // Relations
  recommendedBooks  RecommendedBook[]
  recommendedMovies RecommendedMovie[]
}

model Book {
  id          String   @id @default(cuid())
  title       String
  author      String
  description String
  coverImage  String
  createdAt   DateTime @default(now())
  updatedAt   DateTime @updatedAt
  // Relations
  recommendedBy RecommendedBook[]
}

model Movie {
  id          String   @id @default(cuid())
  title       String
  director    String
  description String
  posterImage String
  watchLink   String
  createdAt   DateTime @default(now())
  updatedAt   DateTime @updatedAt
  // Relations
  recommendedBy RecommendedMovie[]
}

model RecommendedBook {
  id        String @id @default(cuid())
  user      User   @relation(fields: [userId], references: [id])
  userId    String
  book      Book   @relation(fields: [bookId], references: [id])
  bookId    String
  createdAt DateTime @default(now())

  @@unique([userId, bookId])
}

model RecommendedMovie {
  id        String @id @default(cuid())
  user      User   @relation(fields: [userId], references: [id])
  userId    String
  movie     Movie  @relation(fields: [movieId], references: [id])
  movieId   String
  createdAt DateTime @default(now())

  @@unique([userId, movieId])
}
```

### Explanation:

- **Relationships:** Users can have multiple recommended books and movies.
- **Unique Constraints:** Prevent duplicate recommendations per user.

### Setup Prisma:

```bash
npx prisma migrate dev --name init
npx prisma generate
```

---

## Authentication with Clerk

Integrate Clerk for secure user authentication.

```markdown
### src/lib/auth.ts
```

```typescript:path/to/src/lib/auth.ts
import { ClerkProvider } from '@clerk/nextjs';

export const AuthProvider = ({ children }: { children: React.ReactNode }) => {
  return <ClerkProvider>{children}</ClerkProvider>;
};
```

Update your `app/layout.tsx` to include the `AuthProvider`:

```markdown
### src/app/layout.tsx
```

```typescript:path/to/src/app/layout.tsx
import { AuthProvider } from '../lib/auth';
import '../styles/globals.css';

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <AuthProvider>{children}</AuthProvider>
      </body>
    </html>
  );
}
```

### Protecting Routes

Use Clerk's hooks to protect specific pages or components.

```markdown
### src/app/ProtectedPage.tsx
```

```typescript:path/to/src/app/ProtectedPage.tsx
import { useAuth } from '@clerk/nextjs';
import { RedirectToSignIn } from '@clerk/nextjs';
import { ReactNode } from 'react';

interface ProtectedProps {
  children: ReactNode;
}

const ProtectedPage = ({ children }: ProtectedProps) => {
  const { isLoaded, userId } = useAuth();

  if (!isLoaded) return null;
  if (!userId) return <RedirectToSignIn />;

  return <>{children}</>;
};

export default ProtectedPage;
```

Use `ProtectedPage` to wrap components that require authentication.

---

## API Integration

Set up APIs to fetch book and movie data from external sources and handle recommendations.

### 1. API Routes with Next.js 14 (App Directory)

Utilize Next.js server actions and the app directory for API routes.

```markdown
### src/lib/api/books.ts
```

```typescript:path/to/src/lib/api/books.ts
import axios from 'axios';
import { Book } from '@prisma/client';
import { z } from 'zod';

const bookSchema = z.array(
  z.object({
    id: z.string(),
    title: z.string(),
    author: z.string(),
    description: z.string(),
    coverImage: z.string().url(),
  })
);

export const fetchBooks = async (): Promise<Book[]> => {
  const response = await axios.get('https://api.example.com/books');
  const books = bookSchema.parse(response.data);
  return books;
};
```

```markdown
### src/lib/api/movies.ts
```

```typescript:path/to/src/lib/api/movies.ts
import axios from 'axios';
import { Movie } from '@prisma/client';
import { z } from 'zod';

const movieSchema = z.array(
  z.object({
    id: z.string(),
    title: z.string(),
    director: z.string(),
    description: z.string(),
    posterImage: z.string().url(),
    watchLink: z.string().url(),
  })
);

export const fetchMovies = async (): Promise<Movie[]> => {
  const response = await axios.get('https://api.example.com/movies');
  const movies = movieSchema.parse(response.data);
  return movies;
};
```

### 2. Recommendation API

Handle user-specific recommendations.

```markdown
### src/app/api/recommendations/route.ts
```

```typescript:path/to/src/app/api/recommendations/route.ts
import { NextResponse } from 'next/server';
import { prisma } from '../../lib/db';
import { z } from 'zod';
import { auth } from '@clerk/nextjs';

const recommendationSchema = z.object({
  type: z.enum(['book', 'movie']),
  itemId: z.string(),
});

export async function POST(request: Request) {
  try {
    const { userId } = auth();
    if (!userId) {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }

    const body = await request.json();
    const { type, itemId } = recommendationSchema.parse(body);

    if (type === 'book') {
      await prisma.recommendedBook.create({
        data: {
          userId,
          bookId: itemId,
        },
      });
    } else {
      await prisma.recommendedMovie.create({
        data: {
          userId,
          movieId: itemId,
        },
      });
    }

    return NextResponse.json({ message: 'Recommendation added' }, { status: 201 });
  } catch (error) {
    return NextResponse.json({ error: error.message }, { status: 400 });
  }
}
```

### Explanation:

- **Validation:** Using Zod for request validation.
- **Authentication:** Ensuring only authenticated users can add recommendations.

---

## Web Scraper Development

Develop a scraper to extract movie data from free movie sites like Sflix. Ensure compliance with the site's terms of service.

### 1. Setup Scraper with Cheerio and Puppeteer

Use Puppeteer for dynamic content and Cheerio for parsing.

```markdown
### scripts/scraper.ts
```

```typescript:path/to/scripts/scraper.ts
import axios from 'axios';
import cheerio from 'cheerio';
import puppeteer from 'puppeteer';
import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

const scrapeSflix = async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  try {
    await page.goto('https://sflix.example.com');

    const content = await page.content();
    const $ = cheerio.load(content);

    $('.movie-item').each(async (index, element) => {
      const title = $(element).find('.title').text().trim();
      const director = $(element).find('.director').text().trim();
      const description = $(element).find('.description').text().trim();
      const posterImage = $(element).find('img').attr('src') || '';
      const watchLink = $(element).find('a.watch').attr('href') || '';

      if (title && watchLink) {
        await prisma.movie.upsert({
          where: { title },
          update: { director, description, posterImage, watchLink },
          create: { title, director, description, posterImage, watchLink },
        });
      }
    });

    console.log('Scraping completed!');
  } catch (error) {
    console.error('Error scraping Sflix:', error);
  } finally {
    await browser.close();
    await prisma.$disconnect();
  }
};

scrapeSflix();
```

### Enhancements:

- **Puppeteer:** Handles dynamic content and JavaScript-rendered pages.
- **Upsert Operation:** Avoids duplicate entries by updating existing records or creating new ones.

### 2. Running the Scraper

Add a script to `package.json`:

```json
"scripts": {
  "scrape": "ts-node scripts/scraper.ts"
}
```

Run the scraper:

```bash
npm run scrape
```

### 3. Scheduling Scraper

Use a cron job or a serverless function to run the scraper periodically.

---

## Frontend Development

Develop a responsive and interactive user interface to display book and movie recommendations.

### 1. Components

Organize components into relevant directories.

#### Books List

```markdown
### src/components/books/BooksList.tsx
```

```typescript:path/to/src/components/books/BooksList.tsx
'use client';

import { useQuery } from '@tanstack/react-query';
import { fetchBooks } from '../../lib/api/books';
import BookCard from './BookCard';

const BooksList = () => {
  const { data, isLoading, error } = useQuery(['books'], fetchBooks);

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error loading books.</div>;

  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
      {data.map((book) => (
        <BookCard key={book.id} book={book} />
      ))}
    </div>
  );
};

export default BooksList;
```

#### Book Card

```markdown
### src/components/books/BookCard.tsx
```

```typescript:path/to/src/components/books/BookCard.tsx
'use client';

import { motion } from 'framer-motion';
import Image from 'next/image';
import { Book } from '../../types';

interface Props {
  book: Book;
}

const BookCard = ({ book }: Props) => {
  return (
    <motion.div
      className="border rounded-lg p-4 shadow-lg"
      whileHover={{ scale: 1.05 }}
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 0.5 }}
    >
      <Image
        src={book.coverImage}
        alt={book.title}
        width={500}
        height={750}
        className="w-full h-64 object-cover rounded"
        loading="lazy"
      />
      <h2 className="text-xl font-semibold mt-2">{book.title}</h2>
      <p className="text-gray-600">by {book.author}</p>
      <p className="mt-2">{book.description}</p>
    </motion.div>
  );
};

export default BookCard;
```

#### Movies List

```markdown
### src/components/movies/MoviesList.tsx
```

```typescript:path/to/src/components/movies/MoviesList.tsx
'use client';

import { useQuery } from '@tanstack/react-query';
import { fetchMovies } from '../../lib/api/movies';
import MovieCard from './MovieCard';

const MoviesList = () => {
  const { data, isLoading, error } = useQuery(['movies'], fetchMovies);

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error loading movies.</div>;

  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
      {data.map((movie) => (
        <MovieCard key={movie.id} movie={movie} />
      ))}
    </div>
  );
};

export default MoviesList;
```

#### Movie Card

```markdown
### src/components/movies/MovieCard.tsx
```

```typescript:path/to/src/components/movies/MovieCard.tsx
'use client';

import { motion } from 'framer-motion';
import Image from 'next/image';
import { Movie } from '../../types';

interface Props {
  movie: Movie;
}

const MovieCard = ({ movie }: Props) => {
  return (
    <motion.div
      className="border rounded-lg p-4 shadow-lg"
      whileHover={{ scale: 1.05 }}
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 0.5 }}
    >
      <Image
        src={movie.posterImage}
        alt={movie.title}
        width={500}
        height={750}
        className="w-full h-64 object-cover rounded"
        loading="lazy"
      />
      <h2 className="text-xl font-semibold mt-2">{movie.title}</h2>
      <p className="text-gray-600">Directed by {movie.director}</p>
      <p className="mt-2">{movie.description}</p>
      <a
        href={movie.watchLink}
        target="_blank"
        rel="noopener noreferrer"
        className="text-blue-500 mt-2 inline-block"
      >
        Watch Now
      </a>
    </motion.div>
  );
};

export default MovieCard;
```

### 2. Pages

#### Home Page

```markdown
### src/app/page.tsx
```

```typescript:path/to/src/app/page.tsx
'use client';

import BooksList from '../components/books/BooksList';
import MoviesList from '../components/movies/MoviesList';
import AnimatedNav from '../components/common/AnimatedNav';
import { useAuth } from '@clerk/nextjs';
import { useRouter } from 'next/navigation';

const HomePage = () => {
  const { isLoaded, userId } = useAuth();
  const router = useRouter();

  if (isLoaded && !userId) {
    router.push('/sign-in');
  }

  return (
    <div className="container mx-auto p-4">
      <AnimatedNav />
      <section className="my-8">
        <h1 className="text-3xl font-bold mb-4">Book Recommendations</h1>
        <BooksList />
      </section>
      
      <section className="my-8">
        <h1 className="text-3xl font-bold mb-4">Movie Recommendations</h1>
        <MoviesList />
      </section>
    </div>
  );
};

export default HomePage;
```

### Explanation:

- **AnimatedNav:** Provides a consistent navigation bar with animations.
- **Authentication Check:** Redirects unauthenticated users to the sign-in page.

---

## Animations

Enhance user experience with engaging animations using Framer Motion and React Spring.

### Example: Animated Navigation

```markdown
### src/components/common/AnimatedNav.tsx
```

```typescript:path/to/src/components/common/AnimatedNav.tsx
'use client';

import { motion } from 'framer-motion';
import Link from 'next/link';

const AnimatedNav = () => {
  return (
    <motion.nav
      initial={{ y: -100 }}
      animate={{ y: 0 }}
      transition={{ type: 'spring', stiffness: 50 }}
      className="bg-gray-800 p-4"
    >
      <ul className="flex space-x-4">
        <li>
          <Link href="/" className="text-white hover:text-gray-300">
            Home
          </Link>
        </li>
        <li>
          <Link href="/books" className="text-white hover:text-gray-300">
            Books
          </Link>
        </li>
        <li>
          <Link href="/movies" className="text-white hover:text-gray-300">
            Movies
          </Link>
        </li>
      </ul>
    </motion.nav>
  );
};

export default AnimatedNav;
```

### Example: Page Transitions

Implement smooth page transitions using Framer Motion.

```markdown
### src/app/layout.tsx
```

```typescript:path/to/src/app/layout.tsx
import { AuthProvider } from '../lib/auth';
import '../styles/globals.css';
import { motion, AnimatePresence } from 'framer-motion';
import { usePathname } from 'next/navigation';

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const pathname = usePathname();

  return (
    <html lang="en">
      <body>
        <AuthProvider>
          <AnimatePresence exitBeforeEnter>
            <motion.div
              key={pathname}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -20 }}
              transition={{ duration: 0.3 }}
            >
              {children}
            </motion.div>
          </AnimatePresence>
        </AuthProvider>
      </body>
    </html>
  );
}
```

### Explanation:

- **AnimatePresence:** Enables exit animations when components are removed from the tree.
- **motion.div:** Wraps page content to animate transitions.

---

## Deployment

Deploy your application using Vercel for seamless integration with Next.js.

### 1. Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/my-recommendation-app.git
git push -u origin main
```

### 2. Deploy on Vercel

1. **Sign Up/Log In:** Visit [Vercel](https://vercel.com/) and sign up or log in.
2. **Import Project:** Import your GitHub repository.
3. **Configure Environment Variables:** Set `DATABASE_URL`, `CLERK_API_KEY`, and `CLERK_FRONTEND_API` in Vercel's dashboard.
4. **Deploy:** Vercel will automatically build and deploy your project.

### Optimizations:

- **Image Optimization:** Ensure `next.config.js` includes domains for external images.

```markdown
### next.config.js
```

```javascript:path/to/next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  images: {
    domains: ['example.com', 'sflix.example.com'], // Add your image domains here
  },
};

module.exports = nextConfig;
```

---

## Testing and Optimization

Ensure your application is robust, performs efficiently, and adheres to best practices.

### 1. Unit Testing with Jest

Setup Jest for testing React components.

```markdown
### jest.config.js
```

```javascript:path/to/jest.config.js
module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'jsdom',
  setupFilesAfterEnv: ['<rootDir>/tests/setup.ts'],
  moduleNameMapper: {
    '\\.(css|less|scss|sass)$': 'identity-obj-proxy',
  },
};
```

```markdown
### tests/setup.ts
```

```typescript:path/to/tests/setup.ts
import '@testing-library/jest-dom';
```

#### Example Test

```markdown
### src/components/books/__tests__/BookCard.test.tsx
```

```typescript:path/to/src/components/books/__tests__/BookCard.test.tsx
import { render, screen } from '@testing-library/react';
import BookCard from '../BookCard';

test('renders book details', () => {
  const book = {
    id: '1',
    title: 'Sample Book',
    author: 'Author Name',
    description: 'This is a sample book description.',
    coverImage: 'https://example.com/cover.jpg',
  };

  render(<BookCard book={book} />);
  
  expect(screen.getByText('Sample Book')).toBeInTheDocument();
  expect(screen.getByText('by Author Name')).toBeInTheDocument();
  expect(screen.getByText('This is a sample book description.')).toBeInTheDocument();
  expect(screen.getByAltText('Sample Book')).toHaveAttribute('src', 'https://example.com/cover.jpg');
});
```

### 2. Integration Testing with React Testing Library

Ensure that components interact correctly.

#### Example Integration Test

```markdown
### tests/integration/HomePage.test.tsx
```

```typescript:path/to/tests/integration/HomePage.test.tsx
import { render, screen } from '@testing-library/react';
import HomePage from '../../src/app/page';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { ClerkProvider } from '@clerk/nextjs';

const queryClient = new QueryClient();

test('renders HomePage with books and movies', () => {
  render(
    <ClerkProvider>
      <QueryClientProvider client={queryClient}>
        <HomePage />
      </QueryClientProvider>
    </ClerkProvider>
  );

  expect(screen.getByText('Book Recommendations')).toBeInTheDocument();
  expect(screen.getByText('Movie Recommendations')).toBeInTheDocument();
});
```

### 3. Performance Optimization

#### a. Code Splitting

Utilize dynamic imports to load components only when needed.

```typescript
import dynamic from 'next/dynamic';

const BooksList = dynamic(() => import('../components/books/BooksList'), {
  loading: () => <p>Loading books...</p>,
});
```

#### b. Image Optimization

Use Next.js `Image` component for optimized images.

```typescript
import Image from 'next/image';

<Image
  src={book.coverImage}
  alt={book.title}
  width={500}
  height={750}
  className="w-full h-64 object-cover rounded"
  loading="lazy"
/>
```

#### c. Caching with React Query

Configure React Query for efficient data fetching and caching.

```typescript:path/to/src/lib/api/react-query.ts
import { QueryClient } from '@tanstack/react-query';

export const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 1000 * 60 * 5, // 5 minutes
      cacheTime: 1000 * 60 * 30, // 30 minutes
      refetchOnWindowFocus: false,
    },
  },
});
```

Wrap your application with `QueryClientProvider`:

```typescript:path/to/src/app/layout.tsx
import { AuthProvider } from '../lib/auth';
import '../styles/globals.css';
import { motion, AnimatePresence } from 'framer-motion';
import { usePathname } from 'next/navigation';
import { QueryClientProvider } from '@tanstack/react-query';
import { queryClient } from '../lib/api/react-query';

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const pathname = usePathname();

  return (
    <html lang="en">
      <body>
        <AuthProvider>
          <QueryClientProvider client={queryClient}>
            <AnimatePresence exitBeforeEnter>
              <motion.div
                key={pathname}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -20 }}
                transition={{ duration: 0.3 }}
              >
                {children}
              </motion.div>
            </AnimatePresence>
          </QueryClientProvider>
        </AuthProvider>
      </body>
    </html>
  );
}
```

### d. SEO Optimization

Ensure your application is SEO-friendly.

```markdown
### src/app/head.tsx
```

```typescript:path/to/src/app/head.tsx
export default function Head() {
  return (
    <>
      <title>Books and Movies Recommendation</title>
      <meta name="description" content="Discover and watch recommended books and movies." />
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      {/* Add more SEO tags as needed */}
    </>
  );
}
```

---

## Testing and Optimization

Ensure your application is robust and performs efficiently.

### 1. Unit Testing with Jest

Set up Jest for testing React components and functions.

#### Example Test for BookCard

```markdown
### src/components/books/__tests__/BookCard.test.tsx
```

```typescript:path/to/src/components/books/__tests__/BookCard.test.tsx
import { render, screen } from '@testing-library/react';
import BookCard from '../BookCard';

test('renders book details', () => {
  const book = {
    id: '1',
    title: 'Sample Book',
    author: 'Author Name',
    description: 'This is a sample book description.',
    coverImage: 'https://example.com/cover.jpg',
  };

  render(<BookCard book={book} />);
  
  expect(screen.getByText('Sample Book')).toBeInTheDocument();
  expect(screen.getByText('by Author Name')).toBeInTheDocument();
  expect(screen.getByText('This is a sample book description.')).toBeInTheDocument();
  expect(screen.getByAltText('Sample Book')).toHaveAttribute('src', 'https://example.com/cover.jpg');
});
```

### 2. Integration Testing with React Testing Library

Ensure that components interact correctly.

#### Example Integration Test for HomePage

```markdown
### tests/integration/HomePage.test.tsx
```

```typescript:path/to/tests/integration/HomePage.test.tsx
import { render, screen } from '@testing-library/react';
import HomePage from '../../src/app/page';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { ClerkProvider } from '@clerk/nextjs';

const queryClient = new QueryClient();

test('renders HomePage with books and movies', () => {
  render(
    <ClerkProvider>
      <QueryClientProvider client={queryClient}>
        <HomePage />
      </QueryClientProvider>
    </ClerkProvider>
  );

  expect(screen.getByText('Book Recommendations')).toBeInTheDocument();
  expect(screen.getByText('Movie Recommendations')).toBeInTheDocument();
});
```

### 3. Performance Optimization

#### a. Code Splitting

Utilize dynamic imports to load components only when needed.

```typescript
import dynamic from 'next/dynamic';

const BooksList = dynamic(() => import('../components/books/BooksList'), {
  loading: () => <p>Loading books...</p>,
});
```

#### b. Image Optimization

Use Next.js `Image` component for optimized images.

```typescript
import Image from 'next/image';

<Image
  src={book.coverImage}
  alt={book.title}
  width={500}
  height={750}
  className="w-full h-64 object-cover rounded"
  loading="lazy"
/>
```

#### c. Caching with React Query

Configure React Query for efficient data fetching and caching.

```typescript:path/to/src/lib/api/react-query.ts
import { QueryClient } from '@tanstack/react-query';

export const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 1000 * 60 * 5, // 5 minutes
      cacheTime: 1000 * 60 * 30, // 30 minutes
      refetchOnWindowFocus: false,
    },
  },
});
```

Wrap your application with `QueryClientProvider`:

```typescript:path/to/src/app/layout.tsx
import { AuthProvider } from '../lib/auth';
import '../styles/globals.css';
import { motion, AnimatePresence } from 'framer-motion';
import { usePathname } from 'next/navigation';
import { QueryClientProvider } from '@tanstack/react-query';
import { queryClient } from '../lib/api/react-query';

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const pathname = usePathname();

  return (
    <html lang="en">
      <body>
        <AuthProvider>
          <QueryClientProvider client={queryClient}>
            <AnimatePresence exitBeforeEnter>
              <motion.div
                key={pathname}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -20 }}
                transition={{ duration: 0.3 }}
              >
                {children}
              </motion.div>
            </AnimatePresence>
          </QueryClientProvider>
        </AuthProvider>
      </body>
    </html>
  );
}
```

### d. SEO Optimization

Ensure your application is SEO-friendly.

```markdown
### src/app/head.tsx
```

```typescript:path/to/src/app/head.tsx
export default function Head() {
  return (
    <>
      <title>Books and Movies Recommendation</title>
      <meta name="description" content="Discover and watch recommended books and movies." />
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      {/* Add more SEO tags as needed */}
    </>
  );
}
```

---

## Conclusion

By following this optimized structure and implementing the provided enhancements, you can build a robust, scalable, and maintainable books and movie recommendation system using Next.js 14+. Ensure to adhere to best practices in code organization, error handling, performance optimization, and security to maintain a high-quality application.

### References

- [Prisma Documentation](https://www.prisma.io/docs/)
- [Clerk Documentation](https://docs.clerk.dev/)
- [Next.js Documentation](https://nextjs.org/docs)
- [Framer Motion Documentation](https://www.framer.com/motion/)
- [React Query Documentation](https://tanstack.com/query/latest)
- [Web Scraping with Puppeteer](https://pptr.dev/)
- [Zod Validation Library](https://zod.dev/)
