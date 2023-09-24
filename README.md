# ISP Speed Monitor & Notifier

A simple Python script to monitor your internet download speed and automatically notify you and tweet to your ISP if the speed drops below a user-defined threshold.

## Features

- Monitor internet download speed in real-time.
- Set custom speed threshold for alerts.
- Automatic Twitter notification to the selected ISP.
- Supported ISPs include AT&T, Comcast (Xfinity), Verizon, and more!

## Prerequisites

- A Twitter Developer account and app with API credentials.
- Python environment with the following packages:
  - `tweepy`
  - `speedtest-cli`
  - `configparser`

## Setup

1. Clone the repository:

```bash
git clone https://github.com/robbylew/SpeedyTweety.git
```

2. Navigate to the repository:

```bash
cd YOUR_REPOSITORY_NAME
```

3. Install the required Python libraries:

```bash
pip install requirements.txt
```

4. Set up your Twitter Developer API credentials. For security, consider using environment variables or an external configuration file to store these.

5. Run the script:

```bash
python src\main.py
```

6. Follow the prompts to set your desired speed threshold and select your ISP.

## Usage

Once you've set the threshold and selected your ISP, the script will monitor your internet download speed every 20 seconds. If the speed drops below the set threshold, it will notify you and send a tweet to the ISP's official Twitter handle about the speed drop.

## Contributing

Pull requests are welcome! Please make sure to update tests as appropriate.


## License

[MIT](https://choosealicense.com/licenses/mit/)

---

