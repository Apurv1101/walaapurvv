[app]

title = My Application
package.name = myapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

requirements = python3,kivy,opencv-python,requests

orientation = portrait
fullscreen = 0

android.permissions = CAMERA, RECORD_AUDIO, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, INTERNET
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]

log_level = 2
warn_on_root = 1


[ios]

ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0
ios.codesign.allowed = false
