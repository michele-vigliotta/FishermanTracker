# Valutazione del modello di classificazione YOLOv11 addestrato con il file best_cls.pt (ootenuto da tunig auto)
# sul set di test classification_mix


from ultralytics import YOLO

model = YOLO('best_cls.pt')


results = model.val(
    data='classification_mix',
    split='test'
)
print(f"Test Accuracy: {results.top1:.2%}")


