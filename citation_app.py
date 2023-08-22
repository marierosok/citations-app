import dhlab as dh
import streamlit as st
import pandas as pd
import citation_finder as cf

st. set_page_config(layout="wide")

subject=st.text_input('Angi et temaord', 'film*', help='No va du flink')
st.write(subject)

korpus = dh.Corpus(doctype='digibok', limit=10, subject=subject)

df = cf.citation_finder(korpus)
df.columns = ["urn","citation"]
res = df.merge(korpus.frame, left_on='urn', right_on='urn')['urn title authors year citation'.split()]


st.dataframe(res)

