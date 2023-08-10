import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title('Fashion Trends Dashboard')
st.markdown('This dashboard can be used to view fashion trends and product information from ssense')
st.divider()

# Set dropdowns for product type and designer
product_option = st.sidebar.selectbox('Choose Product Type', ('Jeans', 'Shirts'))
designer_option = st.sidebar.selectbox('Choose Designer', ('Blumarine', 'Diesel', 'MM6'))

jeans_df = pd.read_csv("../jeans.csv")
mean_blumarine_jeans = jeans_df['blumarine'].mean()
mean_diesel_jeans = jeans_df['diesel'].mean()
mean_mm6_jeans = jeans_df['MM6'].mean()


mean_price_jeans = [{'Blumarine':mean_blumarine_jeans},{'Diesel':mean_diesel_jeans},{'MM6':mean_mm6_jeans}]



# Create bar chart for t-shirts

shirts_df = pd.read_csv("../tshirts.csv")
mean_blumarine_shirts = shirts_df['blumarine'].mean()
mean_diesel_shirts = shirts_df['diesel'].mean()
mean_mm6_shirts = shirts_df['MM6'].mean()

mean_shirt_prices = [{'Blumarine':mean_blumarine_shirts},{'Diesel':mean_diesel_shirts},{'MM6':mean_mm6_shirts}]



#maxmin_mm6_df = pd.read_csv("../max_and_min_mm6.csv")
max_blumarine_jeans = jeans_df['blumarine'].max()
max_diesel_jeans = jeans_df['diesel'].max()
max_mm6_jeans = jeans_df['MM6'].max()
min_blumarine_jeans = jeans_df['blumarine'].min()
min_diesel_jeans = jeans_df['diesel'].min()
min_mm6_jeans = jeans_df['MM6'].min()
maxmin_jeans = [{'Blumarine Max Price':max_blumarine_jeans}, {'Blumarine Min Price':min_blumarine_jeans},{'Diesel Max Price': max_diesel_jeans}, {'Diesel Min Price': min_diesel_jeans},{'MM6 Max Price':max_mm6_jeans}, {'MM6 Min Price':min_diesel_jeans}]


max_blumarine_shirts = shirts_df['blumarine'].max()
max_diesel_shirts = shirts_df['diesel'].max()
max_mm6_shirts = shirts_df['MM6'].max()
min_blumarine_shirts = shirts_df['blumarine'].min()
min_diesel_shirts = shirts_df['diesel'].min()
min_mm6_shirts = shirts_df['MM6'].min()
maxmin_shirts = [{'Blumarine Max Price':max_blumarine_shirts}, {'Blumarine Min Price':min_blumarine_shirts},{'Diesel Max Price': max_diesel_shirts}, {'Diesel Min Price': min_diesel_shirts},{'MM6 Max Price':max_mm6_shirts}, {'MM6 Min Price':min_diesel_shirts}]


mm6_global_trends_df = pd.read_csv("../mm6_global_trends.csv")
mm6_us_trends_df = pd.read_csv("../mm6_us_trends.csv")
blumarine_global_trends_df = pd.read_csv("../blumarine_global_trends.csv")
blumarine_us_trends_df = pd.read_csv("../blumarine_us_trends.csv")
diesel_global_trends_df = pd.read_csv("../diesel_global_trends.csv")
diesel_us_trends_df = pd.read_csv("../diesel_us_trends.csv")

#designer_global_trends_df = pd.read_csv("../designer_global_trends_data.csv")

# Plotly chart
designers = ['Blumarine','Diesel','MM6']
#fig = go.Figure(data_jeans = [
    #go.Bar(name='Max Price',x=designers,y=[max_blumarine_jeans,max_diesel_jeans,max_mm6_jeans]),
    #go.Bar(name='Min Price',x=designers,y = [min_blumarine_jeans,min_diesel_jeans,min_mm6_jeans])
#])
#fig.update_layout(barmode='group')
#st.plotly_chart(fig,theme="streamlit",use_container_width=True)

# Javascript Library
#st.components.v1.html(""")


st.text("Global Search Trends per Country - Last 12 months")

if designer_option == 'Blumarine':
    st.bar_chart(blumarine_global_trends_df, x='Country')
    st.text("United States Search Trends per State - Last 12 months")
    st.bar_chart(blumarine_us_trends_df, x='Region')
elif designer_option== 'Diesel':
    st.bar_chart(diesel_global_trends_df, x='Country')
    st.text("United States Search Trends per State - Last 12 months")
    st.bar_chart(diesel_us_trends_df, x='Region')
elif designer_option == 'MM6':
    st.bar_chart(mm6_global_trends_df, x='Country')
    st.text("United States Search Trends per State - Last 12 months")
    st.bar_chart(mm6_us_trends_df, x='Region')


st.text("Product Price comparisons per Designer")

if product_option == 'Jeans':
    st.bar_chart(mean_price_jeans)
    st.bar_chart(maxmin_jeans)



elif product_option == 'Shirts':
    st.bar_chart(mean_shirt_prices)
    st.bar_chart(maxmin_shirts)