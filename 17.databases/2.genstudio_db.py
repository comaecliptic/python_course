import sqlite3
import pandas as pd


conn = sqlite3.connect('genstudio.db')

conn.execute('''CREATE TABLE IF NOT EXISTS metadata (
    id INTEGER PRIMARY KEY,
    dna_chip_id TEXT,
    breed TEXT,
    sex TEXT
)''')

conn.execute('''CREATE TABLE IF NOT EXISTS alleles (
    snp_id INTEGER PRIMARY KEY,
    snp_name TEXT,
    snp_aux INTEGER,
    sample_id TEXT,
    snp TEXT,
    allele1_top TEXT,
    allele2_top TEXT,
    allele1_forward TEXT,
    allele2_forward TEXT,
    allele1_ab TEXT,
    allele2_ab TEXT,
    chr TEXT,
    pos INTEGER,
    gc_score REAL,
    gt_score REAL,
    theta REAL,
    r REAL,
    b_allele_freq REAL,
    log_r_ratio REAL,
    FOREIGN KEY (sample_id) REFERENCES metadata (dna_chip_id)
)''')

metadata = pd.read_csv('genotyping_data/metadata.csv', chunksize=4)
genstudio = pd.read_csv('genotyping_data/genstudio.csv', chunksize=4)

for chunk in metadata:
    query = 'INSERT INTO metadata (dna_chip_id, breed, sex) VALUES (?, ?, ?)'
    conn.executemany(query, chunk.iloc[:, 1:].values.tolist())

for chunk in genstudio:
    query = 'INSERT INTO alleles (snp_name, snp_aux, sample_id, snp, allele1_top,' \
            'allele2_top, allele1_forward, allele2_forward, allele1_ab, allele2_ab,' \
            'chr, pos, gc_score, gt_score, theta, r, b_allele_freq, log_r_ratio)' \
            'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    conn.executemany(query, chunk.drop(columns=['SNP Index']).iloc[:, 1:].values.tolist())

conn.commit()
conn.close()
