
from ultralytics import YOLO

model = YOLO('best_cls.pt')


results = model.val(
    data='classification_mix',
    split='test'
)
print(f"Test Accuracy: {results.top1:.2%}")


