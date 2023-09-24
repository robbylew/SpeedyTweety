import speedtest
import time
import tweepy


def get_download_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1_000_000  # Convert bytes per second to megabits per second
    return download_speed


def setup_twitter(api_key, api_secret_key, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)


def tweet_isp(api, message):
    api.update_status(status=message)


def select_isp():
    isp_list = {
        "1": "@ATT",
        "2": "@comcast",
        "3": "@Xfinity",
        "4": "@verizon",
        "5": "@GetSpectrum",
        "6": "@CoxComm",
        "7": "@CenturyLink",
        "8": "@LumenTechCo",
        "9": "@FrontierCorp",
        "10": "@TMobile",
        "11": "@MediacomCable",
        "12": "@Windstream"
    }

    print("Please select your ISP:")
    for key, value in isp_list.items():
        print(f"{key}. {value}")

    selection = input()
    return isp_list.get(selection, "@DefaultISP")


def main():
    # Twitter credentials (for safety, consider fetching these from environment variables or an external file)
    api_key = 'YOUR_API_KEY'
    api_secret_key = 'YOUR_API_SECRET_KEY'
    access_token = 'YOUR_ACCESS_TOKEN'
    access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

    # Set up Twitter API
    api = setup_twitter(api_key, api_secret_key, access_token, access_token_secret)

    # Get user's threshold value for download speed
    try:
        threshold_speed = float(input("Enter the download speed (in Mbps) you consider too low: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    # Select ISP
    isp_handle = select_isp()

    print(
        f"Monitoring your download speed. Will notify you when it drops below {threshold_speed:.2f} Mbps and tweet to {isp_handle}...")

    while True:
        current_speed = get_download_speed()
        print(f"Current download speed: {current_speed:.2f} Mbps")
        if current_speed < threshold_speed:
            print(f"ALERT: Your download speed has dropped below the threshold!")
            tweet_message = f"Hey {isp_handle}, my download speed has dropped to {current_speed:.2f} Mbps, which is below acceptable limits. Please address this issue!"
            tweet_isp(api, tweet_message)
        time.sleep(10)  # Check every 10 seconds


if __name__ == "__main__":
    main()
