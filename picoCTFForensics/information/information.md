# Information

# Description
Files can always be changed in a secret way. Can you find the flag? cat.jpg

# Approach
The flag in this challenge can be found using "exiftool". This tool allows us to view the metadata of a file.
Sure enough, when we view the metadata of the file we find this weird section:

License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9

This is a base64 encoded message. It's important to be able to identify when stuff like this pops up.

# Flag
 picoCTF{the_m3tadata_1s_modified}
