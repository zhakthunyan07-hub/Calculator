[app]

# (str) Title of your application
title = Calculator

# (str) Package name
package.name = calculator

# (str) Package domain (needed for android packaging)
package.domain = org.calc

# (str) Source files where the .py files are located
source.dir = .

# (list) Source files to include (let empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_pattern = images/*.png,icons/*.png

# (list) List of exclusions using pattern matching
#source.exclude_pattern = license,images/unsorted/*.gif

# (list) List of directory to exclude
#source.exclude_dirs = tests, bin, venv

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (list) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.dirs = ../my_custom_source_dir

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
# Valid orientations: landscape, portrait, all-up, all-down
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PYTHON_SCRIPT,NAME2:ENTRYPOINT_TO_PYTHON_SPECSERVICE

#
# OSX Specific
#

#
# Number of CPU to use for parallel compilation
#-
#osx.python_version = 3
#osx.kivy_version = 1.9.1

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for android)
#android.presplash_color = #FFFFFF

# (string) Adaptive icon background color (Android O+)
#android.adaptive_icon_background = #FFFFFF

# (list) Permissions
#android.permissions = INTERNET

# (list) Features
#android.features = android.hardware.usb.host

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.min_api = 21

# (int) Android SDK version to use
android.sdk = 31

# (str) Android NDK version to use
android.ndk = r23b

# (int) Android NDK API to use. If not specified, will be equal to android.min_api or android.api depending on the sdk version
#android.ndk_api = 

# (bool) Use --private data directory (True) or --dir public storage (False)
#android.private_storage = True

# (list) Android ARM architecture to build for, options are: arm64-v8a, armeabi-v7a, x86, x86_64
android.archs = arm64-v8a

# (bool) Enable AndroidX support
#android.androidx = True

# (bool) Automatically accept SDK license
android.accept_sdk_license = True

# (str) External extras to add
#android.add_extras = 

# (str) Python for android (p4) git clone or branch
p4 = 0

