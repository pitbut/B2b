# B2B Platform UZ — мобильное приложение

Нативная Android-обёртка (через [Capacitor](https://capacitorjs.com/)) вокруг
живого сайта **b2b.robutpit.com**, который работает на отдельном VPS. Само
приложение не содержит бизнес-логики и не дублирует сайт — оно просто
открывает `https://b2b.robutpit.com` в системном WebView и даёт иконку на
экране телефона, полноэкранный режим без адресной строки и задел под
пуш-уведомления. Вся логика (заказы, чат, Telegram-бот и т.д.) остаётся на
VPS в репозитории `my-portfolio/projects/b2b-platform` — здесь ничего не
дублируется.

## Как собрать

Сборка автоматическая, через GitHub Actions (`.github/workflows/build-android.yml`):
любой push в `main` собирает debug APK и публикует его в
[Releases](../../releases/tag/latest) под тегом `latest` — то есть по сайту
можно повесить постоянную ссылку на скачивание:

```
https://github.com/pitbut/b2b/releases/download/latest/app-debug.apk
```

## Локальная сборка (по желанию)

```bash
npm install
npx cap sync android
cd android && ./gradlew assembleDebug
```
APK появится в `android/app/build/outputs/apk/debug/app-debug.apk`.

## Почему debug-сборка, а не «настоящий» релиз

Debug APK не требует ключа подписи и отлично подходит для прямой раздачи
(не через Google Play) — устанавливается так же, просто при первой установке
Android попросит разрешить «установку из неизвестных источников». Если
понадобится публикация в Google Play или более «чистая» сборка — тогда
нужен release-ключ подписи (keystore) и `assembleRelease`, это отдельный шаг.

## Иконка и splash-экран

Сейчас используется плейсхолдер (`scripts/gen_icons.py` — тёмный фон сайта +
надпись «B2B»), сгенерированный скриптом. Как только будет готов реальный
логотип — перегенерировать иконки через тот же скрипт или вручную заменить
файлы в `android/app/src/main/res/mipmap-*/` и `drawable*/splash.png`.

## Push-уведомления (следующий шаг, не сделано)

Пока приложение уведомления не шлёт — этот канал сейчас закрывает Telegram-бот
на сайте. Если понадобятся push прямо в приложение — добавляем Firebase
Cloud Messaging (`@capacitor/push-notifications`) отдельным шагом, это не
требует переделки текущей структуры.

## iOS

Не собирается — для iOS нужен macOS-раннер и Apple Developer аккаунт
(платный, $99/год) даже для сборки .ipa без публикации в App Store. Пока
делаем только Android; если понадобится iOS — добавим отдельный workflow.
