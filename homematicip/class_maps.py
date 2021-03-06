from homematicip.base.enums import *

from homematicip.device import *

from homematicip.group import *

from homematicip.securityEvent import *
from homematicip.rule import *
from homematicip.functionalHomes import *

TYPE_CLASS_MAP = {
    DeviceType.DEVICE: Device,
    DeviceType.HEATING_THERMOSTAT: HeatingThermostat,
    DeviceType.SHUTTER_CONTACT: ShutterContact,
    DeviceType.SHUTTER_CONTACT_INVISIBLE: ShutterContact,
    DeviceType.WALL_MOUNTED_THERMOSTAT_PRO: WallMountedThermostatPro,
    DeviceType.BRAND_WALL_MOUNTED_THERMOSTAT: WallMountedThermostatPro,
    DeviceType.SMOKE_DETECTOR: SmokeDetector,
    DeviceType.FLOOR_TERMINAL_BLOCK_6: FloorTerminalBlock6,
    DeviceType.PLUGABLE_SWITCH_MEASURING: PlugableSwitchMeasuring,
    DeviceType.TEMPERATURE_HUMIDITY_SENSOR_DISPLAY: TemperatureHumiditySensorDisplay,
    DeviceType.ROOM_CONTROL_DEVICE: TemperatureHumiditySensorDisplay,
    DeviceType.TEMPERATURE_HUMIDITY_SENSOR: TemperatureHumiditySensorWithoutDisplay,
    DeviceType.PUSH_BUTTON: PushButton,
    DeviceType.ALARM_SIREN_INDOOR: AlarmSirenIndoor,
    DeviceType.MOTION_DETECTOR_INDOOR: MotionDetectorIndoor,
    DeviceType.KEY_REMOTE_CONTROL_ALARM: KeyRemoteControlAlarm,
    DeviceType.PLUGABLE_SWITCH: PlugableSwitch,
    DeviceType.FULL_FLUSH_SHUTTER: FullFlushShutter,
    DeviceType.BRAND_SHUTTER: FullFlushShutter,
    DeviceType.PRECENCE_DETECTOR_INDOOR: PresenceDetectorIndoor,
    DeviceType.PLUGGABLE_DIMMER: PluggableDimmer,
    DeviceType.BRAND_DIMMER: BrandDimmer,
    DeviceType.BRAND_SWITCH_MEASURING: BrandSwitchMeasuring,
    DeviceType.PRINTED_CIRCUIT_BOARD_SWITCH_BATTERY: PrintedCircuitBoardSwitchBattery,
    DeviceType.TEMPERATURE_HUMIDITY_SENSOR_OUTDOOR: TemperatureHumiditySensorOutdoor,
    DeviceType.WEATHER_SENSOR: WeatherSensor,
    DeviceType.WEATHER_SENSOR_PRO: WeatherSensorPro,
    DeviceType.ROTARY_HANDLE_SENSOR: RotaryHandleSensor,
    DeviceType.FULL_FLUSH_SWITCH_MEASURING: FullFlushSwitchMeasuring,
    DeviceType.MOTION_DETECTOR_PUSH_BUTTON: MotionDetectorPushButton,
    DeviceType.WATER_SENSOR: WaterSensor,
    DeviceType.SHUTTER_CONTACT_MAGNETIC: ShutterContact
}

TYPE_GROUP_MAP = {
    GroupType.GROUP: Group,
    GroupType.SECURITY: SecurityGroup,
    GroupType.SWITCHING: SwitchingGroup,
    GroupType.EXTENDED_LINKED_SWITCHING: ExtendedLinkedSwitchingGroup,
    GroupType.LINKED_SWITCHING: LinkedSwitchingGroup,
    GroupType.ALARM_SWITCHING: AlarmSwitchingGroup,
    GroupType.HEATING_HUMIDITY_LIMITER: HeatingHumidyLimiterGroup,
    GroupType.HEATING_TEMPERATURE_LIMITER: HeatingTemperatureLimiterGroup,
    GroupType.HEATING_CHANGEOVER: HeatingChangeoverGroup,
    GroupType.INBOX: InboxGroup,
    GroupType.SECURITY_ZONE: SecurityZoneGroup,
    GroupType.HEATING: HeatingGroup,
    GroupType.HEATING_COOLING_DEMAND: HeatingCoolingDemandGroup,
    GroupType.HEATING_EXTERNAL_CLOCK: HeatingExternalClockGroup,
    GroupType.HEATING_DEHUMIDIFIER: HeatingDehumidifierGroup,
    GroupType.HEATING_COOLING_DEMAND_BOILER: HeatingCoolingDemandBoilerGroup,
    GroupType.HEATING_COOLING_DEMAND_PUMP: HeatingCoolingDemandPumpGroup,
    GroupType.SWITCHING_PROFILE: SwitchingProfileGroup,
    GroupType.OVER_HEAT_PROTECTION_RULE: OverHeatProtectionRule,
    GroupType.SMOKE_ALARM_DETECTION_RULE: SmokeAlarmDetectionRule,
    GroupType.LOCK_OUT_PROTECTION_RULE: LockOutProtectionRule,
    GroupType.SHUTTER_WIND_PROTECTION_RULE: ShutterWindProtectionRule,
    GroupType.EXTENDED_LINKED_SHUTTER: ExtendedLinkedShutterGroup,
    GroupType.ENVIRONMENT:EnvironmentGroup
}

TYPE_SECURITY_EVENT_MAP = {
    SecurityEventType.SILENCE_CHANGED: SilenceChangedEvent,
    SecurityEventType.ACTIVATION_CHANGED: ActivationChangedEvent,
    SecurityEventType.ACCESS_POINT_CONNECTED: AccessPointConnectedEvent,
    SecurityEventType.ACCESS_POINT_DISCONNECTED: AccessPointDisconnectedEvent,
    SecurityEventType.SENSOR_EVENT: SensorEvent,
    SecurityEventType.SABOTAGE: SabotageEvent,
    SecurityEventType.MOISTURE_DETECTION_EVENT : MoistureDetectionEvent,
    SecurityEventType.SMOKE_ALARM : SmokeAlarmEvent,
    SecurityEventType.EXTERNAL_TRIGGERED : ExternalTriggeredEvent,
    SecurityEventType.OFFLINE_ALARM : OfflineAlarmEvent,
    SecurityEventType.WATER_DETECTION_EVENT : WaterDetectionEvent,
    SecurityEventType.MAINS_FAILURE_EVENT : MainsFailureEvent,
    SecurityEventType.OFFLINE_WATER_DETECTION_EVENT : OfflineWaterDetectionEvent
}

TYPE_RULE_MAP = {
    AutomationRuleType.SIMPLE : SimpleRule
}

TYPE_FUNCTIONALHOME_MAP = {
    FunctionalHomeType.INDOOR_CLIMATE: IndoorClimateHome,
    FunctionalHomeType.WEATHER_AND_ENVIRONMENT: WeatherAndEnvironmentHome,
    FunctionalHomeType.LIGHT_AND_SHADOW: LightAndShadowHome,
    FunctionalHomeType.SECURITY_AND_ALARM: SecurityAndAlarmHome
}
