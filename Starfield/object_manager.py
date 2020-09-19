import star

# All of the objects
objects = []

# Instantiate a new star manager
objects.append(star.Star_Manager())

# Update function
def update_objects():
    for obj in objects:
        obj.step()