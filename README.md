# PPTSynchro
Sync a master PPT machine to a slave PPT machine via wifi or bluetooth, primarily for a main machine doing the projection and a slave machine with better specs that's doing livestreaming.
Controls underlying Presented slide using VBA api which allows the controls to work even if the slide is not on a active window.

# Setup

(requires python 3.9 and recommemds using virtual environment) <br>

1. `pip install -r requirements_windows.txt`
2. edit `config.yaml` to set in wifi/bluetooth mode and set relevant address
3. set in `Sniff_key` mode to find the desired keys name to be binded to `NEXT_KEYS`, `PREV_KEYS` and disabling button `TOGGLE_KEY` on slave

# Run

`python main.py`

# Building package

able to build package successfully using pyinstaller on windows with inclusion additional flags as noted in `build_instructions.txt`

# License

[MIT License](./LICENSE)
