from ultralytics import YOLO


model = YOLO("best_config3_lrbasso.pt")


metrics = model.val(data="detection_mix/detect.yaml", split="test")


print("\n=== RISULTATI SUL TEST SET ===")
print(f"mAP50: {metrics.box.map50():.4f}")
print(f"mAP50-95: {metrics.box.map():.4f}")
print(f"Precision (media): {metrics.box.mp():.4f}")
print(f"Recall (media): {metrics.box.mr():.4f}")



