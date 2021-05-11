'''
Test TMCL Parameters of TMCM1240 via CAN interface and module ID 1.

Created on 15.12.2020

@author: LK
'''

from PyTrinamicMicro.platforms.motionpy1.connections.can_tmcl_interface import can_tmcl_interface
from PyTrinamic.modules.TMCM1240.TMCM_1240 import TMCM_1240
import logging

MODULE_ID = 1
GP_BANK = 0
AP_AXIS = 0

logger = logging.getLogger(__name__)
logger.info("Test module TMCM1240 parameters via CAN")

logger.info("Initializing interface.")
interface = can_tmcl_interface(module_id=MODULE_ID)

logger.info("Initializing module.")
module = TMCM_1240(interface)

logger.info("Testing global parameter access.")

logger.info("Getting global parameter ({}, {}) ...".format("timer_0", module.GPs.timer_0))
logger.info("{}".format(module.getGlobalParameter(module.GPs.timer_0, GP_BANK)))
logger.info("Getting global parameter ({}, {}) ...".format("timer_1", module.GPs.timer_1))
logger.info("{}".format(module.getGlobalParameter(module.GPs.timer_1, GP_BANK)))
logger.info("Getting global parameter ({}, {}) ...".format("timer_2", module.GPs.timer_2))
logger.info("{}".format(module.getGlobalParameter(module.GPs.timer_2, GP_BANK)))
logger.info("Getting global parameter ({}, {}) ...".format("stopLeft_0", module.GPs.stopLeft_0))
logger.info("{}".format(module.getGlobalParameter(module.GPs.stopLeft_0, GP_BANK)))
logger.info("Getting global parameter ({}, {}) ...".format("stopRight_0", module.GPs.stopRight_0))
logger.info("{}".format(module.getGlobalParameter(module.GPs.stopRight_0, GP_BANK)))
logger.info("Getting global parameter ({}, {}) ...".format("input_0", module.GPs.input_0))
logger.info("{}".format(module.getGlobalParameter(module.GPs.input_0, GP_BANK)))
logger.info("Getting global parameter ({}, {}) ...".format("input_1", module.GPs.input_1))
logger.info("{}".format(module.getGlobalParameter(module.GPs.input_1, GP_BANK)))
logger.info("Getting global parameter ({}, {}) ...".format("input_2", module.GPs.input_2))
logger.info("{}".format(module.getGlobalParameter(module.GPs.input_2, GP_BANK)))
logger.info("Getting global parameter ({}, {}) ...".format("input_3", module.GPs.input_3))
logger.info("{}".format(module.getGlobalParameter(module.GPs.input_3, GP_BANK)))
logger.info("Getting global parameter ({}, {}) ...".format("serialBaudRate", module.GPs.serialBaudRate))
logger.info("{}".format(module.getGlobalParameter(module.GPs.serialBaudRate, GP_BANK)))
logger.info("Getting global parameter ({}, {}) ...".format("serialAddress", module.GPs.serialAddress))
logger.info("{}".format(module.getGlobalParameter(module.GPs.serialAddress, GP_BANK)))
logger.info("Getting global parameter ({}, {}) ...".format("ASCIIMode", module.GPs.ASCIIMode))
logger.info("{}".format(module.getGlobalParameter(module.GPs.ASCIIMode, GP_BANK)))
logger.info("Getting global parameter ({}, {}) ...".format("serialHeartbeat", module.GPs.serialHeartbeat))
logger.info("{}".format(module.getGlobalParameter(module.GPs.serialHeartbeat, GP_BANK)))
logger.info("Getting global parameter ({}, {}) ...".format("telegramPauseTime", module.GPs.telegramPauseTime))
logger.info("{}".format(module.getGlobalParameter(module.GPs.telegramPauseTime, GP_BANK)))
logger.info("Getting global parameter ({}, {}) ...".format("serialHostAddress", module.GPs.serialHostAddress))
logger.info("{}".format(module.getGlobalParameter(module.GPs.serialHostAddress, GP_BANK)))
logger.info("Getting global parameter ({}, {}) ...".format("autoStartMode", module.GPs.autoStartMode))
logger.info("{}".format(module.getGlobalParameter(module.GPs.autoStartMode, GP_BANK)))
logger.info("Getting global parameter ({}, {}) ...".format("limitSwitchPolarity", module.GPs.limitSwitchPolarity))
logger.info("{}".format(module.getGlobalParameter(module.GPs.limitSwitchPolarity, GP_BANK)))
logger.info("Getting global parameter ({}, {}) ...".format("protectionMode", module.GPs.protectionMode))
logger.info("{}".format(module.getGlobalParameter(module.GPs.protectionMode, GP_BANK)))
logger.info("Getting global parameter ({}, {}) ...".format("eepromCoordinateStore", module.GPs.eepromCoordinateStore))
logger.info("{}".format(module.getGlobalParameter(module.GPs.eepromCoordinateStore, GP_BANK)))
logger.info("Getting global parameter ({}, {}) ...".format("zeroUserVariables", module.GPs.zeroUserVariables))
logger.info("{}".format(module.getGlobalParameter(module.GPs.zeroUserVariables, GP_BANK)))
logger.info("Getting global parameter ({}, {}) ...".format("serialSecondaryAddress", module.GPs.serialSecondaryAddress))
logger.info("{}".format(module.getGlobalParameter(module.GPs.serialSecondaryAddress, GP_BANK)))
logger.info("Getting global parameter ({}, {}) ...".format("reverseShaftDirection", module.GPs.reverseShaftDirection))
logger.info("{}".format(module.getGlobalParameter(module.GPs.reverseShaftDirection, GP_BANK)))
logger.info("Getting global parameter ({}, {}) ...".format("applicationStatus", module.GPs.applicationStatus))
logger.info("{}".format(module.getGlobalParameter(module.GPs.applicationStatus, GP_BANK)))
logger.info("Getting global parameter ({}, {}) ...".format("downloadMode", module.GPs.downloadMode))
logger.info("{}".format(module.getGlobalParameter(module.GPs.downloadMode, GP_BANK)))
logger.info("Getting global parameter ({}, {}) ...".format("programCounter", module.GPs.programCounter))
logger.info("{}".format(module.getGlobalParameter(module.GPs.programCounter, GP_BANK)))
logger.info("Getting global parameter ({}, {}) ...".format("lastTmclError", module.GPs.lastTmclError))
logger.info("{}".format(module.getGlobalParameter(module.GPs.lastTmclError, GP_BANK)))
logger.info("Getting global parameter ({}, {}) ...".format("tickTimer", module.GPs.tickTimer))
logger.info("{}".format(module.getGlobalParameter(module.GPs.tickTimer, GP_BANK)))
logger.info("Getting global parameter ({}, {}) ...".format("randomNumber", module.GPs.randomNumber))
logger.info("{}".format(module.getGlobalParameter(module.GPs.randomNumber, GP_BANK)))
logger.info("Getting global parameter ({}, {}) ...".format("Intpol", module.GPs.Intpol))
logger.info("{}".format(module.getGlobalParameter(module.GPs.Intpol, GP_BANK)))

logger.info("Testing axis parameter access.")

logger.info("Getting axis parameter ({}, {}) ...".format("TargetPosition", module.APs.TargetPosition))
logger.info("{}".format(module.getAxisParameter(module.APs.TargetPosition, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("ActualPosition", module.APs.ActualPosition))
logger.info("{}".format(module.getAxisParameter(module.APs.ActualPosition, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("TargetVelocity", module.APs.TargetVelocity))
logger.info("{}".format(module.getAxisParameter(module.APs.TargetVelocity, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("ActualVelocity", module.APs.ActualVelocity))
logger.info("{}".format(module.getAxisParameter(module.APs.ActualVelocity, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("MaxVelocity", module.APs.MaxVelocity))
logger.info("{}".format(module.getAxisParameter(module.APs.MaxVelocity, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("MaxAcceleration", module.APs.MaxAcceleration))
logger.info("{}".format(module.getAxisParameter(module.APs.MaxAcceleration, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("MaxCurrent", module.APs.MaxCurrent))
logger.info("{}".format(module.getAxisParameter(module.APs.MaxCurrent, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("StandbyCurrent", module.APs.StandbyCurrent))
logger.info("{}".format(module.getAxisParameter(module.APs.StandbyCurrent, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("PositionReachedFlag", module.APs.PositionReachedFlag))
logger.info("{}".format(module.getAxisParameter(module.APs.PositionReachedFlag, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("HomeSwitch", module.APs.HomeSwitch))
logger.info("{}".format(module.getAxisParameter(module.APs.HomeSwitch, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("RightEndstop", module.APs.RightEndstop))
logger.info("{}".format(module.getAxisParameter(module.APs.RightEndstop, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("LeftEndstop", module.APs.LeftEndstop))
logger.info("{}".format(module.getAxisParameter(module.APs.LeftEndstop, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("RightLimitSwitchDisable", module.APs.RightLimitSwitchDisable))
logger.info("{}".format(module.getAxisParameter(module.APs.RightLimitSwitchDisable, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("LeftLimitSwitchDisable", module.APs.LeftLimitSwitchDisable))
logger.info("{}".format(module.getAxisParameter(module.APs.LeftLimitSwitchDisable, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("SwapLimitSwitches", module.APs.SwapLimitSwitches))
logger.info("{}".format(module.getAxisParameter(module.APs.SwapLimitSwitches, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("A1", module.APs.A1))
logger.info("{}".format(module.getAxisParameter(module.APs.A1, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("V1", module.APs.V1))
logger.info("{}".format(module.getAxisParameter(module.APs.V1, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("MaxDeceleration", module.APs.MaxDeceleration))
logger.info("{}".format(module.getAxisParameter(module.APs.MaxDeceleration, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("D1", module.APs.D1))
logger.info("{}".format(module.getAxisParameter(module.APs.D1, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("StartVelocity", module.APs.StartVelocity))
logger.info("{}".format(module.getAxisParameter(module.APs.StartVelocity, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("StopVelocity", module.APs.StopVelocity))
logger.info("{}".format(module.getAxisParameter(module.APs.StopVelocity, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("RampWaitTime", module.APs.RampWaitTime))
logger.info("{}".format(module.getAxisParameter(module.APs.RampWaitTime, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("THIGH", module.APs.THIGH))
logger.info("{}".format(module.getAxisParameter(module.APs.THIGH, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("min_dcStep_speed", module.APs.min_dcStep_speed))
logger.info("{}".format(module.getAxisParameter(module.APs.min_dcStep_speed, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("RightLimitSwitchPolarity", module.APs.RightLimitSwitchPolarity))
logger.info("{}".format(module.getAxisParameter(module.APs.RightLimitSwitchPolarity, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("LeftLimitSwitchPolarity", module.APs.LeftLimitSwitchPolarity))
logger.info("{}".format(module.getAxisParameter(module.APs.LeftLimitSwitchPolarity, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("softstop", module.APs.softstop))
logger.info("{}".format(module.getAxisParameter(module.APs.softstop, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("HighSpeedChopperMode", module.APs.HighSpeedChopperMode))
logger.info("{}".format(module.getAxisParameter(module.APs.HighSpeedChopperMode, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("HighSpeedFullstepMode", module.APs.HighSpeedFullstepMode))
logger.info("{}".format(module.getAxisParameter(module.APs.HighSpeedFullstepMode, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("MeasuredSpeed", module.APs.MeasuredSpeed))
logger.info("{}".format(module.getAxisParameter(module.APs.MeasuredSpeed, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("PowerDownRamp", module.APs.PowerDownRamp))
logger.info("{}".format(module.getAxisParameter(module.APs.PowerDownRamp, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("dcStep_time", module.APs.dcStep_time))
logger.info("{}".format(module.getAxisParameter(module.APs.dcStep_time, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("dcStep_stallGuard", module.APs.dcStep_stallGuard))
logger.info("{}".format(module.getAxisParameter(module.APs.dcStep_stallGuard, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("relative_positioning_option", module.APs.relative_positioning_option))
logger.info("{}".format(module.getAxisParameter(module.APs.relative_positioning_option, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("MicrostepResolution", module.APs.MicrostepResolution))
logger.info("{}".format(module.getAxisParameter(module.APs.MicrostepResolution, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("Intpol", module.APs.Intpol))
logger.info("{}".format(module.getAxisParameter(module.APs.Intpol, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("DoubleEdgeSteps", module.APs.DoubleEdgeSteps))
logger.info("{}".format(module.getAxisParameter(module.APs.DoubleEdgeSteps, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("ChopperBlankTime", module.APs.ChopperBlankTime))
logger.info("{}".format(module.getAxisParameter(module.APs.ChopperBlankTime, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("ConstantTOffMode", module.APs.ConstantTOffMode))
logger.info("{}".format(module.getAxisParameter(module.APs.ConstantTOffMode, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("DisableFastDecayComparator", module.APs.DisableFastDecayComparator))
logger.info("{}".format(module.getAxisParameter(module.APs.DisableFastDecayComparator, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("ChopperHysteresisEnd", module.APs.ChopperHysteresisEnd))
logger.info("{}".format(module.getAxisParameter(module.APs.ChopperHysteresisEnd, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("ChopperHysteresisStart", module.APs.ChopperHysteresisStart))
logger.info("{}".format(module.getAxisParameter(module.APs.ChopperHysteresisStart, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("TOff", module.APs.TOff))
logger.info("{}".format(module.getAxisParameter(module.APs.TOff, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("SEIMIN", module.APs.SEIMIN))
logger.info("{}".format(module.getAxisParameter(module.APs.SEIMIN, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("SECDS", module.APs.SECDS))
logger.info("{}".format(module.getAxisParameter(module.APs.SECDS, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("smartEnergyHysteresis", module.APs.smartEnergyHysteresis))
logger.info("{}".format(module.getAxisParameter(module.APs.smartEnergyHysteresis, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("SECUS", module.APs.SECUS))
logger.info("{}".format(module.getAxisParameter(module.APs.SECUS, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("smartEnergyHysteresisStart", module.APs.smartEnergyHysteresisStart))
logger.info("{}".format(module.getAxisParameter(module.APs.smartEnergyHysteresisStart, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("SG2FilterEnable", module.APs.SG2FilterEnable))
logger.info("{}".format(module.getAxisParameter(module.APs.SG2FilterEnable, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("SG2Threshold", module.APs.SG2Threshold))
logger.info("{}".format(module.getAxisParameter(module.APs.SG2Threshold, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("GlobalCurrentScaler", module.APs.GlobalCurrentScaler))
logger.info("{}".format(module.getAxisParameter(module.APs.GlobalCurrentScaler, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("smartEnergyActualCurrent", module.APs.smartEnergyActualCurrent))
logger.info("{}".format(module.getAxisParameter(module.APs.smartEnergyActualCurrent, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("smartEnergyStallVelocity", module.APs.smartEnergyStallVelocity))
logger.info("{}".format(module.getAxisParameter(module.APs.smartEnergyStallVelocity, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("smartEnergyThresholdSpeed", module.APs.smartEnergyThresholdSpeed))
logger.info("{}".format(module.getAxisParameter(module.APs.smartEnergyThresholdSpeed, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("RandomTOffMode", module.APs.RandomTOffMode))
logger.info("{}".format(module.getAxisParameter(module.APs.RandomTOffMode, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("ChopperSynchronization", module.APs.ChopperSynchronization))
logger.info("{}".format(module.getAxisParameter(module.APs.ChopperSynchronization, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("PWMThresholdSpeed", module.APs.PWMThresholdSpeed))
logger.info("{}".format(module.getAxisParameter(module.APs.PWMThresholdSpeed, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("PWMGrad", module.APs.PWMGrad))
logger.info("{}".format(module.getAxisParameter(module.APs.PWMGrad, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("PWMAmplitude", module.APs.PWMAmplitude))
logger.info("{}".format(module.getAxisParameter(module.APs.PWMAmplitude, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("PWMScale", module.APs.PWMScale))
logger.info("{}".format(module.getAxisParameter(module.APs.PWMScale, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("PWMMode", module.APs.PWMMode))
logger.info("{}".format(module.getAxisParameter(module.APs.PWMMode, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("PWMFrequency", module.APs.PWMFrequency))
logger.info("{}".format(module.getAxisParameter(module.APs.PWMFrequency, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("PWMAutoscale", module.APs.PWMAutoscale))
logger.info("{}".format(module.getAxisParameter(module.APs.PWMAutoscale, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("ReferenceSearchMode", module.APs.ReferenceSearchMode))
logger.info("{}".format(module.getAxisParameter(module.APs.ReferenceSearchMode, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("ReferenceSearchSpeed", module.APs.ReferenceSearchSpeed))
logger.info("{}".format(module.getAxisParameter(module.APs.ReferenceSearchSpeed, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("ReferenceSwitchSpeed", module.APs.ReferenceSwitchSpeed))
logger.info("{}".format(module.getAxisParameter(module.APs.ReferenceSwitchSpeed, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("ReferenceSwitchDistance", module.APs.ReferenceSwitchDistance))
logger.info("{}".format(module.getAxisParameter(module.APs.ReferenceSwitchDistance, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("LastReferenceSwitchPosition", module.APs.LastReferenceSwitchPosition))
logger.info("{}".format(module.getAxisParameter(module.APs.LastReferenceSwitchPosition, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("FullstepResolution", module.APs.FullstepResolution))
logger.info("{}".format(module.getAxisParameter(module.APs.FullstepResolution, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("FreewheelingMode", module.APs.FreewheelingMode))
logger.info("{}".format(module.getAxisParameter(module.APs.FreewheelingMode, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("LoadValue", module.APs.LoadValue))
logger.info("{}".format(module.getAxisParameter(module.APs.LoadValue, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("ExtendedErrorFlags", module.APs.ExtendedErrorFlags))
logger.info("{}".format(module.getAxisParameter(module.APs.ExtendedErrorFlags, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("DrvStatusFlags", module.APs.DrvStatusFlags))
logger.info("{}".format(module.getAxisParameter(module.APs.DrvStatusFlags, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("EncoderPosition", module.APs.EncoderPosition))
logger.info("{}".format(module.getAxisParameter(module.APs.EncoderPosition, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("encoder_cleat", module.APs.encoder_cleat))
logger.info("{}".format(module.getAxisParameter(module.APs.encoder_cleat, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("max_encoder_deviation", module.APs.max_encoder_deviation))
logger.info("{}".format(module.getAxisParameter(module.APs.max_encoder_deviation, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("PowerDownDelay", module.APs.PowerDownDelay))
logger.info("{}".format(module.getAxisParameter(module.APs.PowerDownDelay, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("absolute_resolver_value", module.APs.absolute_resolver_value))
logger.info("{}".format(module.getAxisParameter(module.APs.absolute_resolver_value, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("external_encoder_position", module.APs.external_encoder_position))
logger.info("{}".format(module.getAxisParameter(module.APs.external_encoder_position, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("external_encoder_resolution", module.APs.external_encoder_resolution))
logger.info("{}".format(module.getAxisParameter(module.APs.external_encoder_resolution, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("external_encoder_max_deviation", module.APs.external_encoder_max_deviation))
logger.info("{}".format(module.getAxisParameter(module.APs.external_encoder_max_deviation, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("reverse_shaft", module.APs.reverse_shaft))
logger.info("{}".format(module.getAxisParameter(module.APs.reverse_shaft, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("step_direction_mode", module.APs.step_direction_mode))
logger.info("{}".format(module.getAxisParameter(module.APs.step_direction_mode, AP_AXIS)))
logger.info("Getting axis parameter ({}, {}) ...".format("unit_mode", module.APs.unit_mode))
logger.info("{}".format(module.getAxisParameter(module.APs.unit_mode, AP_AXIS)))

logger.info("Test completed successfully.")
