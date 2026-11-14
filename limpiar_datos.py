import pandas as pd

d = pd.read_csv('Transmex_student_extract.csv', dtype=str, keep_default_na=False)
n0 = len(d)
ini = pd.to_datetime(d.DISPATCH_START_DATE, errors='coerce')
fin = pd.to_datetime(d.DISPATCH_END_DATE, errors='coerce')

m_fin_nulo = fin.isna()
m_fin_ant = fin < ini
m_term = d.TRUCK_TERMINAL.str.strip() == ''
m_lob = d.LINE_OF_BUSINESS.str.strip() == ''
malo = m_fin_nulo | m_fin_ant | m_term | m_lob

print(f'Filas originales: {n0}')
print(f'Fin nulo: {m_fin_nulo.sum()} | Fin < inicio: {m_fin_ant.sum()} | '
      f'Terminal nula: {m_term.sum()} | LOB nula: {m_lob.sum()}')
d[~malo].to_csv('Transmex_limpio.csv', index=False)
print(f'Eliminadas (union): {malo.sum()} | Restantes: {(~malo).sum()}')
