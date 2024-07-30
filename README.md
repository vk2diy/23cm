# 23cm NBFM transceiver

An open source 23cm narrow band FM transceiver.

KiCad format, optimized for JLCPCB.

## Background

Prompted by a presentation by Richard (VK2VD) at Amateur Radio NSW on the 28th of July, 2024, this repository attempts to provide a design including all KiCad source files representing a derivative of the design by Bas de Jong (PE1JPD) with later firmware updates by Werner Mauser (JN48OL).

Various changes have been made to the design, outlined below.

## Original design details

Bas de Jong (PE1JPD)'s [original project page](http://www.pe1jpd.nl/index.php/23cm_nbfm/) describes the overall design, made in 2015, notably including [this 2016 revised schematic](docs/23nbfmsch32.jpg).

Werner Mauser (JN48OL)'s [forked repository](https://github.com/wemaus/23cm-NBFM-Trx) provides firmware improvements, notably including [this further revised and schematic](docs/23cm NBFM-Transceiver_col.pdf) (redrawn in KiCad 3.0).

## Changes from prior versions

 * __Schematic__: Extensive use of named labels rather than a confusing array of lines.
 * __Power supply__: Drop anachronistic fixation on old-school 13.8V DC 'charged lead acid battery level' to support a modern supply voltage (24V).
 * __MCU__: Use an MCU module instead of a bare chip in order to reduce cost, increase convenience, support USB programming, and focus the schematic on the application.
 * __Components__: As far as possible, specify SMT components that are available in 2024. Prefer to over-specify components where economically insignificant to increase longevity.

## Contents

 * __docs__: Design documentation.
 * __firmware__: Currently unaltered firmware from Werner Mauser (JN48OL).
 * __23cm-trx-kicad__: KiCad project directory for the 23cm transceiver.
