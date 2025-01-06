
# Building a Books and Movie Recommendation System with Next.js 15

Creating a comprehensive recommendation system for books and movies involves several components, including frontend development, backend services, database management, authentication, and web scraping. Below is a detailed guide to help you build this system using Next.js 15, TypeScript, Prisma, PostgreSQL, Clerk for authentication, and animation libraries like Framer Motion and React Spring.

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

---

## Project Structure

Organizing your project efficiently is crucial for maintainability and scalability. Below is the recommended folder structure:

```
my-recommendation-app/
├── prisma/
│   └── schema.prisma
├── src/
│   ├── components/
│   │   ├── auth/
│   │   ├── books/
│   │   ├── movies/
│   │   └── common/
│   ├── lib/
│   │   ├── api/
│   │   ├── db/
│   │   └── scraper/
│   ├── pages/
│   ├── app/
│   │   ├── layout.tsx
│   │   └── page.tsx
│   ├── styles/
│   └── types/
├── scripts/
│   └── scraper.ts
├── public/
├── .env
├── package.json
└── tsconfig.json
```

---

## Initial Setup

1. **Initialize the Next.js Project**

   ```bash
   npx create-next-app@latest my-recommendation-app --typescript
   cd my-recommendation-app
   ```

2. **Install Dependencies**

   ```bash
   npm install prisma @prisma/client react-query zustand framer-motion react-spring clerk next-auth axios cheerio puppeteer
   ```

3. **Configure Environment Variables**

   Create a `.env` file at the root:

   ```env
   DATABASE_URL=postgresql://USER:PASSWORD@HOST:PORT/DATABASE
   CLERK_API_KEY=your-clerk-api-key
   ```

---

## Database Schema with Prisma

Define your database schema to manage books, movies, and user data.

```markdown
### prisma/schema.prisma

```prisma:path/prisma/schema.prisma
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
  // Add relations if necessary
}

model Book {
  id          String   @id @default(cuid())
  title       String
  author      String
  description String
  coverImage  String
  createdAt   DateTime @default(now())
  updatedAt   DateTime @updatedAt
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
}
```
```

After defining the schema, run the following commands to set up Prisma:

```bash
npx prisma migrate dev --name init
npx prisma generate
```

---

## Authentication with Clerk

Integrate Clerk for user authentication to manage user sessions securely.

```markdown
### src/lib/auth.ts

```typescript:path/src/lib/auth.ts
import { ClerkProvider } from '@clerk/nextjs';

export const AuthProvider = ({ children }: { children: React.ReactNode }) => {
  return <ClerkProvider>{children}</ClerkProvider>;
};
```
```

Update your `app/layout.tsx` to include the `AuthProvider`:

```markdown
### src/app/layout.tsx

```typescript:path/src/app/layout.tsx
import { AuthProvider } from '../lib/auth';
import '../styles/globals.css';

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html>
      <body>
        <AuthProvider>{children}</AuthProvider>
      </body>
    </html>
  );
}
```
```

---

## API Integration

Set up APIs to fetch book and movie data from external sources.

```markdown
### src/lib/api/books.ts

```typescript:path/src/lib/api/books.ts
import axios from 'axios';

export const fetchBooks = async () => {
  const response = await axios.get('https://api.example.com/books');
  return response.data;
};
```

### src/lib/api/movies.ts

```typescript:path/src/lib/api/movies.ts
import axios from 'axios';

export const fetchMovies = async () => {
  const response = await axios.get('https://api.example.com/movies');
  return response.data;
};
```
```

---

## Web Scraper Development

Develop a scraper to extract movie data from free movie sites like Sflix.

### 1. Setup Scraper with Cheerio

```markdown
### scripts/scraper.ts

```typescript:path/scripts/scraper.ts
import axios from 'axios';
import cheerio from 'cheerio';
import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

const scrapeSflix = async () => {
  try {
    const { data } = await axios.get('https://sflix.example.com');
    const $ = cheerio.load(data);

    $('.movie-item').each(async (index, element) => {
      const title = $(element).find('.title').text();
      const director = $(element).find('.director').text();
      const description = $(element).find('.description').text();
      const posterImage = $(element).find('img').attr('src');
      const watchLink = $(element).find('a.watch').attr('href');

      await prisma.movie.create({
        data: {
          title,
          director,
          description,
          posterImage,
          watchLink,
        },
      });
    });

    console.log('Scraping completed!');
  } catch (error) {
    console.error('Error scraping Sflix:', error);
  } finally {
    await prisma.$disconnect();
  }
};

scrapeSflix();
```
```

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

**Resources:**
- For a detailed guide on building a scraper, refer to [Joe Osborne's Intro to Web Scraping](https://medium.com/@joerosborne/intro-to-web-scraping-build-your-first-scraper-in-5-minutes-1c36b5c4b110).

---

## Frontend Development

Develop the user interface to display book and movie recommendations.

### 1. Components

#### Books List

```markdown
### src/components/books/BooksList.tsx

```typescript:path/src/components/books/BooksList.tsx
import { useQuery } from 'react-query';
import { fetchBooks } from '../../lib/api/books';
import BookCard from './BookCard';

const BooksList = () => {
  const { data, isLoading, error } = useQuery('books', fetchBooks);

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error loading books.</div>;

  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
      {data.map((book: any) => (
        <BookCard key={book.id} book={book} />
      ))}
    </div>
  );
};

export default BooksList;
```
```

#### Book Card

```markdown
### src/components/books/BookCard.tsx

```typescript:path/src/components/books/BookCard.tsx
import { motion } from 'framer-motion';

interface Book {
  id: string;
  title: string;
  author: string;
  description: string;
  coverImage: string;
}

const BookCard = ({ book }: { book: Book }) => {
  return (
    <motion.div
      className="border rounded-lg p-4"
      whileHover={{ scale: 1.05 }}
    >
      <img src={book.coverImage} alt={book.title} className="w-full h-64 object-cover" />
      <h2 className="text-xl font-semibold mt-2">{book.title}</h2>
      <p className="text-gray-600">by {book.author}</p>
      <p className="mt-2">{book.description}</p>
    </motion.div>
  );
};

export default BookCard;
```
```

#### Movies List

```markdown
### src/components/movies/MoviesList.tsx

```typescript:path/src/components/movies/MoviesList.tsx
import { useQuery } from 'react-query';
import { fetchMovies } from '../../lib/api/movies';
import MovieCard from './MovieCard';

const MoviesList = () => {
  const { data, isLoading, error } = useQuery('movies', fetchMovies);

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error loading movies.</div>;

  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
      {data.map((movie: any) => (
        <MovieCard key={movie.id} movie={movie} />
      ))}
    </div>
  );
};

export default MoviesList;
```
```

#### Movie Card

```markdown
### src/components/movies/MovieCard.tsx

```typescript:path/src/components/movies/MovieCard.tsx
import { motion } from 'framer-motion';

interface Movie {
  id: string;
  title: string;
  director: string;
  description: string;
  posterImage: string;
  watchLink: string;
}

const MovieCard = ({ movie }: { movie: Movie }) => {
  return (
    <motion.div
      className="border rounded-lg p-4"
      whileHover={{ scale: 1.05 }}
    >
      <img src={movie.posterImage} alt={movie.title} className="w-full h-64 object-cover" />
      <h2 className="text-xl font-semibold mt-2">{movie.title}</h2>
      <p className="text-gray-600">Directed by {movie.director}</p>
      <p className="mt-2">{movie.description}</p>
      <a href={movie.watchLink} className="text-blue-500 mt-2 inline-block">
        Watch Now
      </a>
    </motion.div>
  );
};

export default MovieCard;
```
```

### 2. Pages

#### Home Page

```markdown
### src/app/page.tsx

```typescript:path/src/app/page.tsx
import BooksList from '../components/books/BooksList';
import MoviesList from '../components/movies/MoviesList';

const HomePage = () => {
  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-4">Book Recommendations</h1>
      <BooksList />
      
      <h1 className="text-3xl font-bold my-4">Movie Recommendations</h1>
      <MoviesList />
    </div>
  );
};

export default HomePage;
```
```

---

## Animations

Enhance user experience with animations using Framer Motion and React Spring.

### Example: Animated Navigation

```markdown
### src/components/common/AnimatedNav.tsx

```typescript:path/src/components/common/AnimatedNav.tsx
import { motion } from 'framer-motion';

const AnimatedNav = () => {
  return (
    <motion.nav
      initial={{ y: -100 }}
      animate={{ y: 0 }}
      transition={{ type: 'spring', stiffness: 50 }}
      className="bg-gray-800 p-4"
    >
      <ul className="flex space-x-4">
        <li className="text-white">Home</li>
        <li className="text-white">Books</li>
        <li className="text-white">Movies</li>
      </ul>
    </motion.nav>
  );
};

export default AnimatedNav;
```
```

---

## Deployment

Deploy your application using platforms like Vercel for seamless integration with Next.js.

1. **Push to GitHub**

   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/my-recommendation-app.git
   git push -u origin main
   ```

2. **Deploy on Vercel**

   - Sign up on [Vercel](https://vercel.com/).
   - Import your GitHub repository.
   - Set environment variables in Vercel dashboard.
   - Deploy the project.

---

## Testing and Optimization

Ensure your application is robust and performs efficiently.

### 1. Unit Testing with Jest

```markdown
### src/components/books/__tests__/BookCard.test.tsx

```typescript:path/src/components/books/__tests__/BookCard.test.tsx
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
```

### 2. Integration Testing with React Testing Library

Ensure that components interact correctly.

### 3. Performance Optimization

- **Code Splitting:** Utilize dynamic imports to load components only when needed.

  ```typescript
  import dynamic from 'next/dynamic';

  const BooksList = dynamic(() => import('../components/books/BooksList'), {
    loading: () => <p>Loading...</p>,
  });
  ```

- **Image Optimization:** Use Next.js `Image` component for optimized images.

  ```typescript
  import Image from 'next/image';

  <Image src={book.coverImage} alt={book.title} width={500} height={750} />
  ```

---

# Conclusion

By following this structured approach, you can build a robust and scalable books and movie recommendation system using Next.js 15 and the specified technologies. Ensure to adhere to best practices in code organization, error handling, and performance optimization to maintain a high-quality application.

For more detailed guides and resources, refer to the [web scraping tutorial by Joe Osborne](https://medium.com/@joerosborne/intro-to-web-scraping-build-your-first-scraper-in-5-minutes-1c36b5c4b110).
