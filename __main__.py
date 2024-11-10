import speedtest as st
import time

def Type(text, delay=0.05):
    """
    Prints each character in the given text with a specified delay.

    Args:
        text (str): The text to be printed.
        delay (float): The delay (in seconds) between each character. Default is 0.05.
    """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)  # Adding delay for each character
    print()

def Speed_Test():
    """
    Tests the internet connection speed and prints the download, upload speeds,
    and ping in Mbps and ms.
    """
    # Initialize the speed test
    test = st.Speedtest()

    # Get download speed in bits per second and convert to Mbps
    download = test.download()
    download_speed = round(download / 10**6, 2)

    # Get upload speed in bits per second and convert to Mbps
    upload = test.upload()
    upload_speed = round(upload / 10**6, 2)

    # Get ping result in milliseconds
    ping = test.results.ping

    # Print the results
    Type("Upload Speed in Mbps: " + str(upload_speed))
    Type("Download Speed in Mbps: " + str(download_speed))
    Type('Ping: ' + str(ping) + ' ms')

if __name__ == "__main__":
    # Inform the user that the speed test might take a few moments
    Type("The speed test is starting. Please wait, this may take a few moments...")
    # Run the speed test
    Speed_Test()
