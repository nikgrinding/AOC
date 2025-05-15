## Part 1

Santa is wrapping presents and needs to calculate how much wrapping paper and ribbon to buy.

Each present is a box with dimensions in the format `LxWxH` (length × width × height).

For each box, the required **wrapping paper** is:

- Surface area: `2*l*w + 2*w*h + 2*h*l`
- Plus **extra paper** equal to the area of the **smallest side**

**Examples:**

- Input: `2x3x4` → Output: `58`
- Input: `1x1x10` → Output: `43`

### Idea

We can calaculate the surface area of each side individually. Calculate the output by summing all the areas plus the minimum area of all the sides.

## Part 2

Now we calculate how much **ribbon** is needed for each box.

- The ribbon needed to wrap a box is the **smallest perimeter** of any one face
- Plus ribbon for the **bow**, which is equal to the **volume**: `l * w * h`

**Examples:**

- Input: `2x3x4` → Output: `34`
- Input: `1x1x10` → Output: `14`

### Idea

We can calaculate the perimeters of each side individually. Calculate the output by finding the volume of the box plus the minimum perimeter of all the sides.