# 24accuracy.py by Mohammed

def f1_score(tp, fp, tn, fn):
"""
The function will calculate the F1 score 
tp = true posotive
fp = false posotive
tn = true negative
fn = false negative
"""
    if tp == 0: # Checks if the numerator is 0
        return 0
    precision = tp / (tp + fp)
    recall = tp / (tp + fn) 
    f1 = 2 * (precision * recall) / (precision + recall)
    return f1

print(f1_score(40, 10, 30, 20))
print(f1_score(50, 0, 30, 20))
print(f1_score(0, 32, 30, 20))
