# Copyright 2018 Xanadu Quantum Technologies Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Unit tests for the :mod:`pennylane.templates` module.
"""
# pylint: disable=protected-access,cell-var-from-loop
import pytest
import numpy as np
import pennylane as qml
from pennylane.plugins import DefaultGaussian
from pennylane.templates.layers import (CVNeuralNetLayers, CVNeuralNetLayer,
                                        StronglyEntanglingLayers, StronglyEntanglingLayer,
                                        RandomLayers, RandomLayer)
from pennylane.templates.parameters import (parameters_stronglyentanglinglayers_uniform, parameters_stronglyentanglinglayer_uniform,
                                            parameters_randomlayers_uniform, parameters_randomlayer_uniform,
                                            parameters_cvqnnlayers_uniform, parameters_cvqnnlayer_uniform)


class DummyDevice(DefaultGaussian):
    """Dummy device to allow Kerr operations"""
    _operation_map = DefaultGaussian._operation_map.copy()
    _operation_map['Kerr'] = lambda *x, **y: np.identity(2)


class TestParameterIntegration:
    """ Integration tests for the parameter generation methods from pennylane.templates.parameters
    and pennylane.templates.layers."""

    def test_integration_cvqnn_layers(self, gaussian_device, n_subsystems, n_layers):
        """Checks that the pennylane.templates.parameters.parameters_cvqnn_layers() integrates
        with pennnylane.templates.layers.CVNeuralNetLayers()."""

        p = parameters_cvqnnlayers_uniform(n_layers=n_layers, n_wires=n_subsystems)

        @qml.qnode(gaussian_device)
        def circuit(weights):
            CVNeuralNetLayers(*weights, wires=range(n_subsystems))
            return qml.expval.Identity(0)

        circuit(weights=p)

    def test_integration_cvqnn_layer(self, gaussian_device, n_subsystems):
        """Checks that the pennylane.templates.parameters.parameters_cvqnn_layer() integrates
        with pennnylane.templates.layers.CVNeuralNetLayer()."""

        p = parameters_cvqnnlayer_uniform(n_wires=n_subsystems)

        @qml.qnode(gaussian_device)
        def circuit(weights):
            CVNeuralNetLayer(*weights, wires=range(n_subsystems))
            return qml.expval.Identity(0)

        circuit(weights=p)

    def test_integration_stronglyentangling_layers(self, qubit_device, n_subsystems, n_layers):
        """Checks that the pennylane.templates.parameters.parameters_stronglyentangling_layers() integrates
        with pennnylane.templates.layers.StronglyEntanglingLayers()."""

        p = parameters_stronglyentanglinglayers_uniform(n_layers=n_layers, n_wires=n_subsystems)

        @qml.qnode(qubit_device)
        def circuit(weights):
            StronglyEntanglingLayers(*weights, wires=range(n_subsystems))
            return qml.expval.Identity(0)

        circuit(weights=p)

    def test_integration_stronglyentangling_layer(self, qubit_device, n_subsystems):
        """Checks that the pennylane.templates.parameters.parameters_stronglyentangling_layer() integrates
        with pennnylane.templates.layers.StronglyEntanglingLayer()."""

        p = parameters_stronglyentanglinglayer_uniform(n_wires=n_subsystems)

        @qml.qnode(qubit_device)
        def circuit(weights):
            StronglyEntanglingLayer(*weights, wires=range(n_subsystems))
            return qml.expval.Identity(0)

        circuit(weights=p)

    def test_integration_random_layers(self, qubit_device, n_subsystems, n_layers):
        """Checks that the pennylane.templates.parameters.parameters_random_layers() integrates
        with pennnylane.templates.layers.RandomLayers()."""

        p = parameters_randomlayers_uniform(n_layers=n_layers, n_wires=n_subsystems)

        @qml.qnode(qubit_device)
        def circuit(weights):
            RandomLayers(*weights, wires=range(n_subsystems))
            return qml.expval.Identity(0)

        circuit(weights=p)

    def test_integration_random_layer(self, qubit_device, n_subsystems):
        """Checks that the pennylane.templates.parameters.parameters_random_layer() integrates
        with pennnylane.templates.layers.RandomlingLayer()."""

        p = parameters_randomlayer_uniform(n_wires=n_subsystems)

        @qml.qnode(qubit_device)
        def circuit(weights):
            RandomLayer(*weights, wires=range(n_subsystems))
            return qml.expval.Identity(0)

        circuit(weights=p)