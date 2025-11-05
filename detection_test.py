# Valutazione del modello di detection YOLOv11 addestrato con configurazione scelta dal tuning automatico

from ultralytics import YOLO


model = YOLO("best_detection.pt")


metrics = model.val(data="detection_mix/detect.yaml", split="test")

print("\n=== RISULTATI SUL TEST SET ===")
print(f"mAP50: {metrics.box.map50:.4f}")
print(f"mAP50-95: {metrics.box.map:.4f}")
print(f"Precision: {metrics.box.precision:.4f}")
print(f"Recall: {metrics.box.recall:.4f}")

