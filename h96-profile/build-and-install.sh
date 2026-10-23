#!/usr/bin/env bash
set -euo pipefail
TASK_ROOT=$(cd -- "$(dirname -- "$0")/.." && pwd)
if [[ -z "${JAVA_HOME:-}" ]]; then
  echo "Defina JAVA_HOME apontando para um JDK 17." >&2
  exit 2
fi
export ANDROID_HOME="${ANDROID_HOME:-$HOME/Android/Sdk}"
export PATH="$JAVA_HOME/bin:$PATH"
cd "$TASK_ROOT/cleanyourtv/launcher"
./gradlew --no-daemon -PlauncherApplicationId=com.gathin.tvhome.h96 testReleaseUnitTest lintRelease assembleRelease --console=plain
python3 "$TASK_ROOT/h96-profile/install.py" "${1:?Uso: build-and-install.sh IP:PORTA}"
