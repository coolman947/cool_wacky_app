import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Wacky Cursor and Spinning Model')

# Specify the path to the uploads folder
upload_folder = 'uploads'
cursor_image_path = os.path.join(upload_folder, 'your_cursor_image.png')  # Default image

# Load a default cursor image (optional)
cursor_image = pygame.image.load(cursor_image_path)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Clear the window
    window.fill((255, 255, 255))

    # Draw the cursor image at the mouse position
    window.blit(cursor_image, (mouse_x, mouse_y))

    # Update the display
    pygame.display.update()

