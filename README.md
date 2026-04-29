# 🚀 Z-Fetch : Ultimate Social Media Downloader

**Z-Fetch** is a lightning-fast, powerful, terminal-based tool designed to download videos, audios, and playlists from almost any social media platform directly to your Android device via Termux. It features a sleek terminal UI and zero-clutter processing.

## 🌟 What Can It Download?
* **Platforms Supported:** YouTube, Facebook, Instagram, TikTok (No Watermark), X (Twitter), and 1000+ other supported websites.
* **Formats:** MP4 (Video + Audio) and MP3 (Audio only).
* **Playlists:** Automatically detects YouTube playlist links and offers a one-click bulk download option.

## ✨ Key Features
* **Smart Quality Fetching:** Automatically scans the link and shows exactly what resolutions are available (4K, 2K, 1080p, 720p, 480p).
* **Auto-Merge (FFmpeg):** Downloads high-bitrate video and audio separately, merges them, and cleans up temporary files to save storage.
* **Resume Capability:** If the network drops, downloads automatically resume exactly from where they stopped.
* **Clean UI:** Line-wrapping is disabled during download to provide a static, single-line live progress bar for speed and ETA.

---

## ⚡ One-Click Installation (Termux)
Just copy the single command below, paste it into Termux, and press Enter. It will install everything and start the tool automatically!

```bash
pkg update -y && pkg install git python -y && git clone [https://github.com/zetheres/zfetch.git](https://github.com/zetheres/zfetch.git) && cd zfetch && python zfetch.py
```

---

## 🛠️ Step-by-Step Installation (Manual)
If you prefer installing step-by-step, run the following commands one by one in your Termux terminal:

```bash
# 1. Update Termux packages
pkg update && pkg upgrade -y

# 2. Install Git and Python
pkg install git python -y

# 3. Clone this repository
git clone [https://github.com/zetheres/zfetch.git](https://github.com/zetheres/zfetch.git)

# 4. Navigate into the folder
cd zfetch

# 5. Run the tool
python zfetch.py
```

---

## 🚀 How to Use Z-Fetch

1. **First-Time Setup (Important):**
   * When you run the tool for the first time, select **Option 2** (`Setup & Download All Tools`). 
   * It will automatically request storage permissions, and install required background tools like `FFmpeg`, `Node.js`, and `yt-dlp`.
   
2. **Start Downloading:**
   * Select **Option 1** (`Start Download`).
   * Paste your video or playlist link.
   * Choose your desired format (`1` for MP3 Audio, `2` for MP4 Video).
   * Select your preferred quality from the dynamic list. The tool will download and merge it for you!

3. **Change Download Location:**
   * By default, your downloaded files are saved to `/sdcard/Download`. 
   * If you want to change this path, select **Option 3** (`Setup Download Path`) and enter your custom folder location.

4. **Exit the Tool:**
   * Select **Option 5** to safely exit Z-Fetch.

---

## 👨‍💻 Developer Details
* **Developed by:** Zetheres Maverick
* **Telegram:** [@Zetheres](https://t.me/Zetheres)
* **GitHub Repository:** [zetheres/zfetch](https://github.com/zetheres/zfetch)
* **Design Philosophy:** Dark, Glossy, and Minimalist.
