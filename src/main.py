import twitter_api
import speedtest_util
import user_interaction
import time


def main():
    api = twitter_api.setup_twitter()
    threshold = user_interaction.get_threshold()
    isp_handle = user_interaction.select_isp()
    print(f"We will update you every 20 seconds on the speed, and if it falls under the threshold we will tweet for you at {isp_handle}")
    while True:
        speed = speedtest_util.get_current_speed()
        print(f"Current speed: {speed} Mbps")

        if speed < threshold:
            twitter_api.tweet_to_isp(api, isp_handle, speed)
        time.sleep(20)


if __name__ == '__main__':
    main()
