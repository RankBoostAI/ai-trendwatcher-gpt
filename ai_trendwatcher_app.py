
import streamlit as st
import pandas as pd

# Simulatie van trending content data
trending_data = [
    {"Platform": "TikTok", "Trend": "NPC Streaming", "Hashtags": "#npc #ai #funny", "Engagement Score": 95, 
     "AI Content Idea": "Maak een TikTok-video waarin je een NPC-karakter speelt en op hilarische wijze reageert op kijkers."},
    {"Platform": "TikTok", "Trend": "AI Voice Filters", "Hashtags": "#ai #voicefilter #viral", "Engagement Score": 87, 
     "AI Content Idea": "Gebruik AI-stemfilters om beroemde stemmen na te doen en creëer een humoristische dialoog."},
    {"Platform": "Instagram", "Trend": "Streetwear Aesthetic", "Hashtags": "#fashion #streetwear #ootd", "Engagement Score": 90, 
     "AI Content Idea": "Maak een montage-video waarin je verschillende streetwear-looks probeert en je favoriete outfits beoordeelt."},
    {"Platform": "Instagram", "Trend": "Minimalist Home Setup", "Hashtags": "#minimalism #interiordesign #cozy", "Engagement Score": 85, 
     "AI Content Idea": "Film een ‘before and after’ van je kamertransformatie met een minimalistisch design."},
]

# Omzetten in een DataFrame
df_trends = pd.DataFrame(trending_data)

# Streamlit Webapp
st.title("🚀 AI Trendwatcher - Trending Content")
st.write("📌 Ontdek de nieuwste trends op TikTok en Instagram!")

# Filteropties
platform_filter = st.selectbox("🌎 Kies een platform:", ["Alle", "TikTok", "Instagram"])

# Filter toepassen
if platform_filter != "Alle":
    df_filtered = df_trends[df_trends["Platform"] == platform_filter]
else:
    df_filtered = df_trends

# Weergave van trending data
st.dataframe(df_filtered)
