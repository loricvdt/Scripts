# Scripts repository

This repo regroups all the small scripts I decided to make at some point. They are in no mean complete or well coded, they are just useful for very specific things.

Here is a list of the scripts in this repo:

- [gkeep-wallpaper.pyw](gkeep-wallpaper.pyw)

  Displays a Google Keep list on Windows' wallpaper. Uses **ctypes**, **PIL** and [**gkeepapi**](https://github.com/kiwiz/gkeepapi) Python libraries (see documentation for information). Login information, list ID and wallpaper path have to be set in the code. Use any task scheduler to update the wallpaper regularly.

- [redshift-launcher](redshift-launcher)

  Its purpose is to enable or disable (toggle) [redshift](http://jonls.dk/redshift/) at a given temperature (`redshift-launcher temperature`, see redshift usage for detailed information). Quite useful to use as a keyboard shortcut and/or on login.
  
- [add-apt-repository](add-apt-repository)

  Recreates the add-apt-repository command: just adds the "deb ..." argument to a new file in the /etc/apt/sources.list.d/ for Debian distros *(does not work with ppa)*. Mainly done because my distro wouldn't work with the normal add-apt-repository.

