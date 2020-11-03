# Godot - AnimatedTexture resource from Blender

This is a simple python script to create an AnimatedTexture resource file for Godot, 
matching a series of frames in the typical output format from blender. Tested with 3.2.3.

When rendering animations from blender as separate image files for each frame, 
they are typically named in a numbered sequence, such as:

```
0001.png
0002.png
0003.png
0004.png
0005.png
0006.png
0007.png
0008.png
(...etc)
```

Place those images in a folder inside your project (e.g. `res://animations/anim1/`),
and run the script in the console. The script is interactive and will request information input as needed:

- **The location the images are going to be** (in this case, `animations/anim1/`)

It can have an optional prefix. So e.g. if your files are:

```
res://animations/anim1/run_0001.png
res://animations/anim1/run_0002.png
res://animations/anim1/run_0003.png
res://animations/anim1/run_0004.png
```

Your location prefix will be `animations/anim1/run_`

- **The number of digits in the numeric part of the file names** 

In all examples shown here it is **4** (which is the default from blender), but you can have any number of digits.

- **The file extension**

Enter the extension including the dot, e.g. `.png`

If your files have a suffix you can also enter it here (e.g. `_big.png` if the files from the example above are called `res://animations/anim1/run_0001_big.png`)

- **Number of frames**

The numbering system in file names starts from 1, so if your number of frames is 3, they will be `0001`, `0002` and `0003` (unlike indices which would be `0`, `1` and `2`).


Finally, the script will output a file named `animatedtexture_output.tres` (in the folder where the script was invoked), which can be renamed at will. 