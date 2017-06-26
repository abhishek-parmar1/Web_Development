from steganography.steganography import Steganography
Steganography.encode('/home/rajat/Desktop.professional_photo.jpg','secret_image.jpg', 'Abhishek is awsome')
secret_text = Steganography.dencode('secret_image.jpg')
print secret_text