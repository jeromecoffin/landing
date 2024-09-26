import streamlit as st
import pandas as pd
import numpy as np

# Landing Page content
st.set_page_config(page_title="Jérôme Coffin - Tech & Fashion", layout="wide")

# Tailwind CSS Integration
tailwind_css = """
<style>
@import url('https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css');
[data-testid='stHeaderActionElements'] {display: none;}
</style>
"""
st.markdown(tailwind_css, unsafe_allow_html=True)

# Header Section
st.markdown("""
<div class="text-center bg-gray-900 py-12">
  <h1 class="text-5xl font-bold text-white mb-6">Jérôme Coffin</h1>
  <p class="text-xl text-white">The Well-Dressed Guy in the Datacenter</p>
</div>
            <br>
""", unsafe_allow_html=True)

st.markdown("""
<div class="text-center py-8">
  <h1 class="text-2xl font-bold mb-4">Empower Your Business with Custom Cloud Solutions</h1>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="text-center py-8">
  <p class="text-lg max-w-4xl mx-auto">I develop tailored tech solutions for businesses in any industry, delivering custom web apps, data visualization tools, and web scrapers that drive efficiency and insight for all types of stakeholders.
            <br/>I also share my passion for fashion on my <a href="https://www.instagram.com/gijon_coffin">public Instagram account</a>. Don't be surprised, I might be the only tech-guy with a tie.</p>
<h1 class="text-1xl font-bold mb-6"> Contact : jerome.devops@gmail.com</h1>
</div>
""", unsafe_allow_html=True)

# Projects Section

# Custom CSS for card styling
st.markdown("""
    <style>
    .card {
        background-color: #f9f9f9;
        padding: 20px;
        margin: 5px;
        border-radius: 10px;
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
        transition: 0.3s;
        height: 200px;
        text-align: center;
    }
    .card:hover {
        box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
    }
    .title {
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown(""" <div class="text-center py-8">
  <div class="max-w-7xl mx-auto px-4">
    <h2 class="text-3xl font-semibold text-center">My Projects</h2>
    <a href="https://github.com/jeromecoffin" class="text-indigo-600 hover:underline text-xl">Github for source code</a>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
  
  <!-- Project 1 -->
  <div class="bg-white shadow-lg rounded-lg p-6">
    <h3 class="text-xl font-semibold mb-4">Avanta-Sourcing : RFI Generator</h3>
    <p class="text-gray-600 mb-4">Automate and streamline the Request for Information process for sourcing agents.</p>
    <a href="https://www.avanta-sourcing.com" class="text-indigo-600 hover:underline">Learn More</a>
  </div>

  <!-- Project 2 -->
  <div class="bg-white shadow-lg rounded-lg p-6">
    <h3 class="text-xl font-semibold mb-4">Luxury Handbag Price Tracker</h3>
    <p class="text-gray-600 mb-4">A real-time price tracking tool for luxury handbags, designed for collectors and investors.</p>
    <a href="https://github.com/jeromecoffin/scraper" class="text-indigo-600 hover:underline">Learn More</a>
  </div>

  <!-- Project 3 -->
  <div class="bg-white shadow-lg rounded-lg p-6">
    <h3 class="text-xl font-semibold mb-4">Influencer Campaign Management</h3>
    <p class="text-gray-600 mb-4">An all-in-one platform for online brands to manage and optimize influencer marketing campaigns.</p>
    <a href="https://github.com/jeromecoffin/instafollower" class="text-indigo-600 hover:underline">Learn More</a>
  </div>

</div>
  </div>
            </div>""", unsafe_allow_html=True)


st.markdown(f"""<br>""", unsafe_allow_html=True)
st.divider()

# Medium Section
st.markdown("""
    <div class="text-center py-8">
  <div class="max-w-7xl mx-auto px-4">
    <h2 class="text-3xl font-semibold text-center">My Medium</h2>
    <a href="https://medium.com/@jerome.devops" class="text-indigo-600 hover:underline text-xl">@jerome.devops</a>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
  
  <!-- Medium 1 -->
  <div class="bg-white shadow-lg rounded-lg p-6">
    <h3 class="text-xl font-semibold mb-4">The end of docker-compose</h3>
    <p class="text-gray-600 mb-4">It turns out that this docker-compose is now obsolete in CLI V2.</p>
    <a href="https://medium.com/@jerome.devops/the-end-of-docker-compose-e3b7d15330e2" class="text-indigo-600 hover:underline">Learn More</a>
  </div>

  <!-- Medium 2 -->
  <div class="bg-white shadow-lg rounded-lg p-6">
    <h3 class="text-xl font-semibold mb-4">Streamlit on HTTPS</h3>
    <p class="text-gray-600 mb-4">Here is a quick, up-to-date explanation of how to set up Streamlit on HTTPS behind Nginx.</p>
    <a href="https://medium.com/@jerome.devops/finally-streamlit-on-https-for-beginners-4543d7793005" class="text-indigo-600 hover:underline">Learn More</a>
  </div>

  <!-- Medium 3 -->
  <div class="bg-white shadow-lg rounded-lg p-6">
    <h3 class="text-xl font-semibold mb-4">Dirty Coffee in Chiang Mai</h3>
    <p class="text-gray-600 mb-4">My recent stay in Chiang Mai, surprised me with some of the best Arabica beans I’ve ever tasted.</p>
    <a href="https://medium.com/@jerome.devops/dirty-coffee-in-chiang-mai-363b7211952d" class="text-indigo-600 hover:underline">Learn More</a>
  </div>

</div>
  </div>
            </div>
""", unsafe_allow_html=True)

st.divider()

# Instagram Section
st.markdown("""
<div class="text-center py-12">
  <h2 class="text-3xl font-semibold mb-6">My Fashion Journey</h2>
  <p class="text-lg max-w-2xl mx-auto mb-6">Follow me on Instagram for daily outfit inspiration, tips on fashion, and insights into the world of menswear.</p>
  <a href="https://www.instagram.com/gijon_coffin" target="_blank" class="text-indigo-600 hover:underline text-xl">Visit my Instagram</a>
</div>
""", unsafe_allow_html=True)

# Made-up data
df = pd.DataFrame(
    {
        "date": [
            "2021",
            "2022",
            "2023",
            "2024",
        ],
        "Followers": [100, 500, 1000, 1500],
        "Posts": [10, 100, 150, 300],
        "Engagement": [50, 500, 1000, 1500],
        "Reach": [60, 500, 1000, 1500],
    }
)


cols = df.columns.tolist()
cols.remove("date")

choice = st.multiselect("Choose Data type", cols, default="Followers")

datas = df[choice + ["date"]]
st.line_chart(datas, x="date", y=choice)


#Brands Section
st.markdown("""
<div class="text-center py-8">
<h1 class="text-1xl font-bold mb-6"> In collaboration with French Sustainable Brands.</h1>
            </div>
""", unsafe_allow_html=True)

brands = ["Monsieur Mimosa", "Atelier Particulier", "Les Tricots Marcel", "Placide", "L'Habit Français", "Pétrone", "Vestibus", "Mèo Tôm Handmade (Vietnam)", "Marins Barbier"]

col1, col2, col3 = st.columns(3)
idx=1

for brand in brands:
  if idx == 1:
    tile = col1.container(height=500)
    idx = 2
  elif  idx == 2:
    tile = col2.container(height=500)
    idx = 3
  else:
    tile = col3.container(height=500)
    idx = 1
  tile.title(brand)
  imagepath = "images/{}.png".format(brand)

  try:
     tile.image(imagepath, caption="@gijon_coffin")
  except Exception as e:
    st.error(f"Error loading image {imagepath}: {e}")

# Footer Section
st.markdown("""
<div class="text-center bg-gray-900 text-white py-6">
  <p>&copy; 2024 Jérôme Coffin. All Rights Reserved.</p>
</div>
""", unsafe_allow_html=True)
