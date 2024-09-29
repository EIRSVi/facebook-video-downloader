import subprocess
import os
import pyfiglet
from colorama import Fore, init
import time

# Initialize Colorama
init(autoreset=True)

def print_colored_logo():
    # Generate ASCII art for the logo "SRIEVi"
    logo = pyfiglet.figlet_format("SRIEVi", font="slant")
    
    # Center the logo in the terminal
    terminal_width = os.get_terminal_size().columns
    centered_logo = "\n".join(line.center(terminal_width) for line in logo.splitlines())

    # Colors for the gradient effect (cyber-like appearance)
    colors = [Fore.LIGHTCYAN_EX, Fore.CYAN, Fore.MAGENTA, Fore.LIGHTMAGENTA_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTBLUE_EX]

    # Apply a glowing effect to each character in the logo
    print("\n")  # Add spacing before the logo
    for i, char in enumerate(centered_logo):
        if char.strip():  # Apply color only to non-space characters
            print(colors[i % len(colors)] + char, end='', flush=True)
            time.sleep(0.02)  # Slight delay to create a glowing effect
        else:
            print(char, end='', flush=True)
    print("\n")  # New line after the logo

def print_welcome(platform):
    # Call the function to print the colored SRIEVi logo
    print_colored_logo()
    
    # Welcome message
    welcome_message = f"{Fore.LIGHTBLUE_EX}Welcome to the {platform} Video Downloader! \n"
    terminal_width = os.get_terminal_size().columns
    centered_message = welcome_message.center(terminal_width)
    print(centered_message)

    # Updated GitHub and social links
    developer_info = f"Support us {Fore.LIGHTGREEN_EX}@eirsvi "
    centered_developer = developer_info.center(terminal_width)
    print(centered_developer)

    social_links = f"{Fore.LIGHTRED_EX} GitHub | X | YouTube \n"
    centered_social_links = social_links.center(terminal_width)
    print(centered_social_links)

    # Example URL without centering
    example_url = f"EXAMPLE URL: {Fore.LIGHTYELLOW_EX}https://www.facebook.com/zuck/videos/10101858403890501 \n"
    print(example_url)
    
    print()  # Add an extra newline for spacing

def download_video(platform):
    # Call the welcome message function
    print_welcome(platform)
    
    # Prompt user for the video URL
    url = input(f"{Fore.LIGHTCYAN_EX}Enter the FB video URL: {Fore.LIGHTCYAN_EX}")

    # Define a default output directory (e.g., ~/Downloads)
    output_dir = os.path.expanduser('~/Downloads')

    # Generate the output file name
    output_file = os.path.join(output_dir, '%(title)s.%(ext)s')

    try:
        # Command to download video using yt-dlp
        subprocess.run(['yt-dlp', '-o', output_file, url], check=True)
        print(f"{Fore.LIGHTGREEN_EX}Video downloaded successfully: {Fore.LIGHTYELLOW_EX}{output_file}")
    except subprocess.CalledProcessError as e:
        print(f"{Fore.LIGHTRED_EX}Error downloading video: {e}")

if __name__ == "__main__":
    # Call the download function for Facebook with SRIEVi logo
    download_video("Facebook")
