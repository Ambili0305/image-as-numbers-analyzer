import cv2
import matplotlib.pyplot as plt

# Load image
img = cv2.imread("images/sample_image.jpg")

# Print shape
print("Image Shape (Height, Width, Channels):", img.shape)

# Print total pixels
print("Total Pixel Values:", img.size)

# Print datatype
print("Data Type:", img.dtype)

# Pixel at top-left
print("Pixel at (0,0):", img[0, 0])

# Split channels
b, g, r = cv2.split(img)

print("Blue channel shape:", b.shape)
print("Green channel shape:", g.shape)
print("Red channel shape:", r.shape)

# Show original image
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10, 4))

plt.subplot(1, 4, 1)
plt.imshow(img_rgb)
plt.title("Original")
plt.axis("off")

plt.subplot(1, 4, 2)
plt.imshow(r, cmap="Reds")
plt.title("Red")
plt.axis("off")

plt.subplot(1, 4, 3)
plt.imshow(g, cmap="Greens")
plt.title("Green")
plt.axis("off")

plt.subplot(1, 4, 4)
plt.imshow(b, cmap="Blues")
plt.title("Blue")
plt.axis("off")

plt.tight_layout()
plt.show()