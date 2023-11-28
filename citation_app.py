import dhlab as dh
import streamlit as st
import pandas as pd
import citation_finder as cf

st. set_page_config(layout="wide")

subject=st.text_input('Søk på temaord', 'Søk', help='Skriv ønsket søkeord for tema. Du kan bruke * som wildcard før eller etter søkeordet, f.eks. "språk*"')
st.write(subject)

korpus = dh.Corpus(doctype='digibok', limit=500, subject=subject)

df = cf.citation_finder(korpus, get_concs=True)
"Citations output"
st.dataframe(df)

df.columns = ["urn","citation"]
res = df.merge(korpus.frame, left_on='urn', right_on='urn')['urn title author year citation'.split()]

"Corpus + citations"

st.dataframe(res)

