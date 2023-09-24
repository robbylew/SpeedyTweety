import speedtest

def get_current_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1_000_000  # Convert from bits to Megabits
    return round(download_speed, 2)
