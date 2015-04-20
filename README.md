Sane scanning to PDF
====================

xsane requires way to much configuration, this script just scans whatever is
available in the automatic document feeder.

Need duplex scans?
==================

Try the ```-d/--duplex``` switch.

You don't have an automatic document feeder?
============================================

Fear not. This script supports the flatbed as document source. If it doesn't
find an ADF or thinks the ADF is empty, it'll fall back to flatbed.
Unfortunately, you'll have to specify the number of pages then, see the
```-n/--num-pages``` parameter.
