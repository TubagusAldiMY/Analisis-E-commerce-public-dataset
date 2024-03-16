import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# Load DataFrames
customers_df = pd.read_csv('customers.csv')
payments_reviews_df = pd.read_csv('payments_reviews.csv')

# Menampilkan judul
st.title('Dashboard E-commerce')

# Visualisasi Tipe Pembayaran
st.subheader('Tipe Pembayaran yang Sering Digunakan')
# Jumlah Order per Tipe Pembayaran
fig_payment_type, ax_payment_type = plt.subplots(figsize=(10, 6))
sns.barplot(x=customers_df['payment_type'].value_counts().index, y=customers_df['payment_type'].value_counts().values, ax=ax_payment_type)
ax_payment_type.set_title('Jumlah Order per Tipe Pembayaran')
ax_payment_type.set_xlabel('Tipe Pembayaran')
ax_payment_type.set_ylabel('Jumlah Order')

# Menampilkan di Streamlit
st.pyplot(fig_payment_type)


st.subheader('Penjualan berbeda di Berbagai Lokasi Geografis')
# Top 10 Kota dengan Jumlah Pelanggan Terbanyak
fig1, ax1 = plt.subplots(figsize=(15, 6))
sns.barplot(x=customers_df['customer_city'].value_counts().index[:10], y=customers_df['customer_city'].value_counts().values[:10], ax=ax1)
ax1.set_title('Top 10 Kota dengan Jumlah Pelanggan Terbanyak')
ax1.set_xlabel('Kota')
ax1.set_ylabel('Jumlah Pelanggan')
ax1.tick_params(axis='x', rotation=45)
st.pyplot(fig1)

# Jumlah Pelanggan per Negara Bagian
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(x=customers_df['customer_state'].value_counts().index, y=customers_df['customer_state'].value_counts().values, ax=ax2)
ax2.set_title('Jumlah Pelanggan per Negara Bagian')
ax2.set_xlabel('Negara Bagian')
ax2.set_ylabel('Jumlah Pelanggan')
st.pyplot(fig2)