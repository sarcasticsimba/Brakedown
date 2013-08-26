Brakedown
=========

Converts all SVG files in a directory into a CSS file with one class per image containing the SVG as a background-image in data-uri format. Outputs a folder containing that CSS file and a HTML page displaying the converted images.

How to install
--------------
Well, it's a python script. Run it as usual. `python brakedown.py path/to/svgs`

But if you want to be a Brakedown Power User<sup>tm</sup>, you can do the following:

###OS X###
- Add `path/to/Brakedown` to your $PATH

Do one of the following:
- Create a symlink to Brakedown (suggested name: bkd)
OR
- Chop off the `.py` extension
- Alias Brakedown to anything you'd like (If you haven't caught on, I suggest `bkd`)

###Windows###
- Add `C:\Path\to\Brakedown\` to your `%PATH%` environment variable
- If you haven't done so, add `.py` to your `PATHEXT` environment variable
- Psst, you should totally alias Brakedown to `bkd`, all the cool kids are doing it

Usage
-----
`bkd`: grabs all SVGs in your current directory, outputs to current directory

`bkd path/to/svgs`: grabs all SVGs in given path, outputs to given dirctory