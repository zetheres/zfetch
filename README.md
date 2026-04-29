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

## ⚙️ How to Install (For Termux)

Open your Termux app and run the following commands one by one:

```bash
# 1. Update Termux packages
pkg update && pkg upgrade -y

# 2. Install Git and Python
pkg install git python -y

# 3. Clone this repository (Replace YourUsername with your GitHub username)
git clone [https://github.com/YourUsername/Z-Fetch.git](https://github.com/YourUsername/Z-Fetch.git)

# 4. Navigate into the folder
cd Z-Fetch

# 5. Run the tool
python zfetch.py
