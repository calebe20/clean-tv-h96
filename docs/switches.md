# Switches on a TV

Every key a theme can set (the Keys table in [`themes/README.md`](../themes/README.md)) gets a
screenshot of what it does on a real TV. This table is where they are listed: the repo and
[cleanyour.tv/addons#switches](https://cleanyour.tv/addons#switches) both show them from here.

## Adding a key

A new key needs a screenshot. Put it in `docs/switches/<key>.jpg` (an existing screenshot in the
repo that shows the key at work also counts) and add a row below:

- From a real TV, with the key set, as a JPEG or PNG, 16:9 (1280×720 is plenty), under 300 KB.
- Show where the key changes something you can see. For a key that maps a remote button, show the
  screen the button opens; for one that changes behaviour only, show the setting's effect, such as
  the panel, the menu or the app that comes up.
- Blur anything personal: Wi-Fi names, people, addresses.

`tests/test_switches.py` checks that every key has a row here with an image that exists and fits
the rules. Keys from before this rule are on its wanted list; a screenshot for one of them is welcome.

## Screenshots

| Key | Screenshot |
|---|---|
| `columns` | <img src="../themes/six-columns/screenshot.jpg" width="320" alt="columns on a TV"> |
| `sky_intensity` | <img src="sky-sunset.jpg" width="320" alt="sky_intensity on a TV"> |
| `wallpaper_rotation_minutes` | <img src="../themes/scenes/screenshot.jpg" width="320" alt="wallpaper_rotation_minutes on a TV"> |
| `festival` | <img src="../themes/dussehra/screenshot.jpg" width="320" alt="festival on a TV"> |
| `settings_key_panel` | <img src="quick-settings-panel.jpg" width="320" alt="settings_key_panel on a TV"> |
| `home_idle_clock_minutes` | <img src="clock-screensaver.png" width="320" alt="home_idle_clock_minutes on a TV"> |
| `gamepad_passthrough` | <img src="switches/gamepad_passthrough.jpg" width="320" alt="gamepad_passthrough on a TV"> |
| `dock_top_padding` | <img src="switches/compact-home.png" width="320" alt="Reduced space above the dock on an H96 TV stick"> |
| `dock_bottom_offset` | <img src="switches/compact-home.png" width="320" alt="Reduced gap below the dock on an H96 TV stick"> |
| `grid_title` | <img src="switches/grid-title.png" width="320" alt="SmartTube in the second row also shown in the fixed title shelf"> |
| `grid_bands` | <img src="switches/grid-title.png" width="320" alt="Background bands behind both app rows"> |
| `dock_band` | <img src="switches/dock-band.png" width="320" alt="Compact home layout without the dock shelf band"> |
