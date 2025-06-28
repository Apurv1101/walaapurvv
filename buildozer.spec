[app]

title = My Application
package.name = myapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Include all needed modules
requirements = python3,kivy,opencv-python,requests,numpy

# Portrait layout
orientation = portrait
fullscreen = 0

# Permissions needed for:
# - Camera (CAMERA)
# - Mic/speaker (RECORD_AUDIO)
# - Storage (WRITE/READ_EXTERNAL_STORAGE)
# - Network (INTERNET)
android.permissions = CAMERA, RECORD_AUDIO, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, INTERNET

# Keep screen on if needed (optional)
# android.wakelock = True

# Target architectures (both 32-bit and 64-bit ARM)
android.archs = armeabi-v7a, arm64-v8a

# Optional: specify OpenCV Java binding if needed
# android.add_jars = libs/opencv-android.jar

# Allow app data backup
android.allow_backup = True

# Enable logs from Python
android.logcat_filters = *:S python:D

# Keep public storage access (can set private if needed)
# android.private_storage = True

[buildozer]

log_level = 2
warn_on_root = 1

# Optional: output path customization
# build_dir = ./.buildozer
# bin_dir = ./bin

[ios]

ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0
ios.codesign.allowed = false
