import pandas as pd


nucl_table = pd.read_csv('train.csv')
matches_mean = nucl_table.matches.mean()
part_table = nucl_table.query('matches > @matches_mean')[['pos', 'reads_all',  'mismatches', 'deletions', 'insertions']]
part_table.to_csv('train_part.csv')
