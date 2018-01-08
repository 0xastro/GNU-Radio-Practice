# GNU-Radio-Practice
A PLAYGROUND for GNU Radio apps!

### Installation
Its recommended to install GNU Radio with PyBOMBS
or 
for MAC OS X: port install gnuradio
for linux OS: apt-get install gnuradio

### Source Build

To build any oot(out of tree) module manually from source, follow this procedure.


1. `$ cd gr-2trxmimo`
2. `$ mkdir build`
3. `$ cd build`
4. `$ cmake ../` or `$ cmake -DCMAKE_INSTALL_PREFIX=<path_to_install> ../`
5. `$ make`
6. `$ sudo make install`
7. `$ sudo ldconfig`

#### https://readthedocs.org
#### Benchmarks https://wiki.gnuradio.org/index.php/HowToUse
#### Useful OOT MODULES TO BE INSTALLED (gr-inspecor gr-lte gr-ieee802-11)
