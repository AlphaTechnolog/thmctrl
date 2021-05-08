# thmctrl

Manage my dotfiles (based in the Antonio Sarosi dotfiles) themes, more easy.

## Requirements

The requirements to use `thmctrl` are the next programs:

- [wallc](https://github.com/AlphaTechnolog/wallc)
- [pycritty](https://github.com/antoniosarosi/pycritty)
- [antonio sarosi dotfiles](https://github.com/antoniosarosi/dotfiles)

## Installing

To install see the next steps

### Clone

First, clone the project:

```sh
cd ~
mkdir repo
cd repo
git clone https://github.com/AlphaTechnolog/thmctrl
cd thmctrl
```

## Installing with the Makefile

To install `thmctrl` you will have installed `make`, to install
it on debian use the next command:

```sh
sudo apt install make
```

**Note**: Install with your dist package manager.

See the next commands sequence to install thmctrl on linux with
the `make` utility:

```sh
cd $THMCTRL_PATH
make install # That's it!
```

## Uninstalling thmctrl with make

To uninstall thmctrl with `make` use the next commands:

```sh
cd $THMCTRL_PATH
make uninstall # Easy, no?
```

## Getting Started

Now, with thmctrl you must only create profiles,
and change it, to use thmctrl, use the next commands.

### Get help -h/--help

To get help execute commands, like so:

```sh
thmctrl --help
thmctrl -h
```

### Dispatch a profile

This command dispatch a configuration for a specific command:

```sh
thmctrl profile $PROFILENAME # This dispatch all components of thmctrl: pycritty, wallc, qtile theme, etc
```

If you want to only dispatch `pycritty`, `wallc`, or `qtile theme`, you want to
pass the other flag named: `-S`/`--dispatch`, like so:

```sh
thmctrl profile $PROFILENAME -S all # This dispatch all components (this is the default)
thmctrl profile $PROFILENAME -S qtile
thmctrl profile $PROFILENAME -S wallc
thmctrl profile $PROFILENAME -S pycritty
thmctrl profile $PROFILENAME -S gtk
thmctrl profile $PROFILENAME -S shell
```

or with `--dispatch`:

```sh
thmctrl profile $PROFILENAME --dispatch all
thmctrl profile $PROFILENAME --dispatch qtile
thmctrl profile $PROFILENAME --dispatch wallc
thmctrl profile $PROFILENAME --dispatch pycritty
thmctrl profile $PROFILENAME --dispatch gtk
thmctrl profile $PROFILENAME --dispatch shell
```

### Getting the selected profile information

To get the selected profile information use the flag
`-G`/`--get` and pass `full` or `compact`, the `compact` mode, only
show the name of selected profile, but it validate if the selected
profile exists, and the `full` mode, show all flags of existent profile,
see this example:

```sh
thmctrl profile onedark -G compact
```

```
=> [  INF  ] Profile name: onedark
```

```sh
thmctrl profile onedarks -G compact
```

```
=> [  ERR  ] The requested name doesn't exists in config file
```

```sh
thmctrl profile onedark -G full
```

```yaml
onedark:
  pycritty:
    font: Agave
    opacity: '0.95'
    padding:
      x: '0'
      y: '0'
    size: '17'
    theme: onedark
  qtile:
    theme: onedark
  wallc:
    extension: jpg
    wallpaper: '18'
  shell:
    executable:
      /usr/bin/fish
    init:
      omf theme spacefish
  gtk:
    cursor:
      Breeze
    icon:
      Material-Black-Plum-Suru
    theme:
      Material-Black-Plum
```

### Getting all profiles

To get all created profiles you want to use the command `config` with the flag
`--get` or `-G` like so:

```sh
thmctrl config --get # or
thmctrl config -G
```

To get only the names use the `profiles` command, like so:

```sh
thmctrl profiles -A
```

### Fetching a specific profile

To fetch a specific profile by name use the command `config` with the flag
`--fetch` or `-F`

```sh
thmctrl config --fetch $PROFILENAME # or
thmctrl config -F $PROFILENAME
```

### Creating a profile

To create a profile you want to consider the next conditions,

- **pycritty theme**: You want to like a pycritty theme (alacritty)
- **wallc wallpaper**: You want to like a wallc wallpaper and setup wallc (wallpaper)
- **antonio sarosi dotfiles**: You want to use the core of antonio sarosi dotfiles (qtile)
- **various shells (optional)**: This is not necesary, if you want to use any bash, it's right!
- **gtk**: All linux distros use gtk for render the theme of the graphical apps.

The subcommand to create a profile is `create` of command `config` with the following flags:

- `-pt`/`--pycritty-theme`
- `-po`/`--pycritty-opacity`
- `-ppx`/`--pycritty-padding-x`
- `-ppy`/`--pycritty-padding-y`
- `-pf`/`--pycritty-font`
- `-ps`/`--pycritty-size`
- `-wn`/`--wallc-wallpaper-name`
- `-we`/`--wallc-extension-extension` (default jpg)
- `-qt`/`--qtile-theme`
- `-S`/`--shell`
- `-Si`/`--shell-init` (used for change the shell theme) (optional)
- `-gtk`/`--gtk-theme`
- `--gtk-cursor`
- `--gtk-icon`

And the following positional parameters:

- `name`

**Note**: Use the command `thmctrl config create --help` to get more
information about the flags.

An example cli command is:

```sh
thmctrl config create onedark -pt onedark -ps 17 -pf Agave -po 0.95 -ppx 0 -ppy 0 -wn 18 \
-qt onedark -S $(which fish) -Si 'omf theme spacefish' -gtk Material-Black-Plum \
--gtk-cursor Breeze --gtk-icon Material-Black-Plum-Suru

# Or:

thmctrl config create material-ocean --pycritty-theme material-ocean --pycritty-size 12 \
--pycritty-font UbuntuMono --pycritty-opacity 1 --pycritty-padding-x 0 --pycritty-padding-y 0 \
--wallc-wallpaper-name 01 --wallc-wallpaper-extension png --qtile-theme material-ocean \
--gtk-theme Material-Black-Plum --gtk-cursor Breeze --gtk-icon Material-Black-Plum-Suru \
--shell $(which bash)
```

The before commands create two profiles: `onedark` and `material-ocean` with the next config:

```yaml
profiles:
  onedark:
    pycritty:
      font: Agave
      opacity: '0.95'
      padding:
        x: '0'
        y: '0'
      size: '17'
      theme: onedark
    qtile:
      theme: onedark
    wallc:
      extension: jpg
      wallpaper: '18'
    shell:
      executable:
        /usr/bin/fish
      init:
        omf theme spacefish
    gtk:
      cursor:
        Breeze
      icon:
        Material-Black-Plum-Suru
      theme:
        Material-Black-Plum
  material-ocean:
    pycritty:
      font: UbuntuMono
      opacity: '1'
      padding:
        x: '0'
        y: '0'
      size: '12'
      theme: material-ocean
    qtile:
      theme: material-ocean
    wallc:
      extension: png
      wallpaper: '01'
    shell:
      executable:
        /usr/bin/bash
```

If you want to edit the config, use the your favorite editor:

```sh
nvim ~/.thmctrl.yaml # or code, or codium, or sublime_text, or vim, etc
```

## Showing the used theme

To show the used theme, you want to use the command `used`:

```sh
thmctrl used
```

```yaml
onedark:
  pycritty:
    font: Agave
    opacity: '0.95'
    padding:
      x: '0'
      y: '0'
    size: '17'
    theme: onedark
  qtile:
    theme: onedark
  wallc:
    extension: jpg
    wallpaper: '18'
  shell:
    executable:
      /usr/bin/fish
    init:
      omf theme spacefish
  gtk:
    cursor:
      Breeze
    icon:
      Material-Black-Plum-Suru
    theme:
      Material-Black-Plum
```

Or, if you want to show only the name use the flag: `-C`/`--compact`:

```sh
thmctrl used -C
# Or
thmctrl used --compact
```

```
=> [  INF  ] Used theme: "onedark"
```

If you not are using a theme with thmctrl, it display an error:

```
=> [  ERR  ] No theme used
```

## Examples

### Getting your new config:

```sh
thmctrl config --get
# Or:
thmctrl config -G
```

Generate the next output:

```
profiles:
  onedark:
    pycritty:
      font: Agave
      opacity: '0.95'
      padding:
        x: '0'
        y: '0'
      size: '17'
      theme: onedark
    qtile:
      theme: onedark
    wallc:
      extension: jpg
      wallpaper: '18'
    shell:
      executable:
        /usr/bin/fish
      init:
        omf theme spacefish
    gtk:
      cursor:
        Breeze
      icon:
        Material-Black-Plum-Suru
      theme:
        Material-Black-Plum
  material-ocean:
    pycritty:
      font: UbuntuMono
      opacity: '1'
      padding:
        x: '0'
        y: '0'
      size: '12'
      theme: material-ocean
    qtile:
      theme: material-ocean
    wallc:
      extension: png
      wallpaper: '01'
    shell:
      executable:
        /usr/bin/bash
```

### Fetching a specific profile

```sh
thmctrl config -F onedark
```

This generate the next output:

```
onedark:
  pycritty:
    font: Agave
    opacity: '0.95'
    padding:
      x: '0'
      y: '0'
    size: '17'
    theme: onedark
  qtile:
    theme: onedark
  wallc:
    extension: jpg
    wallpaper: '18'
  shell:
    executable:
      /usr/bin/fish
    init:
      omf theme spacefish
  gtk:
    cursor:
      Breeze
    icon:
      Material-Black-Plum-Suru
    theme:
      Material-Black-Plum
```

### Creating an advanced profile

An advanced profile contains good features for a good pc look, for it
now, my currently `thmctrl` theme is `spectrwm-material`, now, I using
`spectrwm` for it, I create this profile, the command to create it profile
is the next:

```sh
thmctrl config create spectrwm-material -pt material-ocean -po 1 -ppx 0 \
-ppy 0 -pf UbuntuMono -ps 12 -gtk Material-Black-Plum --gtk-cursor Breeze \
--gtk-icon Material-Black-Plum-Suru -we jpg -wn 08 -S $(which fish) \
-Si "omf theme spacefish" -qt material-ocean
```

It create the next profile config:

```sh
thmctrl config -F spectrwm-material
```

```yaml
spectrwm-material:
  gtk:
    cursor:
      Breeze
    icon:
      Material-Black-Cherry-Suru
    theme:
      Material-Black-Cherry
  pycritty:
    font:
      UbuntuMono
    opacity:
      1
    padding:
      x:
        0
      y:
        0
    size:
      12
    theme:
      material-ocean
  qtile:
    theme:
      material-ocean
  shell:
    executable:
      /usr/bin/fish
    init:
      omf theme agnoster
  wallc:
    extension:
      jpg
    wallpaper:
      08
```

### An example advanced configuration file

An advanced configuration files contains various profiles, my config
file looks as this:

```yaml
profiles:
  agave-ayu:
    gtk:
      cursor: Breeze
      icon: Material-Black-Plum-Suru
      theme: Material-Black-Plum
    pycritty:
      font: Agave
      opacity: '0.90'
      padding:
        x: '0'
        y: '0'
      size: '16'
      theme: onedark
    qtile:
      theme: onedark
    shell:
      executable: /usr/bin/fish
      init: omf theme spacefish
    wallc:
      extension: jpg
      wallpaper: '03'
  ayu-mirage:
    gtk:
      cursor: Breeze
      icon: Material-Black-Plum-Suru
      theme: Material-Black-Plum
    pycritty:
      font: UbuntuMono
      opacity: '0.90'
      padding:
        x: '0'
        y: '0'
      size: '12'
      theme: onedark
    qtile:
      theme: onedark
    shell:
      executable: /bin/bash
    wallc:
      extension: jpg
      wallpaper: '03'
  chill-material-darker:
    gtk:
      cursor: Breeze
      icon: Material-Black-Plum-Suru
      theme: Material-Black-Plum
    pycritty:
      font: UbuntuMono
      opacity: '1'
      padding:
        x: '0'
        y: '0'
      size: '12'
      theme: material-darker
    qtile:
      theme: material-darker
    shell:
      executable: /usr/bin/fish
      init: omf theme spacefish
    wallc:
      extension: jpg
      wallpaper: '32'
  custom-onedark:
    gtk:
      cursor: Breeze
      icon: Material-Black-Cherry-Suru
      theme: Material-Black-Cherry
    pycritty:
      font: Agave
      opacity: '0.90'
      padding:
        x: '0'
        y: '0'
      size: '16'
      theme: onedark
    qtile:
      theme: onedark-red
    shell:
      executable: /usr/bin/fish
      init: omf theme spacefish
    wallc:
      extension: jpg
      wallpaper: '28'
  dracula:
    gtk:
      cursor: Breeze
      icon: Material-Black-Cherry-Suru
      theme: Material-Black-Cherry
    pycritty:
      font: UbuntuMono
      opacity: '1'
      padding:
        x: '0'
        y: '0'
      size: '12'
      theme: dracula
    qtile:
      theme: dracula
    shell:
      executable: /usr/bin/fish
      init: omf theme agnoster
    wallc:
      extension: jpg
      wallpaper: '31'
  material-darker:
    gtk:
      cursor: Breeze
      icon: Material-Black-Cherry-Suru
      theme: Material-Black-Cherry
    pycritty:
      font: UbuntuMono
      opacity: '1'
      padding:
        x: '0'
        y: '0'
      size: '12'
      theme: material-darker
    qtile:
      theme: material-darker
    shell:
      executable: /usr/bin/fish
      init: omf theme agnoster
    wallc:
      extension: jpg
      wallpaper: 08
  material-ocean:
    gtk:
      cursor: Breeze
      icon: Material-Black-Plum-Suru
      theme: Material-Black-Plum
    pycritty:
      font: UbuntuMono
      opacity: '1'
      padding:
        x: '0'
        y: '0'
      size: '12'
      theme: material-ocean
    qtile:
      theme: material-ocean
    shell:
      executable: /usr/bin/fish
      init: omf theme spacefish
    wallc:
      extension: png
      wallpaper: '01'
  nord-wave:
    gtk:
      cursor: Breeze
      icon: Material-Black-Cherry-Suru
      theme: Material-Black-Cherry
    pycritty:
      font: Mononoki
      opacity: '1'
      padding:
        x: '0'
        y: '0'
      size: '12'
      theme: nord-wave
    qtile:
      theme: nord-wave
    shell:
      executable: /usr/bin/fish
      init: omf theme spacefish
    wallc:
      extension: jpg
      wallpaper: '32'
  nord-wave-blue:
    gtk:
      cursor: Breeze
      icon: Material-Black-Blueberry-Suru
      theme: Material-Black-Blueberry
    pycritty:
      font: Mononoki
      opacity: '0.90'
      padding:
        x: '0'
        y: '0'
      size: '12'
      theme: nord-wave
    qtile:
      theme: nord-wave
    shell:
      executable: /usr/bin/fish
      init: omf theme spacefish
    wallc:
      extension: jpg
      wallpaper: '32'
  onedark:
    gtk:
      cursor: Breeze
      icon: Material-Black-Plum-Suru
      theme: Material-Black-Plum
    pycritty:
      font: Agave
      opacity: '0.90'
      padding:
        x: '0'
        y: '0'
      size: '17'
      theme: onedark
    qtile:
      theme: onedark
    shell:
      executable: /usr/bin/fish
      init: omf theme spacefish
    wallc:
      extension: jpg
      wallpaper: '18'
  onedark-red:
    gtk:
      cursor: Breeze
      icon: Material-Black-Plum-Suru
      theme: Material-Black-Plum
    pycritty:
      font: UbuntuMono
      opacity: '0.90'
      padding:
        x: '0'
        y: '0'
      size: '12'
      theme: onedark
    qtile:
      theme: onedark-red
    shell:
      executable: /bin/bash
    wallc:
      extension: jpg
      wallpaper: '04'
  onedarkx:
    gtk:
      cursor: Breeze
      icon: Material-Black-Plum-Suru
      theme: Material-Black-Plum
    pycritty:
      font: Anonymice
      opacity: '0.90'
      padding:
        x: '0'
        y: '0'
      size: '12'
      theme: onedark
    qtile:
      theme: onedark
    shell:
      executable: /usr/bin/fish
      init: omf theme spacefish
    wallc:
      extension: jpg
      wallpaper: '07'
  opacitied-material-ocean:
    gtk:
      cursor: Breeze
      icon: Material-Black-Plum-Suru
      theme: Material-Black-Plum
    pycritty:
      font: UbuntuMono
      opacity: '0.90'
      padding:
        x: '0'
        y: '0'
      size: '12'
      theme: material-ocean
    qtile:
      theme: material-ocean
    shell:
      executable: /usr/bin/fish
      init: omf theme spacefish
    wallc:
      extension: png
      wallpaper: '01'
  openbox-material-darker:
    gtk:
      cursor: Breeze
      icon: Material-Black-Plum-Suru
      theme: Material-Black-Plum
    pycritty:
      font: UbuntuMono
      opacity: '1'
      padding:
        x: '0'
        y: '0'
      size: '12'
      theme: material-darker
    qtile:
      theme: material-darker
    shell:
      executable: /usr/bin/fish
      init: omf theme spacefish
    wallc:
      extension: jpg
      wallpaper: '04'
  openbox-onedark:
    gtk:
      cursor: Breeze
      icon: Material-Black-Plum-Suru
      theme: Material-Black-Plum
    pycritty:
      font: UbuntuMono
      opacity: '0.90'
      padding:
        x: '0'
        y: '0'
      size: '12'
      theme: onedark
    qtile:
      theme: onedark
    shell:
      executable: /usr/bin/fish
      init: omf theme spacefish
    wallc:
      extension: jpg
      wallpaper: '04'
  plum-dracula:
    gtk:
      cursor: Breeze
      icon: Material-Black-Plum-Suru
      theme: Material-Black-Plum
    pycritty:
      font: UbuntuMono
      opacity: '1'
      padding:
        x: '0'
        y: '0'
      size: '12'
      theme: dracula
    qtile:
      theme: dracula
    shell:
      executable: /usr/bin/fish
      init: omf theme agnoster
    wallc:
      extension: jpg
      wallpaper: '31'
  primitive-material-ocean:
    gtk:
      cursor: Breeze
      icon: Material-Black-Plum-Suru
      theme: Material-Black-Plum
    pycritty:
      font: UbuntuMono
      opacity: '0.90'
      padding:
        x: '0'
        y: '0'
      size: '12'
      theme: material-ocean
    qtile:
      theme: primitive-material
    shell:
      executable: /bin/bash
    wallc:
      extension: jpg
      wallpaper: '04'
  rosepine:
    gtk:
      cursor: Material-Black-Plum
      icon: Material-Black-Plum
      theme: Material-Black-Plum
    pycritty:
      font: Mononoki
      opacity: '1'
      padding:
        x: '0'
        y: '0'
      size: '12'
      theme: rosepine
    qtile:
      theme: rosepine
    shell:
      executable: /usr/bin/fish
      init: omf theme spacefish
    wallc:
      extension: jpg
      wallpaper: '32'
  simple-dracula:
    gtk:
      cursor: Breeze
      icon: Material-Black-Plum-Suru
      theme: Material-Black-Plum
    pycritty:
      font: Agave
      opacity: '1'
      padding:
        x: '0'
        y: '0'
      size: '12'
      theme: dracula
    qtile:
      theme: dracula
    shell:
      executable: /usr/bin/fish
      init: omf theme agnoster
    wallc:
      extension: jpg
      wallpaper: '02'
  simple-material:
    gtk:
      cursor: Breeze
      icon: Material-Black-Plum-Suru
      theme: Material-Black-Plum
    pycritty:
      font: UbuntuMono
      opacity: '1'
      padding:
        x: '0'
        y: '0'
      size: '15'
      theme: material-ocean
    qtile:
      theme: material-ocean
    shell:
      executable: /bin/bash
    wallc:
      extension: png
      wallpaper: '01'
  simple-material-ocean:
    gtk:
      cursor: Breeze
      icon: Material-Black-Plum-Suru
      theme: Material-Black-Plum
    pycritty:
      font: UbuntuMono
      opacity: '0.90'
      padding:
        x: '0'
        y: '0'
      size: '12'
      theme: material-ocean
    qtile:
      theme: primitive-material-ocean
    shell:
      executable: /bin/bash
    wallc:
      extension: jpg
      wallpaper: '04'
  simple-onedark:
    gtk:
      cursor: Breeze
      icon: Material-Black-Plum-Suru
      theme: Material-Black-Plum
    pycritty:
      font: UbuntuMono
      opacity: '0.90'
      padding:
        x: '0'
        y: '0'
      size: '12'
      theme: onedark
    qtile:
      theme: onedark-red
    shell:
      executable: /bin/bash
    wallc:
      extension: jpg
      wallpaper: '04'
  spectrwm-material:
    gtk:
      cursor: Breeze
      icon: Material-Black-Cherry-Suru
      theme: Material-Black-Cherry
    pycritty:
      font: UbuntuMono
      opacity: '1'
      padding:
        x: '0'
        y: '0'
      size: '12'
      theme: material-ocean
    qtile:
      theme: material-ocean
    shell:
      executable: /usr/bin/fish
      init: omf theme agnoster
    wallc:
      extension: jpg
      wallpaper: 08
  xmonad-dracula:
    gtk:
      cursor: Breeze
      icon: Material-Black-Plum-Suru
      theme: Material-Black-Plum
    pycritty:
      font: UbuntuMono
      opacity: '1'
      padding:
        x: '0'
        y: '0'
      size: '12'
      theme: dracula
    qtile:
      theme: dracula
    shell:
      executable: /usr/bin/fish
      init: omf theme spacefish
    wallc:
      extension: jpg
      wallpaper: '03'
  xmonad-onedark:
    gtk:
      cursor: Breeze
      icon: Material-Black-Plum-Suru
      theme: Material-Black-Plum
    pycritty:
      font: UbuntuMono
      opacity: '0.90'
      padding:
        x: '0'
        y: '0'
      size: '12'
      theme: onedark
    qtile:
      theme: onedark
    shell:
      executable: /bin/bash
    wallc:
      extension: jpg
      wallpaper: '03'
```

It contains the next profiles:

```sh
thmctrl profiles -A
```

```
Showing available profiles
  => agave-ayu
  => ayu-mirage
  => chill-material-darker
  => custom-onedark
  => dracula
  => material-darker
  => material-ocean
  => nord-wave
  => nord-wave-blue
  => onedark
  => onedark-red
  => onedarkx
  => opacitied-material-ocean
  => openbox-material-darker
  => openbox-onedark
  => plum-dracula
  => primitive-material-ocean
  => rosepine
  => simple-dracula
  => simple-material
  => simple-material-ocean
  => simple-onedark
  => spectrwm-material
  => xmonad-dracula
  => xmonad-onedark
```

If you want to test it, i recommend you install the next antonio sarosi
windows managers:

- Qtile (Required)
- Spectrwm
- Dwm
- Xmonad
- Openbox (Unrequired, but required for openbox-material and openbox-onedark)

In resume, all windows managers!

## Enjoy

Thanks for use `thmctrl`. If you like this repository please
give me a star :)

**Note**: If the gtk changer doesn't works for gtk 3, check the syntax
of the base gtk 3 config file, the equals (`=`) want to be as this:

```conf
gtk-button-images=0
```
