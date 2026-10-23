"""Install the local H96 launcher without modifying existing debloat or settings."""
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
APK = ROOT / 'cleanyourtv/launcher/app/build/outputs/apk/release/app-release.apk'
PACKAGE = 'com.gathin.tvhome.h96'
COMPONENT = PACKAGE + '/com.gathin.tvhome.MainActivity'
QUERY = ['cmd', 'package', 'resolve-activity', '--brief', '-a',
         'android.intent.action.MAIN', '-c', 'android.intent.category.HOME']
SERIAL = sys.argv[1]


def adb(*args):
    result = subprocess.run(['adb', '-s', SERIAL, *args], check=True,
                            capture_output=True, text=True, timeout=90)
    return result.stdout.strip()


def shell(*args):
    return adb('shell', *args)


def home():
    return shell(*QUERY).splitlines()[-1].strip()


if not APK.is_file() or APK.stat().st_size >= 491520:
    raise SystemExit('APK ausente ou acima do limite de 480 KiB; nada instalado.')
json.loads((ROOT / 'h96-profile/config.json').read_text())
previous_home = home()
if '/' not in previous_home:
    raise SystemExit('Nao foi possivel identificar o Home atual; nada instalado.')
baseline_disabled = set(shell('pm', 'list', 'packages', '-d').splitlines())
print(adb('push', str(APK), '/data/local/tmp/h96-home.apk'))
installed = shell('pm', 'install', '-r', '/data/local/tmp/h96-home.apk')
print(installed)
if installed != 'Success':
    raise SystemExit('Instalacao recusada; Home anterior preservado.')
try:
    adb('push', str(ROOT / 'h96-profile/config.json'), '/data/local/tmp/h96-config.json')
    print(shell('content write --uri content://' + PACKAGE +
                '.theme/config.json < /data/local/tmp/h96-config.json'))
    started = shell('am', 'start', '-W', '-a', 'android.intent.action.MAIN',
                    '-c', 'android.intent.category.HOME', '-n', COMPONENT)
    print(started)
    if 'Status: ok' not in started or 'Error:' in started:
        raise RuntimeError('O novo launcher nao iniciou.')
    print(shell('cmd', 'package', 'set-home-activity', '--user', '0', COMPONENT))
    if home() != COMPONENT:
        raise RuntimeError('O novo launcher nao assumiu o Home.')
    shell('input', 'keyevent', 'KEYCODE_HOME')
    if COMPONENT not in shell('dumpsys', 'activity', 'activities'):
        raise RuntimeError('Atividade do launcher nao encontrada.')
    if baseline_disabled != set(shell('pm', 'list', 'packages', '-d').splitlines()):
        raise RuntimeError('A lista de pacotes desativados mudou.')
    print(shell('cmd', 'package', 'compile', '-m', 'speed', '-f', PACKAGE))
    print('Home instalado. Pacotes e ajustes de sistema preservados.')
except Exception:
    shell('cmd', 'package', 'set-home-activity', '--user', '0', previous_home)
    shell('input', 'keyevent', 'KEYCODE_HOME')
    raise
finally:
    shell('rm', '-f', '/data/local/tmp/h96-home.apk', '/data/local/tmp/h96-config.json')
