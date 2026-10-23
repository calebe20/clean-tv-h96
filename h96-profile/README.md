# Perfil do launcher para H96 Max H313

Este perfil instala a variante local do Clean Your TV como Home no H96 Max H313.
O APK usa a identidade `com.gathin.tvhome.h96`, mantendo o launcher anterior
instalado para permitir retorno imediato.

O código é construído a partir do Clean Your TV e usa apenas recursos locais do
launcher. O perfil não desativa pacotes do aparelho nem altera as configurações do
sistema; a limpeza e os ajustes de cada TV devem ser feitos separadamente, com
backup e possibilidade de restauração.

## Requisitos

- ADB autorizado no aparelho, via USB ou `IP:PORTA`.
- JDK 17.
- Android SDK com plataforma e build-tools compatíveis.
- `JAVA_HOME` apontando para o JDK 17 e `ANDROID_HOME` apontando para o SDK.

## Compilar e instalar

A partir da raiz deste repositório:

```bash
export JAVA_HOME=/caminho/para/jdk-17
export ANDROID_HOME=$HOME/Android/Sdk
adb connect IP:PORTA
bash h96-profile/build-and-install.sh IP:PORTA
```

O script executa os testes JVM, o lint, o build release e instala o APK somente
se ele permanecer abaixo do limite de 480 KiB. Para instalar um APK já compilado:

```bash
python3 h96-profile/install.py IP:PORTA
```

O `config.json` controla a aparência e a organização do Home. Ele mantém quatro
atalhos visíveis, esconde os rótulos inferiores, usa o botão **Apps** no cabeçalho,
e deixa a biblioteca de aplicativos disponível para adicionar ou remover atalhos.
O fundo é vinho escuro, sem wallpaper e sem brilho de aplicativo.

## Restaurar o Home anterior

```bash
bash h96-profile/restore.sh IP:PORTA
```

Esse comando apenas devolve o Home original. Ele não reativa nem desinstala
pacotes do aparelho.

## Segurança e arquivos locais

Não coloque neste repositório dumps do aparelho, backups, diagnósticos, chaves ADB,
IP fixo, nomes de Wi-Fi, contas, APKs gerados ou capturas que exponham informações
do dispositivo. Use `IP:PORTA` nos exemplos e mantenha esses artefatos fora do Git.
