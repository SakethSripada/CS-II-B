from PIL import Image, ImageFilter, ImageEnhance

image = Image.open('sunflower.jpg')

# blurs the image
blurred_image = image.filter(ImageFilter.BLUR)
blurred_image.save('sunflower_blurred.jpg')

# create contour of image
contoured_image = image.filter(ImageFilter.CONTOUR)
contoured_image.save('sunflower_contoured.jpg')

# enhance edges of image
edge_enhanced_image = image.filter(ImageFilter.EDGE_ENHANCE)
edge_enhanced_image.save('sunflower_edge_enhanced.jpg')

enhancer = ImageEnhance.Brightness(image)
brightened_image = enhancer.enhance(1.5)
brightened_image.save('sunflower_brightened.jpg')
