# TFTP

# Description

Figure out how they moved the flag.

# Solution

Finding the flag in this challenge required us to know how to analyze and extract information from pcap files, as well as knowing how to decipher ROT13 encoded messages

First, I extracted the TFTP objects into a singluar directory, which I have attached.
Next, upon opening instructions.txt, we receive this ROT13 message:

GSGCQBRFAGRAPELCGBHEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA
Decoding it, we receive this message:
TFTPDOESNTENCRYPTOURTRAFFICSOWEMUSTDISGUISEOURFLAGTRANSFER.FIGUREOUTAWAYTOHIDETHEFLAGANDIWILLCHECKBACKFORTHEPLAN

We then receive this messsage:
VHFRQGURCEBTENZNAQUVQVGJVGU-QHRQVYVTRAPR.PURPXBHGGURCUBGBF
IUSEDTHEPROGRAMANDHIDITWITH-DUEDILIGENCE.CHECKOUTTHEPHOTOS

DUEDILIGENCE is the passphrase to grab the flag here, we use this command:

sudo steghide extract -sf picture3.bmp -p DUEDILIGENCE

# Flag
picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}
