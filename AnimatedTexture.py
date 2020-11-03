"""
This script generates an AnimatedTexture resource file from a list of
numbered images.

Author:
    Fernando Cosentino
    https://github.com/fbcosentino/godot-AnimatedTexture-from-blender

"""

from __future__ import print_function
import sys


def GetInput(prompt):
    """Gets input from console using the corresponding function 
    based on python version"""
    
    if sys.version_info[0] < 3:
        value = raw_input(prompt)
    else:
        value = input(prompt)
    
    return value
        

        

def Generate(image_prefix, number_of_digits, file_extension, frames):
    """Generates the string content of the file"""


    result = "[gd_resource type=\"AnimatedTexture\" load_steps="+str(frames+1)+" format=2]\n\n"
    # Temporary variable holding ext_resource section
    ext_res = ""
    # Temporary variable holding frames section
    frames_res = "[resource]\nflags = 7\nframes = "+str(frames)+"\nfps = 24.0\n"
    
    for i in range(frames):
        # File number
        num_str = str(i+1)
        # Add padding zeros
        while len(num_str) < number_of_digits:
            num_str = '0'+num_str
        # Add file to ext_resource section
        ext_res += "[ext_resource path=\"res://"+image_prefix+num_str+file_extension+"\" type=\"Texture\" id="+str(i+1)+"]\n"
        # Add item to frames section
        frames_res += "frame_"+str(i)+"/texture = ExtResource( "+str(i+1)+" )\n"
        if i > 0:
            frames_res += "frame_"+str(i)+"/delay_sec = 0.0\n"
            
    result += ext_res+"\n"+frames_res
    return result
    
if __name__ == "__main__":
    print("Complete prefix for the image files:")
    print("    Ex.1: images/my_loop/")
    print("    Ex.2: folder/subfolder/image_")
    location = GetInput("res://")
    
    print("\nNumber of digits (ex: for '0001.jpg' use 4):")
    digits = int(GetInput("Digits: "))
    
    print("\nFile extension (including the dot, ex: .png):")
    num_str = '1'
    while len(num_str) < digits:
        num_str = '0'+num_str
    extension = GetInput("Extension: "+num_str)
    
    frames = int(GetInput("\nNumber of frames: "))
    
    result = Generate(location, digits, extension, frames)
    
    with open("animatedtexture_output.tres", "w") as f: 
        f.write(result)

    print("\nOutput written to animatedtexture_output.tres")