[app]

title = My Application
package.name = myapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Do NOT use opencv-python directly, we are adding native support
requirements = python3,kivy,numpy,requests

# App layout
orientation = portrait
fullscreen = 0

# Permissions for hardware and storage
android.permissions = CAMERA, RECORD_AUDIO, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, INTERNET

# Architecture support
android.archs = armeabi-v7a, arm64-v8a

# Add native OpenCV support
android.add_jars = libs/opencv-android.jar
android.add_libs_armeabi_v7a = libs/armeabi-v7a/libopencv_java4.so
android.add_libs_arm64_v8a = libs/arm64-v8a/libopencv_java4.so

# Optional logging and backup
android.allow_backup = True
android.logcat_filters = *:S python:D

[buildozer]

log_level = 2
warn_on_root = 1

[ios]

ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0
ios.codesign.allowed = false
