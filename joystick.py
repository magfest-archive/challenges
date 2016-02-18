#!/usr/bin/python3
import ioctl_opt
import fcntl
import ctypes
import collections

class devinfo(ctypes.Structure):
  _fields_ = [
    ('bustype', ctypes.c_uint),
    ('vendor', ctypes.c_short),
    ('product', ctypes.c_short),
  ]

HIDIOCGRAWINFO = ioctl_opt.IOR(ord('H'), 0x03, devinfo)
device = open("/dev/hidraw0", "r")
controllerinfo = devinfo()
fcntl.ioctl(device, HIDIOCGRAWINFO, controllerinfo, True)
vendor = controllerinfo.vendor
product = controllerinfo.product

buttonsa = {
  1:"y",
  2:"b",
  4:"select",
  8:"start",
  16:"left",
  32:"down",
  64:"right",
  128:"up"
}
buttonsb = {
  1:"x",
  2:"a",
  4:"l",
  8:"r",
  16:"",
  32:"",
  64:"",
  128:""
}

with open("/dev/hidraw0", "r") as joy:
  while True:
    buttons = [ord(x) for x in joy.read(4)[2:]]
    change = buttons[0] & ~oldbuttons[0]
    if change:
      print("a{0:08b}".format(change))
      print(buttonsa[change])
    change = buttons[1] & ~oldbuttons[1]
    if change:
      print("b{0:08b}".format(change))
      print(buttonsb[change])
    oldbuttons = buttons

