#!/bin/bash
# Copyright (c) 2018 Shapelets.io
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

if [ ! -e "installers/khiva-v0.1.0.pkg" ]; then
    wget https://github.com/shapelets/khiva/releases/download/v0.1.0/khiva-v0.1.0.pkg -O installers/khiva-v0.1.0.pkg
fi

# Installs arrayfire
sudo installer -pkg installers/khiva-v0.1.0.pkg -target /
