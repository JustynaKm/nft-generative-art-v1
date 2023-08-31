from PIL import Image, ImageDraw
import os
import random
import argparse

def generate_monkey(color, output_dir, name):
    image_size = (128, 128)
    bg_color = (255, 255, 255)  # White background

    image = Image.new("RGB", image_size, bg_color)
    draw = ImageDraw.Draw(image)

    # Draw a simple circle to represent the monkey
    monkey_color = color
    monkey_radius = 40
    monkey_position = (image_size[0] // 2, image_size[1] // 2)
    draw.ellipse((monkey_position[0] - monkey_radius, monkey_position[1] - monkey_radius,
                  monkey_position[0] + monkey_radius, monkey_position[1] + monkey_radius), fill=monkey_color)

    image_path = os.path.join(output_dir, f"{name}.png")
    image.save(image_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", type=int, default=1, help="Number of images to generate.")
    parser.add_argument("--output_dir", type=str, default="output", help="Output directory for generated images.")

    args = parser.parse_args()
    n = args.n
    output_dir = args.output_dir

    os.makedirs(output_dir, exist_ok=True)

    for i in range(n):
        # Generate a random color for the monkey
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        generate_monkey(color, output_dir, f"monkey_{i}")
