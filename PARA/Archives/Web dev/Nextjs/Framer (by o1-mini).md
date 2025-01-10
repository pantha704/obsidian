# Comprehensive Guide to Framer Motion Attributes

Framer Motion is a powerful animation library for React, offering a wide range of attributes (props) to create smooth and interactive animations. Below is a comprehensive list of Framer Motion attributes, explained one by one in a logical sequence to help you understand their uses and functionalities.

## 1. `motion` Components

Framer Motion extends regular HTML and SVG elements with animation capabilities via `motion` components. For example:

```jsx
import { motion } from "framer-motion"

<motion.div>Animated Div</motion.div>
```

## 2. Animation Attributes

### `initial`
Defines the starting state of the animation when the component mounts.

```jsx
<motion.div initial={{ opacity: 0 }} />
```

### `animate`
Specifies the target state to which the component should animate.

```jsx
<motion.div animate={{ opacity: 1 }} />
```

### `exit`
Defines the state to animate to when the component is removed from the DOM, used with `AnimatePresence`.

```jsx
<motion.div exit={{ opacity: 0 }} />
```

### `variants`
Allows defining multiple animation states that can be referenced by name, facilitating complex animations.

```jsx
const variants = {
  hidden: { opacity: 0 },
  visible: { opacity: 1 },
}

<motion.div variants={variants} initial="hidden" animate="visible" />
```

### `transition`
Controls the animation's timing and behavior, such as duration, easing, and delay.

```jsx
<motion.div transition={{ duration: 2, ease: "easeOut" }} />
```

## 3. Gesture Attributes

### `whileHover`
Defines animation properties to apply when the component is hovered.

```jsx
<motion.button whileHover={{ scale: 1.1 }} />
```

### `whileTap`
Specifies animation properties when the component is tapped or clicked.

```jsx
<motion.button whileTap={{ scale: 0.9 }} />
```

### `whileDrag`
Sets animation properties while the component is being dragged.

```jsx
<motion.div whileDrag={{ scale: 1.2 }} />
```

### `whileFocus`
Applies animation properties when the component is focused.

```jsx
<motion.input whileFocus={{ borderColor: "#f00" }} />
```

### `whileInView`
Animates the component when it enters the viewport.

```jsx
<motion.div whileInView={{ opacity: 1 }} initial={{ opacity: 0 }} />
```

## 4. Dragging Attributes

### `drag`
Enables dragging on the component. Can be set to `true`, `"x"`, or `"y"` to restrict the drag axis.

```jsx
<motion.div drag="x" />
```

### `dragConstraints`
Defines the boundaries within which the component can be dragged.

```jsx
<motion.div drag constraints={{ left: -100, right: 100, top: -50, bottom: 50 }} />
```

### `dragElastic`
Controls the elasticity of the drag constraints, determining how much the component can exceed its bounds.

```jsx
<motion.div dragElastic={0.2} />
```

### `dragTransition`
Specifies the transition properties for dragging animations.

```jsx
<motion.div dragTransition={{ bounceStiffness: 600, bounceDamping: 10 }} />
```

## 5. Layout Attributes

### `layout`
Enables automatic layout animations when the component's size or position changes.

```jsx
<motion.div layout />
```

### `layoutId`
Allows shared layout animations between components by assigning them the same `layoutId`.

```jsx
<motion.div layoutId="shared-element" />
```

## 6. Style Attributes

### `style`
Applies inline styles to the component, supporting both static values and animated `MotionValue`s.

```jsx
<motion.div style={{ x: 100, opacity: 0.5 }} />
```

## 7. Motion Values

### `useMotionValue`
Creates a `MotionValue` to track and animate numeric values.

```jsx
import { useMotionValue } from "framer-motion"

const x = useMotionValue(0)
```

### `useTransform`
Transforms one `MotionValue` into another, allowing for complex value mappings.

```jsx
import { useTransform } from "framer-motion"

const scale = useTransform(x, [0, 100], [1, 2])
```

## 8. Animation Controls

### `animate`
A key function to programmatically start animations.

```jsx
const controls = useAnimation()
controls.start({ opacity: 1 })
```

### `useAnimation`
Provides control over animations, allowing you to start, stop, or sequence them.

```jsx
import { useAnimation } from "framer-motion"

const controls = useAnimation()
controls.start({ x: 100 })
```

## 9. Advanced Attributes

### `custom`
Passes custom data to variants for dynamic animations.

```jsx
<motion.div custom={1} variants={variants} />
```

### `animatePresence`
A component that enables exit animations when components are removed from the React tree.

```jsx
import { AnimatePresence, motion } from "framer-motion"

<AnimatePresence>
  {isVisible && <motion.div exit={{ opacity: 0 }} />}
</AnimatePresence>
```

### `viewport`
Configures viewport-related settings for `whileInView` animations.

```jsx
<motion.div whileInView={{ opacity: 1 }} viewport={{ once: true }} />
```

### `onAnimationStart`
Callback fired when an animation starts.

```jsx
<motion.div onAnimationStart={() => console.log("Animation started")} />
```

### `onAnimationComplete`
Callback fired when an animation completes.

```jsx
<motion.div onAnimationComplete={() => console.log("Animation complete")} />
```

### `variants`
Defines multiple animation states for the component and its children.

```jsx
const variants = {
  hidden: { opacity: 0 },
  visible: { opacity: 1 },
}

<motion.div variants={variants} initial="hidden" animate="visible" />
```

### `exitBeforeEnter`
Ensures that exit animations complete before entering animations start, used with `AnimatePresence`.

```jsx
<AnimatePresence exitBeforeEnter>
  {isVisible && <motion.div exit={{ opacity: 0 }} />}
</AnimatePresence>
```

## 10. Transition Properties

### `type`
Defines the type of animation, such as `"spring"` or `"tween"`.

```jsx
<motion.div transition={{ type: "spring" }} />
```

### `duration`
Sets the duration of the animation in seconds.

```jsx
<motion.div transition={{ duration: 2 }} />
```

### `delay`
Introduces a delay before the animation starts.

```jsx
<motion.div transition={{ delay: 1 }} />
```

### `ease`
Specifies the easing function for the animation.

```jsx
<motion.div transition={{ ease: "easeOut" }} />
```

### `stiffness`
Controls the stiffness of a spring animation.

```jsx
<motion.div transition={{ type: "spring", stiffness: 300 }} />
```

### `damping`
Determines the damping of a spring animation, affecting its bounciness.

```jsx
<motion.div transition={{ type: "spring", damping: 20 }} />
```

### `mass`
Sets the mass of a spring animation, influencing its momentum.

```jsx
<motion.div transition={{ type: "spring", mass: 1 }} />
```

### `repeat`
Defines the number of times the animation should repeat.

```jsx
<motion.div transition={{ repeat: 2 }} />
```

### `repeatType`
Specifies how the animation repeats, such as `"loop"`, `"mirror"`, or `"reverse"`.

```jsx
<motion.div transition={{ repeatType: "mirror" }} />
```

### `repeatDelay`
Introduces a delay between animation repeats.

```jsx
<motion.div transition={{ repeat: 2, repeatDelay: 1 }} />
```

## 11. Accessibility Attributes

### `aria-*`
Standard ARIA attributes can be used to enhance accessibility alongside animations.

```jsx
<motion.button aria-label="Close" />
```

## 12. Event Handlers

### `onHoverStart` & `onHoverEnd`
Callbacks for hover events.

```jsx
<motion.div onHoverStart={() => console.log("Hovered")} onHoverEnd={() => console.log("Hover ended")} />
```

### `onTapStart` & `onTapEnd`
Callbacks for tap events.

```jsx
<motion.button onTapStart={() => console.log("Tapped")} onTapEnd={() => console.log("Tap ended")} />
```

## 13. Layout Calculation Attributes

### `layoutRoot`
Marks a component as the root for nested layout animations.

```jsx
<motion.div layoutRoot />
```

## 14. Advanced Hooks

### `useViewportScroll`
Tracks the scroll position of the viewport, useful for scroll-linked animations.

```jsx
import { useViewportScroll } from "framer-motion"

const { scrollY } = useViewportScroll()
```

### `useSpring`
Creates a spring-animated `MotionValue`.

```jsx
import { useSpring } from "framer-motion"

const springValue = useSpring(x, { stiffness: 300, damping: 30 })
```

### `useTime`
Provides a continuously updating `MotionValue` representing elapsed time.

```jsx
import { useTime } from "framer-motion"

const time = useTime()
```

### `useTransform`
Transforms one `MotionValue` into another based on a mapping function.

```jsx
import { useTransform } from "framer-motion"

const opacity = useTransform(x, [0, 100], [0, 1])
```

## 15. Custom Attributes

### `custom`
Passes custom data to variants for dynamic animations.

```jsx
<motion.div custom={customData} variants={variants} />
```

## 16. Animation Utilities

### `AnimatePresence`
Handles the presence of components for exit animations.

```jsx
import { AnimatePresence, motion } from "framer-motion"

<AnimatePresence>
  {isVisible && <motion.div exit={{ opacity: 0 }} />}
</AnimatePresence>
```

### `LazyMotion`
Optimizes bundle size by loading animations only when needed.

```jsx
import { LazyMotion, domAnimation } from "framer-motion"

<LazyMotion features={domAnimation}>
  <motion.div />
</LazyMotion>
```

## Conclusion

Framer Motion offers a rich set of attributes to create intricate and responsive animations in React applications. By understanding and effectively utilizing these attributes, you can enhance user interactions and overall UI/UX in your projects.

For more detailed information and advanced usage, refer to the [Framer Motion Documentation](https://www.framer.com/motion/).