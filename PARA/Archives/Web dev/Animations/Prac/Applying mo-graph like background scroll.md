
# Adding Mo Graph-Like Background Animations

To incorporate motion graphics (mo graph)-like background animations that respond to scrolling in your project, you can leverage **React Three Fiber** along with the `useScroll` hook from **@react-three/drei**. This combination allows you to create interactive and performant 3D animations that dynamically adjust based on the user's scroll position.

Below is a step-by-step guide to achieving this:

## 1. Install Required Dependencies

Ensure you have the necessary libraries installed in your Next.js project.

```bash
npm install three @react-three/fiber @react-three/drei
```

## 2. Create the Background Animation Component

We'll create a component that sets up a Three.js scene using React Three Fiber and integrates scroll-based animations.

### File Structure

```
my-threejs-project/
├── components/
│   ├── animations/
│   │   └── ScrollResponsiveBackground.tsx
│   └── ...
├── pages/
│   ├── index.tsx
│   └── ...
├── public/
│   └── models/
│       └── ...
├── styles/
│   └── globals.css
├── hooks/
│   └── usePrefersReducedMotion.ts
├── utils/
│   └── ...
├── types/
│   └── ...
└── ...
```

### ScrollResponsiveBackground Component

```typescript:components/animations/ScrollResponsiveBackground.tsx
import React, { useRef } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { useScroll, OrbitControls } from '@react-three/drei';
import * as THREE from 'three';

const AnimatedSphere: React.FC = () => {
  const meshRef = useRef<THREE.Mesh>(null);
  const scroll = useScroll();

  useFrame(() => {
    if (meshRef.current) {
      // Rotate the sphere based on scroll position
      meshRef.current.rotation.y = scroll.scroll.current * Math.PI * 2;
      meshRef.current.rotation.x = scroll.scroll.current * Math.PI;
    }
  });

  return (
    <mesh ref={meshRef} position={[0, 0, 0]}>
      <sphereGeometry args={[1, 32, 32]} />
      <meshStandardMaterial color="#ff6347" wireframe />
    </mesh>
  );
};

const AnimatedTorus: React.FC = () => {
  const meshRef = useRef<THREE.Mesh>(null);
  const scroll = useScroll();

  useFrame(() => {
    if (meshRef.current) {
      // Animate the torus scale based on scroll position
      meshRef.current.scale.setScalar(1 + scroll.scroll.current * 2);
      meshRef.current.rotation.x += 0.01;
      meshRef.current.rotation.y += 0.005;
    }
  });

  return (
    <mesh ref={meshRef} position={[3, 0, 0]}>
      <torusGeometry args={[0.8, 0.3, 16, 100]} />
      <meshStandardMaterial color="#1e90ff" />
    </mesh>
  );
};

const ScrollResponsiveBackground: React.FC = () => {
  return (
    <div className="w-full h-screen fixed top-0 left-0 z-[-1]">
      <Canvas camera={{ position: [0, 0, 5], fov: 60 }}>
        {/* Lighting */}
        <ambientLight intensity={0.5} />
        <pointLight position={[10, 10, 10]} />

        {/* Animated Objects */}
        <AnimatedSphere />
        <AnimatedTorus />

        {/* Controls (optional) */}
        {/* <OrbitControls enableZoom={false} /> */}
      </Canvas>
    </div>
  );
};

export default ScrollResponsiveBackground;
```

### Explanation

1. **AnimatedSphere Component:**
   - **Purpose:** Creates a rotating sphere that responds to scroll position.
   - **Behavior:** Rotates along the X and Y axes based on the current scroll position.
   - **Visuals:** A wireframe sphere with a tomato color.

2. **AnimatedTorus Component:**
   - **Purpose:** Creates a torus that scales and rotates based on scroll.
   - **Behavior:** 
     - **Scale:** Increases as the user scrolls down.
     - **Rotation:** Continuously rotates around the X and Y axes.
   - **Visuals:** A blue torus mesh.

3. **ScrollResponsiveBackground Component:**
   - **Purpose:** Renders the Three.js scene in the background.
   - **Structure:**
     - **Canvas:** Sets up the Three.js rendering context.
     - **Lighting:** Adds ambient and point lights to illuminate the scene.
     - **Animated Objects:** Includes both `AnimatedSphere` and `AnimatedTorus`.
     - **Controls:** Optional orbit controls for user interaction (commented out).

4. **Styling:**
   - The `div` containing the `Canvas` is fixed and covers the entire viewport, ensuring it stays in the background (`z-[-1]`).

## 3. Integrate the Background Animation into Your Page

You can now integrate the `ScrollResponsiveBackground` component into your page, such as the `index.tsx` file.

### Example: pages/index.tsx

```typescript:pages/index.tsx
import React from 'react';
import ScrollResponsiveBackground from '../components/animations/ScrollResponsiveBackground';

const HomePage: React.FC = () => {
  return (
    <div className="relative w-full h-full">
      {/* Background Animation */}
      <ScrollResponsiveBackground />

      {/* Main Content */}
      <main className="relative z-10 flex flex-col items-center justify-center min-h-screen p-4">
        <h1 className="text-4xl font-bold text-white">Welcome to My Website</h1>
        <p className="mt-4 text-lg text-white">
          Scroll down to see the background animations respond to your actions.
        </p>
      </main>

      {/* Additional Content to Enable Scrolling */}
      <section className="relative z-10 h-[200vh] bg-transparent"></section>
    </div>
  );
};

export default HomePage;
```

### Explanation

- **ScrollResponsiveBackground:** Positioned fixed in the background, it renders the animated Three.js scene.
- **Main Content:** Contains your primary content with a higher `z-index` to appear above the background animations.
- **Additional Content:** A section with increased height (`200vh`) to enable scrolling, allowing you to see the background animations respond.

## 4. Handling Performance and Accessibility

### Optimize Performance

- **Use Efficient Geometries:** Simplify geometries where possible to reduce rendering load.
- **Limit the Number of Objects:** Avoid having too many animated objects in the scene.
- **Use `React.memo`:** Memoize components to prevent unnecessary re-renders.

### Respect User Preferences

Implement a hook to detect if the user prefers reduced motion and disable animations accordingly.

```typescript:hooks/usePrefersReducedMotion.ts
import { useEffect, useState } from 'react';

const usePrefersReducedMotion = () => {
  const [prefersReducedMotion, setPrefersReducedMotion] = useState(false);

  useEffect(() => {
    const mediaQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
    setPrefersReducedMotion(mediaQuery.matches);

    const handler = () => setPrefersReducedMotion(mediaQuery.matches);
    mediaQuery.addEventListener('change', handler);
    return () => mediaQuery.removeEventListener('change', handler);
  }, []);

  return prefersReducedMotion;
};

export default usePrefersReducedMotion;
```

### Modify Animation Based on Preference

Update your animation components to respect the user's motion preferences.

```typescript:components/animations/AccessibleAnimatedSphere.tsx
import React, { useRef } from 'react';
import { useFrame } from '@react-three/fiber';
import { useScroll } from '@react-three/drei';
import * as THREE from 'three';
import usePrefersReducedMotion from '../../hooks/usePrefersReducedMotion';

const AccessibleAnimatedSphere: React.FC = () => {
  const meshRef = useRef<THREE.Mesh>(null);
  const scroll = useScroll();
  const prefersReducedMotion = usePrefersReducedMotion();

  useFrame(() => {
    if (meshRef.current && !prefersReducedMotion) {
      meshRef.current.rotation.y = scroll.scroll.current * Math.PI * 2;
      meshRef.current.rotation.x = scroll.scroll.current * Math.PI;
    }
  });

  return (
    <mesh ref={meshRef} position={[0, 0, 0]}>
      <sphereGeometry args={[1, 32, 32]} />
      <meshStandardMaterial color="#ff6347" wireframe />
    </mesh>
  );
};

export default AccessibleAnimatedSphere;
```

## 5. Additional Enhancements

### Adding More Interactive Elements

- **Particles:** Use particle systems to create dynamic backgrounds.
- **Shaders:** Implement custom shaders for unique visual effects.
- **Animations:** Integrate libraries like **React Spring** for more fluid animations.

### Example: Adding a Particle System

```typescript:components/animations/ParticleBackground.tsx
import React, { useRef } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { Points, PointMaterial, Preload } from '@react-three/drei';
import * as THREE from 'three';

const Particles = () => {
  const pointsRef = useRef<THREE.Points>(null!);
  const count = 1000;
  const positions = new Float32Array(count * 3);

  for (let i = 0; i < count * 3; i++) {
    positions[i] = (Math.random() - 0.5) * 100;
  }

  useFrame(() => {
    if (pointsRef.current) {
      pointsRef.current.rotation.y += 0.001;
    }
  });

  return (
    <Points ref={pointsRef} positions={positions} stride={3} frustumCulled>
      <PointMaterial
        transparent
        color="#ffffff"
        size={0.1}
        sizeAttenuation
        depthWrite={false}
      />
    </Points>
  );
};

const ParticleBackground: React.FC = () => {
  return (
    <Canvas>
      <ambientLight intensity={0.5} />
      <Particles />
      <Preload all />
    </Canvas>
  );
};

export default ParticleBackground;
```

### Explanation

- **Particles Component:**
  - Generates a set of particles positioned randomly in 3D space.
  - Rotates the entire particle system slowly around the Y-axis.

- **ParticleBackground Component:**
  - Renders the `Particles` within the Three.js `Canvas`.
  - Adds ambient lighting for visibility.

## 6. Integrate the Particle Background with Scroll

You can combine the particle system with scroll interactions to create dynamic effects.

### Example: Particle System Responding to Scroll

```typescript:components/animations/ScrollResponsiveParticleBackground.tsx
import React, { useRef } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { Points, PointMaterial, Preload, useScroll } from '@react-three/drei';
import * as THREE from 'three';
import usePrefersReducedMotion from '../../hooks/usePrefersReducedMotion';

const ScrollResponsiveParticles: React.FC = () => {
  const pointsRef = useRef<THREE.Points>(null!);
  const scroll = useScroll();
  const prefersReducedMotion = usePrefersReducedMotion();
  const count = 5000;
  const positions = useRef(new Float32Array(count * 3)).current;

  // Initialize particle positions
  React.useEffect(() => {
    for (let i = 0; i < count * 3; i++) {
      positions[i] = (Math.random() - 0.5) * 100;
    }
  }, [count, positions]);

  useFrame(() => {
    if (pointsRef.current && !prefersReducedMotion) {
      pointsRef.current.rotation.y += 0.001;
      // Example: Adjust particle positions based on scroll
      const offset = scroll.scroll.current * 10;
      pointsRef.current.position.z = offset;
    }
  });

  return (
    <Points ref={pointsRef} positions={positions} stride={3} frustumCulled>
      <PointMaterial
        transparent
        color="#ffffff"
        size={0.05}
        sizeAttenuation
        depthWrite={false}
      />
    </Points>
  );
};

const ScrollResponsiveParticleBackground: React.FC = () => {
  return (
    <div className="w-full h-screen fixed top-0 left-0 z-[-2]">
      <Canvas>
        <ambientLight intensity={0.5} />
        <ScrollResponsiveParticles />
        <Preload all />
      </Canvas>
      {/* Scroll Container */}
      <div style={{ height: '300vh' }}></div>
    </div>
  );
};

export default ScrollResponsiveParticleBackground;
```

### Explanation

- **ScrollResponsiveParticles Component:**
  - Initializes a larger number of particles for a denser background.
  - Adjusts the position of the particle system along the Z-axis based on scroll position.
  - Respects user preferences for reduced motion.

- **ScrollResponsiveParticleBackground Component:**
  - Positions the particle background behind other content using `z-index`.
  - Adds a scrollable `div` to enable scrolling interactions.

## 7. Final Integration

Ensure that your background animation components are properly integrated into your main page to render behind other content.

### Example: Integrate into HomePage

```typescript:pages/index.tsx
import React from 'react';
import ScrollResponsiveBackground from '../components/animations/ScrollResponsiveBackground';
import ScrollResponsiveParticleBackground from '../components/animations/ScrollResponsiveParticleBackground';

const HomePage: React.FC = () => {
  return (
    <div className="relative w-full min-h-screen overflow-x-hidden">
      {/* Particle Background */}
      <ScrollResponsiveParticleBackground />

      {/* Three.js Background Animation */}
      <ScrollResponsiveBackground />

      {/* Main Content */}
      <main className="relative z-10 flex flex-col items-center justify-center min-h-screen p-4">
        <h1 className="text-4xl font-bold text-white">Welcome to My Website</h1>
        <p className="mt-4 text-lg text-white">
          Scroll down to see the background animations respond to your actions.
        </p>
      </main>

      {/* Additional Content to Enable Scrolling */}
      <section className="relative z-10 h-[300vh] bg-transparent"></section>
    </div>
  );
};

export default HomePage;
```

### Explanation

- **ScrollResponsiveParticleBackground & ScrollResponsiveBackground:**
  - Rendered with low `z-index` values to stay in the background.
  
- **Main Content:**
  - Positioned with a higher `z-index` to appear above the animated backgrounds.

- **Scroll Section:**
  - Provides additional scrollable space to trigger the background animations.

## 8. Best Practices

- **Performance Optimization:**
  - Limit the number of animated objects to maintain high frame rates.
  - Use efficient geometries and materials.
  - Leverage memoization techniques like `React.memo` for static components.

- **Accessibility:**
  - Respect user preferences for reduced motion.
  - Ensure that animations do not hinder content readability or user experience.

- **Responsive Design:**
  - Ensure that animations scale and adjust correctly across different screen sizes and devices.

## 9. Resources

- [React Three Fiber Documentation](https://docs.pmnd.rs/react-three-fiber/getting-started/introduction)
- [@react-three/drei](https://github.com/pmndrs/drei)
- [Three.js Documentation](https://threejs.org/docs/)
- [useScroll Hook](https://github.com/pmndrs/drei#usescroll)
- [React Three Fiber Tutorials](https://github.com/pmndrs/react-three-fiber#resources)

## 10. Practice Projects

1. **Interactive Starfield:**
   - Create a dense starfield that moves and twinkles as the user scrolls.

2. **3D Parallax Scrolling:**
   - Implement multiple layers of 3D objects moving at different speeds to create a deep parallax effect.

3. **Animated Landscape:**
   - Develop a 3D landscape that changes based on scroll position, simulating day to night transitions.

4. **Scroll-Based Model Animation:**
   - Animate a complex 3D model (e.g., a spaceship) that transforms or moves in response to scrolling.

By following this roadmap and utilizing the provided examples, you'll be able to create sophisticated mo graph-like background animations that enhance the visual appeal and interactivity of your web projects.
