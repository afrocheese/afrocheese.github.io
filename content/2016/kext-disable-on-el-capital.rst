Disable KEXT Validation on El Capitan (10.11)
#############################################

:date: 2016
:tags: android
:category: android
:authors: Charles Holmes
:summary: 
    Let's disable some kext

Introduction
------------
OS X has recently made it more difficult to load arbitrary KEXT which is great for security, but it's very annoying when you're trying to developer a driver. 

Sign the KEXT
-------------
Often the KEXT won't be signed due to XCode restricting that behavior. It's often easier to just sign it with your own certificate, but you need to create that certificate first. Launch Keychain Access, select the "Keychain Access" menu, "Certificate Assistant" menu, and "Create a Certificate..." option.

.. figure:: /static/kext/kext-create-certificate.png
    :align: center
    :alt: example of creating a certificate
    :width: 75%
 
To manually sign the kext, run the command below.

.. code-block:: bash

    $ codesign -fs "KEXTSigner" TESTKEXT.kext/Contents/MacOS/TESTKEXT
    TESTKEXT.kext/Contents/MacOS/TESTKEXT: replacing existing signature

Enable KEXT Loading
-------------------
The first step is to boot into recovery mode (instructions: https://support.apple.com/en-us/HT201314). tldr; Reboot and hold Command+r. 

Once in Recovery Mode, bring up Terminal 

.. code-block:: bash

    $ csrutil disable
    Successfully disabled System Integrity Protection. Please restart the machine for the changes to take effect.
    $ csrutil enable --without kext
    csrutil: requesting an unsupported configuration. This is likely to break in the future and leave your machine in an unknown state.
    Successfully enabled System Integrity Protection. Please restart the machine for the changes to take effect.

Load the KEXT
-------------
All KEXTs need to be owned by root:wheel before being loaded. So we verify this and load the kext. Once it's loaded, we can make sure it's running by usign kextstat.

.. code-block:: bash

    $ sudo chown -R root:wheel TESTKEXT.kext 
    $ sudo kextload TESTKEXT.kext
    $ kextstat | grep -i test
    154    0 0xffffff7f82f42000 0x5000     0x5000     test.usb_device (1) ABCDEF-1234-5678-ABCDEFGHIJKL <15 4 3>




