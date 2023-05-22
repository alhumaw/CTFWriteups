# Disk, disk, sleuth! II

# Description 

All we know is the file with the flag is named `down-at-the-bottom.txt`... Disk image: dds2-alpine.flag.img.gz

# Solution

Finding this flag involved learning how to utilize Sleuthkit to forensically browse through a disk image.
Through the description, I derived that we can find the inode number by grepping for "down-at-the-bottom"

"fls -r -o 2048 dds2-alpine.flag.img | grep down"
This command recursively searches through the image after the offset of the linux kernel for any files that have the characters "down"

Once I got the output of that, we received the inode and was able to utilize the "icat" command to view the file:

"icat -o 2048 dds2-alpine.flag.img 18291"

# flag 

picoCTF{f0r3ns1c4t0r_n0v1c3_0ba8d02d}

