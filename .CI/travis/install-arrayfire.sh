#!/bin/bash
# Copyright (c) 2018 Shapelets.io
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

if [[ "$TRAVIS_OS_NAME" == "osx" ]]; then
    brew install --force fftw freeimage fontconfig glfw glbinding
    if [ ! -e "./installers/ArrayFire-v3.6.2_OSX_x86_64.pkg" ]; then
        wget http://arrayfire.s3.amazonaws.com/3.6.2/ArrayFire-v3.6.2_OSX_x86_64.pkg -O installers/ArrayFire-v3.6.2_OSX_x86_64.pkg
    fi

    # Installs arrayfire
    sudo installer -pkg ./installers/ArrayFire-v3.6.2_OSX_x86_64.pkg -target /
else
    if [ ! -e "./installers/arrayfire-no-gl.sh" ]; then
        wget https://github.com/shapelets/arrayfire/releases/download/v3.6.2/arrayfire-no-gl.sh -O installers/arrayfire-no-gl.sh
    fi

    sudo mkdir -p /opt/arrayfire-3
    sudo bash installers/arrayfire-no-gl.sh --prefix=/opt/arrayfire-3 --skip-license
    echo "/opt/arrayfire-3/lib" | sudo tee /etc/ld.so.conf.d/arrayfire.conf
    sudo ldconfig
fi
