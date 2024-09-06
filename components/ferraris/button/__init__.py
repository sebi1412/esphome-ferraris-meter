# Copyright (c) 2024 Jens-Uwe Rossbach
#
# This code is licensed under the MIT License.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import esphome.codegen           as cg
import esphome.config_validation as cv

from esphome.components import button
from esphome.const      import (
    DEVICE_CLASS_BUTTON,
    ENTITY_CATEGORY_CONFIG
)
from ..                 import (
    ferraris_ns,
    FerrarisMeter,
    CONF_FERRARIS_ID
)


EnergyMeterSetButton = ferraris_ns.class_("EnergyMeterSetButton", button.Button)

CONF_SET_ENERGY_METER = "set_energy_meter"

CONFIG_SCHEMA = cv.Schema(
{
    cv.GenerateID(CONF_FERRARIS_ID): cv.use_id(FerrarisMeter),
    cv.Optional(CONF_SET_ENERGY_METER): button.button_schema(
        EnergyMeterSetButton,
        icon="mdi:download",
        entity_category=ENTITY_CATEGORY_CONFIG
    )
})


async def to_code(config):
    cmp = await cg.get_variable(config[CONF_FERRARIS_ID])

    if CONF_SET_ENERGY_METER in config:
        btn = await button.new_button(config[CONF_SET_ENERGY_METER])
        await cg.register_parented(btn, config[CONF_FERRARIS_ID])
        cg.add(cmp.set_energy_meter_set_button(btn))
