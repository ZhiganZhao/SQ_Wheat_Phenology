
    !use crop2mlModules
        REAL:: phase1, appFLN, ttFromLastLeafToHeading, localDegfm, ttFromLastLeafToAnthesis        
        phase1 = phase
        IF ((phase1 >= 0) .AND. (phase1 < 1)) THEN
            IF (switchMaize==0) THEN
                IF (cumulTT>= dse) THEN
                    phase = 1
                ELSE
                    phase = phase1
                END IF
            ELSE
                IF (cumulTT >= dse) THEN
                    phase= 1;
                ELSE
                    phase = phase1
                END IF
            END IF
        ELSE IF ((phase1 >= 1) .AND. (phase1 < 2)) THEN
            IF ((isVernalizable==1 .AND. vernaprog >= 1) .OR. (isVernalizable==0)) THEN
                IF (switchMaize==0) THEN
                    IF (dayLength > maxDL) THEN
                        finalLeafNumber = minFinalNumber
                        hasLastPrimordiumAppeared = 1
                    ELSE
                        appFLN = minFinalNumber + sLDL * (maxDL - dayLength)
                        !calculation of final leaf number from dayLength at inflexion plus 2 leaves
                        IF ((appFLN / 2.0) <= leafNumber) THEN
                            finalLeafNumber = appFLN;
                            hasLastPrimordiumAppeared =1
                        ELSE
                            phase = phase1
                        END IF
                    END IF
                ELSE
                    hasLastPrimordiumAppeared = 1
                END IF
                IF (hasLastPrimordiumAppeared==1) THEN
                    phase = 2
                END IF
            ELSE
                phase = phase1
            END IF
        ELSE IF ((phase1 >= 2) .AND. (phase1 < 4)) THEN
            IF (isMomentRegistredZC_39==1) THEN
                IF (phase1 < 3) THEN
                    ttFromLastLeafToHeading = 0.0
                    IF(choosePhyllUse=="Default") THEN
                        ttFromLastLeafToHeading =(pFLLAnth - pHEADANTH) * fixPhyll
                    ELSE IF (choosePhyllUse == "PTQ") THEN
                        ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * phyllochron;
                    ELSE IF (choosePhyllUse == "Test")  THEN
                        ttFromLastLeafToHeading = (pFLLAnth - pHEADANTH) * p
                    END IF
                    IF (cumulTTFromZC_39 >= ttFromLastLeafToHeading) THEN
                        phase = 3
                    ELSE
                        phase = phase1
                    END IF
                END IF
                ttFromLastLeafToAnthesis =0.0;
                IF (choosePhyllUse == "Default") THEN
                    ttFromLastLeafToAnthesis = pFLLAnth * fixPhyll
                ELSE IF (choosePhyllUse == "PTQ") THEN
                    ttFromLastLeafToAnthesis = pFLLAnth * phyllochron
                ELSE IF (choosePhyllUse == "Test") THEN
                    ttFromLastLeafToAnthesis = pFLLAnth * p
                END IF
                IF (cumulTTFromZC_39 >= ttFromLastLeafToAnthesis) THEN
                    phase = 4
                ELSE
                    phase = phase1
                END IF
            ELSE
                phase = phase1
            END IF
        ELSE IF (phase1 == 4) THEN
            IF (grainCumulTT >= dcd) THEN
                phase = 4.5
            ELSE
                phase = phase1
            END IF
        ELSE IF (phase1 == 4.5) THEN
            IF ((grainCumulTT >= dgf) .OR. (gai <= 0)) THEN
                phase = 5
            ELSE
                phase = phase1
            END IF
        ELSE IF ((phase1 >= 5) .AND. (phase1 < 6)) THEN
            localDegfm = degfm
            IF (ignoreGrainMaturation .EQV. .TRUE.) THEN
                localDegfm = -1
            END IF
            IF (cumulTTFromZC_91 >= localDegfm) THEN
                phase = 6
            ELSE
                phase= phase1
            END IF
        ELSE IF ((phase1>= 6) .AND. (phase1 < 7)) THEN
            phase = phase1
        END IF


