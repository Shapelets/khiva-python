# Copyright (c) 2018 Shapelets.io
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


########################################################################################################################
# IMPORT
########################################################################################################################
import unittest
from khiva.library import *


########################################################################################################################

class LibraryTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_set_backend(self):
        backends = get_backends()
        cuda = backends & KHIVABackend.KHIVA_BACKEND_CUDA.value
        opencl = backends & KHIVABackend.KHIVA_BACKEND_OPENCL.value
        cpu = backends & KHIVABackend.KHIVA_BACKEND_CPU.value
        b = get_backend()
        if cuda:
            set_backend(KHIVABackend.KHIVA_BACKEND_CUDA)
            self.assertEqual(get_backend(), KHIVABackend.KHIVA_BACKEND_CUDA)
            set_backend(b)

        if opencl:
            set_backend(KHIVABackend.KHIVA_BACKEND_OPENCL)
            self.assertEqual(get_backend(), KHIVABackend.KHIVA_BACKEND_OPENCL)
            set_backend(b)

        if cpu:
            set_backend(KHIVABackend.KHIVA_BACKEND_CPU)
            self.assertEqual(get_backend(), KHIVABackend.KHIVA_BACKEND_CPU)
            set_backend(b)

    def test_get_device(self):
        backends = get_backends()
        cuda = backends & KHIVABackend.KHIVA_BACKEND_CUDA.value
        opencl = backends & KHIVABackend.KHIVA_BACKEND_OPENCL.value
        cpu = backends & KHIVABackend.KHIVA_BACKEND_CPU.value
        b = get_backend()
        if cuda:
            set_backend(KHIVABackend.KHIVA_BACKEND_CUDA)
            for i in range(get_device_count()):
                set_device(i)
                self.assertEqual(get_device_id(), i)
                set_backend(b)

        if opencl:
            set_backend(KHIVABackend.KHIVA_BACKEND_OPENCL)
            for i in range(get_device_count()):
                set_device(i)
                self.assertEqual(get_device_id(), i)
                set_backend(b)

        if cpu:
            set_backend(KHIVABackend.KHIVA_BACKEND_CPU)
            for i in range(get_device_count()):
                set_device(i)
                self.assertEqual(get_device_id(), i)
                set_backend(b)

    def test_version(self):
        v = version()
        self.assertEqual(v, '0.1.0')


if __name__ == '__main__':
    unittest.main()
