#!/usr/bin/env python3
# coding=utf-8
import optparse
import time
import random
from PIL import Image
import glob,os
import matplotlib.pyplot as plt

__author__ = 'Guoliang Lin'
Softwarename = 'processingimage'
version = '0.0.1'
bugfixs = ''
__date__ = '2019/6/29'


def printinformations():
    print("%s software version is %s in %s" % (Softwarename, version, __date__))
    print(bugfixs)
    print('Starts at :' + time.strftime('%Y-%m-%d %H:%M:%S'))


def programends():
    print('Ends at :' + time.strftime('%Y-%m-%d %H:%M:%S'))


# add your options here! 
def _parse_args():
    """Parse the command line for options."""
    usage = 'usage: %prog -i INPUT -o OUTPUT'
    parser = optparse.OptionParser(usage)
    parser.add_option('-i',
                      '--input', dest='input', type='string',
                      help='input file!')
    #    parser.add_option('-f','--fpkm',dest='fpkm_file',type='string',help='input fpkm file')
    #    parser.add_option('-v','--variation', dest='variation', type='string', help='input variation information file')
    #    parser.add_option('-g', '--gff3', dest='gff', help='gff3 file')
    parser.add_option('-o', '--output', dest='output', type='string', help='output file')
    options, args = parser.parse_args()
    # positional arguments are ignored
    return options


# define your functions here!


if __name__ == '__main__':
    printinformations()
    options = _parse_args()
    # your code here!
    originalpath="./Triploid photo/"
    processedpath="./triploid/"
    for file in glob.glob(originalpath+"*.jpg"):
        # print(os.path.basename(file))
        basename=os.path.basename(file)
        im=Image.open(file)
        # print(im.mode)
        bigsize=max(im.size)
        # im.show()
        # color=random.randint(0,255)*0x010000+random.randint(0,255)*0x0100+random.randint(0,255)
        color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        print(color)
        newIM=Image.new(im.mode,(bigsize,bigsize),color)
        newIM.paste(im,(0,0,*im.size))
        # plt.imshow(newIM)
        # plt.show()
        newIM.save(processedpath+basename,format="jpeg")
    programends()