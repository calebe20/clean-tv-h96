#!/usr/bin/env bash
# Return to yesterday's launcher; keep all existing debloat and system settings.
set -euo pipefail
H96_SERIAL=${1:?Uso: restore.sh IP:PORTA}
adb connect "$H96_SERIAL"
adb -s "$H96_SERIAL" shell cmd package set-home-activity --user 0 com.gathin.tvhome/.MainActivity
adb -s "$H96_SERIAL" shell input keyevent KEYCODE_HOME
adb -s "$H96_SERIAL" shell cmd package resolve-activity --brief -a android.intent.action.MAIN -c android.intent.category.HOME
