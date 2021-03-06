import numpy as np 
from copy import copy
from math import *

def registerzadok(cumulTT=354.582294512,
                  phase=2.0,
                  leafNumber=4.88542196611,
                  calendarMoments=['Sowing'],
                  calendarDates=['21/3/2007'],
                  calendarCumuls=[0.0],
                  cumulTTFromZC_65=0.0,
                  currentdate='9/4/2007',
                  Der=300.0,
                  slopeTSFLN=0.9,
                  TSFLN=2.6,
                  intTSFLN=0.9,
                  FinalLeafNumber=8.7975820132,
                  currentZadokStage='MainShootPlus1Tiller',
                  hasZadokStageChanged=0):
    """


    RegisterZadok Model
    Author: Pierre MARTRE
    Reference: Modeling development phase in the 
                Wheat Simulation Model SiriusQuality.
                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    Institution: INRA/LEPSE Montpellier
    Abstract: Record the zadok stage in the calendar
    	

    """
    roundedFinalLeafNumber = int(FinalLeafNumber+0.5);
    if (leafNumber>=4 and "MainShootPlus1Tiller" not in calendarMoments):
        calendarMoments.append("MainShootPlus1Tiller")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "MainShootPlus1Tiller"
    elif (leafNumber>=5 and "MainShootPlus2Tiller" not in calendarMoments):
        calendarMoments.append("MainShootPlus2Tiller")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "MainShootPlus2Tiller"
    elif (leafNumber>=6 and "MainShootPlus3Tiller" not in calendarMoments):
        calendarMoments.append("MainShootPlus3Tiller")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "MainShootPlus3Tiller"
    elif (FinalLeafNumber > 0 and leafNumber>=(slopeTSFLN * FinalLeafNumber - intTSFLN) and "TerminalSpikelet" not in calendarMoments):
        calendarMoments.append("TerminalSpikelet")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "TerminalSpikelet"
    elif ((leafNumber >= (roundedFinalLeafNumber-4) and (roundedFinalLeafNumber-4) > 0) and "PseudoStemErection" not in calendarMoments):
        calendarMoments.append("PseudoStemErection")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "PseudoStemErection"
    elif ((leafNumber >= (roundedFinalLeafNumber-3) and (roundedFinalLeafNumber-3) > 0) and "1stNodeDetectable" not in calendarMoments):
        calendarMoments.append("1stNodeDetectable")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "1stNodeDetectable"
    elif ((leafNumber >= (roundedFinalLeafNumber-2) and (roundedFinalLeafNumber-2) > 0) and "2ndNodeDetectable" not in calendarMoments):
        calendarMoments.append("2ndNodeDetectable")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "2ndNodeDetectable"
    elif ((leafNumber >= (roundedFinalLeafNumber-1) and (roundedFinalLeafNumber-1) > 0) and "FlagLeafJustVisible" not in calendarMoments):
        calendarMoments.append("FlagLeafJustVisible")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "FlagLeafJustVisible"
    elif (("MidGrainFilling" not in calendarMoments) and phase == 4.5 and cumulTTFromZC_65 >= Der):
        calendarMoments.append("MidGrainFilling")
        calendarCumuls.append(cumulTT)
        calendarDates.append(currentdate)
        hasZadokStageChanged = 1
        currentZadokStage = "MidGrainFilling"                 
    else:
        hasZadokStageChanged = 0;
    return  hasZadokStageChanged, currentZadokStage, calendarMoments, calendarDates, calendarCumuls
