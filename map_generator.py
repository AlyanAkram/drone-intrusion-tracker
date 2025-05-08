import pandas as pd
import folium

def generate_map():
    data = pd.read_csv('data/sightings.csv')
    m = folium.Map(location=[30.3753, 69.3451], zoom_start=6)

    for _, row in data.iterrows():
        popup_text = f"""
        <b>Date:</b> {row['date']}<br>
        <b>Time:</b> {row['time']}<br>
        <b>Location:</b> {row['location']}<br>
        <b>Drone Type:</b> {row['drone_type']}<br>
        <b>Source:</b> {row['source']}
        """
        folium.Marker(
            location=[float(row['latitude']), float(row['longitude'])],
            popup=folium.Popup(popup_text, max_width=300),
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(m)

    m.save('static/drone_map.html')
