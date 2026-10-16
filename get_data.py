from tdc.single_pred import ADME
data = ADME(name = 'BBB_Martins')
split = data.get_split(method = 'scaffold', seed = 42, frac = [0.8, 0.1, 0.1])
for name in ['train', 'valid', 'test']:
    df = split[name][['Drug', 'Y']].rename(columns = {'Drug': 'smiles', 'Y': 'bbb'})
    df.to_csv(f'data/{name}.csv', index = False)
    print(name, len(df), 'fraction crossing BBB:', round(df['bbb'].mean(), 2))
