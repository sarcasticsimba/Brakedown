Brakedown
=========

Converts all SVG files in a directory into a CSS file with one class per image containing the SVG as a background-image in data-uri format. Outputs a folder containing that CSS file and a HTML page displaying the converted images.

How to install
--------------
###OS X###

###Windows###
- Add `C:\Path\to\Brakedown\` to your `%PATH%` environment variable
- If you haven't done so, add `.py` to your `PATHEXT` environment variable
- Recommended: alias brakedown to `bkd`

Usage
-----
`brakedown`: grabs all SVGs in your current directory, outputs to current directory
`breakdown path/to/svgs`: grabs all SVGs in given path, outputs to given dirctory