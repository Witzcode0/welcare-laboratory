import tensorflow as tf
import cv2

# Load the DeepLabV3+ model
model = tf.keras.applications.DeepLabV3Plus(weights='pascal_voc', input_shape=(None, None, 3))

# Load and preprocess the input image
input_image_path = 'doctor.jpg'
image = cv2.imread(input_image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = tf.image.resize(image, (512, 512))  # Resize to match model input size
image = tf.keras.applications.deeplab_v3.preprocess_input(image)

# Perform segmentation
segmentation = model.predict(np.expand_dims(image, 0))
mask = segmentation[0].argmax(axis=-1)

# Create a mask for the person (class 15 in Pascal VOC dataset)
person_mask = (mask == 15).astype(np.uint8) * 255

# Bitwise-AND to isolate the person
isolated_person = cv2.bitwise_and(image, image, mask=person_mask)

# Save the isolated person
output_image_path = 'isolated_person.png'
cv2.imwrite(output_image_path, cv2.cvtColor(isolated_person, cv2.COLOR_RGB2BGR))
print("Isolated person saved successfully.")
