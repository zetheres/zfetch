import os
import subprocess
import json
import sys
import time

TOOL_NAME = "Z-Fetch"
DEV_NAME = "Zetheres Maverick"
TG_LINK = "@Zetheres"
DEFAULT_PATH = "/sdcard/Download"

def clear():
    os.system('clear')

def banner():
    print("\033[1;36m")
    print(r"""
  _______        ______    _       _     
 |__  /___|____ |  ____|  | |     | |    
   / /  |______|| |__  ___| |_ ___| |__  
  / /           |  _|/ _ \ __/ __| '_ \ 
 / /__          | | |  __/ || (__| | | |
/_____|         |_|  \___|\__\___|_| |_|
    """)
    print(f"\033[1;33m  [⚙] Dev: {DEV_NAME}  |  [💬] TG: {TG_LINK}  |  [🚀] Tool: {TOOL_NAME}")
    print("\033[1;32m  [📥] Download any social media videos Facebook, YouTube, Instagram...etc\033[0m")
    print("\033[1;31m-----------------------------------------------------------------\033[0m")

def setup_tools():
    clear()
    banner()
    print("\033[1;32m[*] Starting Full Setup & Update...\033[0m\n")
    
    home_dir = os.path.expanduser("~")
    storage_dir = os.path.join(home_dir, "storage")
    
    if not os.path.exists(storage_dir):
        print("\033[1;33m[*] Requesting Storage Permission...\033[0m")
        os.system("termux-setup-storage")
        time.sleep(3)
    else:
        print("\033[1;32m[*] Storage permission already granted. Skipping...\033[0m")

    print("\n\033[1;36m[*] Updating Termux & Installing Nodejs, FFmpeg...\033[0m")
    os.system("pkg update -y && pkg upgrade -y")
    os.system("pkg install python ffmpeg nodejs -y")
    
    print("\n\033[1;36m[*] Updating yt-dlp Library...\033[0m")
    os.system("pip install --upgrade yt-dlp")
    
    print("\n\033[1;32m[+] Setup & Updates Complete!\033[0m")
    input("\n\033[1;36mPress Enter to return to menu...\033[0m")

def get_path():
    if not os.path.exists("config.json"):
        return DEFAULT_PATH
    with open("config.json", "r") as f:
        data = json.load(f)
        return data.get("path", DEFAULT_PATH)

def set_path():
    clear()
    banner()
    current = get_path()
    print(f"\033[1;33mCurrent Download Path: {current}\033[0m")
    new_path = input("\033[1;32mEnter new path: \033[0m")
    if new_path:
        with open("config.json", "w") as f:
            json.dump({"path": new_path}, f)
        print("\033[1;32m[+] Path updated successfully!\033[0m")
    input("\n\033[1;36mPress Enter to return...\033[0m")

def developer_info():
    clear()
    banner()
    print(f"\033[1;36mDeveloper : \033[1;32m{DEV_NAME}\033[0m")
    print(f"\033[1;36mTelegram  : \033[1;32m{TG_LINK}\033[0m")
    print(f"\033[1;36mProject   : \033[1;32m{TOOL_NAME} Final\033[0m")
    input("\n\033[1;36mPress Enter to return...\033[0m")

def get_available_qualities(url):
    print("\033[1;36m[*] Checking available qualities... Please wait.\033[0m")
    try:
        cmd = f'yt-dlp --print "%(height)s" --no-playlist --no-warnings "{url}" 2>/dev/null'
        output = subprocess.check_output(cmd, shell=True).decode().split()
        heights = sorted(list(set([int(h) for h in output if h.isdigit()])), reverse=True)
        return heights
    except:
        return []

def download_engine():
    clear()
    banner()
    url = input("\033[1;33m[?] Enter Link: \033[0m")
    if not url: return

    save_path = get_path()
    out_tmpl = f"{save_path}/[{TOOL_NAME}] %(title)s.%(ext)s"
    
    playlist_cmd = "--no-playlist"
    if "list=" in url or "playlist" in url.lower():
        print("\n\033[1;36m[*] This is a playlist. You want all files?\033[0m")
        pl_choice = input("\033[1;32mSelect (y/n): \033[0m").strip().lower()
        if pl_choice == 'y':
            playlist_cmd = "--yes-playlist"
        else:
            return 

    print("\n\033[1;32m1. Only MP3 Audio")
    print("2. Mp4 (Video+Audio)\033[0m")
    media_choice = input("\n\033[1;33mSelect Option (1 or 2): \033[0m").strip()

    # শুধু এই লাইনটিতে --trim-filenames 50 যোগ করা হয়েছে
    base_args = f'-c --no-warnings --no-keep-video --trim-filenames 50 {playlist_cmd}'

    if media_choice == '1':
        print("\n\033[1;36m[*] Starting Audio Download...\033[0m")
        cmd = f'yt-dlp {base_args} -f "bestaudio/best" -x --audio-format mp3 -o "{out_tmpl}" "{url}"'
        
        print("\033[?7l", end="", flush=True) 
        subprocess.run(cmd, shell=True)
        print("\033[?7h", end="", flush=True) 
        
    elif media_choice == '2':
        heights = get_available_qualities(url)
        if not heights:
            f_id = "bestvideo+bestaudio/best"
        else:
            print("\n\033[1;32mAvailable Qualities:\033[0m")
            options = []
            count = 1
            for h in [2160, 1440, 1080, 720, 480]:
                if any(height >= h for height in heights):
                    label = "4K" if h == 2160 else "2K" if h == 1440 else f"{h}p"
                    print(f"{count}. {label}")
                    options.append((count, h))
                    count += 1
            
            if not options:
                print("1. Standard Quality")
                options.append((1, 480))

            q_input = input("\n\033[1;33mSelect Quality: \033[0m").strip()
            
            f_id = "bestvideo+bestaudio/best"
            for opt_num, h_val in options:
                if q_input == str(opt_num):
                    f_id = f"bestvideo[height<={h_val}]+bestaudio/best"
                    break

        print(f"\n\033[1;32m[*] Starting Live Download & Processing...\033[0m")
        cmd = f'yt-dlp {base_args} -f "{f_id}" --merge-output-format mp4 -o "{out_tmpl}" "{url}"'
        
        print("\033[?7l", end="", flush=True) 
        subprocess.run(cmd, shell=True)
        print("\033[?7h", end="", flush=True) 
        
    input("\n\033[1;36mProcess Finished. Press Enter...\033[0m")

def main_menu():
    while True:
        clear()
        banner()
        print("\033[1;32m1. Start Download")
        print("2. Setup & Download All Tools")
        print("3. Setup Download Path")
        print("4. Developer Details")
        print("5. Exit\033[0m")
        
        m_choice = input("\n\033[1;33mChoose an option (1-5): \033[0m")
        
        if m_choice == '1':
            download_engine()
        elif m_choice == '2':
            setup_tools()
        elif m_choice == '3':
            set_path()
        elif m_choice == '4':
            developer_info()
        elif m_choice == '5':
            print("\n\033[1;31mThanks for using Z-Fetch. Goodbye!\033[0m")
            sys.exit()
        else:
            print("\033[1;31mInvalid Choice!\033[0m")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\033[1;31mStopped by User. Exiting...\033[0m")
