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

### Running the install script

Now you want to run the install script, like so:

```sh
pwd
# /home/USER/repo/thmctrl
./install.sh
# Installation process!
thmctrl --help
```

### (optional) without the install script (manually)

If you don't want to use the install script, you want to
install manually thmctrl using the terminal executing a commands,
like so:

```sh
pwd
# /home/USER/repo/thmctrl
sudo mkdir /opt/thmctrl
sudo cp -r ./* /opt/thmctrl
sudo chmod -R 777 /opt/thmctrl /opt/thmctrl/*
sudo chown -R USER:USER /opt/thmctrl
sudo ln -s /usr/bin/thmctrl /opt/thmctrl/src/main.py
sudo chmod -R 777 /usr/bin/thmctrl
sudo chown USER:USER /usr/bin/thmctrl
thmctrl --help
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
thmctrl profile PROFILENAME # This dispatch all components of thmctrl: pycritty, wallc, qtile theme.
```

If you want to only dispatch `pycritty`, `wallc`, or `qtile theme`, you want to
pass the other flag named: `-S`/`--dispatch`, like so:

```sh
thmctrl profile PROFILENAME -S all # This dispatch all components (this is the default)
thmctrl profile PROFILENAME -S qtile
thmctrl profile PROFILENAME -S wallc
thmctrl profile PROFILENAME -S pycritty
```

or with `--dispatch`:

```sh
thmctrl profile PROFILENAME --dispatch all
thmctrl profile PROFILENAME --dispatch qtile
thmctrl profile PROFILENAME --dispatch wallc
thmctrl profile PROFILENAME --dispatch pycritty
```

### Getting all profiles

To get all created profiles you want to use the command `config` with the flag
`--get` or `-G` like so:

```sh
thmctrl config --get # or
thmctrl config -G
```

### Fetching a specific profile

To fetch a specific profile by name use the command `config` with the flag
`--fetch` or `-F`

```sh
thmctrl config --fetch PROFILENAME # or
thmctrl config -F PROFILENAME
```

### Creating a profile

To create a profile you want to consider the next conditions,

- **pycritty theme**: You want to like a pycritty theme (alacritty)
- **wallc wallpaper**: You want to like a wallc wallpaper and setup wallc (wallpaper)
- **antonio sarosi dotfiles**: You want to use the core of antonio sarosi dotfiles (qtile)

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

And the following positional parameters:

- `name`

An example cli command is:

```sh
thmctrl config create onedark -pt onedark -ps 17 -pf Agave -po 0.95 -ppx 0 -ppy 0 -wn 18 -qt onedark # or

thmctrl config create material-ocean --pycritty-theme material-ocean --pycritty-size 12 \
--pycritty-font UbuntuMono --pycritty-opacity 1 --pycritty-padding-x 0 --pycritty-padding-y 0 \
--wallc-wallpaper-name 01 --wallc-wallpaper-extension png --qtile-theme material-ocean
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
```

## Examples

### Getting your new config:

```sh
thmctrl config --get
```

Generate the next output:

```
profiles:
  onedark:
    pycritty:
      font:
        Agave
      opacity:
        0.95
      padding:
        x:
          0
        y:
          0
      size:
        17
      theme:
        onedark
    qtile:
      theme:
        onedark
    wallc:
      extension:
        jpg
      wallpaper:
        18
  material-ocean:
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
    wallc:
      extension:
        png
      wallc:
        extension:
          png
        wallpaper:
          01
```

### Fetching a specific profile

```sh
thmctrl config -F onedark
```

This generate the next output:

```
onedark:
  pycritty:
    font:
      Agave
    opacity:
      0.95
    padding:
      x:
        0
      y:
        0
    size:
      17
    theme:
      onedark
  qtile:
    theme:
      onedark
```
## Enjoy

Thanks for use `thmctrl`. If you like this repository please
give me a star :)
