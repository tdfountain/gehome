"""ERD Codes for GE appliances"""
import enum
from typing import Union


@enum.unique
class ErdCode(enum.Enum):
    """
    ERD codes for GE kitchen appliance properties.
    These were mostly lifted from ERD.smali in the the GE SmartHQ app v1.0.3.13
    """

    APPLIANCE_TYPE = "0x0008"
    CLOCK_FORMAT = "0x0006"
    CLOCK_TIME = "0x0005"
    MODEL_NUMBER = "0x0001"
    SABBATH_MODE = "0x0009"
    SERIAL_NUMBER = "0x0002"
    SOUND_LEVEL = "0x000a"
    TEMPERATURE_UNIT = "0x0007"
    USER_INTERFACE_LOCKED = "0x0004"
    UNIT_TYPE = "0x0035"

    # Low-level-type things
    WIFI_MODULE_UPDATING = "0x0099"
    WIFI_MODULE_SW_VERSION = "0x0100"
    WIFI_MODULE_SW_VERSION_AVAILABLE = "0x0101"
    ACM_UPDATING = "0x0102"
    APPLIANCE_SW_VERSION = "0x0103"
    APPLIANCE_SW_VERSION_AVAILABLE = "0x0104"
    APPLIANCE_UPDATING = "0x0105"
    LCD_SW_VERSION = "0x0106"
    LCD_SW_VERSION_AVAILABLE = "0x0107"
    LCD_UPDATING = "0x0108"

    # Dishwasher Codes
    DISHWASHER_CYCLE_NAME = "0x301c"
    DISHWASHER_CYCLE_STATE = "0x300e"
    DISHWASHER_OPERATING_MODE = "0x3001"
    DISHWASHER_PODS_REMAINING_VALUE = "0x301f"
    DISHWASHER_REMINDERS = "0x3003"
    DISHWASHER_USER_SETTING = "0x3007"
    DISHWASHER_TIME_REMAINING = "0xd004"
    DISHWASHER_ERROR = "0x3008"
    DISHWASHER_CYCLE_COUNTS = "0x3009"
    DISHWASHER_UNKNOWN_300C = "0x300c"
    DISHWASHER_UNKNOWN_300F = "0x300f"
    DISHWASHER_UNKNOWN_301d = "0x301d"
    DISHWASHER_UNKNOWN_3035 = "0x3035"
    DISHWASHER_DOOR_STATUS = "0x3037"
    DISHWASHER_UNKNOWN_3045 = "0x3045"
    DISHWASHER_UNKNOWN_304E = "0x304e"
    DISHWASHER_UNKNOWN_3086 = "0x3086"
    DISHWASHER_UNKNOWN_3100 = "0x3100"
    #added by Nick
    DISHWASHER_IS_CLEAN = "0xd003"
    DISHWASHER_REMOTE_START_ENABLE = '0x3087'
    DISHWASHER_UNKNOWN_3200 = "0x3200"
    DISHWASHER_UNKNOWN_3210 = "0x3210"
    DISHWASHER_UNKNOWN_3211 = "0x3211"
    DISHWASHER_UNKNOWN_3212 = "0x3212"
    DISHWASHER_UNKNOWN_3213 = "0x3213"
    DISHWASHER_UNKNOWN_3214 = "0x3214"
    DISHWASHER_UNKNOWN_3215 = "0x3215"
    DISHWASHER_UNKNOWN_3216 = "0x3216"
    DISHWASHER_UNKNOWN_3217 = "0x3217"
    DISHWASHER_UNKNOWN_3218 = "0x3218"
    DISHWASHER_UNKNOWN_3219 = "0x3219"
    DISHWASHER_DELAY_START_MINUTES = "0x321a"
    DISHWASHER_CYCLE = "0x321b"
    DISHWASHER_TEMPERATURE = "0x321c"
    DISHWASHER_DRYING = "0x321d"
    DISHWASHER_WASH_ZONE = "0x321e"
    DISHWASHER_STEAM = "0x321f"
    DISHWASHER_BOTTLE_JETS = "0x3220"

    DISHWASHER_UPPER_REMINDERS = "0x3203"
    DISHWASHER_UPPER_USER_SETTING = "0x3207"
    DISHWASHER_UPPER_UNKNOWN_3208 = "0x3208"
    DISHWASHER_UPPER_UNKNOWN_3209 = "0x3209"
    DISHWASHER_UPPER_CYCLE_STATE = "0x320e"
    DISHWASHER_UPPER_UNKNOWN_320F = "0x320f"
    DISHWASHER_UPPER_UNKNOWN_3222 = "0x3222"
    DISHWASHER_UPPER_DOOR_STATUS = "0x3237"
    DISHWASHER_UPPER_TIME_REMAINING = "0xd204"

    # Laundry Codes
    LAUNDRY_MACHINE_STATE = "0x2000"
    LAUNDRY_SUB_CYCLE = "0x2001"
    LAUNDRY_END_OF_CYCLE = "0x2002"
    LAUNDRY_TIME_REMAINING = "0x2007"
    LAUNDRY_WASHER_TANK_STATUS = "0x2008"
    LAUNDRY_WASHER_TANK_SELECTED = "0x2009"
    LAUNDRY_DELAY_TIME_REMAINING = "0x2010"
    LAUNDRY_DOOR = "0x2012"
    LAUNDRY_WASHER_DOOR_LOCK = "0x2013"
    LAUNDRY_CYCLE = "0x200a"
    LAUNDRY_DRYER_DRYNESS_LEVEL = "0x201a"
    LAUNDRY_DRYER_TUMBLE_STATUS = "0x201b"
    LAUNDRY_DRYER_LEVEL_SENSOR_DISABLED = "0x201c"
    LAUNDRY_UNKNOWN201D = "0x201d"
    LAUNDRY_WASHER_SOIL_LEVEL = "0x2015"
    LAUNDRY_WASHER_WASHTEMP_LEVEL = "0x2016"
    LAUNDRY_WASHER_SPINTIME_LEVEL = "0x2017"
    LAUNDRY_WASHER_RINSE_OPTION = "0x2018"
    LAUNDRY_DRYER_TEMPERATURE_OPTION = "0x2019"
    LAUNDRY_DRYER_SHEET_USAGE_CONFIGURATION = "0x2022"
    LAUNDRY_DRYER_SHEET_INVENTORY = "0x2023"
    LAUNDRY_REMOTE_DELAY_CONTROL = "0x2038"
    LAUNDRY_REMOTE_STATUS = "0x2039"
    LAUNDRY_WASHER_SMART_DISPENSE_TANK_STATUS = "0x203c"
    LAUNDRY_WASHER_SMART_DISPENSE = "0x203d"
    LAUNDRY_WASHER_UNKNOWN203E = "0x203e"
    LAUNDRY_REMOTE_POWER_CONTROL = "0x2040"
    LAUNDRY_UNKNOWN2041 = "0x2041"
    LAUNDRY_DRYER_UNKNOWN2045 = "0x2045"
    LAUNDRY_DRYER_UNKNOWN2046 = "0x2046"
    LAUNDRY_DRYER_UNKNOWN2047 = "0x2047"
    LAUNDRY_DRYER_UNKNOWN2049 = "0x2049"
    LAUNDRY_DRYER_DAMP_ALERT = "0x204a"
    LAUNDRY_DRYER_UNKNOWN204C = "0x204c"
    LAUNDRY_DRYER_DRYNESSNEW_LEVEL = "0x204d"
    LAUNDRY_DRYER_UNKNOWN204F = "0x204f"
    LAUNDRY_DRYER_TEMPERATURENEW_OPTION = "0x2050"
    LAUNDRY_DRYER_UNKNOWN2051 = "0x2051"
    LAUNDRY_DRYER_ECODRY_STATUS = "0x2052"
    LAUNDRY_DRYER_TUMBLENEW_STATUS = "0x2053"
    LAUNDRY_WASHER_UNKNOWN2054 = "0x2054"
    LAUNDRY_WASHER_TIMESAVER = "0x2055"
    LAUNDRY_WASHER_UNKNOWN2057 = "0x2057"
    LAUNDRY_WASHER_POWERSTEAM = "0x2058"
    LAUNDRY_WASHER_PREWASH = "0x205b"
    LAUNDRY_DRYER_UNKNOWN205D = "0x205d"
    LAUNDRY_DRYER_REDUCE_STATIC = "0x205e"
    LAUNDRY_DRYER_UNKNOWN205F = "0x205f"
    LAUNDRY_WASHER_UNKNOWN2060 = "0x2060"
    LAUNDRY_WASHER_TUMBLECARE = "0x2061"
    LAUNDRY_WASHER_UNKNOWN2069 = "0x2069"
    LAUNDRY_DRYER_WASHERLINK_CYCLE = "0x206b"
    LAUNDRY_DRYER_WASHERLINK_STATUS = "0x206c"
    LAUNDRY_DRYER_WASHERLINK_CONTROL = "0x206e"
    LAUNDRY_DRYER_UNKNOWN206F = "0x206f"
    LAUNDRY_WASHER_UNKNOWN2070 = "0x2070"
    LAUNDRY_WASHER_UNKNOWN2072 = "0x2072"

    # Fridge codes
    AIR_FILTER_STATUS = "0x101c"
    DOOR_STATUS = "0x1016"
    FRIDGE_MODEL_INFO = "0x101d"
    HOT_WATER_IN_USE = "0x1018"
    HOT_WATER_SET_TEMP = "0x1011"
    HOT_WATER_STATUS = "0x1010"
    ICE_MAKER_BUCKET_STATUS = "0x1007"
    ICE_MAKER_CONTROL = "0x100a"
    SETPOINT_LIMITS = "0x100b"
    CURRENT_TEMPERATURE = "0x1004"
    TEMPERATURE_SETTING = "0x1005"
    TURBO_COOL_STATUS = "0x100f"
    TURBO_FREEZE_STATUS = "0x100e"
    WATER_FILTER_STATUS = "0x1009"
    FRIDGE_UNKNOWN_1012 = "0x1012"
    FRIDGE_UNKNOWN_1013 = "0x1013"
    FRIDGE_UNKNOWN_1019 = "0x1019"
    CONVERTABLE_DRAWER_MODE = "0x1020"
    INTERIOR_LIGHT = "0x1024"
    PROXIMITY_LIGHT = "0x1028"
    FRIDGE_UNKONWN_1029 = "0x1029"
    LOCKOUT_MODE = "0x102c"
    DISPLAY_MODE = "0x102d"
    FRIDGE_UNKNOWN_102E = "0x102e"
    FRIDGE_UNKNOWN_1100 = "0x1100"
    FRIDGE_UNKNOWN_1101 = "0x1101"
    FRIDGE_UNKNOWN_1102 = "0x1102"
    FRIDGE_UNKNOWN_1103 = "0x1103"
    FRIDGE_UNKNOWN_1104 = "0x1104"

    # Oven codes
    ACTIVE_F_CODE_STATUS = "0x5005"
    CONVECTION_CONVERSION = "0x5003"
    ELAPSED_ON_TIME = "0x5004"
    END_TONE = "0x5001"
    HOUR_12_SHUTOFF_ENABLED = "0x5000"
    KEY_PRESSED = "0x5006"
    LIGHT_BAR = "0x5002"
    LOWER_OVEN_AVAILABLE_COOK_MODES = "0x520b"
    LOWER_OVEN_EXTENDED_COOK_MODES = "0x5213"
    LOWER_OVEN_COOK_MODE = "0x5200"
    LOWER_OVEN_COOK_TIME_REMAINING = "0x5204"
    LOWER_OVEN_CURRENT_STATE = "0x5201"
    LOWER_OVEN_DELAY_TIME_REMAINING = "0x5202"
    LOWER_OVEN_DISPLAY_TEMPERATURE = "0x5209"
    LOWER_OVEN_ELAPSED_COOK_TIME = "0x5208"
    LOWER_OVEN_KITCHEN_TIMER = "0x5205"
    LOWER_OVEN_PROBE_DISPLAY_TEMP = "0x5203"
    LOWER_OVEN_PROBE_PRESENT = "0x5207"
    LOWER_OVEN_REMOTE_ENABLED = "0x520a"
    LOWER_OVEN_USER_TEMP_OFFSET = "0x5206"
    LOWER_OVEN_WARMING_DRAWER_STATE = "0x520c"
    LOWER_OVEN_RAW_TEMPERATURE = "0x520d"
    LOWER_OVEN_LIGHT = "0x5211"
    LOWER_OVEN_LIGHT_AVAILABILITY = "0x5212"
    OVEN_CONFIGURATION = "0x5007"
    OVEN_MODE_MIN_MAX_TEMP = "0x5008"
    UPPER_OVEN_AVAILABLE_COOK_MODES = "0x510b"
    UPPER_OVEN_EXTENDED_COOK_MODES = "0x5113"
    UPPER_OVEN_COOK_MODE = "0x5100"
    UPPER_OVEN_COOK_TIME_REMAINING = "0x5104"
    UPPER_OVEN_CURRENT_STATE = "0x5101"
    UPPER_OVEN_DELAY_TIME_REMAINING = "0x5102"
    UPPER_OVEN_DISPLAY_TEMPERATURE = "0x5109"
    UPPER_OVEN_ELAPSED_COOK_TIME = "0x5108"
    UPPER_OVEN_KITCHEN_TIMER = "0x5105"
    UPPER_OVEN_PROBE_DISPLAY_TEMP = "0x5103"
    UPPER_OVEN_PROBE_PRESENT = "0x5107"
    UPPER_OVEN_REMOTE_ENABLED = "0x510a"
    UPPER_OVEN_USER_TEMP_OFFSET = "0x5106"
    UPPER_OVEN_WARMING_DRAWER_STATE = "0x510c"
    UPPER_OVEN_RAW_TEMPERATURE = "0x510d"
    UPPER_OVEN_LIGHT = "0x5111"
    UPPER_OVEN_LIGHT_AVAILABILITY = "0x5112"
    WARMING_DRAWER_STATE = "0x5009"

    COOKTOP_CONFIG = "0x551c"
    COOKTOP_STATUS = "0x5520"

    PRECISION_COOKING_PROBE_CONTROL_MODE = "0x5670"
    PRECISION_COOKING_PROBE_STATUS = "0x5671"
    PRECISION_COOKING_PROBE_TEMP_TARGET = "0x5672"  # R/W, int 4 places
    PRECISION_COOKING_PROBE_TEMP_CURRENT = "0x5673"
    PRECISION_COOKING_PROBE_TIME_TARGET = "0x5674"  # R/W, int 4 places
    PRECISION_COOKING_START_SOUS_VIDE_TIMER_ACTIVE_STATUS = "0x5675"  # R/W, int 2 places
    PRECISION_COOKING_PROBE_TIME_CURRENT = "0x5676"
    PRECISION_COOKING_PROBE_TARGET_TIME_REACHED = "0x5677"
    PRECISION_COOKING_PROBE_BATTERY_STATUS = "0x5678"

    CLOSED_LOOP_COOKING_CONFIGURATION = "0x5770"

    # Microwave
    MICROWAVE_RECIPE_STATUS = "0x5300"
    MICROWAVE_COOK_SETTING = "0x5c00"
    MICROWAVE_AVAILABLE_MODES = "0x5c01"
    MICROWAVE_UNKNOWN_5C02 = "0x5c02"
    MICROWAVE_UNKNOWN_5C03 = "0x5c03"
    MICROWAVE_UNKNOWN_5C04 = "0x5c04"
    MICROWAVE_UNKNOWN_5C05 = "0x5c05"
    MICROWAVE_UNKNOWN_5C0A = "0x5c0a"
    MICROWAVE_UNKNOWN_5C0B = "0x5c0b"
    MICROWAVE_UNKNOWN_5C0C = "0x5c0c"
    MICROWAVE_UNKNOWN_5C0D = "0x5c0d"
    MICROWAVE_UNKNOWN_5C0E = "0x5c0e"
    MICROWAVE_UNKNOWN_5C0F = "0x5c0f"
    MICROWAVE_UNKNOWN_5C10 = "0x5c10"
    MICROWAVE_STATE = "0x5c11"
    MICROWAVE_UNKNOWN_5C12 = "0x5c12"
    MICROWAVE_UNKNOWN_5C13 = "0x5c13"
    MICROWAVE_REMOTE_ENABLE = "0x5c14"
    MICROWAVE_COOK_TIMER = "0x5c15"
    MICROWAVE_UNKNOWN_5C16 = "0x5c16"
    MICROWAVE_UNKNOWN_5C17 = "0x5c17"
    MICROWAVE_UNKNOWN_5C18 = "0x5c18"
    MICROWAVE_KITCHEN_TIMER = "0x5c19"
    MICROWAVE_COOK_TIME_SETTING_MODIFICATION = "0x5c1a"
    MICROWAVE_UNKNOWN_5C1B = "0x5c1b"
    MICROWAVE_UNKNOWN_5C1E = "0x5c1e"
    MICROWAVE_UNKNOWN_5C20 = "0x5c20"
    MICROWAVE_UNKNOWN_5C2C = "0x5c2c"
    MICROWAVE_UNKNOWN_5C2E = "0x5c2e"

    # Hood
    HOOD_TIMER_AVAILABILITY = "0x500f"
    HOOD_TIMER = "0x5020"
    HOOD_FAN_SPEED = "0x5b00"
    HOOD_FAN_SPEED_AVAILABILITY = "0x5b01"
    HOOD_LIGHT_LEVEL = "0x5b02"
    HOOD_LIGHT_LEVEL_AVAILABILITY = "0x5b03"
    HOOD_DELAY_OFF = "0x5b04"

    # Advantium
    ADVANTIUM_KITCHEN_TIME_REMAINING = "0x0050"
    # ADVANTIUM_MIN_MAX_TEMP = "0x5008" #See: OVEN_MODE_MIN_MAX_TEMP
    # ADVANTIUM_DISPLAY_TEMP = "0x5109"  #See: UPPER_OVEN_DISPLAY_TEMPERATURE
    # ADVANTIUM_REMOTE_ENABLED = "0x510a" #See: UPPER_OVEN_REMOTE_ENABLED
    ADVANTIUM_REMOTE_COOK_MODE_CONFIG = "0x5400"
    ADVANTIUM_COOK_STATUS = "0x5401"
    ADVANTIUM_COOK_SETTING = "0x5402"
    ADVANTIUM_COOK_TIME_REMAINING = "0x5403"
    ADVANTIUM_COOK_TIME_ADJUST = "0x5404"
    ADVANTIUM_PRECISION_VERSION = "0x5405"
    ADVANTIUM_UNKNOWN_5406 = "0x5406"
    ADVANTIUM_COOK_TIME_MIN_MAX = "0x5407"
    ADVANTIUM_MICROWAVE_MIN_MAX = "0x5408"
    ADVANTIUM_PRECISION_MIN_MAX = "0x5409"
    ADVANTIUM_KITCHEN_TIMER_MIN_MAX = "0x540a"

    # Water Filter
    WH_FILTER_VALVE_STATE = "0x115e"
    WH_FILTER_MODE = "0x115f"
    WH_FILTER_POSITION = "0x1167"
    WH_FILTER_FLOW_RATE = "0x1160"
    WH_FILTER_UNKNOWN1163 = "0x1163"
    WH_FILTER_MANUAL_MODE = "0x1168"
    WH_FILTER_FLOW_ALERT = "0x1169"
    WH_FILTER_FLOW_ALERT_SETTINGS = "0x116a"
    WH_FILTER_DAY_USAGE = "0x116d"
    WH_FILTER_LEAK_VALIDITY = "0x116e"
    WH_FILTER_LIFE_REMAINING = "0x1164"

    # Water Softener
    WH_SOFTENER_ERROR_CODE = "0x8004"
    WH_SOFTENER_SALT_LIFE_REMAINING = "0x8005"
    WH_SOFTENER_LOW_SALT = "0x8007"
    WH_SOFTENER_UNKNOWN800D = "0x800d"
    WH_SOFTENER_UNKNOWN800E = "0x800e"
    WH_SOFTENER_SHUTOFF_VALVE_STATE = "0x8033"
    WH_SOFTENER_SHUTOFF_VALVE_CONTROL = "0x8034"

    # Water Heater
    WH_HEATER_TARGET_TEMPERATURE = "0x4024"
    WH_HEATER_TEMPERATURE = "0x4026"
    WH_HEATER_MODE = "0x4020"
    WH_HEATER_MODE_HOURS_REMAINING = "0x4028"
    WH_HEATER_MIN_MAX_TEMPERATURE = "0x4047"
    WH_HEATER_VACATION_MODE_MAX_TIME = "0x4049"
    WH_HEATER_ELECTRIC_MODE_MAX_TIME = "0x404a"
    WH_HEATER_UNKNOWN4021 = "0x4021"
    WH_HEATER_UNKNOWN4022 = "0x4022"
    WH_HEATER_UNKNOWN4023 = "0x4023"
    WH_HEATER_UNKNOWN4025 = "0x4025"
    WH_HEATER_UNKNOWN4040 = "0x4040"
    WH_HEATER_UNKNOWN4041 = "0x4041"
    WH_HEATER_UNKNOWN4046 = "0x4046"
    WH_HEATER_UNKNOWN4048 = "0x4048"
    WH_HEATER_UNKNOWN404B = "0x404b"

    # AIR CONDITIONER
    AC_TARGET_TEMPERATURE = "0x7003"
    AC_FAN_SETTING = "0x7a00"
    AC_OPERATION_MODE = "0x7a01"
    AC_AMBIENT_TEMPERATURE = "0x7a02"
    AC_FILTER_STATUS = "0x7a04"
    AC_POWER_STATUS = "0x7a0f"
    AC_UNKNOWN7A12 = "0x7a12"

    #Window AC
    WAC_DEMAND_RESPONSE_POWER = "0xd005"
    WAC_DEMAND_RESPONSE_STATE = "0xd006"

    #Split AC
    SAC_AVAILABLE_MODES = "0x7b00"
    SAC_SLEEP_MODE = "0x7b05"
    SAC_TARGET_TEMPERATURE_RANGE = "0x7b06"
    SAC_AUTO_SWING_MODE = "0x7b07"

    #Ice Maker
    OIM_STATUS = "0x9100"
    OIM_LIGHT_LEVEL = "0x9101"
    OIM_UNKNOWN9102 = "0x9102"
    OIM_FILTER_STATUS = "0x9104"
    OIM_UNKNOWN9106 = "0x9106"
    OIM_POWER = "0x9107"
    OIM_UNKNOWN9108 = "0x9108"

    #Cafe Coffee Maker
    CCM_IS_BREWING = "0x9000"
    CCM_BREW_TEMPERATURE = "0x9001"
    CCM_BREW_TEMPERATURE_RANGE = "0x9002"
    CCM_UNKNOWN9003 = "0x9003"
    CCM_UNKNOWN9004 = "0x9004"
    CCM_UNKNOWN9005 = "0x9005"
    CCM_BREW_CUPS = "0x9006"
    CCM_UNKNOWN9007 = "0x9007"
    CCM_BREW_STRENGTH = "0x9008"
    CCM_UNKNOWN9009 = "0x9009"
    CCM_UNKNOWN900A = "0x900a"
    CCM_BREW_SETTINGS = "0x900b"
    CCM_CANCEL_BREWING = "0x900c"
    CCM_POT_PRESENT = "0x9012"
    CCM_OUT_OF_WATER = "0x9013"
    CCM_CURRENT_WATER_TEMPERATURE = "0x9014"
    CCM_UNKNOWN9015 = "0x9015"
    CCM_IS_DESCALING = "0x9019"
    CCM_START_DESCALING = "0x901a"
    CCM_CANCEL_DESCALING = "0x901b"

ErdCodeType = Union[ErdCode, str]
