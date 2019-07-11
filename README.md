## This example shows you how to sign data with the hierarchical deterministic (HD) wallet on the MIRkey Hardware Security Module

Please see the accompanying [how to guide](https://ellipticsecure.com/ehsm/how-to/2019/07/11/python-hd-wallet-example.html).

The example code can easily be converted into a utility to sign transactions offline/air-gapped or used on
Bitcoin transaction servers.

## Preparation

1. If you have not done so already, download and install the native shared library for your platform here: 
    [https://ellipticsecure.com/downloads/](https://ellipticsecure.com/downloads/)
    
    Important: Always verify the signature of the downloaded files

2. Initialize the device and set a user PIN with the eHSM Manager or pkcs11 tool

3. Install the ehsm Python wrapper

    ```bash
    pip install ehsm
    ```

## Example

Signing a transaction hash with a BIP32 (Bitcoin etc.) derived key stored on
a MIRkey or eHSM device using the derivation path "m/0/0".

```bash
./hdwallet-example.py 0,0 30440220644ff4e8877ac01ba12e72b1c1dcfee67a4d932d28b721b1249eaf16
Enter the device user PIN:
...
3045022100a26765f2e1709d2028a2ad17245d28d69bf5c5499bb32de6cd9deaff066496130220690bb4326446a413e37ad95072cb4754b559282083be079111c408ca57e85c17
```
