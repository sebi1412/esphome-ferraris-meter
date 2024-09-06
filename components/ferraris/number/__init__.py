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

from esphome.components import number
from esphome.const      import (
    ENTITY_CATEGORY_CONFIG,
    UNIT_KILOWATT_HOURS
)
from ..                 import (
    ferraris_ns,
    FerrarisMeter,
    CONF_FERRARIS_ID
)


EnergyTargetValueNumber = ferraris_ns.class_("EnergyTargetValueNumber", number.Number)

CONF_ENERGY_TARGET_VALUE = "energy_target_value"

CONFIG_SCHEMA = cv.Schema(
{
    cv.GenerateID(CONF_FERRARIS_ID): cv.use_id(FerrarisMeter),
    cv.Optional(CONF_ENERGY_TARGET_VALUE): number.number_schema(
        EnergyTargetValueNumber,
        icon="mdi:counter",
        unit_of_measurement=UNIT_KILOWATT_HOURS,
        entity_category=ENTITY_CATEGORY_CONFIG
    )
})


async def to_code(config):
    cmp = await cg.get_variable(config[CONF_FERRARIS_ID])

    if CONF_ENERGY_TARGET_VALUE in config:
        num = await number.new_number(
                            config[CONF_ENERGY_TARGET_VALUE],
                            min_value=0,
                            max_value=1000000,
                            step=0.01)
        await cg.register_parented(num, config[CONF_FERRARIS_ID])
        cg.add(cmp.set_energy_target_value_number(num))
