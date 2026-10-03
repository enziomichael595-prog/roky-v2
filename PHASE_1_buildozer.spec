[app]

# (str) Title of your application
title = Roky V2.1

# (str) Package name
package.name = rokyv2

# (str) Package domain (needed for android/ios packaging)
package.domain = org.roky

# (source.dir) Source directory (where you store your Python files)
source.dir = .

# (list) Source include patterns (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json,txt

# (list) List of directory to exclude (let empty to not exclude anything)
source.exclude_dirs = tests, bin, .buildozer, .git, .github

# (str) Application versioning (method 1)
version = 2.1.0

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation (landscape, sensorLandscape, portrait or sensorPortrait)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
# Minimal for Phase 1 (basic UI only)
# More permissions added in later phases
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a,armeabi-v7a

# (bool) Enable AndroidX support
android.enable_androidx = True

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = 1

# (bool) Allow backup of application data
android.allow_backup = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning upon buildozer run if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (bool) Accept Android SDK license
android.accept_sdk_license = True
