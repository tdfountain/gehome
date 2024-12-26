import enum

@enum.unique
class ErdPersonality(enum.Enum):
    UNKNOWN = "00"
    PERSONALITY_120V_CAFE = "00000001"
    PERSONALITY_120V_MONOGRAM = "00000002"
    PERSONALITY_UNKNOWN03 = "00000003"
    PERSONALITY_UNKNOWN04 = "00000004"
    PERSONALITY_UNKNOWN05 = "00000005"
    PERSONALITY_120V_GE_PROFILE = "00000006"
    PERSONALITY_UNKNOWN07 = "00000007"
    PERSONALITY_UNKNOWN08 = "00000008"
    PERSONALITY_240V_MONOGRAM = "00000009"
    PERSONALITY_UNKNOWN0A = "0000000A"
    PERSONALITY_UNKNOWN0B = "0000000B"
    PERSONALITY_UNKNOWN0C = "0000000C"
    PERSONALITY_UNKNOWN0D = "0000000D"
    PERSONALITY_GAS_120V_GE_PROFILE = "0000000E"
    PERSONALITY_240V_CAFE = "00000010"