# Test manuale per verificare possibili errori con oggetti simili a canne da pesca

from ultralytics import YOLO


model = YOLO('best_cls.pt')

image_path = 'pics/test4.jpg'

results = model(image_path, conf=0.33)
results[0].show()  # mostra l'immagine con classification
