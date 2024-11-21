import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.title('Analiza półmaratonu') 
df = pd.read_csv("halfmarathon_wroclaw_2024__final.csv", sep=";")

#Liczba zawodników
c0, c1, c2 = st.columns(3)

with c0:
    st.metric("Liczba zawodników", len(df))

#Liczba mężczyzn
with c1:
    st.metric("Liczba mężczyzn", len(df[df["Płeć"] == "M"]))

with c2:
    st.metric("Liczba kobiet", len(df[df["Płeć"] == "K"]))

#10 losowych wierszy
st.header("10 losowych wierszy")
st.dataframe(
    df.sample(10),
    hide_index=True,
    use_container_width=True
)

#Top 5 zawodników
st.header("Top 5 zawodników")
top_colums = ["Miejsce", "Numer startowy", "Imię", "Nazwisko", "Miasto"]
st.dataframe(
    df.sort_values("Miejsce")[top_colums].head(5),
    hide_index=True
)

#Barplot krajów
st.header("Pochodzenie zawodników")
gdf = df.groupby("Kraj", as_index=False).count().rename(columns={"Miejsce": "Liczba zawodników"})
st.bar_chart(gdf, x="Kraj", y="Liczba zawodników")

#Histogram
st.header("Histogram czasu na mecie")
df["Czas"] = pd.to_datetime(df["Czas"], format='%H:$M:$S', errors='coerce').dt.time

#Tworzenie hostogramyu

plt.figure(figsize=(10,6))
plot = sns.histplot(df["Czas"])
st.pyplot(plot.figure)

#Macierz
st.header("Macierz korelacji")
correlation_matrix = df.corr(numeric_only=True)
plt.figure(figsize=(16,12))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
st.pyplot(plt.gcf())