[app]
title = DevAI
package.name = devai
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

requirements = python3==3.10.15,kivy,hostpython3==3.10.15

orientation = portrait
fullscreen = 0

android.archs = arm64-v8a
android.api = 31
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.skip_update = False
android.accept_sdk_license = True
android.copy_libs = 1

p4a.extra_args = --status --force-batch
p4a.bootstrap = sdl2

[buildozer]
log_level = 2
warn_on_root = 1

