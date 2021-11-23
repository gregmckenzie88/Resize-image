import cv2

def calculate_size(scale_percentage, width, height):
  # dimentions must be converted to integers
  # we cannot save fractional pixels
  new_width = int(width * scale_percentage / 100)
  new_height = int(height * scale_percentage / 100)
  # return dimentions in tuple
  return (new_width, new_height)

def resize(image_path, scale_percentage, resized_path):
  # create image object
  image = cv2.imread(image_path)
  # create new dimensions
  new_dimensions = calculate_size(scale_percentage, image.shape[1], image.shape[0])
  # store image object with new dimensions
  resized_image = cv2.resize(image, new_dimensions)
  # save image object to disk
  cv2.imwrite(resized_path, resized_image)

# call with initial image path, percentage scale of new image, and new image path
resize('galaxy.jpeg', 10, 'resized-galaxy.jpeg')
