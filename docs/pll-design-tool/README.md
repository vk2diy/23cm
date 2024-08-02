# PLL Design Tool

The tool recommended by the manufacture of the PLL synthesis chip is [ADIsimPLL](https://www.analog.com/en/lp/resources/adisimpll.html).

## Download and install

The tool is designed for Windows but can be downloaded under Linux and run under [wine](https://www.winehq.org/).

The direct download script is as follows:

```
wget https://www.analog.com/media/en/engineering-tools/design-tools/adisimpll_v5_80_01_setup.zip && \
unzip adisimpll_v5_80_01_setup.zip && \
cd adisimpll_v5_80_01_setup && \
wine64-vanilla-9.0 ADIsimPLL_V5_80_01_setup.exe
```

Note that your `wine` instllation may required a slightly different binary name when executing the final command.

On any modern Linux, press `wine<tab><tab>` to see a list of contenders.

## Running the tool

Under Linux you can run the following command to start ADIsimPLL after installation.

```
wine64-vanilla-9.0 'c:\program files (x86)\applied radio labs\adisimpll ver 5.80\bin\simpll_ad.exe'
```

### Making things easier

There may be a better way to do this but I'm not a regular wine user.

Given this command line is a hassle to type, if you want to run this more than once you can create an alias like this:
```
alias adisimpll="wine64-vanilla-9.0 'c:\program files (x86)\applied radio labs\adisimpll ver 5.80\bin\simpll_ad.exe'"
```

Store than in your `~/.bashrc` (or other shell initialization file) in order to make it permanent.

You will now be able to run the tool by typing `adisimpll`.

## Screenshots

![image](adisim-5.8-ibs-support.jpg)
![image](adisim-5.8-new-devices.jpg)
![image](adisim-5.8-tutorial.jpg)
