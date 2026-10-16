# Predicting Blood-Brain Barrier Penetration: GNN vs. Fingerprint Baseline

Binary classification of whether a molecule crosses the blood-brain barrier (BBB), comparing a graph neural network (Chemprop) against a random forest on Morgan fingerprints.

## Data

- **Dataset:** BBB_Martins from Therapeutics Data Commons (2,030 molecules, label 1 = crosses BBB)
- **Split:** scaffold split (80/10/10, seed 42), so test molecules come from core structures not seen in training
- **Sizes:** 1,624 train / 203 validation / 203 test

## Models

| Model | Details |
|---|---|
| Chemprop GNN | Chemprop 2.3.1, default settings, 30 epochs, best checkpoint chosen on validation loss |
| Random forest | scikit-learn, 500 trees, Morgan fingerprints (radius 2, 2048 bits) |

## Results (test set, AUROC)

| Model | AUROC |
|---|---|
| Chemprop GNN | 0.898 |
| Random forest | 0.922 |

## Takeaways

- Both models rank BBB-crossing molecules well on unseen scaffolds.
- The random forest scored slightly higher. With only about 1,600 training molecules and an untuned GNN, this is plausible: fingerprint models are strong on small molecular datasets.
- The test set has only 203 molecules and I used a single split, so the 0.024 gap is not strong evidence that one model is better. Repeating with multiple seeds would show how stable it is.

## Reproduce

```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python get_data.py
chemprop train --data-path data/train.csv data/valid.csv data/test.csv --smiles-columns smiles --target-columns bbb --task-type classification --epochs 30 --output-dir results/gnn
python baseline.py
```

The GNN's test AUROC is printed at the end of training (`test/roc`).

## Files

- `get_data.py`: downloads BBB_Martins and writes the scaffold-split CSVs
- `baseline.py`: random forest on Morgan fingerprints
- `data/`: train, validation, and test CSVs
- `results/`: Chemprop training output

## Next steps

- Repeat with several split seeds and report mean and spread
- Train the GNN longer and add RDKit descriptors
- Compare against a random split