import pandas as pd
import matplotlib.pyplot as plt


def fill_missing_nuleotide(row):
    nucl_values = row[['A', 'C', 'T', 'G']]
    missing_nucl = nucl_values.index[nucl_values.isnull()]
    row[missing_nucl] = row.reads_all - nucl_values.sum()
    return row


nucl_table = pd.read_csv('train.csv')
nucl_table = nucl_table.apply(fill_missing_nuleotide, axis=1)
nucl_table = nucl_table.astype({'pos': 'int64'})
nucl_table = nucl_table.set_index('pos')
nucl_table[['A', 'T', 'G', 'C']].plot.bar(
    stacked=True,
    title='Nucleotide distribution'
)
plt.xlabel('Position')
plt.ylabel('Quantity')
plt.show()
