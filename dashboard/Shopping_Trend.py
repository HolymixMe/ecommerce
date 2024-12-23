import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import seaborn as sns

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('https://raw.githubusercontent.com/HolymixMe/shopping_trends/main/shopping_trends.csv')
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
    ax.set_xticks(rotation=90)
    st.pyplot(fig)
def plot_size(df):
    size_counts = df['Size'].value_counts()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=size_counts.index, y=size_counts.values, palette='mako')   
    ax.set_xlabel('Ukuran Produk')
    ax.set_ylabel('Jumlah')
    ax.set_xticks(rotation=90)
    st.pyplot(fig)
def plot_color(df):
    color_distribute = df['Color'].value_counts()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=color_distribute.index, y=color_distribute.values, palette='mako')   
    ax.set_xlabel('Ukuran Produk')
    ax.set_ylabel('Jumlah')
    ax.set_xticks(rotation=90)
    st.pyplot(fig)
    
# Visualisasi Pembayaran
def payment_method(df):
    payment_method_distribute = df['Payment Method'].value_counts()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=payment_method_distribute.index, y=payment_method_distribute.values, palette='mako')   
    ax.set_xlabel('Metode Pembayaran')
    ax.set_ylabel('Jumlah')
    st.pyplot(fig)
def shipping_type(df):
    shipping_type_distribute = df['Shipping Type'].value_counts()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=shipping_type_distribute.index, y=shipping_type_distribute.values, palette='mako')   
    ax.set_xlabel('Metode Pembayaran')
    ax.set_ylabel('Jumlah')
    st.pyplot(fig)

def prediction(df):
    label_encoder = LabelEncoder()
    df['Category'] = label_encoder.fit_transform(df['Category'])
    df['Location'] = label_encoder.fit_transform(df['Location'])

    # Fitur dan Target
    X = df[['Age', 'Category', 'Location', 'Discount Applied', 'Promo Code Used']]
    y = df['Purchase Amount (USD)']

    # Membagi data menjadi data latih dan data uji
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Membuat model Random Forest Regressor
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Prediksi pada data uji
    y_pred = model.predict(X_test)

    # Evaluasi model
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # Menampilkan hasil evaluasi
    st.write(f"Mean Absolute Error (MAE): {mae}")
    st.write(f"Mean Squared Error (MSE): {mse}")
    st.write(f"R-squared (R²): {r2}")

    # Visualisasi hasil prediksi vs nilai aktual
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=y_test, y=y_pred)
    plt.xlabel('Actual Purchase Amount (USD)')
    plt.ylabel('Predicted Purchase Amount (USD)')
    plt.title('Actual vs Predicted Purchase Amount')
    plt.show()

    # Menampilkan plot di Streamlit
    st.pyplot(plt)


# Main function
def main():
    st.title("Shopping Trend Analysis")
    st.write("by Muhammad Fahmi Hussain")
    
    # Load data
    df = load_data()
    
    # Pilihan filter
    options = ['Customer', 'Produk', 'Pembayaran', 'Prediksi']
    choice = st.sidebar.selectbox("Pilih Visualisasi", options)
    
    # Filter for order status
    location_options = df['Location'].unique()
    selected_location = st.sidebar.multiselect('Lokasi yang dipilih', location_options, default=location_options)

    # Filter the dataframe based on selected order status
    filtered_df = df[df['Location'].isin(selected_location)]
    
    # Menampilkan visualisasi berdasarkan pilihan filter
    if choice == 'Persebaran Pembeli':
        plot_gender_customer(filtered_df)
        plot_age_customer(filtered_df)
    elif choice == 'Waktu Pengiriman vs Review Score':
        plot_category(filtered_df)
        plot_color(filtered_df)
        plot_size(filtered_df)
    elif choice == 'Angsuran Customer':
        payment_method(filtered_df)
        shipping_type(filtered_df)
    elif choice == 'Prediksi':
        prediction(df)
# Panggil fungsi utama
if __name__ == '__main__':
    main()

