import numpy as np
import pandas as pd
from rdkit import Chem
from rdkit.Chem import rdFingerprintGenerator
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score

gen = rdFingerprintGenerator.GetMorganGenerator(radius=2, fpSize=2048)

def fingerprint(smiles):
    return gen.GetFingerprintAsNumPy(Chem.MolFromSmiles(smiles))

train = pd.read_csv("data/train.csv")
test = pd.read_csv("data/test.csv")

X_train = np.array([fingerprint(s) for s in train['smiles']])
X_test = np.array([fingerprint(s) for s in test['smiles']])

model = RandomForestClassifier(n_estimators=500, random_state=42)
model.fit(X_train, train['bbb'])

auroc = roc_auc_score(test['bbb'], model.predict_proba(X_test)[:, 1])

print('Random forest test AUROOC:', round(auroc, 3))
