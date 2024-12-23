import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('./dashboard/shopping_trends.csv')
    return df

# Visualisasi Pembeli
def plot_gender_customer(df):
    gender_counts = df['Gender'].value_counts()
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90, colors=['#ff9999', '#66b3ff'])
    ax.set_title('Distribusi Gender Pelanggan')
    st.pyplot(fig)

def plot_age_customer(df):
    age_counts = df['Age'].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x=age_counts.index, y=age_counts.values, ax=ax, marker='o', color='b')
    ax.set_title('Distribusi Usia Pelanggan')
    ax.set_xlabel('Usia')
    ax.set_ylabel('Jumlah Pelanggan')
    st.pyplot(fig)

# Visualisasi Barang
def plot_category(df):
    category_counts = df['Category'].value_counts()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=category_counts.index, y=category_counts.values, palette='mako')   
    ax.set_xlabel('Kategori Barang')
    ax.set_ylabel('Jumlah')
    ax.set_title('Distribusi Kategori Barang')
    st.pyplot(fig)
def plot_size(df):
    size_counts = df['Size'].value_counts()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=size_counts.index, y=size_counts.values, palette='mako')   
    ax.set_xlabel('Ukuran Produk')
    ax.set_ylabel('Jumlah')
    ax.set_title('Distribusi Ukuran Produk')
    st.pyplot(fig)
def plot_color(df):
    color_distribute = df['Color'].value_counts()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=color_distribute.index, y=color_distribute.values, palette='mako')   
    ax.set_xlabel('Warna Produk')
    ax.set_ylabel('Jumlah')
    ax.set_xticklabels(rotation=90)
    ax.set_title('Distribusi Warna Produk')
    st.pyplot(fig)
    
# Visualisasi Pembayaran
def payment_method(df):
    payment_method_distribute = df['Payment Method'].value_counts()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=payment_method_distribute.index, y=payment_method_distribute.values, palette='mako')   
    ax.set_xlabel('Metode Pembayaran')
    ax.set_ylabel('Jumlah')
    ax.set_title('Distribusi Metode Pembayaran')
    st.pyplot(fig)
def shipping_type(df):
    shipping_type_distribute = df['Shipping Type'].value_counts()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=shipping_type_distribute.index, y=shipping_type_distribute.values, palette='mako')   
    ax.set_xlabel('Metode Pengiriman')
    ax.set_ylabel('Jumlah')
    ax.set_title('Distribusi Metode Pengiriman)
    st.pyplot(fig)

# Main function
def main():
    st.title("Shopping Trend Analysis")
    st.write("by Muhammad Fahmi Hussain")
    
    # Load data
    df = load_data()
    
    # Pilihan filter
    options = ['Customer', 'Produk', 'Pembayaran dan Pengiriman']
    choice = st.sidebar.selectbox("Pilih Visualisasi", options)
    
    # Filter for order status
    # Daftar lokasi unik
    locations = df['Location'].unique().tolist()

    # Checkbox untuk "Pilih Semua"
    select_all = st.sidebar.checkbox("Pilih Semua", value=True)

    # Membuat checklist untuk tiap lokasi
    selected_locations = []
    st.sidebar.write("Pilih Lokasi:")
    for location in locations:
        if select_all:
            # Jika "Pilih Semua" dipilih, semua checkbox otomatis aktif
            st.sidebar.checkbox(location, value=True, key=location)
            selected_locations.append(location)
        else:
            # Jika "Pilih Semua" tidak dipilih, user memilih lokasi satu per satu
            if st.sidebar.checkbox(location, key=location):
            selected_locations.append(location)

    # Filter DataFrame berdasarkan lokasi yang dipilih
    filtered_data = df[df['Location'].isin(selected_locations)]
    
    # Menampilkan visualisasi berdasarkan pilihan filter
    if choice == 'Customer':
        plot_gender_customer(filtered_df)
        plot_age_customer(filtered_df)
    elif choice == 'Produk':
        plot_category(filtered_df)
        plot_color(filtered_df)
        plot_size(filtered_df)
    elif choice == 'Pembayaran dan Pengiriman':
        payment_method(filtered_df)
        shipping_type(filtered_df)
   
# Panggil fungsi utama
if __name__ == '__main__':
    main()

