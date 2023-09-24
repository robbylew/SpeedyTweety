from . import twitter_api
from . import speedtest_util
from . import user_interaction
import time

def main():
    api = twitter_api.setup_twitter()
    threshold = user_interaction.get_threshold()
    isp_handle = user_interaction.select_isp()

    while True:
        speed = speedtest_util.get_current_speed()
        print(f"Current speed: {speed} Mbps")

        if speed < threshold:
            twitter_api.tweet_to_isp(api, isp_handle, speed)
        time.sleep(10)

if __name__ == '__main__':
    main()
